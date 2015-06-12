import wx
class Shell():
    def __init__ (self,parent):
        wx.Shell.__init__(self, parent)
        self.prueba= wx.Shell.write(self, "Prueba")
