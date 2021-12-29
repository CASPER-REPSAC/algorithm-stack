import sys
sys.stdin = open("algorithm-stack\\baekjoon\graph_traversal\\14502\input.txt")
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
print(a)