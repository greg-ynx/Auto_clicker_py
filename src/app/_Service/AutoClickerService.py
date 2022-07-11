import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode


class AutoClickerService(threading.Thread):

    def __init__(self, controller, interval, button, times=None):
        super(AutoClickerService, self).__init__()
        self.controller = controller
        self.interval = interval
        self.button = button
        self.running = False
        self.program_run = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_run = False

    def run(self):
        time.sleep(0.1)
        while self.program_run:
            while self.running:
                self.controller.click(self.button)
                time.sleep(self.interval)
            time.sleep(0.1)


"""
mouse = Controller()
thread = AutoClickerService(mouse, delay, button)
thread.start()
"""
