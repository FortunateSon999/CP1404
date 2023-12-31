"""
CP1404/CP5632 Practical
Kivy GUI program to convert miles to kilometres
Theodore Lee
Started 10/09/2023
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


MILES_TO_KM = 1.60934


class ConvertMilesToKmApp(App):
    def build(self):
        Window.size = (200, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion(self, miles):
        """Handle conversion of Miles to Kilometres, output result to label widget."""
        try:
            miles = float(self.root.ids.miles.text)
            kilometres = miles * MILES_TO_KM
            self.root.ids.output_label.text = str(kilometres)
        except ValueError:
            miles = 0.0
            self.root.ids.output_label.text = "0.0"

    def increment(self, miles):
        """Increase miles by 1."""
        try:
            miles = float(self.root.ids.miles.text)
            miles += 1
        except ValueError:
            miles = 1
        self.root.ids.miles.text = str(miles)
        self.handle_conversion(miles)


    def reduction(self, miles):
        """Reduce miles by 1."""
        try:
            miles = float(self.root.ids.miles.text)
            miles -= 1
        except ValueError:
            miles = -1
        self.root.ids.miles.text = str(miles)
        self.handle_conversion(miles)


ConvertMilesToKmApp().run()

