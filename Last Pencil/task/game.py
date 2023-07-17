user_input = input("How many pencils would you like to use:\n")
turn = input("Who will be the first (John, Jack):\n")
print("|" * int(user_input))
players = ["Jack", "John"]

count = 1 * int(user_input)
x = int(input(f'{turn} is going first!\n'))
count -= x
while count > 0:

    if turn == players[0]:
        print(count * "|")
        a = int(input(f'{players[1]}s turn:\n'))
        count -= a
        print(count * "|")
        b = int(input(f'{players[0]}s turn:\n'))
        count -= b
    else:
        print(count * "|")
        c = int(input(f'{players[0]}s turn:\n'))
        count -= c
        print(count * "|")
        d = int(input(f'{players[1]}s turn:\n'))
        count -= d
