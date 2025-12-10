class Restaurant:
    """A simple class that represents a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initializing restaurant_name and cuisine_type"""
        
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """A method to describe a restaurant"""

        print(f"I have a restaurant named {self.restaurant_name}.")
        print(f"My restaurant specialty meal is {self.cuisine_type}")

    def open_restaurant(self):
        """A method that shows a restaurant is open"""

        print(f"\n{self.restaurant_name} is now open and serving "\
            f"{self.cuisine_type}\n")

    def set_number_served(self, number_served):
        """Sets the number of customers that have been served"""
        self.number_served = number_served

    def increment_number_served(self, add_customer):
        """This adds the number of customers that have been served"""
        self.number_served += add_customer





my_restaurant = Restaurant("Olive's Eden", "Lamb cuts and ugali")
my_restaurant.describe_restaurant()

print(f"\nNumber served: {my_restaurant.number_served}")
my_restaurant.number_served = 200
print(f"Number served: {my_restaurant.number_served}")

my_restaurant.set_number_served(1000)
print(f"Number served: {my_restaurant.number_served}")

my_restaurant.increment_number_served(250)
print(f"Number served: {my_restaurant.number_served}")

"""my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()


rival_restaurant = Restaurant("Quiver", 'Nyama choma')

rival_restaurant.describe_restaurant()
rival_restaurant.open_restaurant()

another_restaurant = Restaurant('Snack shack', 'kuku choma')

another_restaurant.describe_restaurant()
another_restaurant.open_restaurant()"""
