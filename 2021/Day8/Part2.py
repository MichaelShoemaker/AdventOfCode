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
        ciph = {}
        for i in a[1]:
            if len(i) == 2:
                ciph[1] = i
                #print(1, end = "")
            elif len(i) == 4:
                ciph[4] = i
                #print(4,end="") 
        for i in a[1]:
            if len(i) == 5:
                if len(i.intersection(ciph[4])) == 3: 
                    ciph[5] = i 
                elif len(i.intersection(ciph[4])) == 2:
                else:
                    ciph[2] = i
        print(ciph)
            # elif len(i) == 7:
            #     ciph[8] = i
            #     print(8,end="")

            
            # elif len(i) == 3:
            #     print(7,end ="")
            # elif len(i) == 6:
            #     print(0,end ="")
            # else:
            #     print(i,end="")

        print()



if __name__=='__main__':
    parse_text('test.txt')
    # x = 'hello'
    # print(set(x))
