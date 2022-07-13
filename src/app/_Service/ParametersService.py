from pynput.mouse import Button


class ParametersService:

    def __init__(self, interval=0.1, mouse_button="Left", click_type="Single", repeat_until_stopped=True, times=1,
                 cursor_position=True, cursor_X=0, cursor_Y=0):
        self.click_interval = interval
        self.mouse_button = self.mouseButton_switch(mouse_button)
        self.click_type = self.clickType_switch(click_type)
        self.repeat_until_stopped = repeat_until_stopped
        self.times = None
        if not repeat_until_stopped:
            self.times = times
        self.cursor_position = cursor_position
        self.cursor_X = None
        self.cursor_Y = None
        if not self.cursor_position:
            self.cursor_X = cursor_X
            self.cursor_Y = cursor_Y

    def clickType_switch(self, click_type):
        try:
            match click_type:
                case "Single":
                    return 1
                case "Double":
                    return 2
                case _:
                    raise AttributeError
        except AttributeError:
            print("ClickTypeSwitchError : Wrong click type input")

    def mouseButton_switch(self, mouse_button):
        try:
            match mouse_button:
                case "Left":
                    return Button.left
                case "Right":
                    return Button.right
                case "Middle":
                    return Button.middle
                case _:
                    raise AttributeError
        except AttributeError:
            print("MouseButtonSwitchError : Wrong mouse button input")
