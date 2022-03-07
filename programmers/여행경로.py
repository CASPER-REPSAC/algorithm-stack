"""
from collections import defaultdict

def dfs(tickets, v, answer, cnt, p):
    answer.append(v)
    if cnt == 0:
        return
    elif cnt != 0 and not tickets[v]:
        tickets[p].append(v)
        answer.pop()
        return
    else:
        for i in tickets[v]:
            tmp = tickets[v].pop(0)
            dfs(tickets, tmp, answer, cnt - 1, v)

def solution(tickets):
    answer = []
    cnt = len(tickets)
    tickets_dict = defaultdict(list)
    for ticket in sorted(tickets, key=lambda x:(x[1])):
        tickets_dict[ticket[0]].append(ticket[1])
    
    dfs(tickets_dict, "ICN", answer, cnt, "ICN")
    return answer
"""

from collections import defaultdict

def solution(tickets):
    answer = []

    tickets_dict = defaultdict(list)
    for ticket in sorted(tickets, key=lambda x:(x[1]), reverse=True):
        tickets_dict[ticket[0]].append(ticket[1])
    
    stack = ['ICN']
    while stack:
        tmp = stack[-1]

        if not tickets_dict[tmp]:
            answer.append(stack.pop())
        else:
            stack.append(tickets_dict[tmp].pop())
    answer.reverse()
    return answer

tickets = [["ICN", "A"], ["A", "C"], ["A", "B"], ["B", "D"], ["C", "A"]]
solution(tickets)