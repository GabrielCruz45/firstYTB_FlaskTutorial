June 9, 2025
    Some functionalities used on the tutorial are deprecated, tutorial is from 2019.
I am currently using LLM heavily to understand how to setup the application with app size in mind (lots of routes, tables etc.). Will help me a lot with the libraryApp project.

June 10, 2025
    Used an LLM to help me further understand the functionalities of the app.py script, line by line. Asked it for next steps, told me to:

                    1. Refactor project structure (with the intent of practicing a scalable project structure)
                    2. Implementing CRUD functionality.
                    3. Learn database migrations. 
                    4. Add user authentication.

Depending on how the tutorial flows, I will add these features after completing the "tutorial" app.


June 11, 2025 
    Added stylings to "styles.css".

June 12, 2025
    Session 1:
    Edited init_db.py, had a little typo on ".app_context()" had-> .appcontext()
Ran the script and created the .db file
Tested the web app. Currently can add tasks successfully!
Next onto the delete and update links.

    Session 2:
    Edited .html files because they had a bug. I didn't write {{ super() }} <title>... on child .html file, throwing 404 error when running app. jinja2 headblock was rewriting the <head> section, disregarding styles.css file. Edited further styles.css and file tree. Learned about the networking tab on browse's inspect section!

June 13, 2025
    Session 1:
    Finished app! Added delete and update routes on create_app function. Also, added update.html. Used some cool jinja2 syntax on index.html and update.html in particular the {{task.id}} to send variables from template to script.

    After completing the tutorial's app launch section, will refactor the project structure (separate routes from app.py), add authentification and implement better security practices. Finally will edit app's styling.

    Session 2:
    Updated command line tools (xcode), downloaded heroku.
    Added requirements.txt and Profcile for Heroku deployment.
    Successful deployment! Will now move onto refactoring and styling before finishing with the mini-learning journey.

    Refactored the applications file structure. Made it more modular/prepared it for scaling.
    Removed init_db.py as it was not necessary. When scaling a migration framework is preffered and actually practical.