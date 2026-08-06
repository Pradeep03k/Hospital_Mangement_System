class Doctor:
    """
    Doctor Entity Class
    This class only stores doctor information.
    No database or business logic should be written here.
    """

    def __init__(
        self,
        doctor_id,
        name,
        specialization,
        email,
        password,
        phone,
        consultation_fee=500.00
    ):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.email = email
        self.password = password
        self.phone = phone
        self.consultation_fee = consultation_fee