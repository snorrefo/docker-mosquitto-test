# Use an official Python runtime as a parent image
FROM python:3


# Install tools required to build the project
# We need to run `docker build --no-cache .` to update those dependencies
RUN pip install --no-cache-dir numpy
RUN pip install --no-cache-dir Flask


# Copy the current directory contents into the container at /code
COPY  ./src/ /code/

# Make port 5000 available to the world outside this container
EXPOSE 5000


# Set the working directory to /code
WORKDIR /code/


# Run app.py when the container launches
CMD ["python", "app.py"]
