#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Gesdatos"
__date__ = "$20-jul-2015 18:52:55$"
import wx
from wx import Frame, Panel, BoxSizer, VERTICAL, GROW, ALL, PySimpleApp 
from wx.grid import PyGridTableBase, GridTableMessage, GRIDTABLE_NOTIFY_ROWS_APPENDED, Grid 
from wx.grid import GRIDTABLE_NOTIFY_ROWS_DELETED, GRID_VALUE_STRING,EVT_GRID_CELL_LEFT_CLICK 
from wx.grid import GRIDTABLE_NOTIFY_COLS_DELETED, GRIDTABLE_NOTIFY_COLS_APPENDED 
from wx.grid import GRID_VALUE_BOOL, GRID_VALUE_NUMBER, GRID_VALUE_FLOAT, GRID_VALUE_CHOICE 
from wx.grid import GRID_VALUE_TEXT, GRID_VALUE_LONG,GRID_VALUE_CHOICEINT, GRID_VALUE_DATETIME 
import os, shelve

class DynamicTable(PyGridTableBase): 
    """ 
       DynamicTable: A table with dynamic column names, types and data. 
       Data is retrieved from a shelved file, specified in the constructor. 
       The table can be configured using: 
           AddColumn 
           DeleteColumn 
           AddRow 
           SaveDataToFile 
    """ 

    def __init__(self,parent_grid, file_name):
        'Inicia las carateristicas de las tablas dinámicas'
        PyGridTableBase.__init__(self) 
        self.file_name = file_name 
        self.parent_grid = parent_grid 

        self.column_names, self.column_types, self.column_configs, self.grid_data = self.GetDataFromFile(file_name) 
        #print "Filas: "+str(self.GetNumberRows())
    def __del__(self): 
        'Permite conservar los datos dentro de las tablas'
        self.SaveDataToFile(self.file_name) 

    def GetDataFromFile(self, file_name): 
        """ 
        GetDataFromFile(self, file_name) returns a tuple of data from the file 
        in the following format: 
        (list of column names, list of column types, list of column config 
        data, list of data)  """  
        if not False: #os.path.exists(file_name): 
            return [],[],[], [] 

        shelf = shelve.open(file_name) 
        column_names = shelf['column_names'] 
        column_types = shelf['column_types'] 
        column_configs = shelf['column_configs'] 
        grid_data = shelf['grid_data'] 
        shelf.close() 
        return column_names, column_types, column_configs, grid_data

    def SaveDataToFile(self, file_name): 
        """ 
        SaveDataToFile(self, file_name) saves the column name list, column type list, 
        column config data and data list to the file specified. 
        """ """ 
        if file_name == '': 
            file_name = "%s\\%s" % (os.path.curdir, 'DynamicTable.dat') 
        shelf = shelve.open(file_name,'c',True) 
        shelf['column_names'] = self.column_names 
        shelf['column_types'] = self.column_types 
        shelf['column_configs'] = self.column_configs 
        shelf['grid_data'] = self.grid_data 
        shelf.close() 
        """ 
        
    def GetNumberRows(self): 
        "GetNumberRows is required by the PyGridTableBase interface." 
        return len(self.grid_data) + 1 

    def GetNumberCols(self): 
        "GetNumberCols is required by the PyGridTableBase interface." 
        return len(self.column_names) 

    def IsEmptyCell(self, row, col): 
        "IsEmptyCell is required by the PyGridTableBase interface." 
        try: 
            return not self.grid_data[row][col] 
        except IndexError: 
            return True 

    def GetValue(self, row, col): 
        try: 
            return self.grid_data[row][col] 
        except IndexError: 
            return '' 

    def SetValue(self, row, col, value): 
        #try: 
            if self.column_types[col] == GRID_VALUE_BOOL and value == '': 
                print str(row)+" "+str(col)+" "+str(value)
                value = 0
            print str(len(self.grid_data))+"___ "+str(len(self.grid_data))+" "+str(value)
            self.grid_data[row][col] = value
            
            print str(row)+"---- "+str(col)+" "+str(value)
    
        #except IndexError:
            print str(row)+"+++++ "+str(col)+" "+str(value)
            # add a new row 
            #self.AddRow([''] * self.GetNumberCols()) 

            #This is called recursively: new_row# - cur_max_row# times. 
            self.SetValue(row, col, value) 


    def GetColLabelValue(self, col): 
        "Used to display column names" 
        return self.column_names[col] 

    def GetTypeName(self, row, col): 
        "Returns the column's type" 
        return "%s:%s" %(self.column_types[col], self.column_configs[col]) 

    def CanGetValueAs(self, row, col, typeName): 
        "Returns whether or not the type Name matches the column type." 
        return typeName == self.column_types[col] 

    def CanSetValueAs(self, row, col, typeName): 
        return self.CanGetValueAs(row, col, typeName) 

    def AddColumn(self, column_name, column_type, column_config,default_value = None): 
        "Adds a grid column using the data specified. Note: default_value"
   
        self.column_names.append(column_name) 
        self.column_types.append(column_type) 
        self.column_configs.append(column_config) 

        if len(self.grid_data) > 0: 
            new_data = [] 
            for row in self.grid_data: 
                new_data.append(row.append(default_value)) 
            self.grid_data = new_data 
        self.NotifyGrid(GRIDTABLE_NOTIFY_COLS_APPENDED, 1) 
    def DeleteColumn(self, column_name): 
        "Deletes the column specified by the column_name." 
        error_text = "Specified column name can't be deleted because it"
        assert column_name in self.column_names, error_text 

        column_loc = column_names.index(column_name) 
        self.column_names.pop(column_loc) 
        self.column_types.pop(column_loc) 
        self.column_configs.pop(column_loc) 

        if len(self.grid_data) > 0: 
            new_data = [] 
            for row in self.grid_data: 
                row.pop(column_loc) 
                new_data.append(row) 

            self.grid_data = new_data                 
        self.NotifyGrid(GRIDTABLE_NOTIFY_COLS_DELETED, 1) 
    def AddRow(self, row): 
        "Adds the specified row to the grid." 
        error_text = "AddRowError: Number of columns in row to add doesn't match the number of columns in the grid." 
        assert len(row) == len(self.column_names), error_text 

        self.grid_data.append(row) 
        self.NotifyGrid(GRIDTABLE_NOTIFY_ROWS_APPENDED, 1)                 
                

    def DeleteRow(self, row_number): 
        'Borra las filas que se desean descartar de la interfaz'
        assert row_number < self.GetNumberRows(), "Cannot delete a non-existant row." 
        self.grid_data.pop(row_number) 
        tbl_msg = GridTableMessage(self, GRIDTABLE_NOTIFY_ROWS_DELETED, 1) 
                                
        self.GetView().ProcessTableMessage(tbl_msg) 
        
    def NotifyGrid(self, msg, count): 
        "Notifies the gird of the message and the affected count." 
        tbl_msg = GridTableMessage(self, msg, count)                       
          
        self.GetView().ProcessTableMessage(tbl_msg) 

class DynamicGrid(Grid): 
    def __init__(self, parent, file_name): 
        'Inicia las tablas dinámicas'
        Grid.__init__(self, parent, -1) 

        table = DynamicTable(self,file_name) 

        self.SetTable(table, True) 

        self.SetRowLabelSize(0) 
        self.SetMargins(0,0) 
        self.AutoSizeColumns(False) 
