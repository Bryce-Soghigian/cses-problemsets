def list_to_output(l):
    print(*l, sep=' ')

def main(n):
    output = []

    while n != 1:
        output.append(n)
        if n % 2== 0:
            n //= 2
        else:
            n = (n * 3) + 1 

    output.append(1)
    return output

if __name__ == "__main__":
    inp = int(input())
    list_to_output(main(inp))