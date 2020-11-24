# Main code for Pomo. Joins the kivy GUI with the core functions.

from PomoFoobars import get_formatted_time

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config

# Import numeric property to save the current clock time
from kivy.properties import NumericProperty

# Import clock to schedule function calls
from kivy.clock import Clock

kivy.config.Config.set('graphics', 'resizable', 0)


class MainScreen(Screen):

    pass

class TasksScreen(Screen):
    pass


class MainTimerDisplay(Screen):

    current_time = NumericProperty()

    # rounded_time = int(current_time)

    # formatted_time = get_formatted_time(raw_seconds=current_time)

    def __init__(self, **kwargs):
        super(MainTimerDisplay, self).__init__(**kwargs)

        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

        # Increment the time by one second
        Clock.schedule_interval(self.increment_time, 0.1)
        self.increment_time(0)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None


    def switch_view_to_tasks_screen(self):
        print('ran')
        sm = ScreenManager()
        sm.transition.direction = 'left'
        sm.current = 'tasks'



    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        keys_and_events = {
            'left': self.switch_view_to_tasks_screen, 
        }
        keyboard_button = keycode[1]

        if keyboard_button in keys_and_events:
            keys_and_events[keyboard_button]




    def key_action(self, *args):
        """
        Checks if the provided keystroke was any of the keys assigned to a shortcut action event.
        """
        keystroke = args[key_down]

        

    def increment_time(self, interval):
        self.current_time += 0.1


    def start(self):
        print('start was run')
        Clock.unschedule(self.increment_time)
        Clock.schedule_interval(self.increment_time, 0.1)


    def stop(self):
        print('stop was run')
        Clock.unschedule(self.increment_time)


    def get_formatted_time(self, raw_seconds):
        # Calculate the time remaining as a sum total of rounded seconds
        time_remaining = int(raw_seconds)

        # calculate hours and update the seconds variable to be without any total hours
        hours = time_remaining // 3600
        time_remaining %= 3600

        # calculate the number of minutes remaining
        minutes = time_remaining // 60
        time_remaining %= 60

        # Calculate total seconds that are not tied up with hours or minutes
        seconds = time_remaining

        result = f'{hours:02}:{minutes:02}:{seconds:02}'
        return result



class PoMoApp(App):  # <- Main Class
    pass

if __name__ == "__main__":
    # set window size (width, height)

    Window.size = (600, 150)
    pomo = PoMoApp()
    pomo.run()
