import pandas as pd
from sklearn.model_selection import train_test_split


data = pd.read_csv("usersreview.csv")
df = pd.DataFrame(data)

train,test = train_test_split(df, test_size=0.20, random_state=0)

train,val = train_test_split(train, test_size=0.10, random_state=0)

train.to_csv('train.csv',index=False)
test.to_csv('test.csv',index=False)
val.to_csv('val.csv',index=False)