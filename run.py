from task_tracker import create_app

# create the flask app utilizing the factory
app = create_app()

# the if statement ensures that the server only runs when the script is executed directly
# it prevents the server from starting if this file is imported as a module into another script
if __name__ == "__main__":
    app.run(debug=True)