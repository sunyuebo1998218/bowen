import xlrd
def shuju():
    a=[]
    f=xlrd.open_workbook(r'E:\python\web自动化\data\shuju.xlsx')
    sheet=f.sheets()[0]
    for i in range(sheet.nrows):
        a.append(sheet.row_values(i))

    return a
shuju()