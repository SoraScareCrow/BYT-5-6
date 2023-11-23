class HouseBuilder:
    def build_walls(self):
        pass

    def build_doors(self):
        pass

    def build_windows(self):
        pass

    def get_result(self):
        pass

class StoneHouseBuilder(HouseBuilder):
    def __init__(self):
        self.house = House("Stone House")

    def build_walls(self):
        self.house.add_part("Stone Walls")

    def build_doors(self):
        self.house.add_part("Wooden Door")

    def build_windows(self):
        self.house.add_part("Glass Windows")

    def get_result(self):
        return self.house

class WoodHouseBuilder(HouseBuilder):
    def __init__(self):
        self.house = House("Wood House")

    def build_walls(self):
        self.house.add_part("Wooden Walls")

    def build_doors(self):
        self.house.add_part("Wooden Door")

    def build_windows(self):
        self.house.add_part("Plastic Windows")

    def get_result(self):
        return self.house

class House:
    def __init__(self, house_type):
        self.house_type = house_type
        self.parts = []

    def add_part(self, part):
        self.parts.append(part)

    def describe(self):
        return f"{self.house_type} with {' and '.join(self.parts)}"

class HouseDirector:
    def __init__(self, builder):
        self._builder = builder

    def construct_house(self):
        self._builder.build_walls()
        self._builder.build_doors()
        self._builder.build_windows()
        return self._builder.get_result()

def main():
    builder_type = input("Type of house to build (stone/wood): ").strip().lower()
    builder = StoneHouseBuilder() if builder_type == "stone" else WoodHouseBuilder()
    director = HouseDirector(builder)
    house = director.construct_house()
    print(house.describe())

if __name__ == "__main__":
    main()