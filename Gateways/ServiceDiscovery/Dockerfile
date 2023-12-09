# Use the official Python 3.12 image as the base image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY . .

# Expose the port the gRPC server will be running on
EXPOSE 50051

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the gRPC server when the container starts
CMD ["python", "__init__.py"]
