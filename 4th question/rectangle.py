# Define the Rectangle class
class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        return iter([
            {'length': self.length},
            {'width': self.width}
        ])

# Testing the Rectangle class
if __name__ == "__main__":
    # Create an instance of Rectangle
    rect = Rectangle(length=10, width=5)

    # Iterate over the instance
    for item in rect:
        print(item)
