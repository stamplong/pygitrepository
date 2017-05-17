tableDate = [['apples','orange','cherries','banana'],
             ['alice','Bob','carol','david'],
             ['dogs','cats','moose','goose']]
for x in range(len(tableDate[0])):
    for y in range(len(tableDate)):
        print tableDate[y][x].rjust(10),
    print '\n'
