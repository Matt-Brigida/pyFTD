import pandas as pd

# url = "https://www.sec.gov/files/data/fails-deliver-data/cnsfails202201b.zip"

def pull_month(int year, int month):
    if month < 10:
        month = "0" + str(month)
    base_url_a = "https://www.sec.gov/files/data/fails-deliver-data/cnsfails" + str(year) + str(month) + "a.zip"
    base_url_b = "https://www.sec.gov/files/data/fails-deliver-data/cnsfails" + str(year) + str(month) + "b.zip"
    ftds_a = pd.read_csv(url, compression='zip', delimiter='|')
    





