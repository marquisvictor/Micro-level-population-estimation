import os 
import pandas as pd
import matplotlib.pyplot as plt

path = 'path/to/your/working/directory'
os.chdir(path)

layer = iface.activeLayer()

df = df.DataFrame()

ln = []
wn = []
s = []

for f in layer.getFeatures():
    ln.append(f['lga_name'])
    wn.append(f['ward_name'])
    s.append(f['_sum'])

df['lga_name'] = ln
df['ward_name'] = wn
df['no_of_persons'] = s

print(df.head(20))

df.plot(x='ward_name', y='no_of_persons', kind='bar', color='red')
plt.show()

df.to_csv('Lagos Island.csv', index=False)