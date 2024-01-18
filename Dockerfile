# Use a base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file and install dependencies
COPY requirement.txt .
RUN pip install --no-cache-dir -r requirement.txt

# Copy the rest of the project files to the working directory
COPY . .

# Set environment variables if needed
ENV ENV_VAR_NAME=value

# Expose any necessary ports
EXPOSE 8000

# Define the command to run your application
CMD ["python", "app.py"]