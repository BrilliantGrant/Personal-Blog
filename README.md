# Personal Blog

This project was generated with python3.6 Flask framework

Personal Blog is an application that helps in creating and sharing your opinions also other users can read and comment on them.

#### 9th February 2018

### By Brilliant Kaimba briegrant416@gmail.com

### Description

This is an application that helps in creating and sharing your opinions also other users can read and comment on them.

## User Stories
As a user I would like to:
* View the blog posts submitted
* Comment on blog posts
* Be alerted when a new post is made by joining a subscription.

As a writer I would like to:
* Sign in to the blog.
* Create blog posts from the application.
* Delete comments that I find insulting or degrading.
* Update or delete blogs posts I have created.

## Specifications

| Behavior        | Input           | Outcome  |
| ------------- |:-------------:| -----:|
| Register to be a user | Your email : bri@g.com <br> Username : bri101 <br> Password : bri1 | New user is registered |
| User Log in | Your email :bri@g.com <br> Password : bri1 | Logged in |
| Display post title | N/A | List of post titles with the writer's name |
| See an entire post | **Click** on a **post's title** | Directed to a page with the post's title, writer's name and comments on the post |
| Comment on a post | **Click Comment** | An authenticated user is directed to a page with a form where the user can create and submit a comment on a post |
| Writer Log in | Your email : writer@login.com <br> Password : writer | Logged in and can access writer's routes |
|
| Create a Post | **Click Create Post** | An authenticated user with a writer's role is directed to a page with a form where the user can create and submit a new post |
| Delete a comment | **Click delete** for the specific comment | An authenticated user with a writer's role deletes a comment |
| Delete a post | **Click Delete Post** | An authenticated user with a writer's role deletes a post and its comments |
| Update a post | **Click Update Post** | An authenticated user with a writer's role is directed to a page with a form where the user can update the post and submit it |

## Setup/Installation Requirements

* install Flask $ python3.6 -m pip install flask
* Install python version 3.6
* Install gunicorn: (virtual)$ python3.6 -m pip install gunicorn
* Install Heroku cli that helps to deploy your application.
* Clone https://github.com/BrilliantGrant/Personal-Blog.git
* Atleast have a computer or a laptop
* Have an internet connection
* Visit  https://blogbri.herokuapp.com/

## Known Bugs

There are No known bugs

## Technologies Used
* Python3.6
* Flask framework
* Flask
* Bootstrap
* Postgres Database





