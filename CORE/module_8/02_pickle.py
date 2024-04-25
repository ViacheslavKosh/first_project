import pickle

my_data = {"key": "value", "num": 42}

serialized_data = pickle.dumps(my_data)
print(serialized_data)

deserialized_data = pickle.loads(serialized_data)
print(deserialized_data)

