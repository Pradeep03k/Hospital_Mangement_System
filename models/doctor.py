class Doctor:
    def __init__(self, name, specialization, email, password, phone=None, consultation_fee=500.00, doctor_id=None):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.email = email
        self.password = password
        self.phone = phone
        self.consultation_fee = consultation_fee