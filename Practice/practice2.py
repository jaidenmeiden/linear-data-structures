from customGrid import CustomGrid

matrix = CustomGrid(3, 3)
print(matrix)
for row in range(matrix.get_height()):
    for column in range(matrix.get_width()):
        matrix[row][column] = row * column

print(matrix)
print("height:", matrix.get_height())
print("width:", matrix.get_width())
print("getitem (Row):", matrix.__getitem__(1))
print("getitem (Value):", matrix.__getitem__(2)[0])
print(matrix.__str__())
