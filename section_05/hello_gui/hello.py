import sys, platform
from PyQt5 import QtWidgets

if __name__ == '__main__':
   app = QtWidgets.QApplication(sys.argv)
   w = QtWidgets.QWidget()
   b = QtWidgets.QLabel(w)
   b.setText(f"Hello World! (Python {platform.python_version()})")
   w.setGeometry(100,100,200,50)
   b.move(30,20)
   w.setWindowTitle("PyQt in Docker")
   w.show()
   sys.exit(app.exec_())

