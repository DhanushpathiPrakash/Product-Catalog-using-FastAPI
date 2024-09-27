FROM python:3
ENV PYTHONBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt


COPY . /app

EXPOSE 8000

CMD ["bash", "-c", "alembic upgrade head && uvicorn main:app --host 0.0.0.0 --port 8000"]


