from datetime import datetime, timezone
from django.shortcuts import redirect, HttpResponse
from google_auth_oauthlib.flow import Flow
from calendarOAuth import credentialFile
from googleapiclient.discovery import build
import os, json

# 
# Read the Readme.md file
# 

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
scopes = ['https://www.googleapis.com/auth/calendar']
flow = Flow.from_client_config(client_config=credentialFile.getClientConfig(), scopes=scopes, redirect_uri='http://127.0.0.1:8000/rest/v1/calendar/redirect')

def GoogleCalendarInitView(request):
    authorization_url, _ = flow.authorization_url(access_type='offline')
    return redirect(authorization_url)

def GoogleCalendarRedirectView(request):
    flow.fetch_token(authorization_response=request.build_absolute_uri())
    credential = flow.credentials
    service = build('calendar', 'v3', credentials=credential)
    events_result = service.events().list(calendarId='primary', timeMin=datetime.utcnow().isoformat() + 'Z', singleEvents=True, orderBy='startTime').execute()
    events = events_result.get('items', [])
    return HttpResponse(json.dumps(events), content_type='application/json')