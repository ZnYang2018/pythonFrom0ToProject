with open('picture.png', 'rb') as picture:
    print(type(picture))
    print(picture)

with open('text.txt', 'r') as text:
    print(type(text))
    print(text)
    print(text.readline())
    while True:
        line = text.readline()
        print(f'Line: {line}')
        if line == '':
            break
