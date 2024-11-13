# import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar"]


def update_event(new_event):
    '''Updates a new google calendar event using the google API'''
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    try:
        service = build('calendar', 'v3', credentials=creds)
        event = service.events().insert(calendarId='primary', body=new_event).execute()
    except HttpError as error:
        print(f"An error occurred: {error}")


def create_event(day, progess, current, title):
    '''Creates a json event'''
    event = {
            'summary': "Read " + title + " to " + progess + ' ' + str(current),
            'start': {
                'dateTime': day.isoformat() + 'T08:00:00-07:00',
                'timeZone': 'America/New_York',
                },
            'end': {
                'dateTime': day.isoformat() + 'T09:00:00-07:00',
                'timeZone': 'America/New_York',
                },
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'popup', 'minutes': 10},
                    ],
                },
        }

    return event
