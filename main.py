import random

n = 8

def make_board():
    board = []
    for i in range(n):
        board.append(random.randint(0, n-1))
    return board

def get_score(board):
    score = 0
    for i in range(n):
        for j in range(i+1, n):
            if board[i] != board[j] and abs(board[i] - board[j]) != abs(i - j):
                score += 1
    return score

def mix(p1, p2):
    cut = random.randint(0, n-1)
    child = p1[:cut] + p2[cut:]
    return child

def change(board):
    new = board[:]
    pos = random.randint(0, n-1)
    new[pos] = random.randint(0, n-1)
    return new

def sort_by_score(boards):
    for i in range(len(boards)):
        for j in range(i + 1, len(boards)):
            if get_score(boards[j]) > get_score(boards[i]):
                temp = boards[i]
                boards[i] = boards[j]
                boards[j] = temp
    return boards

def solve():
    players = []
    for i in range(100):
        players.append(make_board())

    for gen in range(1000):
        players = sort_by_score(players)
        best = players[0]
        if get_score(best) == 28:
            print("Gen:", gen)
            print("Found:", best)
            return
        next_gen = []
        for i in range(20):
            next_gen.append(players[i])
        while len(next_gen) < 100:
            dad = random.choice(players[:50])
            mom = random.choice(players[:50])
            baby = mix(dad, mom)
            if random.random() < 0.3:
                baby = change(baby)
            next_gen.append(baby)
        players = next_gen

    print("Kichu mile nai")

solve()
