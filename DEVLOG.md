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
    Removed init_db.py as it was not necessary. When scaling, a migration framework is preffered and actually practical.


    Session 3:
    Separated routes.py in to each route's particular script and added Flask-Migrate for even more modularity. Updated requirements.txt and __init__.py because of these changes. Will move on to stylings.


June 14, 2025
    Session 1:
    Edited further styles.css. h1 tag doesn't seem to be appearing, will debug later on.


    Session 2:
    Edited further styles.css. Added "zebra "striping to table, still the first and bottom rows, when hovered, lose the radius. Will follow up later. Will add media query for mobile responsive desgin.

    Session 3:
    Finally happy with styling. Abandoned border-radii. Wasn't achieving desired results and I don't want to spend a lot of more time on this project. Will end (until now) with stylings and move on to media queries, the final frontier.


June 15, 2025
    Session 1:
    Will start with authentication (https://www.youtube.com/watch?v=Fr2MxT9M0V4), felt a little bit tired of dealing with css.


June 16, 2025
    Session 1:
    Realized I should've opened up a new branch when making substantial changes to the application. Need to practice this skill, will start with this session just to start getting a feel for it. 
    
    Learned new Git commands, check gitLearnings.txt for more info.

    Restarted migration, learned that it's recommended to start the application development with the migration set up. You will probably change the database schema later on, and adds version control to your databases. Check migration_instructions.txt for further information.

    Added the new database in the configuration section of the app. Added it to models.py. Purposefuly left the password column to practice migration. Let's see how it goes, but first will push all the changes so far to the userAuth branch whilst creating the remote branch on GitHub.com

    Pushed changes to GitHub.com, learned a little bit about pull requests. Also, "migrated" the databases successfully!

    Will now move to Login, Register, Dashboard routes and Logout mechanism.

    Remember to start changing the content inside the html files. The application's core logic changed.
    Changed the content of the pertinent HTML and blueprints files to work with the developing user authentication feature.

    Before moving on to styling with sass (to acquire the new skill), I'll have to link up both tables in order for them to be shown at the task_tracker.html template *after* the user logs in.