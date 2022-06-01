# Python 401d18

## Lab(33): RESTful docker Django, nopw with gunicorn and JWT auth. 

### Author: Tyler Egashira

### Setup

$ docker-compose up
Use postman or Thunderclient
with default admin you can get an API token from "http://0.0.0.0:8000/api/token/" via POST method
with that token in hand you will be able to make a GET request at "http://0.0.0.0:8000/api/v1/stuffed_animals/"

Look at them stuffies! 

### Features

  * admin
  * users
  * CRUD Functionality w/ permissions
  * JWT authorizations

### User Acceptance Tests:

* post, update, delete methods working as intended
* unable to delete when logged out

### Routes

1. admin/
2. api/v1/stuffed_animals/
3. api-auth/
4. api/token/ [name='token_obtain_pair']
5. api/token/refresh/ [name='token_refresh']