from random import choice, randint

n = 100
m = 10000
q = 1000000

ops = ['RESET', 'DISABLE', 'GETMIN', 'GETMAX']

with open('input4.txt', 'w') as f:
    f.write(f'{n} {m} {q}\n')

    for _ in range(q):
        op = choice(ops)

        if op == 'RESET':
            f.write(f'{op} {randint(1, n)}\n')
        elif op == 'DISABLE':
            f.write(f'{op} {randint(1, n)} {randint(1, m)}\n')
        else:
            f.write(f'{op}\n')