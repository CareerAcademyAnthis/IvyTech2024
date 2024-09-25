class Asset:
    # initialize the asset class
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self._revenue = 0.0

    def revenue(self):
        return self._revenue

    def display(self):
        print(f"Asset Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Total Revenue: ${self._revenue:.2f}")


class Apartment:
    # Initialize the apartment class
    def __init__(self, rent, maintenance):
        self._rent = rent
        self._maintenance = maintenance

    def revenue(self):
        return self._rent - self._maintenance


class Building(Asset):
    # Initialize the building
    def __init__(self, name, address, num_apartments, apartment_rent, apartment_maintenance):
        super().__init__(name, address)
        self.num_apartments = num_apartments
        self.apartments = [Apartment(apartment_rent, apartment_maintenance) for _ in range(num_apartments)]
        self._revenue = self.calculate_revenue()

    def calculate_revenue(self):
        total_revenue = sum(apartment.revenue() for apartment in self.apartments)
        return total_revenue


class Villa(Asset):
    # Initialze Villas
    def __init__(self, name, address, rent, maintenance):
        super().__init__(name, address)
        self._rent = rent
        self._maintenance = maintenance
        self._revenue = self.calculate_revenue()

    def calculate_revenue(self):
        return self._rent - self._maintenance


try:
    villa = Villa("Indiana Beach Villa", "123 IBeach Rd", 1200, 400 )
    building = Building("Earl Apartments", "4321 Earl St", 200, 850, 250)

    assets = [villa, building]

    for asset in assets:
        if asset.revenue() <= 0:
            raise ValueError(f"{asset.name} does not generate any revenue")
        asset.display()

except ValueError as e:
    print(e)

