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
    def get_id(self):
        return self.id

    def get_address(self):
        return self.address

    def get_city(self):
        return self.city

    def get_state(self):
        return self.state

    def get_zip(self):
        return self.zip

    def get_deadline(self):
        return self.deadline

    def get_weight(self):
        return self.weight

    def get_special_instructions(self):
        return self.special_instructions

    def get_time_delivered(self):
        return self.time_delivered

    def get_status(self):
        return self.status

    # Setters
    def set_id(self, id):
        self.id = id

    def set_address(self, address):
        self.address = address

    def set_city(self, city):
        self.city = city

    def set_state(self, state):
        self.state = state

    def set_zip(self, zip):
        self.zip = zip

    def set_deadline(self, deadline):
        self.deadline = deadline

    def set_weight(self, weight):
        self.weight = weight

    def set_special_instructions(self, special_instructions):
        self.special_instructions = special_instructions

    def set_time_delivered(self, time_delivered):
        self.time_delivered = time_delivered

    def set_status(self, status):
        self.status = status

    def to_string(self):
        package_info = 'ID: {id}\nAddress: {address}, {city} {zip}\nWeight: {weight}\nDeadline: {deadline}\nStatus: {status}({time_delivered})\n'.format(
            id=self.id, address=self.address, city=self.city, zip=self.zip, weight=self.weight, deadline=self.deadline, status=self.status,
            time_delivered=self.time_delivered if self.time_delivered is not None else ''
        )
        print(package_info)
