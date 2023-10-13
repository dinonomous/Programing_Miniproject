# Programing_Miniproject
 
LMS file is the main project file created by django

# django-admin startproject LMS

we can see LMS file again and landing_page(app) in side of main LMS folder the LMS file in side the main LMS is the main app into which the quaries from users come and gets suparated into suburls(made by different apps) to create apps 

# django-admin startapp landing_page

the quaries from user is recived to the urls.py in the LMS app if user request for a main url (or) "\ " the main page of website 

the urls in the LMS transfers the path to urls in landing page

the urls in the landing page checks for the request and transfer the controls to different functions in the views.py file depending on the request of user

in views.py a function index which return the HTML page which is stored in templates folder 

all the HTML,CSS,JS files are to located in templates 

to run the server and launch the website we use 

make shure that you are in right folder so that you can access manage.py

# python manage.py runserver