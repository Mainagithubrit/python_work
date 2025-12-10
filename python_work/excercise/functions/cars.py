def make_car(car, model, **car_info):
    car_info["car_type"] = car
    car_info["model"] = model
    return car_info


car = make_car("land rover", "defender 110", color="blue", sunroof=True)

print(car)
