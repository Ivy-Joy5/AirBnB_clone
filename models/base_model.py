class BaseModel:
    """
    Base class for all models in the project.
    """

    def __init__(self, name):
        """
        Initialize the BaseModel object with a name.

        Args:
            name (str): The name of the object.
        """
        self.name = name

    def say_hello(self):
        """
        Prints a greeting.
        """
        print(f"Hello, {self.name}!")
