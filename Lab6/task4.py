import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('NYC_Jobs.csv', encoding = 'utf-8')

data = data[['Agency',
             'Work Location',
             'Salary Range From',
             'Salary Range To']]

data['Salary'] = data.groupby('Salary Range From')\
                 ['Salary Range To'].transform(np.median)

job_category = data.groupby('Agency')

data_js = pd.DataFrame([data.loc[job_category.groups[i], 'Salary'].\
                       values for i in job_category.groups],\
                       index = job_category.groups.keys())
data_js = data_js.median(axis = 1)
data_js.plot(kind = 'bar')
plt.show()
                       

work_location = data.groupby('Work Location')
data_wl = pd.DataFrame([data.loc[work_location.groups[i], 'Salary'].\
                        values for i in work_location.groups],\
                        index = work_location.groups.keys())
data_wl = data_wl.median(axis = 1)
data_wl.plot(kind = 'bar')
plt.show()
                        
