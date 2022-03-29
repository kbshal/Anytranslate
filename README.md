# Anytranslate
Anytranslate is an wrapper API for google translate


This python program fetches the data from [Google translate](https://translate.google.com/) and provides them in a pythonic and usable way


## About

This is a API wrapper for Google Translate.

## How to use?
Install poetry from [here](https://python-poetry.org/docs/) on your system
```sh
poetry shell
poetry install
```

And finally start the program by 
```sh
gunicorn trans_api:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8080
```

## Why use this?

- It is asynchronous.
- Data can be fetched in json format from endpoint



## LICENSE
 - Check the license from [here](https://github.com/kbshal/Anytranslate/blob/master/LICENSE)












