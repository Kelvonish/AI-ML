from sklearn.metrics import mean_absolute_error,mean_squared_error
import pandas as pd
data =pd.read_csv("Housing.csv")
y_true =data['price']
y_pred = data['lotsize']
#mean_absolute_error
#print(mean_absolute_error(y_true, y_pred))

#mean squared error
print(mean_squared_error(y_true, y_pred))

#root mean squared error


#data  = pd.DataFrame(data)

#print(data.head())