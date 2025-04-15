FROM python:3.12-slim

# Create app directory
WORKDIR /app

# Install Flask
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY flaskapp.py .

# Expose port
EXPOSE 1337

# Run the app
CMD ["python", "flaskapp.py"]

