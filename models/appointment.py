class Appointment:
    def __init__(self,patient_id,doctor_id,appointment_date,appointment_time,reason_for_visit=None,status="Pending",appointment_id=None):
        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.appointment_date = appointment_date  # Expected format: 'YYYY-MM-DD' or datetime.date
        self.appointment_time = appointment_time  # Expected format: 'HH:MM:SS' or datetime.time
        self.status = status                       # 'Pending', 'Confirmed', 'Completed', or 'Cancelled'
        self.reason_for_visit = reason_for_visit