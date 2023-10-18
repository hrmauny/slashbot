#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import time

from matplotlib import pyplot as plt
from BaseCase import BaseCase
import pandas as pd


class TestMonthlyAnalysis(BaseCase):
    """
    Unit test for Testing monthly analysis function
    """

    def test_monthly_expendiure_analysis(self):
        """
        Asserts when validate_entered_amount is given an empty string,
        0 is returned

        """
        self.user.transactions['Food']=[{'Date': datetime.datetime(2023, 9, 3, 0, 0), 'Value': 12.0}]
        self.user.transactions['Transport']=[{'Date': datetime.datetime(2023, 9, 3, 0, 0), 'Value': 100.0}]
        self.user.transactions['Food'].append({'Date': datetime.datetime(2023, 10, 3, 0, 0), 'Value': 40.0})
        self.user.transactions['Groceries']=[{'Date': datetime.datetime(2023, 8, 3, 0, 0), 'Value': 40.0}]
        result=self.user.create_chart_for_monthly_analysis('')
        df1=pd.DataFrame([{"month-year":"2023_Aug","Value":40},{"month-year":"2023_Oct","Value":40},{"month-year":"2023_Sep","Value":112}])
        fig=plt.figure()
        plt.bar(df1["month-year"],df1['Value'])
        plt.ylabel("Expenses")
        fig_name1="data/{}_monthly_analysis.png".format('test') 
        plt.savefig(fig_name1,bbox_inches="tight")
        time.sleep(5)
        assert open("data/test_monthly_analysis.png","rb").read() == open(result[0],"rb").read()
        assert len(result)==2