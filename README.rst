# Wordpress to CSV

This app exports Wordpress post to csv. It uses [django-wordpress](https://github.com/istrategylabs/django-wordpress). Tested with Python 3.6/Django 1.11.

## How to use from A to Z

1. ``' git clone https://github.com/xenu256/wordpress_to_csv```
2. ``` cd wordpress_to_csv```
3. If WP site is already dropped, just create new database and import backup there.
4. Edit settings.py with Wordpress database prefix and credentials
5. ``` python manage.py wpexport ```
6. Collect csv from exports/ and use it for better site.
