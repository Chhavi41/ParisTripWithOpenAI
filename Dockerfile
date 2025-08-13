FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your app code
COPY . .

# Install dotenv
RUN pip install python-dotenv

# Command to run your app
CMD ["python", "main.py"]
