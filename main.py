from kivy.app import App
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class VentanaApp(App):
    def build(self):
        self.width_input = TextInput(
            hint_text="Ancho",
            input_filter="float",
            multiline=False,
        )
        self.height_input = TextInput(
            hint_text="Alto",
            input_filter="float",
            multiline=False,
        )
        self.result_label = Label(
            text="Ingresa las medidas y presiona Calcular.",
            halign="left",
            valign="top",
        )
        self.result_label.bind(size=self._fit_result_text)

        fields = GridLayout(cols=2, spacing=dp(8), size_hint_y=None, height=dp(52))
        fields.add_widget(Label(text="Ancho", halign="left"))
        fields.add_widget(self.width_input)
        fields.add_widget(Label(text="Alto", halign="left"))
        fields.add_widget(self.height_input)

        actions = BoxLayout(spacing=dp(8), size_hint_y=None, height=dp(48))
        calculate_button = Button(text="Calcular")
        calculate_button.bind(on_release=self.calculate)
        clear_button = Button(text="Limpiar")
        clear_button.bind(on_release=self.clear)
        actions.add_widget(calculate_button)
        actions.add_widget(clear_button)

        layout = BoxLayout(
            orientation="vertical",
            padding=dp(16),
            spacing=dp(12),
        )
        layout.add_widget(Label(text="Medidas de ventana", font_size="22sp", size_hint_y=None, height=dp(40)))
        layout.add_widget(fields)
        layout.add_widget(actions)
        layout.add_widget(self.result_label)
        return layout

    def calculate(self, _button):
        try:
            width = float(self.width_input.text)
            height = float(self.height_input.text)
            if width <= 0 or height <= 0:
                raise ValueError
        except ValueError:
            self.result_label.text = "Escribe valores numericos mayores que cero."
            return

        lateral = height - 0.50
        rail = width - 0.25
        head = (width - 0.50) / 2
        lock = height - 1
        glass_width = (width - 4) / 2
        glass_height = height - 4
        self.result_label.text = (
            f"Llavin y enganche: {lock:.2f}\n"
            f"Alfeizar y cabezal: {head:.2f}\n"
            f"Lateral: {lateral:.2f}\n"
            f"Riel y cabezal del marco: {rail:.2f}\n"
            f"Vidrio: {glass_width:.2f} x {glass_height:.2f}"
        )

    def clear(self, _button):
        self.width_input.text = ""
        self.height_input.text = ""
        self.result_label.text = "Ingresa las medidas y presiona Calcular."

    @staticmethod
    def _fit_result_text(label, size):
        label.text_size = (size[0], None)


if __name__ == "__main__":
    VentanaApp().run()
if __name__ == "__main__":
    app().run()