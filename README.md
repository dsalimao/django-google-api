# Sample code to call Google API in Django

Google documented an [example](https://developers.google.com/api-client-library/python/guide/django) to use Google API with Django.
And here is the [code](https://github.com/googleapis/google-api-python-client/tree/master/samples/django_sample) in github.

Problem is [oauth2client](https://pypi.org/project/oauth2client/) lib is deprecated, and is not compatible with latest versions of Django.

This is a simple example to use Google API with Django 2.1.

## Dependencies
[google-auth](https://google-auth.readthedocs.io/en/latest/)

[oauthlib](https://oauthlib.readthedocs.io/en/latest/installation.html)

## Try it

Config [API credentials](https://console.cloud.google.com/apis/credentials) in Google Cloud console.

Modify [client_secrets.json](https://github.com/dsalimao/django-google-api/blob/master/client_secrets.json)

```shell
python3 manage.py runserver
```

Then point to [localhost:8000/gmail/start_oauth_flow](http://localhost:8000/gmail/start_oauth_flow)
You should see Google login page.

Click to continue, and it jumps to a query form. Try to enter a query string and click *Query* button. It will make a call
to [Gmail API](https://developers.google.com/gmail/api/v1/reference/),
and show [messages](https://developers.google.com/gmail/api/v1/reference/users/messages/list) found.
