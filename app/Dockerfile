# Use official Python image
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy dependency file first (better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

# Expose port (Flask runs on 5000)
EXPOSE 5000

# Run the app
CMD ["python", "app/main.py"]