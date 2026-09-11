class Billing:
    def __init__(self, patient_id, total_amount, appointment_id=None, payment_status="Unpaid", payment_method="Cash", bill_id=None):
        self.bill_id = bill_id
        self.patient_id = patient_id
        self.appointment_id = appointment_id
        self.total_amount = total_amount
        self.payment_status = payment_status
        self.payment_method = payment_method