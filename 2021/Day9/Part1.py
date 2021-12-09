def make_data(file):
    f = open(file).read().splitlines()
    data = []
    for i in f:
        data.append([int(x) for x in i])
    return data

def find_lows(data):
    risk = 0
    for r, row in enumerate(data):
        for c, col in enumerate(row):
            # print("Checking row {} val {}".format(r, col))
            #Top Left Corner
            if r == 0 and c == 0:
                #print("cond1")
                if data[r][c+1] > col and data[r+1][c] > col:
                    risk += (1+int(col))
                    print("LowVal {} at position {},{}".format(col, r, c))
            #Lower Left Corner
            elif r == len(data) and c == 0:
                #print("cond2")
                if data[r-1][c] > col and data[r][c+1] > col:
                    risk += (1+int(col))
                    print("LowVal {} at position {},{}".format(col, r, c))
            #Upper Right Corner
            elif r == 0 and c ==len(data[0])-1:
                # print("r {}, c {}, len(row[0]) {}".format(r,c,row[0]))
                # print("cond3")
                if data[r][c-1] > col and data[r+1][c] > col:
                    risk += (1+int(col))
                    print("LowVal {} at position {},{}".format(col, r, c))
            #Lower Right Corner
            elif r == len(data) and c == len(data[0])-1:
                # print("cond4")
                if data[r][c-1] > col and data[r-1][c] > col:
                    risk += (1+int(col))
                    print("LowVal {} at position {},{}".format(col, r, c))
            #Left Side
            elif c == 0:
                # print("cond5")
                if data[r-1][c] > col and data[r][c+1] > col and data[r+1][c] > col:
                    risk += (1+int(col))
                    print("LowVal {} at position {},{}".format(col, r, c))
            #Top side
            elif r == 0:
                #print("cond6")
                #print("r {}, c {}, len(row[0]) {}".format(r,c,len(data[0])))
                #print("cond6 {} {} {} col is {}".format(data[r][c-1],data[r+1][c],data[r][c+1], col))
                if data[r][c-1] > col and data[r+1][c] > col and data[r][c+1] > col:
                    print("LowVal {} at position {},{}".format(col, r, c))
                    risk += (1+int(col))
            #Right Side
            elif c == len(row)-1:
                #print("cond7")
                if data[r-1][c] > col and data[r][c-1] > col and data[r+1][c] > col:
                    risk += (1+int(col))
                    print("LowVal {} at position {},{}".format(col, r, c))
            #Bottom Side
            elif r == len(data)-1:
                #print("cond8")
                if data[r][c-1] > col and data[r-1][c] > col and data[r][c+1] > col:
                    risk += (1+int(col))
                    print("LowVal {} at position {},{}".format(col, r, c))
            else:
                try:
                    if data[r][c-1] > col and data[r-1][c] > col and data[r][c+1] > col and data[r+1][c] > col:
                        risk += (1+int(col))
                        print("LowVal {} at position {},{}".format(col, r, c))
                except Exception as e:
                    print(str(e))
                    print(row, col,r,c)
    return risk

if __name__=='__main__':
    print(find_lows(make_data('input.txt')))
    
    # for r, row in enumerate(data):
    #     for c, col in enumerate(row):
    #         print(row)
