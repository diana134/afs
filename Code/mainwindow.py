import sys
sys.path.insert(0, '../Forms/')
from PyQt4.QtGui import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow

app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())