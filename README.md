# DjToolsContact

DjToolsContact is a simple Django app to manage a company contact information and contacts
requests from a form

## Quick start

1. Add "contact" to your INSTALLED_APPS setting like this::
```
INSTALLED_APPS = [
    ...
    'djtools.contact',
]
```

2. Add your Google Maps API key in your project settings GOOGLE_MAPS_API_KEY

3. Add the settings context processor to use the `GOOGLE_MAPS_API_KEY` in your templates.
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
4. Include the contact URLconf in your project urls.py like this::
```
path('contact/', include('contact.urls')),
```
5. Run `python manage.py migrate` to create the contact models.

6. Start the development server and visit http://127.0.0.1:8000/admin/
   to create add the contact information (you'll need the Admin app enabled).

7. Visit http://127.0.0.1:8000/contact/ to see the contact information and send contact requests.
