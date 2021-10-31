import sys


if __name__ == "__main__":
    k = int(sys.stdin.readline())

    num_list = list(map(int, sys.stdin.readline().split()))
    num_list_len = len(num_list)


    for i in range(k-1, -1 ,-1):
        for j in range(2**i, num_list_len+1, 2**(i+1)):
            print(num_list[j-1], end=' ')
        print()
    
    # 2 ** (k-1)
    # 2 ** (k-2), 2 ** (k-2) + 2 ** (k-1)
    # 2 ** (k-3), 2 ** (k-3) + 2 ** (k-2), 2 ** (k-3) + 2 ** (k-2) + 2 ** (k-1)

