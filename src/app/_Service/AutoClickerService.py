import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode


class AutoClickerService(threading.Thread):

    def __init__(self, controller, interval, button, times=None, click_type="Single", x=None, y=None):
        super(AutoClickerService, self).__init__()
        self.controller = controller
        self.interval = interval
        self.button = button
        self.times = times
        self.click_type = click_type
        self.x = x
        self.y = y
        self.running = False
        self.program_run = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_run = False

    def run_click(self):
        match(self.click_type):
            case "Single"
        self.controller.click(self.button)
        time.sleep(self.interval)

    def run(self):
        while self.program_run:
            if self.times != None:
                i = 0
                while i < self.times:
                    self.run_click()
                    i += 1
            else:
                while self.running:
                    self.run_click()
            time.sleep(0.1)


"""
mouse = Controller()
thread = AutoClickerService(mouse, delay, button)
thread.start()
"""
