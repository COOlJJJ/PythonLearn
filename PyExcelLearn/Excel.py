import datetime

import xlrd

# 读取Excel
# 使用pip install xlrd==1.2.0 新版不支持xlsx
# 文件名以及路径，如果路径或者文件名有中文给前面加一个r拜师原生字符。
data = xlrd.open_workbook(r"C:\Users\Z0047YMR\Desktop\ST160设备.xlsx")

# table = data.sheets()[0]          #通过索引顺序获取
# table = data.sheet_by_index(0) #通过索引顺序获取
table = data.sheet_by_name('Sheet1')  # 通过名称获取

for i in range(table.nrows):
    print(table.row_values(i))
# 获取某sheet中的有效行数
print(table.nrows)
# 获取整行数据
rows_value = table.row_values(1)
print(rows_value)

# 获取整列数据
cols_value = table.col_values(1)
print(cols_value)

# 读取单元格
cell_A1 = table.cell(0, 0).value
print(cell_A1)
cell_A2 = table.cell(0, 1).value
print(cell_A2)
# 使用行/列索引
cell_B1 = table.row(0)[1].value
print(cell_B1)
cell_B2 = table.col(4)[1].value
print(cell_B2)

# python读取excel中单元格的内容返回的有5种类型。ctype : 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
type1 = table.cell(1, 4).ctype
print(type1)

date = xlrd.xldate_as_tuple(cell_B2, 0)
print(date)
print(datetime.date.today())
# 时间转换
print(datetime.datetime(*date))
