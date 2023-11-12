"""
CP1404 Practical
Kivy GUI program with dynamic labels
Creator: Casey Summers (12/11/2023)
Expected: 40m
Actual: 25m
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelApp(App):
    """DynamicLabelApp is a Kivy App that showcases dynamic labels."""

    def __init__(self, **kwargs):
        """Initialise the app."""
        super().__init__(**kwargs)
        # list of names
        self.names = ["Dave", "Greg", "Bob", "Jeff", "Martin"]
        # self.names = ["Dave", "Greg", "Bob"]  # Test list for dynamic spacing

    def build(self):
        """Build the Kivy app from the .kv file."""
        self.title = "Dynamic Label App"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_dynamic_widgets()
        return self.root

    def create_dynamic_widgets(self):
        """Create dynamic widgets."""
        for name in self.names:
            # Create dynamic label for each name
            temp_label = Label(text=name)
            # Add dynamic label
            self.root.ids.main.add_widget(temp_label)


DynamicLabelApp().run()
