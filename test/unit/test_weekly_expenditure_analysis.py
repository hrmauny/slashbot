#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
import time

from matplotlib import pyplot as plt
from BaseCase import BaseCase
import pandas as pd


class TestWeeklyAnalysis(BaseCase):
    """
    Unit test for Testing weekly analysis function
    """

    def test_weekly_expendiure_analysis(self):
        """
        Asserts when validate_entered_amount is given an empty string,
        0 is returned

        """
        self.user.transactions['Food']=[{'Date': datetime.datetime(2023, 9, 3, 0, 0), 'Value': 12.0}]
        self.user.transactions['Transport']=[{'Date': datetime.datetime(2023, 9, 3, 0, 0), 'Value': 100.0}]
        self.user.transactions['Food'].append({'Date': datetime.datetime(2023, 10, 3, 0, 0), 'Value': 40.0})
        self.user.transactions['Groceries']=[{'Date': datetime.datetime(2023, 8, 3, 0, 0), 'Value': 40.0}]
        result=self.user.create_chart_for_weekly_analysis('')
        df1=pd.DataFrame([{"week_number":31,"Value":40},{"week_number":35,"Value":112},{"week_number":40,"Value":40}])
        fig=plt.figure()
        plt.plot(df1['week_number'].values,df1['Value'].values,marker="o")
        plt.ylabel("Expenses")
        plt.xlabel("Week Number")
        fig_name1="data/{}_weekly_analysis.png".format("test") 
        plt.savefig(fig_name1,bbox_inches="tight")
        time.sleep(5)
        assert open("data/test_weekly_analysis.png","rb").read() == open(result[0],"rb").read()
        assert len(result)==2