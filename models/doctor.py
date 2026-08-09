class Doctor:

    def __init__(
        self,
        doctor_id=None,
        name=None,
        specialization=None,
        email=None,
        password=None,
        phone=None,
        consultation_fee=500.00
    ):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.email = email
        self.password = password
        self.phone = phone
        self.consultation_fee = consultation_fee