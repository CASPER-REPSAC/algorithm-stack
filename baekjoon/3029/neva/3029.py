from sys import stdin

now_h, now_m, now_s = map(int, stdin.readline().strip().split(':'))
throw_h, throw_m, throw_s = map(int, stdin.readline().strip().split(':'))

now_time = now_h * 3600 + now_m * 60 + now_s
throw_time = throw_h * 3600 + throw_m * 60 + throw_s
wait_time = throw_time - now_time

if wait_time < 0:
  wait_time += 86400
elif wait_time == 0:
  wait_time = 86400

wait_h = wait_time // 3600
wait_time -= wait_h * 3600
wait_m = wait_time // 60
wait_time -= wait_m * 60
wait_s = wait_time

print("%02d:%02d:%02d" % (wait_h, wait_m, wait_s))
