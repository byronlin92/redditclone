# Reddit clone

https://redditclone92.herokuapp.com/

![Homepage](static/img/screenshot.png)

# Set up
1. create virtual env within repo: `virtualenv venv -p python3`
2. activate virtual env: `source venv/bin/activate`
3. `python manage.py makemigrations`
4. `python manage.py migrate`
5. `python manage.py runserver` and use pip to install any missing packages (eg. Django)

Functionalities implemented:
1. Create subreddits (from admin)
2. User management (create, login)
3. Create post (ability to add title, description, URL, image upload)
4. Create/update/delete comments
5. Nested comments
6. score (upvote/downvote)
