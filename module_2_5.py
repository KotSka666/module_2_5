import pprint # импортируем pprint 
def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        row = []
        matrix.append(row)
        for j in range(m):
            row.append(value)
    return matrix

print(get_matrix(10, 5, 20)) # вывести в строчку
pprint.pprint(get_matrix(10, 5, 20))# более удобно для чтения

