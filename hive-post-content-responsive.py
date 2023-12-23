from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QPushButton, QMessageBox, QLineEdit, QLabel, QTextBrowser
from jsonrpc_requests import Server
import os

basedir = os.path.dirname(__file__)

class Ui:
    def __init__(self):
        # Load the .ui file
        ui_file = QFile(os.path.join(basedir, "hive-post-content-responsive.ui"))
        ui_file.open(QFile.ReadOnly)

        ui_loader = QUiLoader()
        self.ui_widget = ui_loader.load(ui_file)

        ui_file.close()

        # Access a widget (e.g., a QPushButton named "GetPostInfoButton")
        self.GetPostInfoButton = self.ui_widget.findChild(QPushButton, "GetPostInfoButton")
        
        # Load all QLineEdit widgets
        self.author = self.ui_widget.findChild(QLineEdit, "author")
        self.title = self.ui_widget.findChild(QLineEdit, "title")
        self.tags = self.ui_widget.findChild(QLineEdit, "tags")
        self.creationdate = self.ui_widget.findChild(QLineEdit, "creationdate")
        self.TextBoxPermlink = self.ui_widget.findChild(QLineEdit, "TextBoxPermlink")

        # Load all QLabel widgets
        self.payout = self.ui_widget.findChild(QLabel, "payout")
        self.is_payout = self.ui_widget.findChild(QLabel, "is_payout")
        self.authors_payout = self.ui_widget.findChild(QLabel, "authors_payout")
        self.curators_payout = self.ui_widget.findChild(QLabel, "curators_payout")

        # Load all QTextBrowser widgets
        self.body = self.ui_widget.findChild(QTextBrowser, "body")

        # Connect the button's clicked signal to a slot
        if self.GetPostInfoButton:
            self.GetPostInfoButton.clicked.connect(self.CheckPostInfo)

    # This is the slot that gets called when the button is clicked
    def ValidURLErrorMessage(self):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Paste a valid Hive url')
            msg.setWindowTitle("Error")
            msg.exec_()

    def ParseURL(self, url_to_parse):
        if len(url_to_parse) > 1:
            permlink = url_to_parse[1].split("/", 2)
        else:
            permlink = url_to_parse[0].split("/", 2)
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
        self.payout.setText(payout)
        self.is_payout.setText(is_payout)
        self.authors_payout.setText(authors_payout)
        self.curators_payout.setText(curators_payout)
        self.body.setPlainText(body)

    def CheckPostInfo(self):
        self.author.setText("")
        self.title.setText("")
        self.tags.setText("")
        self.creationdate.setText("")
        self.payout.setText("")
        self.is_payout.setText("")
        self.authors_payout.setText("")
        self.curators_payout.setText("")
        self.body.setPlainText("")
        unparced_url = self.TextBoxPermlink.text()
        try:
            post_url = unparced_url.split("@", 1)
            try:
                self.ParseURL(post_url)
            except:
                self.ValidURLErrorMessage()
        except:
            try:
                url_list = ["", unparced_url]
                self.ParseURL(url_list)
            except:
                self.ValidURLErrorMessage()

if __name__ == "__main__":
    app = QApplication([])
    window = Ui()
    window.ui_widget.show()  # Show the loaded widget
    app.exec()