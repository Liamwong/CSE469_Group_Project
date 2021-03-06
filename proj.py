import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from matplotlib import pyplot as plt
import numpy as np

REDUCE_DATA = False
LINEAR_R = False
QUAD_R = False


df = pd.read_csv("output.csv")
keep = ['age', 'hours-per-week']
for col in df.columns: 
    if col not in keep:
        df = df.drop(col, axis=1)

def header_keeper(header, data):
    for i in range(len(data[header])):
        if len(data[header][i]) == 2:
            data[header][i] = data[header][i][0]
        else:
            data[header][i] = data[header][i][0] + data[header][i][1]

header_keeper('age', df)
header_keeper('hours-per-week', df)

scaler = StandardScaler()

if REDUCE_DATA:
    df = df.iloc[:5000:]

scaler.fit(df[['hours-per-week']])
df['hours-per-week'] = scaler.transform(df[['hours-per-week']])

scaler.fit(df[['age']])
df['age'] = scaler.transform(df[['age']])

km = KMeans(n_clusters=6)
y_predicted = km.fit_predict(df[['age','hours-per-week']])
df['cluster']=y_predicted

df1 = df[df.cluster==0]
df2 = df[df.cluster==1]
df3 = df[df.cluster==2]
df4 = df[df.cluster==3]
df5 = df[df.cluster==4]
df6 = df[df.cluster==5]
df7 = df[df.cluster==6]
plt.figure(figsize=(10, 10))
plt.scatter(df1.age,df1['hours-per-week'],color='green')
plt.scatter(df2.age,df2['hours-per-week'],color='red')
plt.scatter(df3.age,df3['hours-per-week'],color='black')
plt.scatter(df4.age,df4['hours-per-week'],color='orange')
plt.scatter(df5.age,df5['hours-per-week'],color='blue')
plt.scatter(df6.age,df6['hours-per-week'],color='pink')
plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],color='purple',marker='*',label='centroid')
plt.xlabel("Age")
plt.ylabel("Hours Per Week")
plt.legend()



# (age, hours)
X_val = np.array(df['age'])
Y_val = np.array(df['hours-per-week'])

if LINEAR_R:
    m, b, c = np.polyfit(X_val, Y_val, 1)
    plt.plot(X_val, m * X_val + b, 'purple')

if QUAD_R:
    model = np.poly1d(np.polyfit(X_val, Y_val, 2))
    polyline = np.linspace(-1, 4, 50)
    plt.plot(polyline, model(polyline))


plt.show()

