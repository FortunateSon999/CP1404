"""
CP1404/CP5632 Practical
Dynamic Kivy Widgets example
Theodore Lee
Started 10/09/2023
"""

# dynamic_labels.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    def build(self):
        # List of names
        names = ['John', 'Jane', 'Bob', 'Alice']

        # Create a BoxLayout
        layout = BoxLayout(orientation='vertical')

        # Create and add labels for each name
        for name in names:
            label = Label(text=name)
            layout.add_widget(label)

        return layout


DynamicLabelsApp().run()
