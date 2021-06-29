def main(n,nums):
    # Loop from 1 to n
    nums = sorted(nums)
    if nums[0] != 1:
        print(1)
        return
    for i in range(1,n-1):
        diff = int(nums[i]) - int(nums[i-1])
        if diff > 1:
            print(nums[i-1] + 1)
            return
            
    
    if nums[-1] != n:
        print(n)
        return


if __name__ == "__main__":
    inp = int(input())
    inpTwo = map(int, input().split())
    main(inp,inpTwo)