
import openpyxl,xlrd
import matplotlib.pyplot as plt
import pandas 
import csv 
#这两行代码解决 plt 中文显示的问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# #excel文件的读取
# file=xlrd.open_workbook('c:\\Users\\btr\Desktop\\screeSharesInfo1.xlsx')


# sheet = file.sheet_by_name("new title")
# # 获取表的行数
# nrows = sheet.nrows
# # 获取表的列数
# ncols = sheet.ncols
# print("行: %d, 列: %d" % (nrows, ncols))

# #以下代码为参考代码
# #获取第一行的内容,索引从0开始
# row = sheet.row_values(0)
# #获取第一列的整列的内容
# col = sheet.col_values(0)
# #获取第一列，第0~4行（不含第4行）
# sheet.col_values(0,0,4)
# #获取单元格值，第几行第几个，索引从0开始
# sheet.cell(2,0).value


# # 获取第一行第一列的数据
# cell_value = sheet.cell_value(0, 0)
# print(cell_value)
 
# # 获取第一行的数据
# row_value = sheet.row_values(0)
# print(row_value)




# #x轴，不变的
# sheet.col_values(0,1,:)
# #y轴，可变的
# sheet.col_values(20,1,:)



# industry=sheet.col_values(20,1,int(sheet.nrows))
# info=industry.groupby(industry)
# print(info)

# #这两行代码解决 plt 中文显示的问题
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False

# shares = ('碳酸饮料', '绿茶', '矿泉水', '果汁', '其他')
# ratio = [6, 7, 6, 1, 2]

# plt.bar(shares, ratio)
# plt.title('11')

# plt.show()
# input()




#1.加载数据集
df=pandas.read_excel("c:\\Users\\btr\\Desktop\\screeSharesInfo1.xlsx")

# print("\n每个行业的平均市盈率：")
# #print(df.groupby('行业一级')['市盈率'].mean())

# print(df.groupby('行业一级')['行业一级'].count().sort_values())

# print(df.groupby('行业一级')['行业一级'].count().sort_values()[2])

# print(type(df.groupby('行业一级')['行业一级'].count()))
# print("\n分组：")
# print(type(df.groupby('行业一级')))

# print("\n分组->感兴趣的列：")
# print(type(df.groupby('行业一级')['市盈率']))


industry_statistics = df.groupby(['行业一级'])['行业一级'].count().sort_values()
industry_statistics.plot(kind='bar',figsize=(10, 5), title='行业统计',xlabel='行业',ylabel='个数')
aa=pandas.DataFrame(industry_statistics)
print(type(aa))
print(aa)
plt.show()



# tips=sns.load_dataset("tips")
# print(tips.head())
# fig=plt.figure()
# histogram=fig.add_subplot(1,1,1)
# histogram.hist(tips['total_bill'],bins=10)
# histogram.set_title("Histogram of Total Bill")
# histogram.set_xlabel("Frequency")
# histogram.set_ylabel("Total Bill")
# fig.show()
# input()


