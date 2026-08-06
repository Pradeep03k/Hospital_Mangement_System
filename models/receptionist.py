class Receptionist:

    def __init__(self, receptionist_id, name, email, password, phone, shift="Day"):
        self.receptionist_id = receptionist_id
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone
        self.shift = shift