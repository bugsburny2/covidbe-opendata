# @Author ggrosjean(bugsburny2)
import requests
import tempfile
from zipfile import ZipFile
import tek_decode
import csv
import datetime
import sys
# This assumes that the TEK is renewed once every 24h on the device.

TEK_DOWNLOAD_PATH = "https://c19distcdn-prd.ixor.be/version/v1/diagnosis-keys/country/BE/date";
EXTRACTION_PATH = "temp_tek_folder"
DAYS_IN_PAST = 14
CSV_FILE_PATH = "../../static/csv/coronalert.csv"
# 1: Confirmed test - Low transmission risk level
# 2: Confirmed test - Standard transmission risk level
# 3: Confirmed test - High transmission risk level
# 4: Confirmed clinical diagnosis
# 5: Self report
# 6: Negative case
# 7: Recursive case
# 8: Unused/custom

RISK_MAP =  {
  0: "-",
  1: "Confirmed test - Low transmission risk level",
  2: "Confirmed test - Standard transmission risk level",
  3: "Confirmed test - High transmission risk level",
  4: "Confirmed clinical diagnosis",
  5: "Self report",
  6: "Negative case",
  7: "Recursive case",
  8: "Unused/custom"
}

# Argument new_file=
def main(new_file=False):
    csv_file_path = CSV_FILE_PATH

    # if sys.version_info >= (3, 0, 0):
    if (new_file):
        print('Overwriting everything in ', csv_file_path)
        file = open(csv_file_path, 'w', newline='')
    else:
        print('Appending data to ', csv_file_path)
        file = open(csv_file_path, 'a', newline='')
    # else:
    #     file = open(csv_file_path, 'wb')

    w = csv.writer(file,  dialect='excel')
    w.writerow({"DATE", "RISK_LEVEL", "COUNT"})

    # The size of each step in days
    day_delta = datetime.timedelta(days=1)
    if (new_file):
        start_date = datetime.date.today() - (DAYS_IN_PAST * day_delta)
    else:
        start_date = datetime.date.today() - (1 * day_delta)

    print('Oldest date retrieved:  ', start_date)
    end_date = datetime.date.today()

    for i in range((end_date - start_date).days):
        date = start_date + i*day_delta
        date_string = date.strftime('%Y-%m-%d')
        print("Retrieving date", date_string)

        tek_count_at_date = fetch_data_for_date(date_string)
        for i in range(len(tek_count_at_date)):
            csv_row = [date, RISK_MAP[i], tek_count_at_date[i]]
            w.writerow(csv_row)

def fetch_data_for_date(date_string):
    # fetch the zip file containing the new infection TEKs
    zip_filepath = fetch_tek_zip(date_string)
    extracted_folder = EXTRACTION_PATH + "/" + date_string
    extract_zip(zip_filepath, extracted_folder)

    payload_file = extracted_folder + "/export.bin"
    count_array = tek_decode.count_keys_in_file(payload_file)
    print (date_string, ":", count_array)
    return count_array

def fetch_tek_zip(date):
    filename = "coronalert.zip"
    file = open(filename, "wb")
    payload = requests.get(TEK_DOWNLOAD_PATH + "/" + date)
    file.write(payload.content)
    file.close()
    return file.name


def extract_zip(zipFilePath, targetDirectory):
    with ZipFile(zipFilePath, 'r') as zipObj:
        # Extract all the contents of zip file in different directory
        zipObj.extractall(targetDirectory)


import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
from flask_babel import gettext


def plotter():
    df_app = pd.read_csv(CSV_FILE_PATH)
    idx = pd.date_range(df_app.DATE.min(), df_app.DATE.max())
    print(df_app.DATE.min())
    print(idx)
    print(df_app.COUNT)
    df_app.index = pd.DatetimeIndex(df_app.index)
    newin_bar = go.Bar(x=idx, y=df_app.COUNT, name=gettext('#New Hospitalized'))
    # newin_bar = px.bar(x=df_app.index, y=df_app.COUNT)
    fig_hospi = go.Figure(data=[newin_bar], )
    fig_hospi.update_layout(template="plotly_white", height=500, margin=dict(l=0, r=0, t=30, b=0),
                            title=gettext("Temporary Exposure Keys"))
    return fig_hospi



main(True)