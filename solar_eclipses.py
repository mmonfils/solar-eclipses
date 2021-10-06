# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 17:22:43 2021

@author: mmonf
"""

import pandas as pd
import requests

# Writing a script to retrieve and locally save the data
# from the Wikipedia website

url = "https://en.wikipedia.org/wiki/" \
    "List_of_solar_eclipses_in_the_21st_century"

r = requests.get(url)
df_list = pd.read_html(r.text)
df = df_list[1]
df.to_csv('solar_eclipses.csv', index=False)
