import pickle

my_data = {"key": "value", "num": 42}

with open("data.pickle", "wb") as file:
    pickle.dump(my_data, file)

with open('data.pickle', 'rb') as file:
    deserialized_data = pickle.load(file)

print(deserialized_data)