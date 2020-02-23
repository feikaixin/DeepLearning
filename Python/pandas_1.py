import pandas as pd

df = pd.DataFrame([[1,2,3],[4,5,6]],columns=["a", "b", "c"])

# 获取列名字
df.columns.values

# 读取文件
csv = pd.read_csv('../SalesJan2009.csv')

# 获取数据
csv.iloc[1,:]
csv.Transaction_date

# 添加列
csv["Price2"] = csv.Price
# 添加行
csv2 = csv.append(csv, ignore_index=True)

# 复杂查询
# select * from csv where Latitude>30
a = csv.loc[(csv.Latitude>30) & (csv.Latitude>0),:].reset_index()

# select * from csv where Country like 'Aus%'
b = csv.loc[csv.Country.str.startswith('Aus') , :].reset_index()

# 去除空格  左边空格lstrip  右空格 rstrip
csv.Country = csv.Country.str.rstrip()

# order by
csv.sort_values('Price', ascending=False)

# group by
f = csv.groupby(csv.Country).mean()
print(f)



