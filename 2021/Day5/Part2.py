def blank_grid(x, y):
    a = []
    for i in range(x+1):
        a.append([0]*(y+1))
    return a

def make_grid(start, end):
    xmax = max([x[0] for x in start]+[x[0] for x in end])
    ymax = max([y[1] for y in start]+[y[1] for y in end])
    grid = blank_grid(xmax, ymax)
    return grid

def plot(coords, grid):
    for i in range(len(coords)):
        grid[coords[i][0]][coords[i][1]] +=1
    return grid

#Starter Code Source: https://stackoverflow.com/questions/57891415/how-to-find-all-coordinates-efficiently-between-two-geo-points-locations-with-ce
def make_coords(start, end):
    # your geo points
    all_steps = []
    
    
    STEP = 1
    for i in range(len(start)):
        x1, y1 = start[i][0], start[i][1]
        x2, y2 = end[i][0], end[i][1]

        if x1 > x2:           
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        if x1 == x2:
            if y1 > y2:
                while y2 <= y1:
                    all_steps.append((x1,y2))
                    y2 += 1
            elif y1 <= y2:
                while y1 <= y2:
                    all_steps.append((x1, y1))
                    y1 += 1
        else:
            for i in range(int((x2-x1)/STEP) + 1):
                x = x1 + i*STEP
                y = (y1-y2)/(x1-x2) * (x - x1) + y1
                all_steps.append((x,int(y)))
    return all_steps
        

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
    s, f = get_coordinates('input.txt')
    blankgrid = make_grid(s,f)
    coords = make_coords(s,f)
    grid = plot(coords, blankgrid)
    count = 0
    for i in grid:
        for s in i:
            if s >= 2:
                count+=1
    print(count)

    