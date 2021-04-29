
"""

|--------------------------------------------------
|                                                 |
|      initialize early data of matrix            |
|                                                 |
|--------------------------------------------------
|                                                 |
|        1. read data from txt file               |
|        1. map data into dictionary              |
|                                                 |
|--------------------------------------------------

"""
#initialize step
row_a = 2
col_a = 2
col_b = 2

mapperOutput = open("mapperOutput.txt", "w")











"""

|--------------------------------------------------
|                                                 |
|                    Map                          |
|                                                 |
|--------------------------------------------------
|                                                 |
|        1. for each (i , k )                     |
|           create (key , value)                  |
|            key : ( i , k)                       |
|            Value : M(ik)                        |
|                                                 |
|--------------------------------------------------

"""
#Start Map


for line in open("input.txt"):
    matrix_index, row, col, value = line.rstrip().split(",")
    if matrix_index == "A":
        for i in range(0, col_b):
            key = row + "," + str(i)
            mapperOutput.write("%s\t%s\t%s" % (key, col, value) + "\n")
    else:
        for j in range(0, row_a):
            key = str(j) + "," + col
            mapperOutput.write("%s\t%s\t%s" % (key, row, value) + "\n")
mapperOutput.close()


"""

|--------------------------------------------------
|                                                 |
|                   Shuffle                       |
|            group && aggregation                 |
|                                                 |
|--------------------------------------------------
|                                                 |
|                                                 |
|     for each item in  list mentioned            |
|         for each item in new list               |
|            if(key[0] == key[1] && j[0] == j[1]) |
|                list mentioned[item] *           |
|                    new list[item]               |
|                                                 |
|                                                 |
|--------------------------------------------------

"""
#Start Shuffle

numbers1 = list()
for line in open("mapperOutput.txt"):
    curr_index, index, value = line.rstrip().split("\t")
    index, value = map(int, [index, value])
    numbers1.append((curr_index, index, value))
numbers2 = numbers1
initValue1 = list()
initValue2 = list()
for i in numbers1:
    checker = 0
    for j in numbers2:
        if i == j:
            if checker == 0:
                checker += 1
                continue
        if i[0] == j[0]:
            if i[1] == j[1]:
                initValue1.append([i[0],str(i[1]),i[2]*j[2]])


"""

|--------------------------------------------------
|                                                 |
|                    Reduce                       |
|                                                 |
|--------------------------------------------------
|                                                 |
|                                                 |
|   Compare each item in the list with itself     |
|        if (key[0] == key[1] && j[0] != j[1])    |
|         find key in new list and append to them |
|                                                 |
|--------------------------------------------------

"""
#Start Reduce


initValue2 = initValue1
myOut = dict()
counter = 0
for i in initValue1:
    if counter > (row_a*col_b*col_a):
        break
    if i[0] in myOut.keys():
        counter += 1
        continue
    counter += 1
    myOut[i[0]] = i[2]
    inercounter = 0
    for j in initValue2:
        if i[0] == j[0]:
            if i[1] != j[1]:
                inercounter += 1
                if inercounter > col_b - 1:
                    continue
                myOut[i[0]] += j[2]

for key,value in myOut.items():
    print(key,value)