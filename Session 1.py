class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f'Car: {self.brand}, Model: {self.model}, Year: {self.year}')

#Creating objects from the Car class
Car1 = Car('Toyota', 'Corolla', '2022')
Car2 = Car('Honda', 'Civic', '2023')
Car3 = Car('Ford', 'Mustang', '2021')
Car4 = Car('BMW', 'X5', '2024')
Car5 = Car('Mercedes-Benz', 'C-Class', '2020')

#Testing to display the car info
Car4.display_info()