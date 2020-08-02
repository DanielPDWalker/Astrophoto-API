# Astrophoto-API 
![](https://img.shields.io/github/workflow/status/danielpdwalker/Astrophoto-API/Django%20CI/master)  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An astrophotography Django project for tracking your pictures of targets in the night sky. The application comes with a database with the messier objects pre-loaded, and two other models for adding your own captured images. These are one catagory called "Asteroids, Comets and Meteors" and one called "Solar System Objects" for more general objects in the solar system; planets, moons and so on. 

There are 3 APIs, (that are also browsable) for loading/downloading/updating bulk information if needed, though I have also added the ability to maintain information through the Django admin area. 

Finally I added a frontend for a nice way to display your images. On the frontend there is also a little filtering system to show what you have and havent captured, so you know what targets you have in the database that you still need to go for.


## Features
Images and Information at: [https://danielpdwalker.com/astrophoto_application_api](https://danielpdwalker.com/astrophoto_application_api)

(Just images at the bottom of this readme)

- Three rest APIs for each of the target types. Messier Objects, Asteroids, Comets and Meteor and Solar System Objects.
- Kept to the rest specifications, though the APIs are fully browsable through the front end.
- Frontend to display images as well as saved information about the target.


## How to use
1. Clone this repository, or download as ZIP if you wish.
2. Install the latest version of python 3.
4. Using your terminal of choice, move to the location you have saved this application.
5. Create a virtual enviroment (A version of python you will use just for using this app). 
```python3 -m venv venv```
6. Start the virtual enviroment ```source venv/bin/activate``` linux/mac or ```source venv/scripts/activate``` on windows
7. Install the requirements ```pip install -r requirements.txt```
8. Start the app ```python3 manage.py runserver```
9. Open your browser of choice and go type ```localhost:8000``` in the address bar.
- To login to the admin area you go to ```localhost:8000/admin``` and use the username: admin and password: password
- You can login as admin in the browsable API area as well, top right of the top bar. 

Please note: You will have to navitage to the application folder and activate the virtual enviroment whenever you want to run it!

You can right click in the folder and "Open terminal here" or something like that, start your virtual enviroment then start with your commands without the navigation though!

## Images
<hr>

![Homepage](https://github.com/DanielPDWalker/Astrophoto-API/blob/master/.readme_images/homepage.JPG)
<hr>

![Messier Objects](https://github.com/DanielPDWalker/Astrophoto-API/blob/master/.readme_images/messier_objects.JPG)
<hr>

![Admin Area](https://github.com/DanielPDWalker/Astrophoto-API/blob/master/.readme_images/admin_area.JPG)
<hr>

![API Root](https://github.com/DanielPDWalker/Astrophoto-API/blob/master/.readme_images/api_root.JPG)
<hr>

![Messier Objects API](https://github.com/DanielPDWalker/Astrophoto-API/blob/master/.readme_images/messier_objects_api.JPG)
