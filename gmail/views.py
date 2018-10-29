from .credentials import google_credentials
from django.shortcuts import redirect, reverse, render
from django.http import HttpResponseRedirect
from django_google_api_example import settings
from google_auth_oauthlib.flow import Flow
from google.auth.transport.requests import AuthorizedSession
import json

flow = Flow.from_client_secrets_file(
    settings.GOOGLE_OAUTH2_CLIENT_SECRETS_JSON,
    scopes=['https://www.googleapis.com/auth/userinfo.profile', 'https://www.googleapis.com/auth/userinfo.email',
            'https://www.googleapis.com/auth/gmail.readonly'],
    redirect_uri='http://localhost:8000/gmail/oauth_return')


def start_oauth_flow(request):
    auth_url, _ = flow.authorization_url(prompt='consent')
    return redirect(auth_url)


def oauth_return(request):
    code = request.GET['code']
    flow.fetch_token(code=code)

    # Get user email address
    session = flow.authorized_session()
    user_info = session.get('https://www.googleapis.com/userinfo/v2/me').json()
    user_email = user_info['email']

    # Store user's Google credential.
    google_credentials[user_email] = flow.credentials

    # Update login user in Django session
    request.session['user'] = user_email

    return HttpResponseRedirect(reverse('gmail:index'))


def index(request):
    return render(request, 'gmail/index.html')


def messages(request):
    q=request.POST['q']

    # Load credential
    user = request.session['user']
    credentials = google_credentials[user]
    authed_session = AuthorizedSession(credentials)

    # Call Gmail API
    parameter = {'q': q}
    response = authed_session.get(
        'https://www.googleapis.com/gmail/v1/users/me/messages', params=parameter)
    messages = json.loads(response.text)['messages']

    context = {'messages': messages, 'q': q}
    return render(request, 'gmail/messages.html', context)
