def parse_text(file):
    f = open(file).readlines()
    parts = []
    for i in f:
        parts.append(i.split('|')[1].replace('\n','').split(' '))

    count = 0
    for p in parts:
        for j in p:
            if len(j) in [2,3,4,7]:
                count += 1
    print(count)



if __name__ == '__main__':
    parse_text('input.txt')