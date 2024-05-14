class ChatMessage:
    WHOISIN = 0
    MESSAGE = 1
    LOGOUT = 2

    def __init__(self, type, message):
        self.type = type
        self.message = message

    def __str__(self):
        return f"{self.type} {self.message}"