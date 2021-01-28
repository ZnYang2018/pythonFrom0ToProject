import os
import os.path
print(repr(os.sep)) # \
print(repr(os.linesep)) # \r\n
print(os.getcwd()) # current working directory


print(os.path.abspath(r'a\b'))
path = r'D:\GitHub\ZnYang2018\pythonFrom0ToProject\PythonFromZeroToProject\src\Chapter14\sample01.py'
# 文件名
print(os.path.basename(path)) # sample01.py
# 目录名
print(os.path.dirname(path)) # D:\GitHub\ZnYang2018\pythonFrom0ToProject\PythonFromZeroToProject\src\Chapter14
# 文件名与扩展名分离
print(os.path.splitext(path)) # D:\GitHub\ZnYang2018\pythonFrom0ToProject\PythonFromZeroToProject\src\Chapter14  sample01.py
print(os.path.splitext(os.path.basename(path))) # ('sample01', 'py')

print('\\'.join(['a','b','c']))
print(os.path.join('a', 'b','c'))