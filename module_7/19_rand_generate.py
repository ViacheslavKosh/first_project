from random import randint

def rand_generator(start, end, quantity):
    count = 0
    while count < quantity:
        yield randint(start, end)
        count += 1

if __name__ == '__main__':
    for rn in rand_generator(1, 20, 5):
        print(rn, end=' ')
