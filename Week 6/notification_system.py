"""Send notifications through interchangeable channels."""


class NotificationSender:
    """Define the send operation that every notification sender must provide."""

    def send(self, message):
        raise NotImplementedError("Senders must implement send().")


class EmailSender(NotificationSender):
    """Send a notification by email."""

    def send(self, message):
        print(f"Email notification: {message}")


class SMSSender(NotificationSender):
    """Send a notification by SMS."""

    def send(self, message):
        print(f"SMS notification: {message}")


class WhatsAppSender(NotificationSender):
    """Send a notification by WhatsApp."""

    def send(self, message):
        print(f"WhatsApp notification: {message}")


class NotificationService:
    """Send messages using the sender provided when the service is created."""

    def __init__(self, sender):
        self.sender = sender

    def send_notification(self, message):
        self.sender.send(message)


if __name__ == "__main__":
    message = "Your order has been shipped."

    email_service = NotificationService(EmailSender())
    sms_service = NotificationService(SMSSender())
    whatsapp_service = NotificationService(WhatsAppSender())

    email_service.send_notification(message)
    sms_service.send_notification(message)
    whatsapp_service.send_notification(message)