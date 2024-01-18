class SessionState:
    def __init__(self):
        self.user_token = None

    def login(self, user_token):
        self.user_token = user_token

    def logout(self):
        self.user_token = None

    def is_logged_in(self):
        return self.user_token is not None
