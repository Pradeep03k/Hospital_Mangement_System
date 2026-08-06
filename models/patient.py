class Patient:

    def __init__(self, patient_id, name, email, password, phone, age, gender, address):
        self.__patient_id = patient_id
        self.__name = name
        self.__email = email
        self.__password = password
        self.__phone = phone
        self.__age = age
        self.__gender = gender
        self.__address = address

    # Getter Methods
    def get_patient_id(self):
        return self.__patient_id

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password

    def get_phone(self):
        return self.__phone

    def get_age(self):
        return self.__age

    def get_gender(self):
        return self.__gender

    def get_address(self):
        return self.__address

    # Setter Methods
    def set_name(self, name):
        self.__name = name

    def set_email(self, email):
        self.__email = email

    def set_password(self, password):
        self.__password = password

    def set_phone(self, phone):
        self.__phone = phone

    def set_age(self, age):
        self.__age = age

    def set_gender(self, gender):
        self.__gender = gender

    def set_address(self, address):
        self.__address = address