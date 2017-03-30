import numpy as np


class DisplayInfo (QObject):
    def __init__(self, parent=0):
        super().__init__(parent)
        _diag = 24.0/2.54
        _res = (1920, 1080)
        _ratio = (16.0, 9.0)

    def dotsPerCM(self):
        x = np.sqrt( self._diag**2/(self._ratio[0]**2 + self._ratio[1]**2))
        w, l = self._ratio[0]*x, self._ratio[1]*x
        return ( self._res[0]/w, self.res[1]/l )

    @pyqtProperty(float)
    def dots(self):
        return dotsperCM()



