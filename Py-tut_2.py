import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import requests

arr = np.array([1,2,3,4])
arr=arr
    
print("Mean:", arr.mean())
print("Reshape:\n", arr.reshape(2,2))

# file manipulation
df = pd.read_csv("titanic.csv")
print(df.head())            # gives top 5 elements in the file
print(df.describe())        # gives all the mean, std, min, max
print(df[df["Age"] > 50])  # all the passengers with age above 50

#--------------------------------

# Plotting work
sns.histplot(df["Age"].dropna(), bins=30, kde=True)
plt.show()
sns.barplot(x="Sex", y="Survived", data=df)
plt.show()

#--------------------------------

#Madel training
df = pd.read_csv("titanic.csv")
df = df[["Survived", "Pclass", "Age", "Fare", "Sex"]].dropna() # removing any columns whose mentioned fields are missing

# Convert categorical "Sex" to numeric so male would be considered 0 and female as 1
df["Sex"] = df["Sex"].map({"male":0, "female":1})

X = df[["Pclass", "Age", "Fare", "Sex"]] # taking this as input feature matrix based on which model will predict survived or not
y = df["Survived"]  # your target vector (output label to predict)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=200)    # more iterations needed if the data is huge, more features (i.e. longer paths), data is not scaled
model.fit(X_train, y_train)

pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, pred))

#--------------------------------

# Requests 
response = requests.get("https://api.github.com/users/openai")
data = response.json()
print(data["name"], data["public_repos"])