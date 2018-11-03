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
import createRequest_ui

class GetTrans(QDialog, createRequest_ui.Ui_window01):

    def __init__(self):
        QDialog.__init__(self)

        # initial value


        self.setupUi(self)
        self.setUrl.setText( "https://gurujsonrpc.appspot.com" )
        self.processBtn.clicked.connect( self.process )
        self.closeBtn.clicked.connect(self.close )

    def process (self) :

        ## main program
        resp = ""
        data = ""
        x = 1
        print( "value of " + str(self.setMsg.toPlainText()) )
        if self.setMsg.toPlainText() :
            print ("not empty message")
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
                    print ( json_data )
                    #print( json_data['transactionRequestError']['errors']['code'] )
                    #print( json_data.get( 'transactionRequestError' ) )
                except ValueError as e:
                    print( 'invalid json: %s' % e )
                    return None  # or: raise

                x += 1
                resp = resp + str(r.status_code) + os.linesep
                resp = resp + str(r.text) + os.linesep
                self.setResult.setText(str(resp))

        else :
                print ("empty message")
                data = self.setMsg.toPlainText()
                print ( str(data))
                r = requests.post( self.setUrl.text(), json=data )
                print("res="+str(r.text))
                try:
                    json_data = json.loads( r.text )
                    #print( json_data['transactionRequestError']['errors']['code'] )
                    #print( json_data.get( 'transactionRequestError' ) )
                except ValueError as e:
                    print( 'invalid json: %s' % e )
                    return None  # or: raise

                resp = resp + str(r.status_code) + os.linesep
                resp = resp + str(r.text) + os.linesep
                self.setResult.setText(str(resp))

        QMessageBox.information(self, "information", "process completed successfully")

app = QApplication(sys.argv)
dialog  =   GetTrans()
dialog.show()
app.exec_()

## end ##