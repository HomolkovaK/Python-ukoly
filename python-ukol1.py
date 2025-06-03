from math import ceil
class Locality:
    def __init__(self, name, locality_coefficient):
        self.name = name
        self.locality_coefficient = locality_coefficient

class Property:
    def __init__(self, locality):
        self.locality = locality

class Estate(Property):
    def __init__(self, locality, estate_type, area):
        super().__init__(locality)
        self.estate_type = estate_type
        self.area = area
    def calculate_tax(self):
        if self.estate_type == "land":
            tax = ceil(self.area * 0.85 * self.locality.locality_coefficient)
        elif self.estate_type == "building site":
            tax = ceil(self.area * 9 * self.locality.locality_coefficient)
        elif self.estate_type == "forrest":
            tax = ceil(self.area * 0.35 * self.locality.locality_coefficient)
        else:
            tax = ceil(self.area * 2 * self.locality.locality_coefficient)
        return tax
    def __str__(self):
        return f"{self.estate_type}, lokalita: {self.locality.name}, {self.area} metrů čtverečních, daň {Estate.calculate_tax(self)} Kč."
    
class Residence(Property):
    def __init__(self, locality, area, commercial):
        super().__init__(locality)
        self.area = area
        self.commercial = commercial
    def calculate_tax(self):
        if self.commercial == True:
            tax = ceil(2*(self.area * self.locality.locality_coefficient * 15))
        else:
            tax = ceil(self.area * self.locality.locality_coefficient * 15)
        return tax



lokalita1 = Locality("Manětín", 0.8)       
pozemek1 = Estate(lokalita1, "land", 900)
pozemek2 = Residence(lokalita1, 120, False)
lokalita2 = Locality("Brno", 3)
pozemek3 = Residence(lokalita2, 90, True)

print(f"Daň z nemovitosti je {Estate.calculate_tax(pozemek1)}")
print(Residence.calculate_tax(pozemek2))
print(Residence.calculate_tax(pozemek3))

print(str(pozemek1))