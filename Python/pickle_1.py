import pickle

# dump & dumps函数    第三个参数 表示 协议
dataList = [[1, 1, 'yes'],
            [1, 1, 'yes'],
            [1, 0, 'no'],
            [0, 1, 'no'],
            [0, 1, 'no']]
dataDic = { 0: [1, 2, 3, 4],
            1: ('a', 'b'),
            2: {'c':'yes','d':'no'}}

with open('dataFile.pkl', 'wb') as f:
  pickle.dump(dataList, f, -1)
  pickle.dump(dataDic, f, -1)

with open('dataFile.pkl', 'rb') as  f:
  data1 = pickle.load(f)
  data2 = pickle.load(f)

print(data1)
print(data2)