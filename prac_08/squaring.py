"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Creator: Lindsay Ward, IT@JCU (13/10/2015)
Modified: Casey Summers (11/11/2023)
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Lindsay Ward'


class SquareNumberApp(App):
    """SquareNumberApp is a Kivy App for squaring a number."""
    def build(self):
        """Build the Kivy app from the kv file."""
        Window.size = (275, 150)  # had to adjust window to see all contents
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        """Handle calculation (could be button press or other call), output result to label widget."""
        try:
            result = float(value) ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            pass


SquareNumberApp().run()
