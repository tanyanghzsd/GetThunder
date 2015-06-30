# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from PyQt4 import QtCore
from bs4 import BeautifulSoup
import urllib,urllib2
import sys,os,re

reload(sys)   
sys.setdefaultencoding('utf8')



try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(415, 622)
        self.textBrowser = QtGui.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(15, 160, 381, 451))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(160, 70, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 130, 161, 16))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.GetThunder)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "迅雷会员账号密码获取器", None))
        self.pushButton.setText(_translate("Form", "获取", None))
        self.label.setText(_translate("Form", "迅雷会员账号与密码：", None))


class MyForm(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.GetThunder)
    def GetThunder(self):
        self.get()

    def get(self):
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:38.0) Gecko/20100101 Firefox/38.0'}
        url='http://www.xunleihuiyuan.net/'
        req=urllib2.Request(url,headers=headers)
        html = urllib2.urlopen(req)
        html=html.read()
        soup=BeautifulSoup(html)
        regex=re.compile(r'http://www.xunleihuiyuan.net/vip/.*?\.html',re.S)
        items=soup.find_all('a',attrs={'href':regex})
        URL=[]
        for item in items:
            URL.append(item['href'])
        url=URL[0]

        req=urllib2.Request(url,headers=headers)
        html = urllib2.urlopen(req)
        html=html.read()
        soup=BeautifulSoup(html)
        contents=soup.find_all('div',class_='post-body formattext')

        for content in contents:
            vip=content.text
        # print content.text

        vip=vip.replace('迅雷会员账号',';迅雷会员账号：')
        vip=vip.replace('密码','        密码：')
        vip=vip.replace('【点击获取180天迅雷会员帐号】','')
        vip=vip.split(';')
        VIP=[]
        self.ui.textBrowser.setText('')
        for i in vip:
            # print i
            # VIP.append(i)
            self.ui.textBrowser.append(i)


        



if __name__ == '__main__':
    app=QtGui.QApplication(sys.argv)
    myapp=MyForm()
    myapp.show()
    sys.exit(app.exec_())