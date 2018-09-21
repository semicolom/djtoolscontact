# Django Tools Contact

Django Tools Contact is a simple Django app to manage a company contact information and contacts
requests from a form

## Quick start

1. Add "djtools.contact" to your INSTALLED_APPS setting like this::
```
INSTALLED_APPS = [
    ...
    'djtools.contact',
]
```

2. Add your Google Maps API key nd your contact information in your project settings:
```
DJTOOLS_CONTACT_GMAPS_APIKEY = "ABCDE123"
DJTOOLS_CONTACT_SITE_DOMAIN = "www.example.com"
DJTOOLS_CONTACT_MAIL_FROM = "no-reply@example.com"
DJTOOLS_CONTACT_MAIL_TO = ["admin@example.com"]

```

3. Add the settings context processor to use the `DJTOOLS_CONTACT_GMAPS_APIKEY` in your templates.
```
TEMPLATES = [
    {
        'OPTIONS': {
            'context_processors': [
                ...
                'djtools.contact.context_processors.settings_context',
            ],
        },
    },
]
```

4. Include the contact URLconf in your project urls.py like this:
```
path('contact/', include('djtools.contact.urls')),
```

5. Run `python manage.py migrate` to create the contact models.

6. Start the development server and visit http://127.0.0.1:8000/admin/
   to create add the contact information (you'll need the Admin app enabled).

7. Visit http://127.0.0.1:8000/contact/ to see the contact information and send contact requests.

## References
https://github.com/pydanny/cookiecutter-djangopackage/
