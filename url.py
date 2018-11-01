from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import urllib.request

class DownLoader(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        #layout      =   QVBoxLayout()
        #layout      =   QHBoxLayout()
        layout      =   QGridLayout()

        self.url            =   QLineEdit()
        self.saveLocation   =   QLineEdit()
        self.buttonSaveFile =   QPushButton( ".." )
        self.progressBar    =   QProgressBar()
        self.buttonDownload =   QPushButton("download")
        self.buttonExit     =   QPushButton( "exit" )

        self.url.setText("http://speedtest.reliableservers.com/100MBtest.bin")
        self.saveLocation.setText("C:\Shared\Kostas.Tmp")

        self.url.setPlaceholderText("URL")
        self.saveLocation.setPlaceholderText("file save location")

        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignHCenter)

        layout.addWidget(self.url,              0,  0)
        layout.addWidget(self.saveLocation,     1,  0)
        layout.addWidget(self.buttonSaveFile,   1,  1)
        layout.addWidget(self.progressBar,      2,  0)
        layout.addWidget(self.buttonDownload,   3,  0)
        layout.addWidget(self.buttonExit,       3,  1)

        self.setLayout(layout)

        #lineEdit.textChanged.connect(label.setText)
        #lineEdit.textChanged.connect( self.changeTextLabel )

        self.setWindowTitle("Costas Utils - File downLoad")
        #self.windowIcon("")
        self.setFocus()

        self.buttonSaveFile.clicked.connect(self.saveFile)
        self.buttonDownload.clicked.connect(self.download)
        self.buttonExit.clicked.connect( self.close )

    def saveFile(self):
        setSaveFile     = QFileDialog.getSaveFileName(self, caption="save file as", directory=".", filter="All Files (*.*)")
        self.saveLocation.setText(QDir.toNativeSeparators(setSaveFile)) # με βοηθάει με τα / & \ , τα μετατρέπει μόνο του στο σωστό λειτουργικό

    def download(self):
        url             =   self.url.text()
        saveLocation    =   self.saveLocation.text()

        try :
            urllib.request.urlretrieve(url, saveLocation, self.stateOfDownLoad )
        except Exception as error :
                QMessageBox.warning(self, "warning", "download failed "+str(error))
                return

        QMessageBox.information(self, "information", "the download is complete")
        self.progressBar.setValue(0)

    def stateOfDownLoad(self,   blockNum, blockSize, totalSixe):
        if totalSixe > 0 :
            percent = (blockNum * blockSize * 100 ) / totalSixe
            self.progressBar.setValue( percent )

    def changeTextLabel(self, text):

        self.label.setText(text)

app = QApplication(sys.argv)
# dialog = QDialog()
dialog  =   DownLoader()
dialog.show()
app.exec_()
