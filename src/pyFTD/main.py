import pandas as pd
import time

# Example URL:
# "https://www.sec.gov/files/data/fails-deliver-data/cnsfails202201b.zip"
# is for the second half of January 2022.  The first half would be 202201a
# Data are available from the SEC for the interval

def pull_month(year, month):
    """Retrive a month of failure to deliver data.

    Keyword arguments:
    year -- integer year (default none)
    month -- integer month, with no leading 0 (default none)
    """
    if month < 10:
        month = "0" + str(month)
    base_url_a = "https://www.sec.gov/files/data/fails-deliver-data/cnsfails" + str(year) + str(month) + "a.zip"
    base_url_b = "https://www.sec.gov/files/data/fails-deliver-data/cnsfails" + str(year) + str(month) + "b.zip"
    ftds_a = pd.read_csv(base_url_a, compression='zip', delimiter='|', on_bad_lines='warn')
    ftds_a.dropna(axis = 0, how = 'any', inplace = True)
    time.sleep(10)
    ftds_b = pd.read_csv(base_url_b, compression='zip', delimiter='|', on_bad_lines='warn')
    ftds_b.dropna(axis = 0, how = 'any', inplace = True)
    month_data = pd.concat([ftds_a, ftds_b], axis = 0).reset_index(drop=True)
    return(month_data)
    





