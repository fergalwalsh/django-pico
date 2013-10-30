
1. `pip install django-pico`


2. Add "djpico" to your INSTALLED_APPS setting like this:
```
    INSTALLED_APPS = (
        ...
        'djpico',
    )
```


3. Include the polls URLconf in your project urls.py like this::

    `url(r'^pico/', include('djpico.urls')),`



See [Pico](https://github.com/fergalwalsh/pico/) for more information.