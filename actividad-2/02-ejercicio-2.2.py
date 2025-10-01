from enum import Enum

class PlanetType(Enum):
    GASEOUS = "GASEOSO"
    TERRESTRIAL = "TERRESTRE"
    DWARF = "ENANO"

class Planet:
    def __init__(self,
                name=None,
                satellite_count=0,
                mass=0.0,
                volume=0.0,
                diameter=0,
                sun_distance=0,
                planet_type=PlanetType.TERRESTRIAL,
                is_observable=False
            ):
        self.name = name
        self.satellite_count = satellite_count
        self.mass = mass
        self.volume = volume
        self.diameter = diameter
        self.sun_distance = sun_distance
        self.planet_type = planet_type
        self.is_observable = is_observable

    @property
    def density(self):
        if self.volume == 0:
            return 0
        return self.mass / self.volume
    
    def is_outer_planet(self):
        limit = 149597870 * 3.4
        return self.sun_distance > limit


    def print(self):
        print(f'Nombre = {self.name}')
        print(f'Cantidad de satélites = {self.satellite_count}')
        print(f'Masa = {self.mass}')
        print(f'Volumen = {self.volume}')
        print(f'Diámetro = {self.diameter}')
        print(f'Distancia al sol = {self.sun_distance}')
        print(f'Tipo de planeta = {self.planet_type.value}')
        print(f'Es observable = {"Sí" if self.is_observable else "No"}')


p1 = Planet("Tierra", 1, 5.9736E24, 1.08321E12, 12742, 150000000, PlanetType.TERRESTRIAL, True)
p1.print()
print(f"Densidad del planeta {p1.density}")
print(f"Es planeta exterior = {str(p1.is_outer_planet())}")
print()

p2 = Planet("Júpiter", 79, 1.899E27, 1.4313E15, 139820, 750000000, PlanetType.GASEOUS, True)
p2.print()
print(f"Densidad del planeta {p2.density}")
print(f"Es planeta exterior = {str(p2.is_outer_planet())}")