from enum import Enum

class FuelType(Enum):
    GASOLINE = "GASOLINA"
    BIOETHANOL = "BIOETANOL"
    DIESEL = "DIESEL"
    BIODIESEL = "BIODIESEL"
    NATURAL_GAS = "GAS NATURAL"

class CarType(Enum):
    CITY = "CIUDAD"
    SUBCOMPACT = "SUBCOMPACTO"
    COMPACT = "COMPACTO"
    FAMILY = "FAMILIAR"
    EXECUTIVE = "EJECUTIVO"
    SUV = "SUV"

class CarColor(Enum):
    WHITE = "BLANCO"
    BLACK = "NEGRO"
    RED = "ROJO"
    ORANGE = "NARANJA"
    YELLOW = "AMARILLO"
    GREEN = "VERDE"
    BLUE = "AZUL"
    VIOLET = "VIOLETA"

class Car:
    def __init__(
        self,
        brand,
        model,
        engine,
        fuel_type,
        car_type,
        door_count,
        seat_count,
        max_speed,
        color
    ):
        self.brand = brand
        self.model = model
        self.engine = engine
        self.fuel_type = fuel_type
        self.car_type = car_type
        self.door_count = door_count
        self.seat_count = seat_count
        self.max_speed = max_speed
        self.color = color
        self.current_speed = 0

    def motor(self):
        return self.engine

    def fuel_type(self):
        return self._fuel_type
    
    def set_fuel_type(self, fuel_type):
        self._fuel_type = fuel_type

    def car_type(self):
        return self.car_type

    def doors(self):
        return self.door_count
    
    def accelerate(self, speed_increase):
        if self.current_speed + speed_increase < self.max_speed:
            self.current_speed += speed_increase
        else:
            print("No se puede incrementar a una velocidad superior a la máxima del automóvil.")

    def slow_down(self, speed_decrease):
        if (self.current_speed - speed_decrease) > 0:
            self.current_speed -= speed_decrease
        else:
            print("No se puede decrementar a una velocidad negativa.")
    
    def set_current_speed(self, speed):
        self.current_speed = speed

    def brake(self):
        self.current_speed = 0

    def calculate_arrival_time(self, distance_km):
        if self.current_speed == 0:
            print("La velocidad actual es 0. No se puede calcular el tiempo de llegada.")
            return None
        return distance_km / self.current_speed

    def print(self):
        print(f"Marca = {self.brand}")
        print(f"Modelo = {self.model}")
        print(f"Motor = {self.engine}")
        print(f"Tipo de combustible = {self.fuel_type.value}")
        print(f"Tipo de automóvil = {self.car_type.value}")
        print(f"Número de puertas = {self.door_count}")
        print(f"Cantidad de asientos = {self.seat_count}")
        print(f"Velocida máxima = {self.max_speed}")
        print(f"Color = {self.color.value}")


auto1 = Car(
    brand="Ford",
    model=2018,
    engine=3,
    fuel_type=FuelType.DIESEL,
    car_type=CarType.EXECUTIVE,
    door_count=5,
    seat_count=6,
    max_speed=250,
    color=CarColor.BLACK
)

auto1.print()
auto1.set_current_speed(100)
print("Velocidad actual = ", auto1.current_speed)
auto1.accelerate(20)
print("Velocidad actual = ", auto1.current_speed)
auto1.slow_down(50)
print("Velocidad actual = ", auto1.current_speed)
auto1.brake()
print("Velocidad actual = ", auto1.current_speed)
auto1.slow_down(20)