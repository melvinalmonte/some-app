# Some-app

This is just some app that lets you add users, fetch all users, fetch single user and delete user to a database.
Nothing fancy just a small app

## Getting Started

Just clone this repo.
### Prerequisites

Python 3 with pip3


### Installing

Once cloned go to the project root file and create a virtual environment

```
$ python3 -m venv .venv
```

Activate environment

for Linux and MacOS:
```
$ Source .venv/bin/activate
```
for Windows:
```
$ .venv/Scripts/activate.bat
```

Install dependencies:

```
$ pip install -r requirements.txt
```

###Run App

Ensure that your instance of mariadb is running

Set your environment variables:

```
$ source ./set_env db-username db-passwd db-hostname db-port db-name
```

Run it!

```
$ python app.py
```



## Example:

Add user to db:
```
curl -d '{"first_name":"jane", "last_name":"doe"}' -H "Content-Type: application/json" -X POST http://localhost:5000/users
```
Expected response:
```
{
"Message":"User Added"
}
```
Get all users in db:
```
curl -H "Content-Type: application/json" -X GET http://localhost:5000/users
```
Expected Response:

```json
{"users":
  [{
      "first_name":"jane",
      "last_name":"doe",
      "public_id":"be89585d-57bb-4c31-aa48-92079055713f"
  }]
}

```
Get single user in db:
```
curl -H "Content-Type: application/json" -X GET http://localhost:5000/users/public-id
```

Expected Response:

```json
{"user":
    [{
      "first_name":"jane",
      "last_name":"doe",
      "public_id":"be89585d-57bb-4c31-aa48-92079055713f"
    }]
}
```
Delete single user in db:
```
curl -H "Content-Type: application/json" -X DELETE http://localhost:5000/users/public-id
```

Expected Response:
```json
{
  "message":"User has been deleted"
}

```

## Built With


* [Python Flask](https://palletsprojects.com/p/flask/) - The web framework used
* [Maria DB](https://mariadb.org/) - Database used.