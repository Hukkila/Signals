from test import MyEmitter

class ReceiveEmitter():

    # Define a slot function to receive the signal
    def on_custom_signal_received(self, message):
        print("Received message:", message)

    def main_dodo(self):
        # Create an instance of the custom class
        emitter = MyEmitter()
        # Connect the custom signal to the slot function
        emitter.custom_signal.connect(self.on_custom_signal_received)

        # Send a signal using the emit() method
        emitter.send_signal("Hello, World!")