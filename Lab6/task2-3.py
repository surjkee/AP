import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('NYC_Jobs.csv', encoding = 'utf-8')

print('10 recording')
print(data[:10])
print()

print('10 agencies')
print(data['Agency'][:10])
print()

print('All agencies, business titles, work locations')
print(data[['Agency', 'Business Title', 'Work Location 1']])
print()

data['Agency'].value_counts(sort = False).plot.bar()
plt.show()



