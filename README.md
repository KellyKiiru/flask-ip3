# Pitch App

![project's landing page](./app/static/resources/Screenshot%20from%202022-05-15%2011-48-21.png)

## By Kelly Kiiru

This is a Flask application that allows users to submit their one minute pitches and other users to vote on them and leave comments of their feedback on them. The pitches are organized by category. 


## Table of Content

+ [Description](#description)
+ [Setup/Installation Requirements](setup&installationrequirements)
+ [BDD & TDD](#bdd&tdd)
+ [UserStory](#userstory)
+ [Technology & Tools](#technology&tools)
+ [Reference](#reference)
+ [Licence](#licence)
+ [Authors Info](#authors-info)

## Description

This is a Flask application that allows users to submit pitches where other users can also create their own pitches and leave comments to other pitches by previous users. 


## Setup Installations Requirements
   * To run the application, in your terminal:

    1. Clone this [github repo] (https://github.com/KellyKiiru/flask-ip3.git)
    2. Create a virtual environment
    3. Read the requirements file and Install all the requirements. Or run pip3 install -r requirements.txt to automatically install all the requirements
    4. Prepare environment variables
    -export DATABASE_URL='postgresql+psycopg2://username:password@localhost/pitching'
    -export SECRET_KEY='Your secret key'
    4. Run chmod a+x start.sh
    5. Run ./start.sh
    6. Access the application through `localhost:5000`
  
#### Prerequisites

You must have git, flask, postgres and python3.8+ installed in your pc.
To install flask and Postgres, you can use the following commands:

#flask
$ pip install flask

#postgres
$ sudo apt-get install postgresql postgresql-contrib libpq-dev

### Development

Want to contribute? Great!

To fix a bug or enhance an existing module, follow these steps:

- Fork the repo
- Create a new branch (`git checkout -b improve-feature`)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (`git commit -am 'Improve feature'`)
- Push to the branch (`git push origin improve-feature`)
- Create a Pull Request 


### Deployment environment
* Heroku

## BDD
| Behaviour | Input | Output |

| Display the pitches categories. | **On page load** | Each category can be viewed on click |
| Authentication Required | **Add New Pitch** | Redirected to a Login/Registration Page |
| Display form where one can add comments  | **Add Comments** | Redirected to view Comments Page |
| Display Profile of User | **Click User Profile** | Redirected to Update Profile Page



## TDD

To test the app, run this command in the terminal;

`$ python3 manage.py test`


## User Story
* A user can see the pitches other people have posted.
* A user can be signed in and leave a comment.
* A user can vote on the pitch they liked and give it a downvote or upvote. -[bug]
* A user can view the pitches they have created in their profile page
* A user can comment on the different pitches and leave feedback
* A user can submit a pitch in any category.
* A user can view the different categories

### Technology & Tools
* Python
* Flask
* HTML
* CSS
* Bootstrap
* Postgres
* Javascript(jQuery)
* Pip

## Reference

* [Setting up Postgres, SQLAlchemy, and Alembic](https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/)
* [Flask for Beginners](https://www.fullstackpython.com/flask.html)


## License

MIT License

Copyright (c) 2022 `Kelly Kiiru` 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Authors Contact Details

* [Email](infowithkiiru@gmail.com)
* [LinkedIn](https://www.linkedin.com/in/kiiru-ryan-15a852231/)

