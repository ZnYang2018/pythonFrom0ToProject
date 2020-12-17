# 获取ASCII (Unicode)对应的字符
while True:
    val = input('Please input an ascii (0-1114111)\n')
    if val.isdigit():
        int_val = int(val)
        if 0 <= int_val < 0x110000:
            print(f'{val}=>{chr(int_val)}')
