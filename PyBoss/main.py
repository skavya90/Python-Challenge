#!/usr/bin/env python
# coding: utf-8

import pandas as pd
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

emp_data = 'C:\\Users\\skavy\\Desktop\\Bootcamp\\Python-Challenge\\PyBoss\\employee.csv'
emp_data_df = pd.read_csv(emp_data, encoding="utf-8")
emp_data_df.head()

split_name=emp_data_df["Name"].str.split(' ',expand=True).rename(columns= {0:'First name',1:'Last name'})
emp_data_df["DOB"] = emp_data_df["DOB"].astype('datetime64[ns]')
format_DOB=emp_data_df["DOB"].dt.strftime('%m/%d/%Y')
new_SSN = emp_data_df["SSN"].replace(r'^\d{3}-\d{2}', "***-**", regex=True)
State_abb = emp_data_df["State"].replace(us_state_abbrev)
new_csv_df = pd.concat([emp_data_df["Emp ID"],split_name,format_DOB,new_SSN,State_abb],axis=1)

new_csv_df.to_csv("new_pyboss.csv",index = False,header = True,encoding="utf-8")


# In[ ]:




