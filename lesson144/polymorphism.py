# Polymorphism in Python Object-Oriented Programming
# Polymorphism is the principle that allows
# derived classes from the same superclass
# to have methods with the same signature
# but different behaviors.
# Method signature = Same name and number
# of parameters (return type is not part of the signature)
# Opinion + related principles:
# Method signature: same name, parameters, and return type
# SO"L"ID
# Liskov Substitution Principle:
# Objects of a superclass should be replaceable
# by objects of a subclass without breaking the application.
# Method overloading (overload) 🐍 = ❌
# Method overriding (override) 🐍 = ✅

from abc import ABC, abstractmethod


class Notification(ABC):
    def __init__(self, message):
        self.message = message

    @abstractmethod
    def send(self) -> bool: ...


class EmailNotification(Notification):
    def send(self) -> bool:
        print('Email: sending - ', self.message)
        return True


class SMSNotification(Notification):
    def send(self) -> bool:
        print('SMS: sending - ', self.message)
        return False


def notify(notification: Notification):
    notification_sent = notification.send()

    if notification_sent:
        print('Notification sent')
    else:
        print('Notification NOT sent')


email_notification = EmailNotification('testing email')
notify(email_notification)

sms_notification = SMSNotification('testing SMS')
notify(sms_notification)
