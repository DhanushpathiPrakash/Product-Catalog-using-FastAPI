# catalog
This project is a simple catalog API built using FastAPI and SQLAlchemy with SQLite as the database. The project is containerized using Docker and migrations are handled by Alembic.

### Clone the Repository

    git clone https://github.com/DhanushpathiPrakash/catalog.git

Install Dependency 
If you want to run the application without Docker, first create a virtual environment and install the dependencies:<br>
    
    pythom -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate 
    pip install -r requirements.txt 
### Running the Application With Docker
##### Build the Docker image:

    docker-compose build
##### Run the container:
    
    docker-compose up

Once the container is running, the API will be available at <code> http://localhost:8000</code>

Open the interactive API documentation at <code> http://localhost:8000/docs</code>

### Without Docker
##### Creating a New Migration
If you make changes to the models and need to create a new migration, run:

    alembic revision --autogenerate -m "Message describing the migration"

This will generate a new migration file in the migrations/versions/ directory.

##### Applying Migrations

To apply migrations, run:

    alembic upgrade head
If you're using Docker, migrations are applied automatically when the container starts.

##### To run the app
  
    uvicorn main:app --reload
Visit <code>http://127.0.0.1:8000/docs</code> for the FastAPI interactive documentation.


Here are some of the available API endpoints. Visit /docs for the complete and interactive documentation.

<code>GET /product/</code> - Get all products <br>
<code>POST /product/</code> - Create a new product<br>
<code>PUT /product/{product_id}</code> - Update a product<br>
<code>DELETE /product/{product_id}</code> - Delete a product

Running Tests
To run the tests, ensure you're inside the virtual environment or container, and then use:

    pytest
The tests are located in the test_main.py file and ensure that the API works as expected.

### Testing the API Online:

You can test the API using the hosted link at: https://catalog-jvmr.onrender.com/docs.

This should provide a fully functional environment for interacting with the catalog API