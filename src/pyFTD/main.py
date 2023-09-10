import pandas as pd
import time

# Example URL:
# "https://www.sec.gov/files/data/fails-deliver-data/cnsfails202201b.zip"
# is for the second half of January 2022.  The first half would be 202201a
# Data are available from the SEC for the interval

## Unnecessary class approach---------

## @pd.api.extensions.register_dataframe_accessor("ftd")
class FTDdata:
    def __init__(self, year: int, month: int):
        self.year = year
        self.month = month
        # self._validate(pandas_obj)
        # self._obj = pandas_obj

    # @staticmethod
    def pull_month(self):
        """Retrive a month of failure to deliver data.

        Keyword arguments:
        year -- integer year (default none)
        month -- integer month, with no leading 0 (default none)
        """
        if self.month < 10:
            self.month = "0" + str(self.month)
        base_url_a = "https://www.sec.gov/files/data/fails-deliver-data/cnsfails" + str(self.year) + str(self.month) + "a.zip"
        base_url_b = "https://www.sec.gov/files/data/fails-deliver-data/cnsfails" + str(self.year) + str(self.month) + "b.zip"
        ftds_a = pd.read_csv(base_url_a, compression='zip', delimiter='|', on_bad_lines='warn')
        ftds_a.dropna(axis = 0, how = 'any', inplace = True)
        time.sleep(10)
        ftds_b = pd.read_csv(base_url_b, compression='zip', delimiter='|', on_bad_lines='warn')
        ftds_b.dropna(axis = 0, how = 'any', inplace = True)
        month_data = pd.concat([ftds_a, ftds_b], axis = 0).reset_index(drop=True)
        return(month_data)

    # @staticmethod
    def _validate(obj):
        # verify there are data---
        if obj.shape[0] < 2:
            raise AttributeError("Looks like no data.")

    def plot(self):
        # probably nothing to plot, maybe a good summary method---
        pass
