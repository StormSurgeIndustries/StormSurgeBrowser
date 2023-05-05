import sys,os
import json
import config
try:
    from PyQt5.QtWidgets import *
    from PyQt5.QtGui import *
    from PyQt5.QtCore import *
    from PyQt5.QtWebEngineWidgets import *
    from PyQt5.QtPrintSupport import *
except Exception as e:
    print(e)
    os.system('pip install PyQt5')
    os.system('pip install PyQtWebEngine')
    from PyQt5.QtWidgets import *
    from PyQt5.QtGui import *
    from PyQt5.QtCore import *
    from PyQt5.QtWebEngineWidgets import *
    from PyQt5.QtPrintSupport import *

layout = QHBoxLayout()
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)      
        self.setWindowTitle("StormSurge Browser")
        self.setWindowIcon(QIcon("icons/logo.png"))
        
        self.setGeometry (100, 100, 1000,1000)

        toolbar = QToolBar()
        self.addToolBar(toolbar)
        

        toolbar.setStyleSheet(f"background-color: {config.toolBarColor}; color: {config.toolBarFontColor};")
        
        #back
        self.backButton = QPushButton()
        self.backButton.setIcon(QIcon('icons/back.png'))
        self.backButton.clicked.connect(self.backBtn)
        toolbar.addWidget(self.backButton)

        
        #reload
        self.reloadButton = QPushButton()
        self.reloadButton.setIcon(QIcon('icons/reload.png'))
        self.reloadButton.clicked.connect(self.reloadBtn)
        toolbar.addWidget(self.reloadButton)


        #forward
        self.forwardButton = QPushButton()
        self.forwardButton.setIcon(QIcon('icons/forward.png'))
        self.forwardButton.clicked.connect(self.forwardBtn)
        toolbar.addWidget(self.forwardButton)
        
        #home
        self.homeButton = QPushButton()
        self.homeButton.setIcon(QIcon('icons/home.png'))
        self.homeButton.clicked.connect(self.homeBtn)
        toolbar.addWidget(self.homeButton)

        #addressbar
        self.addressLineEdit = QLineEdit()
        self.addressLineEdit.resize(1000, 10)
        self.addressLineEdit.setFont(QFont("Sanserif", 18))
        self.addressLineEdit.returnPressed.connect(self.searchBtn)
        toolbar.addWidget(self.addressLineEdit)

        #search
        self.searchButton = QPushButton()
        self.searchButton.setIcon(QIcon('icons/search.png'))
        self.searchButton.clicked.connect(self.searchBtn)
        toolbar.addWidget(self.searchButton)
        self.webEngineView = QWebEngineView()
        self.setCentralWidget(self.webEngineView)
        self.addressLineEdit.setText(config.initialUrl)
        self.webEngineView.load(QUrl(config.initialUrl))
        self.webEngineView.setStyleSheet("background-color: #111111;")



        #window controls
        WindowControls = QToolBar()
        self.addToolBar(WindowControls)
        WindowControls.setStyleSheet(f"background-color: {config.toolBarColor}; color: {config.toolBarFontColor};")
        
        self.minimizeBtn = QPushButton()
        self.minimizeBtn.setIcon(QIcon('icons/minimize.png'))
        self.minimizeBtn.clicked.connect(self.showMinimized)
        WindowControls.addWidget(self.minimizeBtn)

        self.windowBtn = QPushButton()
        self.windowBtn.setIcon(QIcon('icons/window.png'))
        self.windowBtn.clicked.connect(self.showNormal)
        WindowControls.addWidget(self.windowBtn)

        self.maximizeBtn = QPushButton()
        self.maximizeBtn.setIcon(QIcon('icons/maximize.png'))
        self.maximizeBtn.clicked.connect(self.showMaximized)
        WindowControls.addWidget(self.maximizeBtn)

        self.closeBtn = QPushButton()
        self.closeBtn.setIcon(QIcon('icons/exit.png'))
        self.closeBtn.clicked.connect(self.close)
        WindowControls.addWidget(self.closeBtn)
        


        bookmarks = QToolBar()
        self.addToolBar(bookmarks)

        bookmarks.setStyleSheet(f"background-color: {config.toolBarColor}; color: {config.toolBarFontColor};")
        
        #bookmark1
        self.bookmark1 = QPushButton()
        self.bookmark1.setIcon(QIcon('icons/youtube.png'))
        self.bookmark1.clicked.connect(self.bookmark1run)
        bookmarks.addWidget(self.bookmark1)

    #bookmark functions
    def bookmark1run(self):
        self.addressLineEdit.setText(config.bookmark1)
        self.webEngineView.load(QUrl(config.bookmark1))

    def searchBtn(self):
        currenturl = self.addressLineEdit.text()
        self.webEngineView.load(QUrl(currenturl))

    def backBtn(self):
        self.webEngineView.back()

    def forwardBtn(self):
        self.webEngineView.forward()

    def reloadBtn(self):
        self.webEngineView.reload()

    def homeBtn(self):
        self.addressLineEdit.setText(config.initialUrl)
        self.webEngineView.load(QUrl(config.initialUrl))




        
        
        


        
app = QApplication(sys.argv)
window = Window()
window.setLayout(layout)
window.show()
sys.exit(app.exec_())
