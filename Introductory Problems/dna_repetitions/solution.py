def main(sequence):
    k = 1
    length = len(sequence)
    if len(sequence) == 1:
        print(1)
        return
    
    hashmap = {}
    maximum = 0
    left = 0
    for right in range(length):
        if sequence[right] in hashmap:
            hashmap[sequence[right]] +=1
        else:
            hashmap[sequence[right]] = 1
        
        while len(hashmap.values()) > k:
            if sequence[left] in hashmap:
                hashmap[sequence[left]] -= 1
                if hashmap[sequence[left]] == 0:
                    del hashmap[sequence[left]]

                left += 1
        maximum = max(maximum, right-left + 1)
    
    print(maximum)




if __name__ == "__main__":
    inp = str(input())
    main(inp)