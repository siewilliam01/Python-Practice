import time

fib_seq = [0, 1]

def main():
    fib_next = fib_seq[-1] + fib_seq[-2]
    fib_seq.append(fib_next)
    time.sleep(.1)

while True:
    for i in range(10):
        print(fib_seq[-1])
        main()
    time.sleep(1)