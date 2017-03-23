import sys

from PyQt5.QtCore import pyqtProperty, QCoreApplication, QObject, QUrl
from PyQt5.QtQml import qmlRegisterType, QQmlComponent, QQmlEngine

class EEGApp(QObject):
    def __init__(self, parent=None):
        eegdata = None
        sens = 7.0
        speed = 30.0
        

app = QCoreApplication(sys.argv)

# Register the Python type.  Its URI is 'People', it's v1.0 and the type
# will be called 'Person' in QML.
qmlRegisterType(Person, 'People', 1, 0, 'Person')

# Create a QML engine.
engine = QQmlEngine()

# Create a component factory and load the QML script.
component = QQmlComponent(engine)
component.loadUrl(QUrl('example.qml'))

# Create an instance of the component.
#person = component.create()


