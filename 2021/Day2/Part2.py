def make_moves(file):
    moves = []
    f = open(file).readlines()
    for line in f:
        line = line.replace('\n','')
        moves.append((line.split(' ')[0],int(line.split(' ')[1])))
    return moves


def move(data):
    x = 0
    y = 0
    aim = 0
    for m in data:
        if m[0]=='forward':
            x+=m[1]
            y+=(m[1]*aim)
        elif m[0]=='down':
            aim+=m[1]
        elif m[0]=='up':
            aim-=m[1]
        else:
            print("Invalid move {}".format(m))

        # print("X is {}, aim is {} depth is {}".format(x,aim,y))

    return x * y



if __name__=='__main__':
    print(move(make_moves('input.txt')))