[![Typing SVG](https://readme-typing-svg.demolab.com/?lines=Learn+Wagtail;Beginner+Friendly;Follow+README.md+for+steps)](https://git.io/typing-svg)

[Documentation](#Documentation)
[Installation](#Installation)

## What is Wagtail?
Wagtail is an open-source Django Content Management System (CMS) powered by python.

## Installation

For Linux/Mac

On your terminal:

- Install wagtail with pip (install pip if you do not have it installed.)
```bash
  pip install wagtail
```
- To verify installation:
```bash
  pip show wagtail
```

## Start a new project

- {project-name} could be anything you wish to name your project.
```bash
  wagtail start {project-name}
```

```bash
  cd {project-name}
```

## Set up a virtual Environment

- If you have python3, then type python3  instead of python.
```bash
  python -m venv .venv
```

- Activate virtual environment:
```bash
  source .venv/bin/activate
```

- Install all requirements for wagtail in venv:
```bash
  pip install -r requirements.txt
```

## Set up the server

- Start the server
```bash
  python manage.py runserver 0:8000
```

- Now you will see "unapplied migrations", so hit 'ctrl+C' to quit the server and type:
```bash
  python manage.py migrate
```

- Start server again
```bash
  python manage.py runserver 0:8000
```

> NOTE: If you get an error saying "That port is already in use", then first type:
```bash
  sudo fuser -k 8000/tcp
```
- This will kill the running port process.
- Then start server again.

## Localhost:8000

- Now open the localhost:8000 on any browser.
![Screenshot from 2024-03-10 23-39-02](https://github.com/uzayr-iqbal-hamid/learn-wagtail/assets/134723279/6b4cc37b-e720-4f47-a9e3-a0b632a489a5)


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

## Edit the Home page

- Open the project folder with VS Code or any IDE you use.
- Go to home/templates/home/home_page.html file
- Start editing to see the changes in the home page.
![Screenshot from 2024-03-10 23-23-44](https://github.com/uzayr-iqbal-hamid/learn-wagtail/assets/134723279/0b1e2bb9-f42e-4505-a6b2-8063b6ef71a1)


## Extend the HomePage model

- On the home/models.py
```bash
  from wagtail.admin.panels import FieldPanel
```

- Under the class HomePage(Page):
```bash
  banner_title = models.CharField(max_length=100, default='welcome')
```

- On your terminal, make migrations:
```bash
  python manage.py makemigrations
```
- migrate the changes
```bash
  python manage.py migrate
```
- Add FieldPanel:
```bash
  content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
  ]
```
![Screenshot from 2024-03-10 23-22-18](https://github.com/uzayr-iqbal-hamid/learn-wagtail/assets/134723279/bd20d3c0-da87-4035-87bf-e2ee1d6d682d)

## Documentation

Refer the Wagtail Documentation for further assistance: https://docs.wagtail.org/en/latest/releases/6.0.html
