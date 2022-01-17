code = 20151125
row = col = 1
while (row,col) != (2981,3075):
    if row == 1:
        row = col + 1
        col = 1
    else:
        row -= 1
        col += 1
    code = (code * 252533) % 33554393
print("Part 1:",code)