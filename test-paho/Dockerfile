# Use an official Python runtime as a parent image
FROM python:3

# Set the working directory to /code
WORKDIR /code

# Install any needed packages specified in requirements.txt
RUN pip install paho-mqtt

# Copy the current directory contents into the container at /code
COPY ./src/myapp.py /code/



# Run app.py when the container launches
#CMD ["python", "app.py"]
