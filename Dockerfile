# Dockerfile for Profit Flex Bot - Railway Deployment

FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libpq-dev \
    fonts-dejavu-core \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create directory for trade images
RUN mkdir -p trade_images

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Expose port
EXPOSE 5000

# Copy start script
COPY start.sh .
RUN chmod +x start.sh

# Default command (can be overridden by Railway)
CMD ["./start.sh"]
