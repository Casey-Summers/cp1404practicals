"""
CP1404/CP5632 Practical
Kivy GUI program to convert miles into kilometres
Creator: Casey Summers (11/11/2023)
Expected: 35m
Actual: 30m
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILES_TO_KM_CONVERSION = 1.609


class MilesToKilometreApp(App):
    """MilesToKilometre is a Kivy App for converting between miles and kilometres."""

    def build(self):
        """Build the Kivy app from the kv file."""
        Window.size = (500, 350)
        self.title = "Miles to KM Converter"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self, value, increment):
        """Handles how a number is incremented 'Up' or 'Down' by the respective buttons."""
        try:
            number = float(value) + increment
        except ValueError:
            number = float(increment)
        self.root.ids.input_miles.text = str(number)

    def convert_miles_to_km(self, value):
        """Converts between miles and kilometres using a constant. """
        try:
            result = float(value) * MILES_TO_KM_CONVERSION
            self.root.ids.result_label.text = str(result)
        # Value errors instead reset the value to zero, until valid
        except ValueError:
            self.root.ids.result_label.text = str(0.0)

    # # function to handle converting with a button
    # def handle_convert_m_km(self, value):
    #     try:
    #         result = float(value) * MILES_TO_KM_CONVERSION
    #         self.root.ids.result_label.text = str(result)
    #     except ValueError:
    #         self.root.ids.result_label.text = str(0.0)


MilesToKilometreApp().run()
