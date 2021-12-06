import numpy as np

f= open('test.txt')
raw = f.read().splitlines()
nums = set()
board = []
allboards = []

tracker = 0
for i in raw:

    # if len(i.strip())==0:
    #     pass
    if len(i)>14:
        for x in i.split(','):
            #print(x)
            nums.add(int(x))
    elif len(i.strip()) > 1 and tracker == 0:
        board.append([int(x.strip()) for x in i.split(' ') if len(x.strip())>0 ])

    else:
        tracker = 0
        allboards.append(board)
        board = []
        #x = np.vstack([x,np.array([int(x.strip()) for x in i.split(' ') if len(x.strip())>0 ])])


print(len(allboards))
