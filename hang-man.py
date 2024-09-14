import wonderwords
from wonderwords import RandomWord

r = RandomWord()
c = c1 = 0

# generate a random word
a = r.word()
b = list(a)
d = len(b)
e = ['_'] * d
print(' '.join(e))

while c < 6:
    f = input('Enter a letter: ')
    if f in b:
        for i in range(d):
            if f == b[i]:
                e[i] = f
        print(' '.join(e))
        if e == b:
            print('You won!')
            break
    else:
        c += 1
        print(' '.join(e))
        print(f'You have {6 - c} chances left')
        if c == 6:
            print(f'You lost! The word was {a}')
            break


