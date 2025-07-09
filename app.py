from flask import Flask # imports the main Flask class from the flask library

app = Flask(__name__) # the app variable is your web application object
# you need a central object so that you can define all your application's routes and configurations

# python decorator, tell your app to immediately trigger the following function 
# after the user navigates to the specified URL path
@app.route('/')
# view function; Flask executes this function whenever the user visits '/'
def index():
    return "Hello, World!" # returns string -> "Hello, World!"

# the if statement ensures that the server only runs when the script is executed directly
# it prevents the server from starting if this file is imported as a module into another script
if __name__ == "__main__":
    app.run(debug=True)