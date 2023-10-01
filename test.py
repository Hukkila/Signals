from PySide2.QtCore import QObject, Signal

# Define a custom class that inherits from QObject
class MyEmitter(QObject):
    # Define a custom signal
    custom_signal = Signal(str)

    def send_signal(self, message):
        # Emit the custom signal with the provided message
        self.custom_signal.emit(message)


class SendSignal:
    def __init__(self):
        self.emitter = MyEmitter()

    def sender(self):
        # Call the send_signal method of the MyEmitter instance with the provided message
        self.emitter.send_signal("Hello, World!")


