def manhattan(array):
    adding = 0
    for i in array:
        adding+= abs(145-i[0])
        adding+= abs(140-i[1])
        adding+= abs(122-i[2])
        print(adding)
        adding=0

manhattan([[3, 14, 16],[84, 68, 115],[121, 172, 173],[152, 193, 195],[112, 158, 156],[93, 147, 149],[144, 185, 187],[88, 136, 150],[93, 139, 137],[250, 247, 242],[19, 29, 98],[129, 174, 177],[102, 132, 0],[201, 54, 60],[32, 82, 81],[61, 107, 105],[88, 156, 227],[11, 31, 32],[145, 186, 188],[104, 124, 249],[254, 193, 14],[135, 180, 185],[100, 127, 32],[163, 198, 200],[127, 175, 177]])