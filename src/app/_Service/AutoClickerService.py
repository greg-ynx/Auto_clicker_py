import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, Key


class AutoClickerService(threading.Thread):

    def __init__(self, controller, interval, button, times=None, click_type=1, x=None, y=None):
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
        print("Starting auto clicker.")
        self.running = True
        print("Auto clicker running...")

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_run = False
        print("Auto clicker program ended.")

    def run_click(self):
        if (self.x is not None) & (self.y is not None):
            self.controller.position = self.x, self.y
        self.controller.click(self.button, self.click_type)
        time.sleep(self.interval)

    def run(self):
        i = 0
        while self.program_run:
            while self.running:
                if self.times is not None:
                    while i < self.times:
                        if not self.running:
                            break
                        self.run_click()
                        i += 1
                    self.stop_clicking()
                else:
                    self.run_click()
            time.sleep(0.1)
