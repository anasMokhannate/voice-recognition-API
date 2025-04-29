# # Use an official Python base image
# FROM python:3.10-slim

# # Install system dependencies
# RUN apt-get update && apt-get install -y \
#     curl \
#     git \
#     ffmpeg \
#     && rm -rf /var/lib/apt/lists/*
# # Install Python dependencies
# RUN pip install --no-cache-dir \
#     flask \
#     requests

# # installing pyTorch for cpu
# RUN pip install torch --index-url https://download.pytorch.org/whl/cpu 

# # Copy your app code into the container
# WORKDIR /app
# COPY . /app

# # Expose Flask port
# EXPOSE 5000

# # Run Flask app
# CMD ["python", "app.py"]


# Use a lightweight base image
FROM python:3.10-slim

# System dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# install pyTorch for cpu
RUN pip install torch --index-url https://download.pytorch.org/whl/cpu 
# Set working directory
WORKDIR /app

# Copy only requirements first to cache dependencies
COPY requirements.txt .

# Install dependencies (Whisper included)
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the rest of the app
COPY . .

# Expose port and run app
EXPOSE 5000
CMD ["python", "app.py"]
