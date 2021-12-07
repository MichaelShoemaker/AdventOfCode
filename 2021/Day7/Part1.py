import statistics

def calc(file):
    f = open(file).read().splitlines()
    l = [int(x) for x in f[0].split(',')]
    meetup = (int(statistics.mean(l)))
    cost = 0
    for i in l:
        cost += abs(i-meetup)
    return meetup

if __name__=='__main__':
    print(calc('test.txt'))