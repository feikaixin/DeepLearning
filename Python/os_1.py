import os


# 获取文件的绝对路径 
os.path.abspath(__file__)
# 获取当前文件所在文件夹的路径
os.getcwd()
# 创建一个文件件
os.mkdir('fei')
# 删除 指定位置的文件夹 
os.rmdir('fei')
# 删除文件
os.remove('fei.txt')
# 分离文件名与扩展名  返回的 值是一个tuple
os.path.splitext(os.path.abspath(__file__))

# 判断给出的路径是否是一个文件夹
os.path.isdir('/')

# 判断给出的 是不是 一个文件
os.path.isfile('/')

# 返回..  代表当前的父目录
os.pardir

# 更改当前的 工作目录
os.chdir('/')