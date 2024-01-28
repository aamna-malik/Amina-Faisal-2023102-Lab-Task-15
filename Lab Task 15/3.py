class PrefixDecoratorMeta(type):
    def __new__(cls, name, bases, namespace):
        # Add a prefix to all method names in the class
        prefixed_namespace = {}
        prefix = "decorated_"
        for key, value in namespace.items():
            if callable(value):  # Check if the attribute is a method
                prefixed_namespace[prefix + key] = value
            else:
                prefixed_namespace[key] = value

        # Create the class using the modified namespace
        return super().__new__(cls, name, bases, prefixed_namespace)

# Applying the metaclass as a decorator
class DecoratedClass(metaclass=PrefixDecoratorMeta):
    def method1(self):
        return "Original method1"

    def method2(self):
        return "Original method2"

# Creating an instance of the decorated class
instance = DecoratedClass()

# Calling the decorated methods
result1 = instance.decorated_method1()
result2 = instance.decorated_method2()

# Displaying the results
print(result1)  # Output: Original method1
print(result2)  # Output: Original method2
