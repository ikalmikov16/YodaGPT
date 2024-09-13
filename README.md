# YodaGPT in Django

This Project is a Web App where you can chat with Master YodaGPT built with the OpenAI API.
The purpose of this AI chatbot is to behave as a personal and mental advisor, offering guidance and wisdom in a fun way using Yoda's character.
YodaGPT will provide thoughtful and profound advice on personal and mental matters, using philosophical insights.
YodaGPT will encourage self-reflection and growth, inspiring calm, clarity, and self-improvement.

It maintains chat context and also offers the option to delete specific messages by the click of a button.
You can check out how it works here: https://ika16.pythonanywhere.com/chatbot

## Backend
The project is built in Django and includes some of its built-in features like user authentication.
I  created a Message database model, where each object stores a question, 
answer, time created, and foreign key relationship to its user.

Upon each new message request, the program retrieves all previous messages from the database, sends them to the 
OpenAI API for context, creates the newest message object, and returns all the messages for output.
For the Message deletion function, it deletes the message object from the database and rerenders the page.

## Frontend
For the frontend, I used Bootstrap for the navbar, text input, and buttons. 
For the user authentication forms I used Django's built in forms and crispy-forms package for styling.
The rest of the pages, I designed myself using html and css. This includes the home and chatbot pages.

### If you would like to install the project and use it locally:
* Create a virtual environment and install the dependencies from requiremnts.txt
* Create .env file and include your Django secret key, openai api key, and database information
* You would also have to connect the project to your own MySQL database, or use sqlite3