# Use the official Python image as a base
FROM python

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY . /app

# Install the required dependencies
RUN pip install -r requirements.txt

EXPOSE 3000

# Define the command to run the app and expose the port the app runs on
CMD ["python", "./web.py"]