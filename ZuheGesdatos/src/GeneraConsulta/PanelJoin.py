#!/usr/bin/python
#-*- coding: latin-1 -*-
import wx
import wx.grid
import ConnectionDataBase
import ConnSchema
import pprint


class PanelJoin(wx.Panel,):
    def __init__(self, parent,connection,*args, **kwds):
        self.conn = connection
        self.connSchema = ConnSchema.ConnSchema(self.conn)
        #Interfaz
        self.rows = 0
        self.fila = 0
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Panel.__init__(self, parent)
	
	self.SetBackgroundColour("3399FF")
        self.sampleList1 =self.connSchema.GetTables("db_avitours") 
        self.lblTbOrigen = wx.StaticText(self, label="Tabla Origen:", pos=(20, 20))
        self.cbxTbOrigen = wx.ComboBox(self, pos=(20, 45), size=(100, -1), choices=self.sampleList1, style=wx.CB_DROPDOWN)
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBoxTbOrigen, self.cbxTbOrigen)

        self.sampleList2= []
        self.lblClOrigen = wx.StaticText(self, label="Clave Origen:", pos=(20, 90))
        self.cbxClOrigen= wx.ComboBox(self, pos=(20, 115), size=(100, -1), choices=self.sampleList2, style=wx.CB_DROPDOWN)
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBoxClOrigen, self.cbxClOrigen)

        self.sampleList3 = []
        self.lblTbDestino = wx.StaticText(self, label="Tabla Destino:", pos=(20, 160))
        self.cbxTbDestino = wx.ComboBox(self, pos=(20, 185), size=(100, -1), choices=self.sampleList3, style=wx.CB_DROPDOWN)
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBoxTbDestino, self.cbxTbDestino)
        
        self.sampleList4 = []
        self.lblClDestino = wx.StaticText(self, label="Clave Destino:", pos=(20, 230))
        self.cbxClDestino = wx.ComboBox(self, pos=(20, 250), size=(100, -1), choices=self.sampleList4, style=wx.CB_DROPDOWN)
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBoxClDestino, self.cbxClDestino)
        

        self.button = wx.Button(self, label="Agregar", pos=(25, 300), size=(70,30))
        self.Bind(wx.EVT_BUTTON, self.Agregar,self.button)

        self.button_2 = wx.Button(self, label="Eliminar", pos=(100, 300),size=(70,30))
        self.Bind(wx.EVT_BUTTON, self.Eliminar,self.button_2)
        
        

        self.grid_panel = wx.Panel(self,pos=(200,20),size=(620,300))
        self.grid = wx.grid.Grid(self.grid_panel,pos=(5,5),size=(580,180))
        self.grid.CreateGrid(0, 5)
        self.grid.SetColLabelValue(0,"Tabla Origen")
        self.grid.SetColLabelValue(1,"Clave Origen")
        self.grid.SetColLabelValue(2,"Tabla Destino")
        self.grid.SetColLabelValue(3,"Clave Destino")
        self.grid.SetColLabelValue(4,"Tipo Join")
        self.grid.SetRowLabelSize(20)
        self.grid.SetColSize(0,120)
        self.grid.SetColSize(1,120)
        self.grid.SetColSize(2,120)
        self.grid.SetColSize(3,120)
        self.grid.SetColSize(4,120)
        dimensionador = wx.BoxSizer(wx.VERTICAL) 
        dimensionador.Add(self.grid, 1, wx.EXPAND) 
        self.grid_panel.SetSizer(dimensionador) 


    def on_edit_cell(self, event):
        
        print "CELL EDITING", event.GetString()

    def EvtComboBoxTbOrigen(self, event):
        sampleList3 = self.connSchema.GetPrimaryKeys("db_avitours",event.GetString())
        pp = pprint.PrettyPrinter(indent=4)
        #pp.pprint(sampleList3)
        self.cbxClOrigen.SetItems(sampleList3)

    def EvtComboBoxClOrigen(self, event):
        sampleList4 = self.connSchema.GetForeignTables("db_avitours",self.cbxTbOrigen.GetValue(),event.GetString())
        pp = pprint.PrettyPrinter(indent=4)
        #pp.pprint(sampleList4)
        self.cbxTbDestino.SetItems(sampleList4)

    def EvtComboBoxTbDestino(self, event):
        sampleList5 = self.connSchema.GetForeignKeys("db_avitours",self.cbxTbOrigen.GetValue(),self.cbxClOrigen.GetValue(),event.GetString())
        pp = pprint.PrettyPrinter(indent=4)
        #pp.pprint(sampleList5)
        self.cbxClDestino.SetItems(sampleList5)
             

    def EvtComboBoxClDestino(self, event):
        print('')
	

    def OnClick(self,event):

        
        self.grid.GetTable().AddRow([''] * self.grid.GetTable().GetNumberCols())
        try:
            print "Valor de 1,1"+str(self.grid.GetTable().GetValue(1,1))
        except IndexError:
            print("no hay valor")

    def Agregar(self,event):

        if self.cbxTbOrigen.GetValue() != "":
            self.grid.AppendRows()
            self.tChoiceEditor = wx.grid.GridCellChoiceEditor(["INNER JOIN","LEFT JOIN","RIGHT JOIN"], allowOthers=True)
            self.grid.SetCellEditor(self.fila, 4, self.tChoiceEditor)
            self.fila += 1
            self.rows += 1
            self.grid.SetCellValue(self.rows-1, 0,self.cbxTbOrigen.GetValue())
            self.grid.SetCellValue(self.rows-1, 1,self.cbxClOrigen.GetValue())
            self.grid.SetCellValue(self.rows-1, 2,self.cbxTbDestino.GetValue())
            self.grid.SetCellValue(self.rows-1, 3,self.cbxClDestino.GetValue())

            
            self.grid.MakeCellVisible(self.rows, 0)
            self.grid.ForceRefresh()
        

    def Eliminar(self,event):
        
        if self.rows > 0: 
            self.grid.DeleteRows(self.rows-1)
            self.rows -= 1
            self.fila -= 1
            self.grid.ForceRefresh()

    def GetRowsValue(self):
        datos = [[0 for x in range(5)] for x in range(self.rows)] 
        for i in range(0,self.rows):
            for j in range(0,self.fila):
                datos[i][j] = self.grid.GetCellValue(i,j)
        return datos
            