# Use an official Python runtime as a parent image
FROM python:3

# Set the working directory to /code
WORKDIR /code

RUN apt-get install subversion

COPY ./src/requirements.txt /tmp/

# Install tools required to build the project
# We need to run `docker build --no-cache .` to update those dependencies
# Install any needed packages specified in requirements.txt
RUN pip install -r /tmp/requirements.txt

# Copy the current directory contents into the container at /code
COPY ./src/app.py /code/





# Make port 5000 available to the world outside this container
EXPOSE 5000


# Run app.py when the container launches
#CMD ["python", "app.py"]
