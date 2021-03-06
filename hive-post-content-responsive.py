from PyQt5 import QtWidgets, uic
import sys
from jsonrpc_requests import Server
from PyQt5.QtWidgets import QMessageBox

class Ui(QtWidgets.QMainWindow):

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

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('hive-post-content-responsive.ui', self)
        self.GetPostInfoButton.clicked.connect(self.CheckPostInfo) # We defined the function we want to run with the button
        self.show()

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
