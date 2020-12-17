# 字符串居左,居中,居右对其

print('居左'.ljust(21, '-'))
print('居右'.rjust(21, '-'))
print('居中'.center(21, '-'))

print(format('居左', '*>20'))
print(format('居右', '*<20'))
print(format('居中', '*^20'))
