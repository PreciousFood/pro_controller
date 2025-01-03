from pygame import joystick, event, init, Clock

class ProController:
    def __init__(self, id, needs_pump = False, update_interval = 0):
        init()
        self._js = joystick.Joystick(id)
        self.name = self._js.get_name()

        self.needs_pump = needs_pump

        
        self.update_frequency = 1/update_interval if update_interval > 0 else 0 # frequency of zero means as fast as possible
        self._clock = Clock()

        # index is the button number, value is the button name
        # self.js.get_numbuttons() says there are 20, I only know of 16...not sure where the other 4 are
        self.buttons = ["a", "b", "x", "y", "-", "home", "+", "lstick", "rstick", "l", "r", "up", "down", "left", "right", "capture"]
        self.pressed_buttons = []

    def update(self):
        self._clock.tick(self.update_frequency)
        if self.needs_pump:
            for _ in event.get():
                pass

        self.pressed_buttons = [self.buttons[i] for i in range(self._js.get_numbuttons()) if self._js.get_button(i)]
        

    def rumble(self, intensity, duration):
        # too low values will give an intitial kick then do nothing
        self._js.rumble(intensity, 0, duration)  # i have no clue how the high and low translate to the pro controller, this seems to work fine
    def stop_rumble(self):
        self._js.stop_rumble()

    @property
    def a(self): return "a" in self.pressed_buttons
    @property
    def b(self): return "b" in self.pressed_buttons
    @property
    def x(self): return "x" in self.pressed_buttons
    @property
    def y(self): return "y" in self.pressed_buttons
    @property
    def minus(self): return "-" in self.pressed_buttons
    @property
    def home(self): return "home" in self.pressed_buttons
    @property
    def plus(self): return "+" in self.pressed_buttons
    @property
    def lstick(self): return "lstick" in self.pressed_buttons
    @property
    def rstick(self): return "rstick" in self.pressed_buttons
    @property
    def l(self): return "l" in self.pressed_buttons
    @property
    def r(self): return "r" in self.pressed_buttons
    @property
    def up(self): return "up" in self.pressed_buttons
    @property
    def down(self): return "down" in self.pressed_buttons
    @property
    def left(self): return "left" in self.pressed_buttons
    @property
    def right(self): return "right" in self.pressed_buttons
    @property
    def capture(self): return "capture" in self.pressed_buttons

    @property
    def zl(self):
        zl = self._js.get_axis(4)
        if zl <= 0: return False # is zero before ever pressed
        if zl  >= 0: return True
    @property
    def zl_raw(self):
        return self._js.get_axis(4)
    @property
    def zr(self):
        zr = self._js.get_axis(5)
        if zr <= 0: return False # is zero before ever pressed
        if zr  >= 0: return True
    @property
    def zr_raw(self):
        return self._js.get_axis(5)
    
    @property
    def ljoy_x(self):
        return self._js.get_axis(0)
    @property
    def ljoy_y(self):
        return self._js.get_axis(1)
    @property
    def ljoy(self):
        return (self.ljoy_x, self.ljoy_y)
    @property
    def rjoy_x(self):
        return self._js.get_axis(2)
    @property
    def rjoy_y(self):
        return self._js.get_axis(3)
    @property
    def rjoy(self):
        return (self.rjoy_x, self.rjoy_y)



if __name__ == "__main__":
    # test
    pro = ProController(0, True)
    print(pro.name)

    while True:
        pro.update()

        if pro.capture:
            break