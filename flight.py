import pandas as pd

df=pd.read_csv("flight.csv")
df.shape
print(df.head())
df.info()
df.isnull().sum()
df.dtypes
df.columns
df=df.drop(['Unnamed: 0'],axis=1)
df=df.drop(['flight'],axis=1)
df.rename(columns={'class':'grade'},inplace=True)

y=df["price"]
#x=df.drop(["price"],axis=1)
x=df[['airline','source_city', 'departure_time', 'stops',
       'arrival_time', 'destination_city', 'grade', 'days_left',
       'average_price_source', 'average_price_destination',
       'average_price_stops','hours','mins']]
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
print(df.head())
from sklearn.tree import DecisionTreeRegressor
model2=DecisionTreeRegressor()
model2.fit(x_train,y_train)
y_pred=model2.predict(x_test)
model2.score(x_train,y_train)
model2.score(x_test,y_test)
x=df[['airline','source_city', 'departure_time', 'stops',
       'arrival_time', 'destination_city', 'grade', 'days_left',
       'average_price_source', 'average_price_destination',
       'average_price_stops','hours','mins']]
y=df['price']
y_pred=model2.predict(x)

import pickle
pickle.dump(model2,open('model.pkl','wb'))
# loading model to compare the results
model=pickle.load(open('model.pkl','rb'))

