#!/bin/bash

# Build the Docker image
echo "Building Docker image..."
docker build -t codegen-agent .

# Create output directories
echo "Creating output directories..."
mkdir -p generated_code

# Set permissions
echo "Setting permissions..."
chmod +x agent.py

echo "Setup complete! You can now run the agent with:"
echo "docker run -it --rm -v $(pwd)/generated_code:/app/generated_code codegen-agent"