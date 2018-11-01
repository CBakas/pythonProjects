__author__      = "Costas Bakas"
__copyright__   = "Copyright 2018, http request"

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import urllib.request
import codecs
import os
import operator
import requests
import json

class GetTrans(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        layout                  =   QGridLayout()
        self.setUrlabel         =   QLabel("url")
        self.setUrl             =   QLineEdit()
        self.setmsgLabel        =   QLabel("json message")
        self.setMsg             =   QTextEdit()
        self.progressBar        =   QProgressBar()
        self.buttonProcess      =   QPushButton( "process" )
        self.buttonExit         =   QPushButton( "exit" )
        self.resultsLabel       =   QLabel("results")
        self.results            =   QTextEdit()

        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignHCenter)

        layout.addWidget(self.setUrlabel,       0,  0)
        layout.addWidget(self.setUrl,           0,  1)
        self.setUrl.setFixedWidth(400)
        layout.addWidget(self.setmsgLabel,      2,  0)
        layout.addWidget(self.setMsg,           2,  1)
        self.setMsg.setFixedWidth(600)

        layout.addWidget(self.resultsLabel,     6,  0)
        layout.addWidget(self.results,          6,  1)

        layout.addWidget(self.buttonProcess,    8,  0)
        layout.addWidget(self.buttonExit,       8,  1)

        self.setLayout(layout)

        self.setUrl.setText("https://gurujsonrpc.appspot.com")
        self.setWindowTitle("Costas, http request v1 2018")

        self.setFocus()

        self.buttonProcess.clicked.connect(self.process )
        self.buttonExit.clicked.connect(self.close )

    def process (self) :

        ## main program
        resp = ""
        data = ""
        x = 1

        if self.setMsg.toPlainText() == "" :

            for x in range( x, x + 1 ):

                data    =   {   'method': 'guru.test', 'params': ['Guru'], 'id': 123   }

                data['id'] = x

                print( data )
                self.setMsg.setText(str(data))

                r = requests.post( self.setUrl.text(), json=data )

                print( "response " )
                print( "-----" )
                print( x, r.status_code, r.text )
                print( "-----" )

                try:
                    json_data = json.loads( r.text )
                    print( json_data['transactionRequestError']['errors']['code'] )
                    print( json_data.get( 'transactionRequestError' ) )
                except:
                    print( "" )

                x += 1
                resp = resp + str(r.status_code) + os.linesep
                resp = resp + str(r.text) + os.linesep
                self.results.setText(str(resp))

        else :
                data = self.setMsg.toPlainText()
                print ( str(data))
                r = requests.post( self.setUrl.text(), json=data )

                try:
                    json_data = json.loads( r.text )
                    print( json_data['transactionRequestError']['errors']['code'] )
                    print( json_data.get( 'transactionRequestError' ) )
                except:
                    print( "" )

                resp = resp + str(r.status_code) + os.linesep
                resp = resp + str(r.text) + os.linesep
                self.results.setText(str(resp))

        QMessageBox.information(self, "information", "process completed successfully")

app = QApplication(sys.argv)
dialog  =   GetTrans()
dialog.show()
app.exec_()

## end ##