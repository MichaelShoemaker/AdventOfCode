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
    for m in data:
        if m[0]=='forward':
            x+=m[1]
        elif m[0]=='down':
            y+=m[1]
        elif m[0]=='up':
            y-=m[1]
        else:
            print("Invalid move {}".format(m))

    return x * y



if __name__=='__main__':
    print(move(make_moves('input.txt')))