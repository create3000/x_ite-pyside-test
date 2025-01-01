import sys
import os

from PySide6.QtWebEngineCore import QWebEngineProfile, QWebEngineSettings
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from PySide6.QtCore import QCoreApplication, QLoggingCategory, QUrl

url = "file://" + os .getcwd () + "/x3d.html"

# Developer Console is available in Chrome at: http://127.0.0.1:2345

os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--enable-logging --log-level=3 --remote-debugging-port=2345"
os.environ["QT_LOGGING_RULES"] = "qt.webenginecontext.debug=true"

def main(args):
   app = QApplication(sys.argv)

   settings = QWebEngineProfile.defaultProfile().settings()
   settings.setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)

   # QWebEngineView
   browser = QWebEngineView()
   browser.setWindowTitle("Pyside Test")
   browser.load(QUrl(url))
   browser.show()

   sys.exit(app.exec_())

if __name__ == "__main__":
   main(sys.argv)
