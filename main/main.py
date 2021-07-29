# Philip Roberts 2020

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QLineEdit
import readWrite
import translate

# Set up application
app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

window.setWindowTitle("Philip's Text Disalienation Program")# Set window title

# Format Application
app.setStyleSheet(readWrite.fileToString("stylesheet.css"))

# Add Widgets
convertButton = QPushButton("Convert Input")
textBox = QLineEdit("Type or paste text here...")
textBox.setClearButtonEnabled(True)

# Add Widgets to layout(s)

layout.addWidget(textBox)
layout.addWidget(convertButton)

# Add events
def convert():
    # Create new alert box with translated text
    alert = QMessageBox()
    # Set the content of the alert box
    alert.setText(translate.translateString(textBox.displayText()))
    alert.exec_()

convertButton.clicked.connect(convert)


# Run App
window.setLayout(layout)
window.show()
app.exec_()
