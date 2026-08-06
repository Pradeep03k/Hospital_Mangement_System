class Admin:
    def __init__(self, username, password, email, admin_id=None):
        self.admin_id = admin_id
        self.username = username
        self.password = password
        self.email = email