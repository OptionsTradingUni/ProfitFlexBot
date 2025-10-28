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

# Default command (can be overridden by Railway)
CMD sh -c "gunicorn --bind=0.0.0.0:${PORT:-5000} --reuse-port --workers=2 web_server:app & python profit_flex_bot.py"
