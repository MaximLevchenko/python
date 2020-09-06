


def main():
    fib_seq=[0,1]
    while True:
        fib=fib_seq[-1]+fib_seq[-2]
        fib_seq.append(fib)
        if fib>4000000:
            break

    print(fib_seq)
main()

