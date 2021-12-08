def make_data(file):
    return [int(x) for x in open(file).read().split(',')]

#List to hold fish
school = []
babies = []

class JellyFish:
    def __init__(self, age):
        self.age = age


    def move(self):
        if self.age - 1 < 0:
            self.age = 6
        else:
            self.age -= 1


if __name__=='__main__':
    days = 4
    for x in make_data('test.txt'):
        school.append(JellyFish(x))

    for i in range(days):
        print()
        #print("Day {} there are {} fish".format(i, len(school)))
        for j in school:
            print(j.age, end ="")
            if j.age == 0:
                babies.append(JellyFish(8))
                j.move()
            else:
                j.move()
        school = school + babies

    print(len(school))
            


#Need to make a jellyfish for each item in number in the list saving that number as their age
#As days move the age decreases by 1
#If age reaches 0 they spawn a new jellyfish with an age of 8 and their age is set to 6
