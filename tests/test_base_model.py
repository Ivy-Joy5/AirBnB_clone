import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_save(self):
        # Create an instance of BaseModel with the required 'name' argument
        obj = BaseModel(name="My BaseModel")
        
        # Assuming you have a save method that you want to test
        result = obj.save()  # Call the save method on the object
        
        # Use assert to check that the result is as expected
        self.assertTrue(result)  # This checks if save() worked (assuming it returns True)

if __name__ == "__main__":
    unittest.main()

