#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import wx.grid
import ConnectionDataBase
import ConnSchema
import pprint


class PanelSelect(wx.Panel,):
    def __init__(self, parent,connection,*args, **kwds):
        self.conn = connection
        #Interfaz
        self.rows = 0
        self.fila = 0
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Panel.__init__(self, parent)
	self.SetBackgroundColour("3399FF")
        self.sampleList = ['db_avitours']
        self.lblSchema = wx.StaticText(self, label="Seleccione el Modelo:", pos=(20, 20))
        self.cbxSchema = wx.ComboBox(self, pos=(20, 45), size=(100, 100), choices=self.sampleList, style=wx.CB_DROPDOWN)
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

	self.button_3 = wx.Button(self, label="Subir", pos=(50, 300),size=(30,30))
        self.Bind(wx.EVT_BUTTON, self.Subir,self.button_3)
        


	self.grid_panel = wx.Panel(self,pos=(200,20),size=(620,300))
        self.grid = wx.grid.Grid(self.grid_panel,pos=(5,5),size=(580,180))
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
      
        

    def Subir(self, event):
	
	#Values=[]
	self.Seleccion = self.grid.GetSelectedRows()
  	#Values[0]=self.grid.GetCellValue(self,self.Seleccion[0] , 0)
	#Values[1]=self.grid.GetCellValue(self,self.Seleccion[0] , 1)
	#Values[2]=self.grid.GetCellValue(self,self.Seleccion[0] , 2)
	#Values[3]=self.grid.GetCellValue(self,self.Seleccion[0] , 3)

	if self.Seleccion[0] >= 1:
		self.grid.DeleteRows(self.Seleccion[0])
		self.grid.SetRowPos(self, self.Seleccion[0], self.Seleccion[0]-1)
 		self.grid.ForceRefresh()
		

        
    def MoveRow(self,frm,to):
        grid = self.grid

        if grid:
            # Move the rowLabels and data rows
            oldLabel = self.grid.rowLabels[frm]
            oldData = self.grid.data[frm]
            del self.grid.rowLabels[frm]
            del self.grid.data[frm]

            if to > frm:
                self.grid.rowLabels.insert(to-1,oldLabel)
                self.grid.data.insert(to-1,oldData)
            else:
                self.grid.rowLabels.insert(to,oldLabel)
                self.grid.data.insert(to,oldData)

            # Notify the grid
            grid.BeginBatch()

            msg = wx.grid.GridTableMessage(
                    self.grid, wx.grid.GRIDTABLE_NOTIFY_ROWS_DELETED, frm, 1
                    )

            grid.ProcessTableMessage(msg)

            msg = wx.grid.GridTableMessage(
                    self.grid, wx.grid.GRIDTABLE_NOTIFY_ROWS_INSERTED, to, 1
                    )

            grid.ProcessTableMessage(msg)
            grid.EndBatch()
             

    def EvtComboBox(self, event):
        print('')#Evento de combo box: %s' % event.GetString())

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
            self.tChoiceEditor = wx.grid.GridCellChoiceEditor(["Sum","Media","Max","Min"], allowOthers=True)
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

    def GetRowsValue(self):
        datos = [[0 for x in range(4)] for x in range(self.rows)] 
	for i in range(0,self.rows):
    	    for j in range(0,self.fila):
		datos[i][j] = self.grid.GetCellValue(i,j)
        return datos
