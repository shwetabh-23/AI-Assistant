
import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import datetime
from google.auth.transport.requests import Request

def get_emails():
    SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
    emails = {}
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                r'/media/harsh/01DA3D86EB842930/ML Projects/JARVIS---AI-Assistant/google-apis/credentials.json', SCOPES
            )
            creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("gmail", "v1", credentials=creds)
        results = service.users().messages().list(userId="me", labelIds=['INBOX'], maxResults=10).execute()
        messages = results.get("messages", [])

        if not messages:
            print("No messages found.")
        else:
            for message in messages:
                msg = service.users().messages().get(userId="me", id=message['id']).execute()
                subject = next(h['value'] for h in msg['payload']['headers'] if h['name'] == 'Subject')
                snippet = msg['snippet']
                emails[subject] = snippet
            return emails
    except HttpError as error:
        if error.resp.status == 401:
            print("Authorization error. Please re-run the script.")
        else:
            print(f"An error occurred: {error}")

def get_date_day():
    
    current_datetime = datetime.datetime.now()

    current_date = current_datetime.date()
    current_day = current_datetime.strftime("%A")  
    current_time = current_datetime.time()

    return current_date, current_day

def get_time_of_day():
    current_hour = datetime.datetime.now().hour

    if 5 <= current_hour < 12:
        return "Morning"
    elif 12 <= current_hour < 17:
        return "Afternoon"
    else:
        return "Evening"

if __name__ == '__main__':
    date, day = get_date_day_time()
    get_emails()
    time_of_day = get_time_of_day()
    breakpoint()
