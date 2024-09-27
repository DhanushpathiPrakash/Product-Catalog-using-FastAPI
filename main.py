from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from starlette import status
import schemas
import models
from database import engine, SessionLocal
from fastapi.responses import JSONResponse
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/product')
def create(request: schemas.Product, db: Session = Depends(get_db)):
    try:
        if not request.name or not request.price or not request.quantity:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Missing required fields')
        new_product = models.Product(**request.model_dump())
        db.add(new_product)
        db.commit()
        db.refresh(new_product)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content={"message": "Product created successfully."})
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"An error occurred while creating product:{str(e)}")

@app.get('/product', response_model=schemas.ProductsResponse)
def get(
        db: Session = Depends(get_db),
        min_price: float = Query(None, description='Min price for product'),
        max_price: float = Query(None, description='Max price for product'),
        ):
    try:
        product = db.query(models.Product)
        if min_price is not None:
            product = product.filter(models.Product.price >= min_price)
        if max_price is not None:
            product = product.filter(models.Product.price <= max_price)
        products = product.all()
        if not products:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='No products found')
        return {"data":products}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR , detail=f"unable to retrieve product:{str(e)}")

@app.get('/product/{product_id}', response_model=schemas.ProductsResponse)
def get_by(product_id, db: Session = Depends(get_db)):
    try:
        product = db.query(models.Product).filter(models.Product.id == product_id).first()
        if not product:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='No products found')
        response_data = {"data": [product]}
        return response_data
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"unable to retrieve product:{str(e)}")

@app.put('/product/{product_id}')
def put(product_id, request: schemas.ProductUpdate, db: Session = Depends(get_db)):
    try:
        product = db.query(models.Product).filter(models.Product.id == product_id).first()
        if not product:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='No products found')
        product_data = request.dict(exclude_unset=True)
        for key, value in product_data.items():
            setattr(product, key, value)
        db.commit()
        db.refresh(product)
        return {"message": "Product updated successfully."}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"An error occurred while updating product:{str(e)}")

@app.delete('/product/{product_id}')
def delete(product_id, db: Session = Depends(get_db)):
    try:
        product = db.query(models.Product).filter(models.Product.id == product_id)
        if not product:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='No products found')
        product.delete(synchronize_session=False)
        db.commit()
        return {"message": "Product deleted successfully."}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"An error occurred while deleting product:{str(e)}")