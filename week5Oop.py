class Smartphone:
    def _init_(self, brand, model, storage, color, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.color = color
        self.price = price
        self.__battery = 100
        self.is_on = False
    
    def power(self):
        self.is_on = not self.is_on
        status = "on" if self.is_on else "off"
        return f"{self.brand} {self.model} is now {status}!"
    
    def call(self):
        if self.is_on and self.__battery > 5:
            self.__battery -= 5
            return "Calling... "
        return "Cannot call!"
    
    def photo(self):
        if self.is_on and self.__battery > 2:
            self.__battery -= 2
            return "Photo taken! 📸"
        return "Cannot take photo!"
    
    def specs(self):
        return f"{self.brand} {self.model} | {self.color} | {self.storage}GB | ${self.price}"

class PremiumPhone(Smartphone):
    def _init_(self, brand, model, storage, color, price, camera):
        super()._init_(brand, model, storage, color, price)
        self.camera = camera
    
    def video(self):
        if self.is_on and self.__battery > 8:
            self.__battery -= 8
            return "Recording 4K video! 🎥"
        return "Cannot record video!"

phone1 = Smartphone("Samsung", "A54", 128, "Black", 399)
print(phone1.power())
print(phone1.call())
print(phone1.specs())

phone2 = PremiumPhone("iPhone", "15 Pro", 256, "Silver", 999, "48MP")
print(phone2.power())
print(phone2.video())




#activity2
class Vehicle:
    def _init_(self, name):
        self.name = name
    
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return f"{self.name} is driving! "

class Plane(Vehicle):
    def move(self):
        return f"{self.name} is flying! "

class Boat(Vehicle):
    def move(self):
        return f"{self.name} is sailing! "


vehicles = [Car("Toyota"), Plane("Boeing"), Boat("Speedboat")]

for vehicle in vehicles:
    print(vehicle.move())
