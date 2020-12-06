import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from matplotlib import pyplot as plt

df = pd.read_csv("output.csv")
keep = ['age', 'hours-per-week']

for col in df.columns: 
    if col not in keep:
        df = df.drop(col, axis=1)
        
for i in range(len(df['age'])):
    if len(df['age'][i]) == 2:
        df['age'][i] = df['age'][i][0]
    else:
        df['age'][i] = df['age'][i][0] + df['age'][i][1]
        
for i in range(len(df['hours-per-week'])):
    if len(df['hours-per-week'][i]) == 2:
        df['hours-per-week'][i] = df['hours-per-week'][i][0]
    else:
        df['hours-per-week'][i] = df['hours-per-week'][i][0] + df['hours-per-week'][i][1]
        
scaler = StandardScaler()

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

