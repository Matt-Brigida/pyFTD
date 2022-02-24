import pandas as pd

base_url = "https://www.sec.gov/files/data/fails-deliver-data/cnsfails"




url = "https://www.sec.gov/files/data/fails-deliver-data/cnsfails202201b.zip"

ftds = pd.read_csv(url, compression='zip', delimiter='|')
