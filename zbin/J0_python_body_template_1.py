#  《First_Define_Template_1》= 《# 【ZHoldPlace_NodeName】_zukgit_website  =   【ZHoldPlace_Node_Website】》
#  《First_Define_Template_1》= 《createexcel('【ZHoldPlace_Title】.xlsx')》
#  《First_Define_Template_2》= 《【ZHoldPlace_pythonMethodName】_book = load_workbook('【ZHoldPlace_J0_Dir_PATH】【ZHoldPlace_Title】.xlsx')》
#  《First_Define_Template_3》= 《【ZHoldPlace_pythonMethodName】_excel_writer = pd.ExcelWriter('【ZHoldPlace_J0_Dir_PATH】【ZHoldPlace_Title】.xlsx', engine='openpyxl')》
#  《First_Define_Template_4》= 《【ZHoldPlace_pythonMethodName】_excel_writer.book = 【ZHoldPlace_pythonMethodName】_book》
#  《First_Define_Template_5》= 《【ZHoldPlace_pythonMethodName】_excel_writer.sheets = dict((ws.title, ws) for ws in 【ZHoldPlace_pythonMethodName】_book.worksheets)》
#  《First_Define_Template_6》= 《【ZHoldPlace_pythonMethodName】_data_List = pd.DataFrame()》

#  《Method_Call_Template_1》= 《【ZHoldPlace_propKey2ValueList_Index】 = pro.【ZHoldPlace_pythonMethodName】(【ZHoldPlace_propKey2ValueList】, fields='【ZHoldPlace_fieldList】')》
# 《Method_Call_Template_3》=  《print(" 【ZHoldPlace_leaf_chinese_title】 【ZHoldPlace_propKey2ValueList_Index】 返回数据 row 行数 = "+str(【ZHoldPlace_propKey2ValueList_Index】.shape[0]))》 
#  《Method_Call_Template_2》= 《【ZHoldPlace_pythonMethodName】_data_List = 【ZHoldPlace_pythonMethodName】_data_List.append(【ZHoldPlace_propKey2ValueList_Index】)》

#  《Tail_Define_Template_1》=  《print("【ZHoldPlace_pythonMethodName】_data_List.__len__() = "+str(【ZHoldPlace_pythonMethodName】_data_List.__len__()))》
#  《Tail_Define_Template_1》=  《【ZHoldPlace_pythonMethodName】_data_List.to_excel(【ZHoldPlace_pythonMethodName】_excel_writer,'【ZHoldPlace_leaf_chinese_title】',index=False)》
#  《Tail_Define_Template_2》= 《【ZHoldPlace_pythonMethodName】_excel_writer.save()》




############################## 头部定义  Begin ##############################
#《Head_Define_Template》
############################## 头部定义  End ##############################


############################## 循环method调用  Begin ##############################
#《Method_Call_Template》
############################## 循环method调用  End ##############################


############################## 尾部  Begin ##############################
#《Tail_Define_Template》
############################## 尾部  End ##############################


"""  方法调用模板
         ###################   头部定义 Begin ###################
stock_basic_book = load_workbook('股票列表.xlsx')
stock_basic_excel_writer = pd.ExcelWriter('股票列表.xlsx', engine='openpyxl')
stock_basic_excel_writer.book = stock_basic_book
stock_basic_excel_writer.sheets = dict((ws.title, ws) for ws in stock_basic_book.worksheets)
data_List_stock_basic = pd.DataFrame;
          ###################   头部定义 End ###################


          ###################   调用数据Method Begin ###################
data_L = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,fullname,enname,market,exchange,curr_type,list_status,list_date,delist_date,is_hs')
data_List_stock_basic = data_List_stock_basic.append(data_L);

data_D = pro.stock_basic(exchange='', list_status='D', fields='ts_code,symbol,name,area,industry,fullname,enname,market,exchange,curr_type,list_status,list_date,delist_date,is_hs')
data_List_stock_basic = data_List_stock_basic.append(data_D);
          ###################   调用数据Method End ###################


          ###################   尾部定义 Begin ###################
data_List_stock_basic.to_excel(stock_basic_excel_writer,'股票列表')
stock_basic_excel_writer.save()
          ###################   尾部定义 End ###################
"""