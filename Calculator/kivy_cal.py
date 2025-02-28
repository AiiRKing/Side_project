from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class CalculatorApp(App):
    def build(self):
        self.expression = ""
        self.result_label = Label(text="0", font_size=50, size_hint_y=0.3)

        # Create buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.result_label)

        grid = BoxLayout(orientation='vertical')
        for i in range(0, len(buttons), 4):
            row = BoxLayout()
            for j in range(4):
                btn = Button(text=buttons[i + j])
                btn.bind(on_press=self.on_button_click)
                row.add_widget(btn)
            grid.add_widget(row)

        # Add Clear button
        clear_button = Button(text="C", size_hint_y=0.2)
        clear_button.bind(on_press=self.clear)
        layout.add_widget(clear_button)

        layout.add_widget(grid)
        return layout

    def on_button_click(self, instance):
        text = instance.text
        if text == '=':
            try:
                self.result_label.text = str(eval(self.expression))
            except:
                self.result_label.text = "Error"
            self.expression = ""
        else:
            self.expression += text
            self.result_label.text = self.expression

    def clear(self, instance):
        self.expression = ""
        self.result_label.text = "0"

# Run the app
if __name__ == '__main__':
    CalculatorApp().run()