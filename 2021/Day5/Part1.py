import typing
#x1,y1 -> x2,y2
def blank_grid(x, y):
    a = []
    for i in range(y+1):
        a.append([0]*(x+1))
    return a

def make_grid(start, end):
    xmax = max([x[0] for x in start]+[x[0] for x in end])
    ymax = max([y[1] for y in start]+[y[1] for y in end])
    grid = blank_grid(xmax, ymax)
    return start,end,grid

def draw_lines(start, end, grid):
    for i in range(0,len(end)):
        #Xs match
        if start[i][0] == end[i][0]:
            #Get min and max y
            mark1 = min(start[i][1], end[i][1])
            mark2 = max(start[i][1], end[i][1])
            while mark1 < mark2:
                grid[start[i][0]][mark1] += 1
                mark1 +=1
        #Ys match        
        elif start[i][1] == end[i][1]:
            #Get the min and max x
            mark1 = min(start[i][0], end[i][0])
            mark2 = max(start[i][0], end[i][0])
            while mark1 < mark2:
                grid[start[i][1]][mark1] += 1
                mark1 +=1   
    return grid
        

#Create two lists of tuples for the coordinates
def get_coordinates(file):
    f = open(file).read().splitlines()
    start = []
    finish = []
    for item in f:
        s = item.split('->')
        start.append((int(s[0].split(',')[0]),int(s[0].split(',')[1])))
        finish.append((int(s[1].split(',')[0]),int(s[1].split(',')[1])))
    return start, finish


if __name__=='__main__':
    start, end, grid = make_grid(get_coordinates('input.txt')[0],get_coordinates('input.txt')[1])
    result = draw_lines(start, end, grid)
    count = 0
    for i in result:
        for r in i:
            if r >= 2:
                count += 1
    print(count)



