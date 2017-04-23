Welcome to Message Board!
==========================


Hey! This is the ReadMe file for **MessageBoard**. This will help you in Getting Started with the projecct.

----------

Installation
-------------
Message board is built using Python, Django and MySQL so you will need to have python, django and mysql setup in your system. Won't go into the details of setting up python and django.

Additionally you will need these python frameworks to setup the application:

> **Django Rest Framework:**
> 1. pip install djangorestframework
> 2.  pip install markdown



#### <i class="icon-folder-open"></i> Setting It Up

Please clone the repo in your local system using **git clone** statement. Once you have cloned the repo you will need to add a specific database and user in your MySQL database.

#### <i class="icon-pencil"></i> Create Database and User in MySQL

Please use the commands given below after opening mysql command line as the root user.

>CREATE database msg_board;
>CREATE USER 'myuser'@'localhost' IDENTIFIED BY 'myuser123';
>GRANT ALL PRIVILEGES ON *.* TO 'myuser'@'localhost';
>FLUSH PRIVILEGES;

Alternatively you can edit the settings file located at (msg_borad/msg_board/settings.py) and change your database settings accordingly.

#### <i class="icon-pencil"></i> Django Migrations
Please navigate to **msg_board** folder on your command line and you will see a **manage.py** file there. Once you are there, please run the following commands to set up the database and models.
> python manage.py migrate
> python manage.py makemigrations board
> python manage.py migrate board

This will create all necessary models for you to run the project. 
(Optional): Please run **python manage.py createsuperuser** if you intend to use Django Admin panel which can be handy in managing the messages or creating secret tokens.

#### <i class="icon-hdd"></i> Running The Project

One you are done with all the settings and configurations, please run **python manage.py runserver** and this will run a local django server on your machine. Open your browser and navigate to <a>127.0.0.1:8000</a> or <a>http://localhost:8000/</a> and you be seeing the home screen where you can post messages.

----------

API Details
-------------------
We have create 4 specific apis for this app which you can use. Given below are the details.

#### Post Message API
**Request Type**:  Post
**URL**: <a>http://localhost:8000/api/msg-board/post-msg</a>
**Post Params**: Add a **text** field with the message you want to post. The message length has been restricted to 140 characters.
**Optional Params**: You can also add **sender_name** and **sender_email** in the post data.

**OUTPUT**
The output would contain a json with the status and the message id. Sample shown below:
> {"message":"Message posted successfully",
> "message_id":32,
> "success":true}


####  Retrieve All Messages API
**Request Type**:  Get
**URL**: http://localhost:8000/api/msg-board/get-all-msgs

**OUTPUT**
The output would contain a json with the status and the message id. Sample shown below:
> {
  "count": 1,
  "success": true,
  "msgs": [
    {
      "sender_name": "anonymous",
      "created_at": "2017-04-24 00:54:18.547631",
      "msg_text": "taeeada",
      "sender_email": "None",
      "msg_source": "127.0.0.1",
      "id": 32
    }
  ]
}

####  Delete Message API
**Request Type**:  Get
**URL**: http://localhost:8000/api/msg-board/delete-msg
**Get Params**: ID: message id of the message to be deleted and token: secret token
**Sample URL**: http://localhost:8000/api/msg-board/delete-msg?id=1&token=amandakdajdajadajdaajadjajadad

**OUTPUT**
The output would contain a json with the status and a message. Sample shown below:
> {
  "message": "Message deleted successfully",
  "success": true
}

####  Delete All Message API
**Request Type**:  Get
**URL**: http://localhost:8000/api/msg-board/delete-all-msgs
**Get Params**: token: secret token
**Sample URL**: http://localhost:8000/api/msg-board/delete-all-msgs?token=amandakdajdajadajdaajadjajadad

**OUTPUT**
The output would contain a json with the status and a message. Sample shown below:
> {
  "message": "Message deleted successfully",
  "success": true
}


Secret Tokens
-------------

Created a separated model for secret tokens named **SecretToken**. You can use django admin panel for managing secret tokens.
