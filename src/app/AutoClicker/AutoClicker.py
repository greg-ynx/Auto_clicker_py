import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode


class AutoClicker(threading.Thread):
    def __init__(self):
        super(AutoClicker, self).__init__()
        self.interval = 0.001  # seconds
        self.mouse = Controller()
        self.mouse_button = Button.left
        self.click_type = "Single"
        self.repeat_times = 1
        self.repeat_until_stopped = True
        self.cursor_position = False
        self.cursor_posX = 0
        self.cursor_posY = 0
        self.running = False
        self.hotkeySetting = KeyCode(127)

    def start_f(self):
        self.running = True
        while self.running:
            self.mouse.click(self.mouse_button)
            time.sleep(self.interval)
        time.sleep(0.1)

    def stop_f(self):
        self.running = False

    def pick_location(self):
        return 0

    def convert_time(self, hours, mins, secs, ms):
        self.interval = hours * 60 ** 2 + mins * 60 + secs + ms / 1000

    def get_hotkey(self):
        return self.hotkeySetting

    def set_hotkey(self, key):
        self.hotkeySetting = key

    def get_repeat_times(self):
        return self.repeat_times

    def set_repeat_times(self, value):
        self.repeat_times = value
