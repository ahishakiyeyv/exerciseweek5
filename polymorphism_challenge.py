class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")


class Car(Vehicle):
    def move(self):
        return "Driving..."


class Plane(Vehicle):
    def move(self):
        return "Flying..."


class Boat(Vehicle):
    def move(self):
        return "Sailing..."


# Polymorphism in action
print("\nActivity 2:")
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    print(vehicle.move())
