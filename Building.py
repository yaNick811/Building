class Building:
    def __init__(self, numbersOfFloors, buildingType):
        self.numberOfFloors = numbersOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        if isinstance(other, Building):
            return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType
        return False

moscow = Building(40, 99)
sochi = Building(23, 34)
print(moscow == sochi)
