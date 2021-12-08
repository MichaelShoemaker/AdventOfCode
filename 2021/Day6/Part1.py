def make_data(file):
    return [int(x) for x in open(file).read().split(',')]

#List to hold fish
school = []

class JellyFish:
    def __init__(self, age):
        self.age = age

    def spawn():
        return JellyFish(8)

    def move(self):
        if self.age - 1 == 0:
            self.age = 6
            self.spawn()
        else:
            self.age -= 1


if __name__=='__main__':
    print(make_data('test.txt'))


#Need to make a jellyfish for each item in number in the list saving that number as their age
#As days move the age decreases by 1
#If age reaches 0 they spawn a new jellyfish with an age of 8 and their age is set to 6
