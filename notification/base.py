# language: notification/base.py
class NotificationBase:
    def send(self, message):
        raise NotImplementedError("This method should be overridden by subclasses")