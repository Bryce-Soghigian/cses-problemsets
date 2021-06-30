def main(n):
    total = 0
    k = 5
    while(n /k >= 1):
        total += int(n/k)
        k *= 5
    print(int(total))
        
if __name__ == "__main__":
    inp = int(input())
    main(inp)