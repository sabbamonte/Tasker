Since Covid-19 hit the world it made me and my wife rethink our priorities and goals in life.
I started the programming journey in June and it sparked the desire in me to become a Web Developer.
I fell in love with it, especially Back-End Developing. 

We are both back in school and since everything is online I was looking for a way to help her consolidate subjects, links and notes to each specific subject as well as tasks, be it for school or professional life.

This is why I created Tasker. It's a web application where you can save, add and edit General Tasks and Notes for each specific subject of your choosing. My wife complained to me that whenever she's studying a particular subject, she has to go find and pull up different links for each every time she studies it. This is why I included links for her so that she would be able to consolidate everything. This makes it quick and easy to use. She will be able to go straight to work and not waste time setting everything up every time. This creates a type of Organizer where you can just pull Tasker up and everything will be in one place and organized. It will be your starting place for whenever you're ready to work and/or study. No need to carry around several notebooks for each individual subject or tasks. Everything will be in one place at your finger tips and easy to use. Tasker is unique to each user since I included a User model as well as others to save the custom tasks, subjects etc. to the Django database.

I am very proud of my project and being able to help someone through technology, be it something small. It showcases how far I've come since taking my very first class. I did not have any prior knowledge before the start of this journey. While I was creating this project I was trying to incorporate every single aspect of what we've learned in this course. For this reason I believe it sets itself apart from the prior projects, where each one tackled only the subject we've learned in that week's lecture. However, this project intentionally includes every aspect of the past projects and lectures, thus becoming something unique, complex yet recognizable. In my opinion this will satisfy the requirements and complexity to pass this Final Project. I really hope you enjoy it and would love some feedback, if possible.

What it contains:
Inside the main project's directory is the application called Tasker. 
In the static folder you will find the CSS file as well as the Javascript file (script.js)
script.js includes all of the code to make the app more responsive and interactive. In there I also included several fetch commands for different API's that tie into my views.py/urls.py where all the paths are.
In views.py I created all the Python code to the routes/paths of the app. Through GET, POST and PUT I manipulate the objects either through the data provided through JSON or through a <form> in the HTML templates. 
The templates folder contains all the HTML files of the app.
models.py has all the different models/objects in it. I created a User as well, so that the app is unique to each user. I also created a superuser to manipulate the admin interface, hence the admin.py file.
I don't believe I downloaded any additional libraries besides pylint. But that seems to be necessary to run Python on VSC anyway.

