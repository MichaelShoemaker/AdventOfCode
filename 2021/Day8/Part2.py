# one = 
# two = 
# three = 
# four = 
# five =
# six = 
# seven = 
# eight = 
# nine = 

def parse_text(file):
    all_lines = []
    f = open(file).read().splitlines()
    for line in f:
        data = line.split('|')
        # print([x for x in data[0].split(' ')])
        all_lines.append(([set(x) for x in data[0].split(' ')],[set(x) for x in data[1].split(' ')]))
        
    for a in all_lines:
        for i in a[1]:
            if len(i) == 7:
                print(8,end="")
            elif len(i) == 4:
                print(4,end="")
            elif len(i) == 2:
                print(1, end = "")
            elif len(i) == 3:
                print(7,end ="")
            elif len(i) == 6:
                print(0,end ="")
            else:
                print(i,end="")
                
        print()



if __name__=='__main__':
    parse_text('test.txt')
    # x = 'hello'
    # print(set(x))
