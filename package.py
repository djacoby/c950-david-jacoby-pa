class Package:
    def __init__(self, id, address, city, state, zip, time, weight, special_instructions):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.time = time
        self.weight = weight
        self.special_instructions = special_instructions

    def get_package(self):
        return [self.id, self.address, self.city, self.state, self.zip, self.time, self.weight, self.special_instructions]

    # TODO: Write getters and setters for properties
