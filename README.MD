# Bitly URL Shortener


This script uses [Bitly API](https://bitly.com) to create short versions of given Hyperlinks known as Bitlinks. It can also be used to fetch total amount of click for previously created Bitlinks.


### Installation guidelines


You must have Python3 installed on your system.
You may use `pip` (or `pip3` to avoid conflict with Python2) to install dependencies.
```
pip install -r requirements.txt
```
It is strongly advised to use [virtualenv/venv](https://docs.python.org/3/library/venv.html) for project isolation.

In order to access Bitly API endpoints, you'll need a valid 'access_token' ([get it here](https://app.bitly.com/settings/api/))

This script uses `.env` file in root folder to store the 'access_token'. So, do not forget to create one!

Here is how contents of your `.env` file should look like:
```
BITLY_ACCESS_TOKEN='putyouraccesstokenhere'
```


### Basic usage (for the lack of any other...)

```
py main.py https://google.com
Bitlink: https://bit.ly/######

py main.py https://bit.ly/######
Click count: 0
```
You can use `-h` flag to display help message
```
py main.py -h
```

### Project goals

This project was created for educational purposes as part of [dvmn.org](https://dvmn.org/) Backend Developer course.