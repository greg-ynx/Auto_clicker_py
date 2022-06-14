import time
import threading


class ClickMouse(threading.Thread):
    def __init__(self, interval, button, mouse):
        super(ClickMouse, self).__init__()
        self.interval = interval
        self.button = button
        self.mouse = mouse
        self.running = False
        self.program_running = True

    def start_f(self):
        self.running = True

    def stop_f(self):
        self.running = False

    def exit(self):
        self.stop_f()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                self.mouse.click(self.button)
                time.sleep(self.interval)
            time.sleep(0.1)
