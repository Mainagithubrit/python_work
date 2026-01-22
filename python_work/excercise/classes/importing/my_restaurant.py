from restaurant import Restaurant

my_restaurant = Restaurant("Olive's Eden", "Lamb cuts and ugali")
my_restaurant.describe_restaurant()

print(f"\nNumber served: {my_restaurant.number_served}")
my_restaurant.number_served = 200
print(f"Number served: {my_restaurant.number_served}")

my_restaurant.set_number_served(1000)
print(f"Number served: {my_restaurant.number_served}")

my_restaurant.increment_number_served(250)
print(f"Number served: {my_restaurant.number_served}")
