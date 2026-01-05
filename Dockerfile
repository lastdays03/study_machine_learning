# Base Image
FROM python:3.9-slim

# Working Directory
WORKDIR /app

# Copy Code
COPY src/serving/app.py /app/app.py

# Install Dependencies
RUN pip install fastapi uvicorn pydantic numpy

# Expose Port
EXPOSE 8000

# Start Command
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
