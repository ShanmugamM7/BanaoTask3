# calendar_api.py
import os
from datetime import datetime, timedelta
from google.oauth2 import service_account
from googleapiclient.discovery import build



SERVICE_ACCOUNT_FILE = r"C:\Users\macha\Music\Git\Django_Projects\BanaoTask1\secrets\calendarapi-415015-7475e6f832ac.json"
SCOPES = ['https://www.googleapis.com/auth/calendar']

def get_calendar_service():
    # import pdb;pdb.set_trace()
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    return build('calendar', 'v3', credentials=credentials)

def create_calendar_event(start_datetime):
    # import pdb;pdb.set_trace()

    service = get_calendar_service()
    start_datetime = start_datetime + timedelta(minutes=390)-timedelta(hours=12)
    end_datetime = start_datetime + timedelta(minutes=45)

    starttime_str = start_datetime.strftime("%Y-%m-%dT%H:%M:%S")
    endtime_str = end_datetime.strftime("%Y-%m-%dT%H:%M:%S")
    event = service.events().insert(
            calendarId='86bc9f929817710fd2fa13b1a606aaf468f19cb58ec7994ae7dacba7e664eb2a@group.calendar.google.com',
            body={
        'summary': 'Doctor-Patient Appointment',
        'description': 'Appointment Scheducle confirmed',
        'start': {
            # 'dateTime': '2024-02-21T10:00:00',
            'dateTime': starttime_str,  # Adjust the date and time
            'timeZone': 'UTC',  # Specify the time zone
        },
        'end': {
            # 'dateTime': '2024-02-21T10:45:00',
            'dateTime': endtime_str,  # Adjust the date and time
            'timeZone': 'UTC',  # Specify the time zone
        }
            }
        ).execute()       
    
    return event
