# imports the main Flask class from the flask library and the render_template function
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy # the goal of SQLAlchemy is to let us interact with a SQL database using Python objects and methods 
from sqlalchemy.orm import DeclarativeBase # foundation for all your database models
from sqlalchemy import select
from datetime import datetime



class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base) # creates empty placeholder object because it received no input
# (so as not to create an error before initializing the app)


# database model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now)

    # repr == representation; this is for debugging purposes, helps quickly identify the object when debugging
    def __repr__(self): # returns a string everytime we create a new element
        return '<Task %r>' % self.id


   
# ---------------------------------------------------------------IMPORTANT!----------------------------------------------------------------
# It doesn't build a table or access a database. 
# It simply registers the structure of your Todo table with that empty db placeholder. 
# The db object now holds onto this "blueprint," waiting for further instructions.
# -----------------------------------------------------------------------------------------------------------------------------------------
    

def create_app():
    app = Flask(__name__) # the app variable is your web application object
    # you need a central object so that you can define all your application's routes and configurations

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' # links to database using SQLAlchemy; /// -> relative path //// -> absolute path
    app.config['SQLALCHEMY_TRACK MODIFICATIONS'] = False # disables feature deprecated
    

    # db knows about the models and app knows where to find the database but it still hasn't been connected

    # fully links the database to the application, dejándose llevar por "app.config['SQLAlchemy_DATABASE_URI'] = 'sqlite:///test.db'"
    db.init_app(app) 

    # --- Routes ---
    # python decorator, tell your app to immediately trigger the following function 
    # after the user navigates to the specified URL path
    @app.route('/', methods=["GET", "POST"])
    # view function; Flask executes this function whenever the user visits '/'
    def index():
        if request.method == "POST":
            task_content = request.form['content']
            new_task = Todo(content=task_content)

            try:
                db.session.add(new_task)
                db.session.commit()
                return redirect('/')
            except:
                return "There was an error adding your task."
        else:
            print("GET")
            # Create a statement to select all tasks, ordered by their creation date
            statement = select(Todo).order_by(Todo.date_created)

            # Execute the statement and get all results as a list of Todo objects
            tasks = db.session.scalars(statement).all()
            return render_template("index.html", tasks=tasks) # runs index.html with tasks arranged in creation order
        
    @app.route('/delete/<int:id>')
    def delete(id):
        task_to_delete = Todo.query.get_or_404(id)

        try:
            db.session.delete(task_to_delete)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was a problem to deleting that task'
        
    @app.route('/update/<int:id>', methods=['GET','POST'])
    def update(id):
        
        task = Todo.query.get_or_404(id)

        if request.method == 'POST':
            task.content = request.form['content']

            try:
                db.session.commit()
                return redirect('/')
            except:
                return 'There was an issue updating your task.'
        else:
            return render_template("update.html", task=task)


        return
    return app




# initialize app
app = create_app()




# the if statement ensures that the server only runs when the script is executed directly
# it prevents the server from starting if this file is imported as a module into another script
if __name__ == "__main__":
    app.run(debug=True)