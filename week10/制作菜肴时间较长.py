#以i,j为右下角的矩阵的大小为（i-1，j-1）最大值，边界全设为0
def top_left_max(matrix,rows,cols):
    top_lest_max_matrix = [[0 for i in range(cols)] for j in range(rows)]
    for i in range(1,rows-1):
        for j in range(1,cols-1):
            if i==1:
                top_lest_max_matrix[i][j] = max(top_lest_max_matrix[i][j-1],matrix[i-1][j-1])
            elif j==1:
                top_lest_max_matrix[i][j] = max(top_lest_max_matrix[i-1][j],matrix[i-1][j-1])
            else:
                top_lest_max_matrix[i][j] = max(top_lest_max_matrix[i-1][j],top_lest_max_matrix[i][j-1],matrix[i-1][j-1])
    return top_lest_max_matrix

#以i,j为右上角的矩阵的大小为（i-1，j-1）最大值，边界全设为0
def bottom_left_max(matrix,rows,cols):
    bottom_left_max_matrix = [[0 for i in range(cols)] for j in range(rows)]
    for i in range(rows-2,0,-1):
        for j in range(1,cols-1):
            if i==rows-2:
                bottom_left_max_matrix[i][j] = max(bottom_left_max_matrix[i][j-1],matrix[i+1][j-1])
            elif j==1:
                bottom_left_max_matrix[i][j] = max(bottom_left_max_matrix[i+1][j],matrix[i+1][j-1])
            else:
                bottom_left_max_matrix[i][j] = max(bottom_left_max_matrix[i+1][j],bottom_left_max_matrix[i][j-1],matrix[i+1][j-1])
    return bottom_left_max_matrix

#以i,j为左下角的矩阵的大小为（i-1，j-1）最大值，边界全设为0

def top_right_max(matrix,rows,cols):
    top_right_max_matrix = [[0 for i in range(cols)] for j in range(rows)]
    for i in range(1,rows-1):
        for j in range(cols-2,0,-1):
            if i==1:
                top_right_max_matrix[i][j] = max(top_right_max_matrix[i][j+1],matrix[i-1][j+1])
            elif j==cols-2:
                top_right_max_matrix[i][j] = max(top_right_max_matrix[i-1][j],matrix[i-1][j+1])
            else:
                top_right_max_matrix[i][j] = max(top_right_max_matrix[i-1][j],top_right_max_matrix[i][j+1],matrix[i-1][j+1])
    return top_right_max_matrix

#以i,j为左上角的矩阵的大小为（i-1，j-1）左下角最大值，边界全设为0
def bottom_right_max(matrix,rows,cols):
    bottom_right_max_matrix = [[0 for i in range(cols)] for j in range(rows)]
    for i in range(rows-2,0,-1):
        for j in range(cols-2,0,-1):
            if i==rows-2:
                bottom_right_max_matrix[i][j] = max(bottom_right_max_matrix[i][j+1],matrix[i+1][j+1])
            elif j==cols-2:
                bottom_right_max_matrix[i][j] = max(bottom_right_max_matrix[i+1][j],matrix[i+1][j+1])
            else:
                bottom_right_max_matrix[i][j] = max(bottom_right_max_matrix[i+1][j],bottom_right_max_matrix[i][j+1],matrix[i+1][j+1])
    return bottom_right_max_matrix

def max_matrix(matrix,rows,cols,x,y):
    top_left_maxn = top_left_max(matrix,rows,cols)[x][y]
    bottom_left_maxn = bottom_left_max(matrix,rows,cols)[x][y]
    top_right_maxn = top_right_max(matrix,rows,cols)[x][y]
    bottom_right_maxn = bottom_right_max(matrix,rows,cols)[x][y]
    return top_left_maxn*bottom_left_maxn*top_right_maxn*bottom_right_maxn

def print_matrix(matrix,rows,cols):
    for rows in matrix:
        print(*rows)




if __name__ == '__main__':

    rows, cols = map(int, input().split())

    # 使用列表推导式构建二维列表
    matrix = [list(map(int, input().split())) for i in range(rows)]
    fina_max=[[0 for i in range(cols)] for j in range(rows)]
    for i in range (rows):
        for j in range(cols):
            fina_max[i][j] = max_matrix(matrix,rows,cols,i,j)
    print_matrix(fina_max,rows,cols)





