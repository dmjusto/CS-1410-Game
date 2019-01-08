## tile_list_maker.py

from random import *

platformList1 = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),
                 (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (0, 12), (0, 13),
                 (0, 14), (0, 15), (0, 16),(1, 0), (2, 0), (3, 0), (4, 0),
                 (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0),
                 (12, 0), (13, 0), (14, 0), (15, 0), (16, 0), (17, 0),
                 (18, 0), (19, 0), (20, 0), (21, 0), (22, 0), (23, 0),
                 (24, 0), (25, 0),(26, 0), (26, 1), (26, 2), (26, 3),
                 (26, 4), (26, 5), (26, 6), (26, 7), (26, 8), (26, 9),
                 (26, 10), (26, 11), (26, 12), (26, 13), (26, 14), (26, 15),
                 (26, 16),(1, 16), (2, 16), (3, 16), (4, 16), (5, 16), (6, 16),
                 (7, 16), (8, 16), (9, 16), (10, 16), (11, 16), (12, 16),
                 (13, 16), (14, 16), (15, 16), (16, 16), (17, 16), (18, 16),
                 (19, 16), (20, 16), (21, 16), (22, 16), (23, 16), (24, 16),
                 (25, 16),(4, 3), (5, 3), (6, 3), (7, 3), (8, 3), (9, 3), (10, 3),
                 (11, 3),(9, 9), (10, 9), (11, 9), (12, 9),(13, 6), (14, 6),
                 (15, 6),(14, 12), (15, 12), (16, 12), (17, 12), (18, 12),
                 (19, 12), (20, 12),(23, 14), (24, 14), (25, 14),(23, 15),
                 (24, 15), (25, 15)]



def main():
    
    platformList2 = []
    platformList3 = []
    i =0
    for x in range(0,len(platformList1)//3):
            i = randint(0,len(platformList1))
            platformList2.append(platformList1[i])
            del platformList1[i]

    for x in range(0,int(len(platformList1)//2.5)):
        i = randint(0,len(platformList1))
        platformList3.append(platformList1[i])
        del platformList1[i]

    print('platformList1 = ',platformList1)
    print('platformList2 = ',platformList2)
    print('platformList3 = ',platformList3)

main()
