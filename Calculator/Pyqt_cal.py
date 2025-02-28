from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QGridLayout, QPushButton

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 300, 400)

        # Create layout
        layout = QVBoxLayout()

        # Add display
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        layout.addWidget(self.display)

        # Add buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        grid = QGridLayout()
        row, col = 0, 0
        for button in buttons:
            btn = QPushButton(button)
            btn.clicked.connect(self.on_button_click)
            grid.addWidget(btn, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Add Clear button
        clear_button = QPushButton("C")
        clear_button.clicked.connect(self.clear)
        grid.addWidget(clear_button, row, 0, 1, 4)

        layout.addLayout(grid)
        self.setLayout(layout)

    def on_button_click(self):
        button = self.sender()
        text = button.text()

        if text == '=':
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except:
                self.display.setText("Error")
        else:
            self.display.setText(self.display.text() + text)

    def clear(self):
        self.display.clear()

# Run the application
if __name__ == '__main__':
    app = QApplication([])
    calc = Calculator()
    calc.show()
    app.exec_()