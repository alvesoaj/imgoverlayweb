## WHAT IS THIS?

Just a very simple WEB APP to insert a watermarker to an uploaded image.

Don't wore about all files, if you just care about the application, just look at:

```
app.py
static/dog.png
templates/home.html
requirements.txt
```

All others is for deploy

### INSTALL DEPENDENCES (HERE WE ARE USING PYTHON3)

#### update pip3 and setuptools

`pip3 install --upgrade pip3 setuptools`

#### install flask - web framework

`pip3 install flask`

#### install fabric - deploy automator (Using a nonoficial port to py3)

`pip3 install fabric3`

#### and/or just install everything with:

`pip3 install -r requirements.txt`

### RUN DEV SERVER

`FLASK_APP=app.py flask run` or `python3 app.py`

### DEPLOY

#### create host config (change it)

`echo '000.000.000.000' > host.txt`

#### perform deploy

`fab deploy`
