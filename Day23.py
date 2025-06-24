from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner

class TempConvert(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(orientation = 'vertical', padding=30, spacing= 30, **kwargs)

        self.input_label = Label(text="Enter Temperature: ", font_size = 20, color=(0, 0, 0, 1))
        self.add_widget(self.input_label)

        self.temp_input = TextInput(multiline=False, input_filter='float')
        self.add_widget(self.temp_input)

        self.spinner = Spinner(
            text = 'Convert To',
            values =('Celsius', 'Fahrenheit'),
            size_hint = (1,None),
            height = 44
        )
        self.add_widget(self.spinner)

        self.convert_button = Button(text = "Convert")
        self.convert_button.bind(on_press=self.convert_temperature)
        self.add_widget(self.convert_button)

        self.result_label = Label(text="")
        self.add_widget(self.result_label)

    def convert_temperature(self,instance):
        try:
            temp = float(self.temp_input.text)
            if self.spinner.text == 'Fahrenheit':
                result = (temp*9/5)+32
                self.result_label.text =f"{temp}C is {result: .2f}F"

            elif self.spinner.text == 'Celsius':
                result = (temp - 32) *5/9
                self.result_label.text =f"{temp}F is {result: .2f}C"
            else:
                self.result_label.text = "Please select Conversion"
        except ValueError:
            self.result_label.text = "Invalid Input. Please Enter a Number."

class TempApp(App):
    def build(self):
        return TempConvert()
    
if __name__ == '__main__':
    TempApp().run()