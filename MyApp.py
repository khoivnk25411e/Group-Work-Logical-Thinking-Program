from PyQt6.QtWidgets import QApplication, QMainWindow

app=QApplication([])
myWindow= MainWindowExtend()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()