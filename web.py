from flask import Flask

# Create an instance of the Flask application
web = Flask(__name__)

# Define a route for the root URL ("/")
@web.route('/')

def index():
    return 'Hello DevOps Engineer, This is your Python Flask App. Congratulations!'

# Run the application
if __name__ == '__main__':
    web.run(host="0.0.0.0", port=int("3000"), debug=True)

