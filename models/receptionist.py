class Receptionist:

    def __init__(self, receptionist_id, name, email, password, phone, shift="Day"):
        self.__receptionist_id = receptionist_id
        self.__name = name
        self.__email = email
        self.__password = password
        self.__phone = phone
        self.__shift = shift

    # Getter Methods
    def get_receptionist_id(self):
        return self.__receptionist_id

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password

    def get_phone(self):
        return self.__phone

    def get_shift(self):
        return self.__shift

    # Setter Methods
    def set_name(self, name):
        self.__name = name

    def set_email(self, email):
        self.__email = email

    def set_password(self, password):
        self.__password = password

    def set_phone(self, phone):
        self.__phone = phone

    def set_shift(self, shift):
        self.__shift = shift