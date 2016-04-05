# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 20:30:09 2016

@author: Aman Deep
"""

print("INVENTO Welcomes you!")

user_need = 0

while user_need !=1 and user_need !=2:
    print("What do you want to do? \n 1) Add new item \n  3)transact ")
    user_need = int(raw_input("1 or 2"))
    if user_need!=1 and user_need!=2:
        print("Please enter a valid command.")

        
        
if user_need == 1:
    print("You have chosen to add a new item")
    from xlrd import open_workbook
    rb= open_workbook('data.xls')
    from xlutils.copy import copy
    wb=copy(rb)
    new_item=raw_input("Please Enter the name of the new ITEM.")
    number_of_packing_sizes=int(raw_input("Please Enter the number of packing sizes available."))    
    packing_size=[]    
        
    for i in xrange(0,number_of_packing_sizes):
        var="Please Enter the packing size, {}".format(i+1)    
        packing_size.append(raw_input(var)) 
    sheet1 = wb.add_sheet(new_item)
    sheet1.write(1,0,'Packing Sizes') 
    for i in xrange(0,number_of_packing_sizes):
       sheet1.write(1,i+1,packing_size[i]) 
    sheet1.write(4,0,'transaction ID')
    sheet1.write(4,1,'Date and Time')
    sheet1.write(0,3,'Number of Transactions')    
    sheet1.write(4,2,'Packing Size')
    sheet1.write(4,3,'Transaction')
    for i in xrange(0,number_of_packing_sizes):
        var="Packets of size {}".format(i+1)
        sheet1.write(4,4+i,var)
        
    sheet1.write(4,5+i,'Total Stock')            
    wb.save('data_temp.xls')           #to keep original file safe 
    import os
    os.remove('data.xls')
    os.rename('data_temp.xls','data.xls')
    
    

if user_need == 2:
    print("what kind of transaction is it? \n 1) In \n 2) Out")
    trns_type = raw_input("1 or 2?")
    if trns_type==1:
        trns_item=int(raw_input("1or 2 or 3"))
    
    