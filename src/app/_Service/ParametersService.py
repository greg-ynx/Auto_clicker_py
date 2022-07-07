class ParametersService:

    def __init__(self, ac):
        self.click_interval = ac.interval_in_seconds()
        self.mouse_button = ac.mouse_button
        self.click_type = ac.click_type
        self.repeat_until_stopped = ac.repeat_until_stopped
        self.cursor_position = ac.cursor_position
        if not self.cursor_position:
            self.cursor_X = ac.cursor_X
            self.cursor_Y = ac.cursor_Y
        