import requests
import pickle
#Writing to file
url ='https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
data = requests.get(url)
# print(data.text)
datalist = data.text.split("\n")
print(datalist)
filename = "iris_data.pkl"
with open(filename, "wb") as f:
    pickle.dump(datalist, f)

# Read the file
filename = "iris_data.pkl"
with open(filename, "rb") as f:
    iris_data = pickle.load(f)
    print(iris_data)