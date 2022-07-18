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

df['toilets need'] = (df.no_of_persons / 100).apply(np.ceil)
df['male units'] = df['toilets need'] * 4
df['female units'] = df['toilets need'] * 8

df1 = df.copy()
print(df1.drop(columns=['lga_name']))

df.plot(x='ward_name', y='toilets need', kind='barh', color='red')
plt.show()