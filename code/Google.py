from __future__ import print_function
import os.path
import json
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials


class google_api:
    def __init__(self):
        print(os.getcwd())
        with open(f"{os.getcwd()}/data/credentials.json", "r") as cred_file:
            cred = (json.load(cred_file))["google"]
            if cred["username"]  == "" and cred["password"] == "":
                raise Exception("username and password are empty, edit credentials file")

    def connect(self):
        print("Connecting to google...")

    def upload_calendar(self):
        pass

    def check_conflicts(self):
        pass


if __name__ == "__main__":
    goog = google_api()
    goog.connect()
