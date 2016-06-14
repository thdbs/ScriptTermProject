from PyQt5 import QtWidgets

class NumItem(QtWidgets.QTableWidgetItem):
    def __lt__(self, other):
        nData = int(self.data(0))
        otherData = int(other.data(0))
        if(nData < otherData): return True
        else: return False
