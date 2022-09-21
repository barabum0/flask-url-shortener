# Simple URL shortener written on Python using Flask Framework!
![Python Shield](https://img.shields.io/pypi/pyversions/requests) ![Flask Shield](https://img.shields.io/github/pipenv/locked/dependency-version/metabolize/rq-dashboard-on-heroku/flask)

## Showcase
#### Main page
![main page img](https://i.imgur.com/j6eBtHn.png)

#### Link does not exist page
![link 404 img](https://i.imgur.com/k5qWp0x.png)

##### I don't very skilled in frontend, so commit if you can make better!

## Setup:
Run this commands one by one
```
git clone https://github.com/barabum0/flask-url-shortener
pip install -r requirements.txt
```
And... It's done!

## Run:
Run this command in app.py directory
```
flask run
```

## Config
There is some options, that you can change. They're located in config.yml
```yaml
domain: localhost:5000/ #Domain, that will be given to user, when he will short link + link code.
```
```yaml
link_length: 5 #Shorten link length
```
```yaml
check_unique: 1 #If redirect link is in database, it won't create new
```
