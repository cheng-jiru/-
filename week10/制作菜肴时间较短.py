#以i,j为右下角的矩阵的大小为（i-1，j-1）最大值，边界全设为0

def max_matrix(matrix,rows,cols):

    top_lest_max_matrix = [[0 for i in range(cols)] for j in range(rows)]
    for i in range(1,rows-1):
        for j in range(1,cols-1):
            if i==1:
                top_lest_max_matrix[i][j] = max(top_lest_max_matrix[i][j-1],matrix[i-1][j-1])
            elif j==1:
                top_lest_max_matrix[i][j] = max(top_lest_max_matrix[i-1][j],matrix[i-1][j-1])
            else:
                top_lest_max_matrix[i][j] = max(top_lest_max_matrix[i-1][j],top_lest_max_matrix[i][j-1],matrix[i-1][j-1])

    bottom_left_max_matrix = [[0 for i in range(cols)] for j in range(rows)]
    for i in range(rows-2,0,-1):
        for j in range(1,cols-1):
            if i==rows-2:
                bottom_left_max_matrix[i][j] = max(bottom_left_max_matrix[i][j-1],matrix[i+1][j-1])
            elif j==1:
                bottom_left_max_matrix[i][j] = max(bottom_left_max_matrix[i+1][j],matrix[i+1][j-1])
            else:
                bottom_left_max_matrix[i][j] = max(bottom_left_max_matrix[i+1][j],bottom_left_max_matrix[i][j-1],matrix[i+1][j-1])

    top_right_max_matrix = [[0 for i in range(cols)] for j in range(rows)]
    for i in range(1,rows-1):
        for j in range(cols-2,0,-1):
            if i==1:
                top_right_max_matrix[i][j] = max(top_right_max_matrix[i][j+1],matrix[i-1][j+1])
            elif j==cols-2:
                top_right_max_matrix[i][j] = max(top_right_max_matrix[i-1][j],matrix[i-1][j+1])
            else:
                top_right_max_matrix[i][j] = max(top_right_max_matrix[i-1][j],top_right_max_matrix[i][j+1],matrix[i-1][j+1])

    bottom_right_max_matrix = [[0 for i in range(cols)] for j in range(rows)]
    for i in range(rows-2,0,-1):
        for j in range(cols-2,0,-1):
            if i==rows-2:
                bottom_right_max_matrix[i][j] = max(bottom_right_max_matrix[i][j+1],matrix[i+1][j+1])
            elif j==cols-2:
                bottom_right_max_matrix[i][j] = max(bottom_right_max_matrix[i+1][j],matrix[i+1][j+1])
            else:
                bottom_right_max_matrix[i][j] = max(bottom_right_max_matrix[i+1][j],bottom_right_max_matrix[i][j+1],matrix[i+1][j+1])
    final_matrix = [top_lest_max_matrix[i][j]*bottom_left_max_matrix[i][j]*top_right_max_matrix[i][j]*bottom_right_max_matrix[i][j] for i in range(rows)for j in range(cols)]




    return final_matrix

def print_list(lst, cols):
    for i in range(0, len(lst), cols):
        print(*lst[i:i+cols])




if __name__ == '__main__':

    rows, cols = map(int, input().split())

    # 使用列表推导式构建二维列表
    matrix = [list(map(int, input().split())) for i in range(rows)]
    final_matrix = max_matrix(matrix,rows,cols)
    print_list(final_matrix, cols)







