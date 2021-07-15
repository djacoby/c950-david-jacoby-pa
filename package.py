# Well formed Package class with attributes of a package and helper functions
class Package:
    def __init__(self, id, address, city, state, zip, deadline, weight, special_instructions):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.special_instructions = special_instructions
        self.status = 'Not Delivered'
        self.time_delivered = None

    # Getters
    
    # Get package id
    # Big 0 = 0(1)
    def get_id(self):
        return self.id
    
    # Get package destination address
    # Big 0 = 0(1)
    def get_address(self):
        return self.address

    # Get package destination city
    # Big 0 = 0(1)
    def get_city(self):
        return self.city

    # Get package destination state
    # Big 0 = 0(1)
    def get_state(self):
        return self.state

    # Get package destination zip
    # Big 0 = 0(1)
    def get_zip(self):
        return self.zip

    # Get delivery deadline
    # Big 0 = 0(1)
    def get_deadline(self):
        return self.deadline

    # Get package weight
    # Big 0 = 0(1)
    def get_weight(self):
        return self.weight

    # Get package special instructions
    # Big 0 = 0(1)
    def get_special_instructions(self):
        return self.special_instructions

     # Get package delivered time
     # Big 0 = 0(1)
    def get_time_delivered(self):
        return self.time_delivered

    # Get package status (Delivered/ Not delivered)
    # Big 0 = 0(1)
    def get_status(self):
        return self.status

    # Setters

    # Set package id
    # Big 0 = 0(1)
    def set_id(self, id):
        self.id = id

    # Set package destination address
    # Big 0 = 0(1)
    def set_address(self, address):
        self.address = address

    # Set package destination city
    # Big 0 = 0(1)
    def set_city(self, city):
        self.city = city

    # Set package destination state
    # Big 0 = 0(1)
    def set_state(self, state):
        self.state = state

    # Set package destination zip
    # Big 0 = 0(1)
    def set_zip(self, zip):
        self.zip = zip

    # Set package delivery deadline
    # Big 0 = 0(1)
    def set_deadline(self, deadline):
        self.deadline = deadline

    # Set package weight
    # Big 0 = 0(1)
    def set_weight(self, weight):
        self.weight = weight

    # Set package delivery special instructions
    # Big 0 = 0(1)
    def set_special_instructions(self, special_instructions):
        self.special_instructions = special_instructions

    # Set package time delivered
    # Big 0 = 0(1)
    def set_time_delivered(self, time_delivered):
        self.time_delivered = time_delivered

    # Set package status (Delivered, Not delivered)
    # Big 0 = 0(1)
    def set_status(self, status):
        self.status = status
