import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QPushButton,QVBoxLayout,QWidget,QAction,QMenuBar,QDialog

class secondwindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("second window")
        self.setGeometry(200,200,400,400)
        layout=QVBoxLayout()
        label=QLabel("it is second window")
        layout.addWidget(label)
        self.setLayout(layout)

class Mywindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PYQT")
        self.setGeometry(200,100,400,400)

        self.central_Widget=QWidget()
        self.setCentralWidget(self.central_Widget)

        self.layout=QVBoxLayout()
        self.central_Widget.setLayout(self.layout)

        self.Label=QLabel("Hello,Panda!",self)
        self.layout.addWidget(self.Label)

        self.button=QPushButton("click here",self)
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.on_button_click)

        self.init_menu()

    def init_menu(self):
        menubar=self.menuBar()

        file_menu=menubar.addMenu("File")
        exit_action=QAction("Exit",self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        view_menu=menubar.addMenu("view")
        second_window_action=QAction("open second window",self)
        second_window_action.triggered.connect(self.open_second_window)
        view_menu.addAction(second_window_action)
    
    def open_second_window(self):
        self.second_window=secondwindow()
        self.second_window.exec_()

    def on_button_click(self):
        self.label.setText("Button Clicked!")

    
if __name__=="__main__" :
    app=QApplication(sys.argv)
    window=Mywindow()
    window.show()
    sys.exit(app.exec_())
