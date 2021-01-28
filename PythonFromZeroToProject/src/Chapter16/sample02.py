import os

os.system('cls')
os.system('cd D:\\')
os.system(r'cd D:\github\ZnYang2018\pythonFrom0ToProject')
diff_stream = os.popen('git diff d32fc616624337552328007ab25057cc078c7bb4 1cba22a81497a7212808df7f48d6740c193a6c94 --full-index')

try:
    result = diff_stream.read()
    print(result)
except Exception as e:
    print(e)