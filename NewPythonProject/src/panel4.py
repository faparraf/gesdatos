#!#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import wx.grid
import ConnectionDataBase
import ConnSchema
import pprint
import pruebashell



class Panel4(wx.Panel,):
    def __init__(self, parent,connection,*args, **kwds):
        self.conn = connection
        self.connSchema = ConnSchema.ConnSchema(self.conn)
        #Interfaz
        self.rows = 0
        self.fila = 0
        wx.Panel.__init__(self, parent)

                
        self.button = wx.Button(self, label="Agregar", pos=(25, 110), size=(80,50))
        self.Bind(wx.EVT_BUTTON, self.Agregar,self.button)

        self.button_2 = wx.Button(self, label="Eliminar", pos=(25, 170),size=(80,50))
        self.Bind(wx.EVT_BUTTON, self.Eliminar,self.button_2)
        
        

        self.grid_panel = wx.Panel(self,pos=(200,20),size=(620,300))
        self.grid = wx.grid.Grid(self.grid_panel,pos=(5,5))
        self.grid.CreateGrid(0, 5)
        self.grid.SetColLabelValue(0,"Operador Lógico")
        self.grid.SetColLabelValue(1,"Campo1")
        self.grid.SetColLabelValue(2,"Criterio")
        self.grid.SetColLabelValue(3,"Campo2")
        self.grid.SetColLabelValue(4,"Valor")
        self.grid.SetRowLabelSize(20)
        self.grid.SetColSize(0,130)
        self.grid.SetColSize(1,120)
        self.grid.SetColSize(2,120)
        self.grid.SetColSize(3,115)
        self.grid.SetColSize(4,115)
        dimensionador = wx.BoxSizer(wx.VERTICAL) 
        dimensionador.Add(self.grid, 1, wx.EXPAND | wx.ALL,border=10)
        self.grid_panel.SetSizer(dimensionador)
        pp = pprint.PrettyPrinter(indent=4)
        
        #DataBase
        
        
        #pp.pprint(self.connCategoria.GetCategorias())
      
        

    def on_edit_cell(self, event):
        
        print "CELL EDITING", event.GetString()

    def EvtComboBoxTbOrigen(self, event):
        sampleList3 = self.connSchema.GetPrimaryKeys("DBPrueba",event.GetString())
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(sampleList3)
        self.cbxClOrigen.SetItems(sampleList3)

    def EvtComboBoxClOrigen(self, event):
        print('Evento de combo box: %s' % event.GetString())

    def EvtComboBoxTbDestino(self, event):
        print('Evento de combo box: %s' % event.GetString())
             

    def EvtComboBoxClDestino(self, event):
        print('Evento de combo box: %s' % event.GetString())

        
   

    def Agregar(self,event):

        self.grid.AppendRows()
        self.tChoiceEditor1 = wx.grid.GridCellChoiceEditor(["And","OR"], allowOthers=True)
        self.grid.SetCellEditor(self.fila, 0, self.tChoiceEditor1)

        self.tChoiceEditor2 = wx.grid.GridCellChoiceEditor([""], allowOthers=True)
        self.grid.SetCellEditor(self.fila, 1, self.tChoiceEditor2)

        self.tChoiceEditor3 = wx.grid.GridCellChoiceEditor(["=","!=","<",">",">=","<="], allowOthers=True)
        self.grid.SetCellEditor(self.fila, 2, self.tChoiceEditor3)
        
        self.tChoiceEditor4 = wx.grid.GridCellChoiceEditor([""], allowOthers=True)
        self.grid.SetCellEditor(self.fila, 3, self.tChoiceEditor4)
        
        self.fila += 1
        self.rows += 1
        
        self.grid.MakeCellVisible(self.rows, 0)
        self.grid.ForceRefresh()
        

    def Eliminar(self,event):
        
        if self.rows > 0: 
            self.grid.DeleteRows(self.rows-1)
            self.rows -= 1
            self.fila -= 1
            self.grid.ForceRefresh()
            
    

