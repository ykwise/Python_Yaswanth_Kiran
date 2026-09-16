from abc import ABC, abstractmethod


class Notification(ABC):

    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(Notification):

    def __init__(self, email):
        self.email = email

    def send(self, message):
        print(f"Email sent to {self.email}")
        print(f"Message: {message}")


class SMSNotification(Notification):

    def __init__(self, phone):
        self.phone = phone

    def send(self, message):
        print(f"SMS sent to {self.phone}")
        print(f"Message: {message}")


class PushNotification(Notification):

    def __init__(self, device_id):
        self.device_id = device_id

    def send(self, message):
        print(
            f"Push notification sent to "
            f"device {self.device_id}"
        )
        print(f"Message: {message}")