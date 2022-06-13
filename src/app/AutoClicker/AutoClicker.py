class AutoCliker :
    def __init__(self):
        self.interval = 100
        self.mouse_button = "Left"
        self.click_type = "Single"
        self.repeat_times = 1
        self.repeat_until_stopped = False
        self.cursor_position = False
        self.cursor_posX = 0
        self.cursor_posY = 0
        self.start = False
        self.stop = True
        self.hotkeySetting = "F6"

    def get_hotkey(self):
        return self.hotkeySetting

    def set_hotkey(self, key):
        self.hotkeySetting = key

    def start_f(self):
        self.stop = False

    def stop_f(self):
        self.stop = True

    def pick_location(self):
        return 0
