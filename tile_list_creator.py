## tile_list_creator.py

x1 = int(input('enter starting x: '))
y1 = int(input('enter starting y: '))

x2 = int(input('enter ending x: '))
y2 = int(input('enter ending y: '))

LIST = [(x1,y1)]


if x1 == x2:

    while y1 < y2:
        y1 += 1
        LIST.append((x1,y1))
    print(LIST)

elif y1 == y2:

    while x1 < x2:
        x1 += 1
        LIST.append((x1,y1))

    print(LIST)
    
