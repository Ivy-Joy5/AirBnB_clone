#!/usr/bin/python3
from models.base_model import BaseModel  # Import the BaseModel class

my_model = BaseModel()  # Create a new instance of BaseModel
my_model.name = "My First Model"  # Add a name to the object
my_model.my_number = 89  # Add a number to the object

print(my_model)  # Print the object (this calls the __str__ method)

my_model.save()  # Call the save method to update the updated_at time
print(my_model)  # Print the object again (this should show the updated time)

my_model_json = my_model.to_dict()  # Convert the object to a dictionary
print(my_model_json)  # Print the dictionary

print("JSON of my_model:")
for key in my_model_json.keys():
    print(f"\t{key}: ({type(my_model_json[key])}) - {my_model_json[key]}")

