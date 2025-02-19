
# Blogger’s Haven

Welcome to the Blogger’s Haven, A web application built using the HTML, CSS and JS in the Frontend and Django and Python in the Backend. This platform allows users to read and interact with articles, submit feedback, comment on posts, like content. Author can delete the post if he/she want.



## Features
* User Authentication: Register, Login, and Logout to interact with content.
* Article Management: Authors can create and delete their articles.
* Categories: Articles are organized by categories for easy browsing.
* Comments: Users can comment on articles to discuss and share feedback.
* Likes: Articles can be liked by users, with a like count displayed on each article.
* Feedback Form: Users can submit feedback or inquiries through a simple form.
* Dark Mode Toggle: Provides an option to switch between light and dark themes for better readability. 
* Email Send: Once user register on the website it will automatic send email to the user with small message. 

## Prerequisites
Before setting up the project, make sure your computer has the following installed:

1. Python (Required)
Python is the programming language used to build this project.

* Check if Python is already installed:

Open Command Prompt (Windows) or Terminal (Mac/Linux) and type:
```bash
  python --version
```
If Python is installed, it will display a version like: Python 3.x.x.

* If Python is NOT installed, download and install it from:
    https://www.python.org/downloads/

2. Install Git (Optional, Recommended)
Git is used to download (clone) the project from GitHub.

* Check if Git is installed:
```bash
  git --version
```
* If Git is NOT installed, download it from:
    https://git-scm.com/downloads
## Steps to Set Up
  
1. clone the repository:
Open Command Prompt (Windows) or Terminal (Mac/Linux) and type:
```bash
  git clone https://github.com/RanadipShrestha/Blogger-s-Blog.git
```
2. Navigate into the project
After downloading, open Command Prompt (Windows) or Terminal (Mac/Linux) and navigate to the project folder:
```bash
  cd blogging-platform
```
3. Create a virtual environment
A virtual environment is a separate space to project dependencies.
```bash
  python -m venv venv
```
you can give any name for environment if you want write your environment name and remove venv " venv= yourname "

4. Activate the virtual environment:
* On Windows
```bash
  venv\Scripts\activate
```
* On macOS/Linux
```bash
  source venv/bin/activate
```
5. Install the required dependencies on your system
Run this command to install all required libraries
```bash
  pip install -r requirements.txt
```
6. Set Up Environment Variables
Django uses environment Variables to store secret keys securely.
Create a .env file in the project folder and add:

    SECRET_KEY= "your_django_secret_key"  

    EMAIL_HOST_USER = Your email 'example@gmail.com' 

    EMAIL_HOST_PASSWORD = your password
  
7. set up DEBUG = True
Change DEBUG = False to DEBUG = True in setting.py

8. Apply database migrations
```bash
  python manage.py migrate
```
9. Create a superuser (admin) account
```bash
  python manage.py createsuperuser
```
10. Run the server
```bash
  python manage.py runserver
```
11. Access the application
Open your browser and go to http://127.0.0.1:8000


