grid = [['.','.','.','.','.','.'],
        ['.','0','0','.','.','.'],
        ['0','0','0','0','.','.'],
        ['0','0','0','0','0','.'],
        ['.','0','0','0','0','0'],
        ['0','0','0','0','0','.'],
        ['0','0','0','0','.','.'],
        ['.','0','0','.','.','.'],
        ['.','.','.','.','.','.']]
gridlen = len(grid)
cyctime = len(grid[0])
for x in range(cyctime):
    for j in range(gridlen):
        print(grid[j][x]),
    print "\n"
