def make_car(manufacturer, model, **car_info):
    cars = {'manufacturer': manufacturer, 'model': model}
    for key, value in car_info.items():
        cars[key] = value
    
    return cars

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
