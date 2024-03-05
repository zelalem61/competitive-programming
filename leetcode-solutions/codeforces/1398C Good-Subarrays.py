import sys

def mod(x):
    M = 10**9 + 7
    return ((x%M + M)%M)

def add(a, b):
    return mod(mod(a) + mod(b))

def solve():
    n = int(input())
    s = input()
    mp = {}
    total = 0
    mp[0] = 1
    sum_val = 0
    for i in range(n):
        x = int(s[i]) - 1
        sum_val += x
        total += mp.get(sum_val, 0)
        mp[sum_val] = mp.get(sum_val, 0) + 1
    print(total)

def main():
    # sys.stdin = open('timber_input.txt', 'r')
    # sys.stdout = open('timber_output.txt', 'w')
    t = int(input())
    for i in range(t):
        solve()

if __name__ == "__main__":
    main()
