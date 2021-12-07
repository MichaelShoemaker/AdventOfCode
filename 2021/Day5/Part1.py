import typing

def blank_grid(x, y):
    return [[0]*(x+1)] * (y+1)

def make_grid(start, end):
    pop_list = []
    for i in range(len(start)):
        if start[i][0] != end[i][0] or start[i][1] != end[i][1]:
            pop_list.append(i)

    xmin = min([x[0] for x in start]+[x[0] for x in end])
    xmax = max([x[0] for x in start]+[x[0] for x in end])

    ymin = min([y[1] for y in start]+[y[1] for y in end])
    ymax = max([y[1] for y in start]+[y[1] for y in end])
    print(xmax, ymax)
    grid = blank_grid(xmax, ymax)
    return start,end,grid

def draw_lines(start, end, grid):
    for i in range(0,len(end)):
        if start[i][0] == end[i][0]:
            mark1 = min(start[i][1], end[i][1])
            mark2 = max(start[i][1], end[i][1])
            while mark1 <= mark2:
                grid[start[i][0]][mark1] += 1
                mark1 +=1
        elif start[i][1] == end[i][1]:
            mark1 = min(start[i][0], end[i][0])
            mark2 = max(start[i][0], end[i][0])
            while mark1 <= mark2:
                grid[mark1][start[i][1]] += 1
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
    start, end, grid = make_grid(get_coordinates('test.txt')[0],get_coordinates('test.txt')[1])
    result = draw_lines(start, end, grid)
    for i in result:
        print(i)

