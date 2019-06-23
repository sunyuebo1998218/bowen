import xlrd
def shuju():
    a=[]
    f=xlrd.open_workbook(r'E:\python\接口框架\data\新建 Microsoft Excel 工作表 (3).xlsx')
    sheet=f.sheets()[0]
    for i in range(sheet.nrows):
        a.append(sheet.row_values(i))

    return a
shuju()