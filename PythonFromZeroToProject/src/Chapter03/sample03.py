# 获取字符对应的ASCII (Unicode)编码
while True:
    char = input('Please input one character\n')
    if len(char) == 1:
        print(ord(char))
    else:
        print(f'One character please. Actual {len(char)}')