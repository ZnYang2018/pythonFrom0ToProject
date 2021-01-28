# 从路径中获取文件名
import os

full_path = r'D:\github\ZnYang2018\pythonFrom0ToProject\PythonFromZeroToProject\src\Chapter14\sample05.py'
file_name = os.path.basename(full_path)
print(file_name)
dir_name = os.path.dirname(full_path)
print(dir_name)
print('-' * 80)
head, tail = os.path.split(full_path)
print(head)
print(tail)
print('-' * 80)
name, ext = os.path.splitext(file_name)
print(name)
print(ext)
