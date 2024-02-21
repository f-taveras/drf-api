# LAB - Class 31/32
## Project: Django REST Framework & Docker Overview
### Author: Felix A. Taveras
### Links and Resources

* [REST Framework Tutorial](https://learndjango.com/tutorials/official-django-rest-framework-tutorial-beginners)
* [Install Docker - Ubuntu](https://www.howtogeek.com/devops/how-to-install-and-get-started-with-docker-desktop-on-linux/)

__Setup no docker:__

__install/activate__ the virtual environment:

    python3 -m venv .venv
    source .venv/bin/activate

Install requirements:
    
    pip install -r requirements.txt

How to initialize/run your application (where applicable)

    python manage.py runserver


__Setup using Docker:__

* make sure to install __docker compose__(see resources)
    
        docker compose build
        docker compose up