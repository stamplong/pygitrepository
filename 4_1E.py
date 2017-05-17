spam1 = []
j = 0
for list_1 in range(8):
    spam1[j][list_1] = "."
    if list_1 == 2 or list_1 == 3 or list_1 == 5 or list_1 == 6:
        spam1[j][list_1] = "0"
    elif list_1 == range(1,7):
        spam1[j][list_1] == '0'
    j +=1
