# Sample script for QGIS Init Script
# This script will open an info dialog


from qgis.PyQt.QtGui import QMessageBox

QMessageBox.information(None, "Hello", "Hello World!")
