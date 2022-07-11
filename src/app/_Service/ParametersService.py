class ParametersService:

    def __init__(self, interval=0.1, mouse_button="left", click_type="Single", repeat_until_stopped=True, times=1,
                 cursor_position=True, cursor_X=0, cursor_Y=0):
        self.click_interval = interval
        self.mouse_button = mouse_button
        self.click_type = click_type
        self.repeat_until_stopped = repeat_until_stopped
        if not repeat_until_stopped:
            self.times = times
        self.cursor_position = cursor_position
        if not self.cursor_position:
            self.cursor_X = cursor_X
            self.cursor_Y = cursor_Y
        