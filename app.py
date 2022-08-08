# from debug_project_app.models import app
# from debug_project_app.models import User, Post, db
# from debug_project_app import app,routes

from debug_project_app import app,routes
from debug_project_app.models import User, Post
if __name__ == "__main__":
    app.run(debug = True)