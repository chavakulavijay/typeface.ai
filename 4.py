def nn(matrix):
    to12 = 256
    le123 = 256

    rig = 0
    bot = 0

    len_row = len(matrix)
    len_col = len(matrix[0])

    for i in range(0,len_row):
        sta12 = 0
        while(sta12 < len_col):
            if (matrix[i][sta12] == 0):
                le123 = min(le123,sta12)
                break
            sta12+=1
        
        end = len_col - 1
        while(end >=0 ):
            if(matrix[i][end] == 0):
                rig = max(end,rig)
                break
            end -= 1

        top_start = 0
        while(top_start < len_row):
            if (matrix[top_start][i] == 0):
                to12 = min(to12,top_start)
                break
            top_start+=1

        bottom_end = len_row - 1
        while(bottom_end >= 0):
            if (matrix[bottom_end][i] == 0):
                bot = max(bot,bottom_end)
                break
            bottom_end-=1
    return (to12,le123),(to12,rig),(bot,le123),(bot,rig)

matrix = []
for i in range(4):
    row = list(map(int,input().split()))
    matrix.append(row)
print(nn(matrix))