#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import wx.grid
import ConnectionDataBase
import ConnSchema
import pprint


class Panel1(wx.Panel,):
    def __init__(self, parent,connection,*args, **kwds):
        self.conn = connection
        #Interfaz
        self.rows = 0
        self.fila = 0
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Panel.__init__(self, parent)
        self.sampleList = ['DBPrueba']
        self.lblSchema = wx.StaticText(self, label="Seleccione el Modelo:", pos=(20, 20))
        self.cbxSchema = wx.ComboBox(self, pos=(20, 45), size=(100, -1), choices=self.sampleList, style=wx.CB_DROPDOWN)
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBoxSchema, self.cbxSchema)

        self.sampleList2 = []
        self.lblTables = wx.StaticText(self, label="Seleccione la Tabla:", pos=(20, 90))
        self.cbxTables = wx.ComboBox(self, pos=(20, 115), size=(100, -1), choices=self.sampleList2, style=wx.CB_DROPDOWN)
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBoxTable, self.cbxTables)
        
        self.sampleList3 = []
        self.lblColumns = wx.StaticText(self, label="Seleccione la Columna:", pos=(20, 160))
        self.cbxColumns = wx.ComboBox(self, pos=(20, 185), size=(100, -1), choices=self.sampleList3, style=wx.CB_DROPDOWN)
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, self.cbxColumns)

        self.button = wx.Button(self, label="Agregar", pos=(25, 230), size=(70,30))
        self.Bind(wx.EVT_BUTTON, self.Agregar,self.button)

        self.button_2 = wx.Button(self, label="Eliminar", pos=(100, 230),size=(70,30))
        self.Bind(wx.EVT_BUTTON, self.Eliminar,self.button_2)
        
        self.grid_panel = wx.Panel(self,pos=(200,20),size=(620,300))
        self.grid = wx.grid.Grid(self.grid_panel,pos=(5,5))
        self.grid.CreateGrid(0, 4)
        self.grid.SetColLabelValue(0,"Tabla")
        self.grid.SetColLabelValue(1,"Columna")
        self.grid.SetColLabelValue(2,"Alias")
        self.grid.SetColLabelValue(3,"Función")
        self.grid.SetRowLabelSize(20)
        self.grid.SetColSize(0,150)
        self.grid.SetColSize(1,150)
        self.grid.SetColSize(2,150)
        self.grid.SetColSize(3,150)
        dimensionador = wx.BoxSizer(wx.VERTICAL) 
        dimensionador.Add(self.grid, 1, wx.EXPAND) 
        self.grid_panel.SetSizer(dimensionador) 

        attr = wx.grid.GridCellAttr()
        attr.SetReadOnly(True)
        self.grid.SetColAttr(0, attr)
        self.grid.SetColAttr(1, attr)
        
        
        #DataBase
        
        self.connSchema = ConnSchema.ConnSchema(self.conn)
        #pp.pprint(self.connCategoria.GetCategorias())
      
        

    def on_edit_cell(self, event):
        
        print "CELL EDITING", event.GetString()
             

    def EvtComboBox(self, event):
        print('Evento de combo box: %s' % event.GetString())

    def EvtComboBoxSchema(self, event):
        self.sampleList2 = self.connSchema.GetTables(event.GetString())
        self.cbxTables.SetItems(self.sampleList2)

    def EvtComboBoxTable(self, event):
        self.sampleList3 = self.connSchema.GetColumns(self.cbxSchema.GetValue(),event.GetString())
        self.cbxColumns.SetItems(self.sampleList3)

    def OnClick(self,event):

        
        self.grid.GetTable().AddRow([''] * self.grid.GetTable().GetNumberCols())
        try:
            print "Valor de 1,1"+str(self.grid.GetTable().GetValue(1,1))
        except IndexError:
            print("no hay valor")

    def Agregar(self,event):
        if self.cbxColumns.GetValue() != "":
            self.grid.AppendRows()
            self.tChoiceEditor = wx.grid.GridCellChoiceEditor(["Sum","Media","Max"], allowOthers=True)
            self.grid.SetCellEditor(self.fila, 3, self.tChoiceEditor)
            self.fila += 1
            self.rows += 1
            self.grid.SetCellValue(self.rows-1, 0,self.cbxTables.GetValue())
            self.grid.SetCellValue(self.rows-1, 1,self.cbxColumns.GetValue())
            self.grid.MakeCellVisible(self.rows, 0)
            self.grid.ForceRefresh()

    def Eliminar(self,event):
        if self.rows > 0: 
            self.grid.DeleteRows(self.rows-1)
            self.rows -= 1
            self.fila -= 1
            self.grid.ForceRefresh()
        
        
