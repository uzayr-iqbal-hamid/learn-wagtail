# learn-wagtail


## Installation

On Linux/Mac

On your terminal:

```bash
  pip install wagtail
```
To verify installation:
```bash
  pip show wagtail
```

## Start a new project

```bash
  wagtail start {project-name}
```

```bash
  cd {project-name}
```

## Set up a virtual Environment

```bash
  python -m venv .venv
```

To activate virtual environment:
```bash
  source .venv/bin/activate
```

Install all requirements for wagtail in venv:
```bash
  pip install -r requirements.txt
```

## Set up the server
```bash
  python manage.py runserver 0:8000
```

Now you will see "unapplied migrations", so hit 'ctrl+C' to quit the server and type:
```bash
  python manage.py migrate
```

Start server again
```bash
  python manage.py runserver 0:8000
```

> NOTE: If you get an error saying "That port is already in use", then first type:
```bash
  sudo fuser -k 8000/tcp
```
This will kill the running port process.
Then start server again.

## Localhost:8000

Now open the localhost:8000 on any browser.

## Set admin user

- Quit the server 'ctrl+C'.

- Then type:
```bash
  python manage.py createsuperuser
```
- Enter the username and password.

- Run the server again.

- Go to localhost:8000.

- Click on admin login.

- Enter the username and password to sign in.

