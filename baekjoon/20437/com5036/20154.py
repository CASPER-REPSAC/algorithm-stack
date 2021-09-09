"""
1. 알파벳 소문자로 이루어진 문자열 W가 주어진다.
2. 양의 정수 K가 주어진다.
3. 어떤 문자를 정확히 K개를 포함하는 가장 짧은 연속 문자열의 길이를 구한다.
4. 어떤 문자를 정확히 K개를 포함하고, 문자열의 첫 번째와 마지막 글자가 해당 문자로 같은 가장 긴 연속 문자열의 길이를 구한다.
"""

T = int(input())
for t in range(T):
    W = input()
    K = int(input())

    """ key : 문자, value: index list"""
    W_idx = {}
    i = 0
    for ch in W:
        if not (ch in W_idx):
            W_idx[ch] = [i]
        else:
            W_idx[ch].append(i)
        i += 1

    for ch in W:
        if ch in W_idx:
            if len(W_idx[ch]) < K:
                del W_idx[ch]

    # print(W_idx)

    if not W_idx:
        print(-1)
        continue

    """ 3. 어떤 문자를 정확히 K개를 포함하는 가장 짧은 연속 문자열의 길이를 구한다."""
    len_list = []
    for key, val in W_idx.items():
        for i in range(len(val) - (K - 1)):
            len_list.append((W_idx[key][i + K - 1] - W_idx[key][i] + 1))

    print(f"{min(len_list)} {max(len_list)}")
