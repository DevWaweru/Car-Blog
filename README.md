# [Car-Blog](https://mycarblog.herokuapp.com)
## Car Blog is a web application for car enthusiasts, with details on the latest top performance cars.
### May 27th, 2018
#### By **[Richard Waweru](https://github.com/devwaweru)**

## Description
[Car-Blog](https://mycarblog.herokuapp.com) is a web application blog meant for car enthusiasts who seek the latest news on super cars. Users can subscribe to the blog to get the latest updates on articles.

The blog supports comments from users who can leave feedback on the blog. The blog admins can determine whether to delete the comments or not. Users can also delete blog posts at their discretion.

After the writer has posted a new blog post, subscribers will receive an email notification with a link to the blog post.

## Specifications
Get the specs [here](https://github.com/devwaweru/Car-Blog/blob/master/SPECS.md

## Set-up and Installation

### Prerequiites
    - Python 3.6
    - Ubuntu software

### Clone the Repo
Run the following command on the terminal:
`git clone https://github.com/DevWaweru/Car-Blog.git && cd Car-Blog`

Install [Postgres](https://www.postgresql.org/download/)
### Create a Virtual Environment
Run the following commands in the same terminal:
```bash
sudo apt-get install python3.6-venv
python3.6 -m venv virtual
source virtual/bin/activate
```

### Install dependancies
Install dependancies that will create an environment for the app to run
`pip3 install -r requirements`

### Prepare environment variables
```bash
export DATABASE_URL='postgresql+psycopg2://<your-username>:<your-password>@localhost/carblog'
export SECRET_KEY='Your secret key'
export DATABASE_URL_TEST='postgresql+psycopg2://<your-username>:<your-password>@localhost/carblog_test'
export MAIL_SERVER='smtp.googlemail.com'
export MAIL_PORT=587
export MAIL_USE_TLS=1
export MAIL_USERNAME=<your-email>
export MAIL_PASSWORD=<your-password> 
```

### Run Database Migrations
```bash
python manage.py db init
python manage.py db migrate -m "initial migration"
python manage.py db upgrade
```
### Running the app in development
In the same terminal type:
`python3 manage.py server`

Open the browser on `http://localhost:5000/`

## Known bugs
Sending batch emails bug
If there are other 

## Technologies used
    - Python 3.6
    - HTML
    - Bootstrap 4
    - JavaScript
    - Heroku
    - Postgresql

## Support and contact details
Contact me on developer.waweru@gmail.com for any comments, reviews or advice.

### License
Copyright (c) **Richard Waweru**