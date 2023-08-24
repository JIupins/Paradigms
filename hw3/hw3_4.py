class NotificationSystem:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, message):
        for observer in self.observers:
            observer.notify(message)


class NotifierSMS:
    def notify(self, message):
        print(f"Отправка уведомления по SMS: {message}")


class NotifierMMS:
    def notify(self, message):
        print(f"Отправка уведомления по MMS: {message}")


notification_system = NotificationSystem()

mms_notifier = NotifierSMS()
sms_notifier = NotifierMMS()

notification_system.add_observer(mms_notifier)
notification_system.add_observer(sms_notifier)

notification_system.notify_observers("Отворяй ворота! Твоя Кукуха улетает....")