import streamlit as st
import pandas as pd
import re
import numpy as np
from io import StringIO
from google.oauth2.service_account import Credentials
import json 
from datetime import datetime, timedelta
import gspread
import numpy as np

credentials_info = {
        "type": st.secrets["google_credentials"]["type"],
        "project_id": st.secrets["google_credentials"]["project_id"],
        "private_key_id": st.secrets["google_credentials"]["private_key_id"],
        "private_key": st.secrets["google_credentials"]["private_key"],
        "client_email": st.secrets["google_credentials"]["client_email"],
        "client_id": st.secrets["google_credentials"]["client_id"],
        "auth_uri": st.secrets["google_credentials"]["auth_uri"],
        "token_uri": st.secrets["google_credentials"]["token_uri"],
        "auth_provider_x509_cert_url": st.secrets["google_credentials"]["auth_provider_x509_cert_url"],
        "client_x509_cert_url": st.secrets["google_credentials"]["client_x509_cert_url"]
    }

scope = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]

credentials = Credentials.from_service_account_info(credentials_info, scopes=scope)

client = gspread.authorize(credentials)
def append_df_to_gsheet(sheet_name, worksheet_name, df):
    
    try:
        spreadsheet = client.open(sheet_name)
    except gspread.exceptions.SpreadsheetNotFound:
        st.error(f"Spreadsheet '{sheet_name}' not found.")
        return

    try:
        worksheet = spreadsheet.worksheet(worksheet_name)
    except gspread.exceptions.WorksheetNotFound:
        st.error(f"Worksheet '{worksheet_name}' not found in spreadsheet '{sheet_name}'.")
        return

    existing_data = worksheet.get_all_records()
    existing_df = pd.DataFrame(existing_data)
    combined_df = pd.concat([existing_df, df], ignore_index=True)
    worksheet.clear()

    worksheet.update([combined_df.columns.values.tolist()] + combined_df.values.tolist())