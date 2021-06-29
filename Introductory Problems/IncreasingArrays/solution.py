def main(n,nums):
    total = 0
    nums = list(nums)
    for i in range(1, n):
        if nums[i] < nums[i-1]:
            total += abs(nums[i]-nums[i-1])
            nums[i] += abs(nums[i]-nums[i-1])
            
        
    print(total)


if __name__ == "__main__":
    inp = int(input())
    inpTwo = map(int, input().split())
    main(inp,inpTwo)