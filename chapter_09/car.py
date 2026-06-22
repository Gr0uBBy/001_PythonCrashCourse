class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()

    def get_odometer(self):
        # return self.odometer
        print(f"This car has {self.odometer} miles on it.")

    def set_odometer(self, odometer):
        if odometer > self.odometer:
            self.odometer = odometer
        else:
            print("You can not roll back the odometer!")

    def update_odometer(self, miles):
        if miles > 0:
            self.odometer += miles
        else:
            print(
                f"Provided miles value ({miles}) is incorrect. Please provide a",
                "correct number and try again.",
            )
