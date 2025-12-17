# ========================
# Base Image
# ========================
FROM python:3.12-slim

# Set environment
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Create working directory
WORKDIR /app

# ========================
# Install dependencies
# ========================
RUN apt-get update && \
    apt-get install -y build-essential libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# ========================
# Copy project
# ========================
COPY . .

# ========================
# Collect static files
# ========================

# ========================
# Expose port
# ========================
EXPOSE 8000

# ========================
# Start Gunicorn
# ========================
CMD gunicorn djangocourse.wsgi:application --bind 0.0.0.0:$PORT
