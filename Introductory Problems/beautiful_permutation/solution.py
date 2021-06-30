from collections import deque
import math
def list_to_output(l):
    print(*l, sep=' ')

def main(n):
    output = deque()
    current = [k for k in range(1, n)]
    output.append(n)
    right = math.floor(n//2)
    left = right - 1
    while left != 0 or right != n-1:
        if left == -1:
            return list(output)

        if current[left] % 2 == 0:
            output.append(current[right])
            output.appendleft(current[left])
        else:
            output.append(current[left])
            output.appendleft(current[right])

        right += 1
        left -= 1
    if n % 2 == 0:
        output.append(1)
    return list(output)


if __name__ == "__main__":
    inp = int(input())
    if inp == 1:
        print(1)
    elif inp <= 3:
        print("NO SOLUTION")
    elif inp == 4:
        list_to_output([2, 4, 1, 3])
    else:
        list_to_output(main(inp))