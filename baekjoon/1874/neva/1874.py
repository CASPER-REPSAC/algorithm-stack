from sys import stdin
from sys import exit

sequence = list()
for _ in range(int(stdin.readline())):
    sequence.append(int(stdin.readline()))

seq_cnt = 1
delay_stack = [1]
instructions = ['+']

for seq_value in sequence:
    if seq_cnt < seq_value:
        for i in range(seq_cnt + 1, seq_value + 1):
            delay_stack.append(i)
            instructions.append('+')
        seq_cnt = seq_value

    if seq_value <= seq_cnt and delay_stack \
            and delay_stack[-1] == seq_value:
        delay_stack.pop()
        instructions.append('-')
    else:
        print("NO")
        exit(0)

print('\n'.join(instructions))
