from PyQt5 import QtCore, QtGui, QtWidgets
from jsonrpc_requests import Server


class Ui_MainWindow(object):

    def CheckPostInfo(self):
        GetPostPermlink = self.TextBoxPermlink.text()
        permlink = GetPostPermlink.split("/", 2)
        username = permlink[0]
        post = permlink[1]
        server = Server('https://api.hive.blog')
        r = server.send_request(method_name="bridge.get_post", is_notification=False, params=[username, post])
        

        author = r["author"]
        title = r["title"]
        tags = " ".join(r["json_metadata"]["tags"])

        creation_date = r["created"]
        payout = str(r["payout"])
        is_payout = str(r["is_paidout"])
        authors_payout = r["author_payout_value"]
        curators_payout = r["curator_payout_value"]
        body = r["body"]

        self.author.setText(author)
        self.title.setText(title)
        self.tags.setText(tags)
        self.creationdate.setText(creation_date)
        self.payput.setText(payout)
        self.is_payput.setText(is_payout)
        self.authors_payout.setText(authors_payout)
        self.curators_payout.setText(curators_payout)
        self.body.setPlainText(body)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(910, 572)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(910, 565))
        MainWindow.setMaximumSize(QtCore.QSize(3000, 3000))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 891, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.PermlinkLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.PermlinkLabel.setObjectName("PermlinkLabel")
        self.horizontalLayout.addWidget(self.PermlinkLabel)
        self.TextBoxPermlink = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.TextBoxPermlink.setObjectName("TextBoxPermlink")
        self.horizontalLayout.addWidget(self.TextBoxPermlink)
        self.GetPostInfoButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.GetPostInfoButton.setObjectName("GetPostInfoButton")
        self.horizontalLayout.addWidget(self.GetPostInfoButton)
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 40, 661, 119))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.author = QtWidgets.QLabel(self.formLayoutWidget)
        self.author.setObjectName("author")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.author)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.title = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.title.setObjectName("title")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.title)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.creationdate = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.creationdate.setObjectName("creationdate")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.creationdate)
        self.tags = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.tags.setObjectName("tags")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.tags)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(680, 61, 221, 91))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.payput = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.payput.setObjectName("payput")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.payput)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.is_payput = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.is_payput.setObjectName("is_payput")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.is_payput)
        self.label_13 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.authors_payout = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.authors_payout.setObjectName("authors_payout")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.authors_payout)
        self.label_15 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_15.setObjectName("label_15")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.curators_payout = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.curators_payout.setObjectName("curators_payout")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.curators_payout)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 160, 891, 401))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.body = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.body.setObjectName("body")
        self.gridLayout.addWidget(self.body, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 910, 0))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.GetPostInfoButton.clicked.connect(self.CheckPostInfo)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hive Post Content"))
        self.PermlinkLabel.setText(_translate("MainWindow", "permlink:"))
        self.GetPostInfoButton.setText(_translate("MainWindow", "Get Post Info"))
        self.label.setText(_translate("MainWindow", "Author:"))
        self.author.setText(_translate("MainWindow", ""))
        self.label_3.setText(_translate("MainWindow", "Title:"))
        self.title.setText(_translate("MainWindow", ""))
        self.label_5.setText(_translate("MainWindow", "Tags:"))
        self.label_7.setText(_translate("MainWindow", "Creation Date:"))
        self.creationdate.setText(_translate("MainWindow", ""))
        self.label_9.setText(_translate("MainWindow", "Payout:"))
        self.payput.setText(_translate("MainWindow", ""))
        self.label_11.setText(_translate("MainWindow", "Is Payout:"))
        self.is_payput.setText(_translate("MainWindow", ""))
        self.label_13.setText(_translate("MainWindow", "Author\'s Payout:"))
        self.authors_payout.setText(_translate("MainWindow", ""))
        self.label_15.setText(_translate("MainWindow", "Curator\'s Payout:"))
        self.curators_payout.setText(_translate("MainWindow", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())