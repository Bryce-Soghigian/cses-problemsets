
# Programming Techniques

This is going to be a light overview of some useful Techniques you can use when working through cp problems.




## 2.1.2 Working With Numbers

Integers! The most used integer type in CP is int, which is a 32 bit type with a value range of -2^31 ... 2^31-1.

Usuallly contest problems are set so bigints or longs are enough.


### Modular Arithmetic

SOmetimes the answer to a problem is a very large number but it is enough to output it "mod" ie the remainder when the answer is divided by M. Where m == mod 10^9  + 7. The idea is that even if the answer is very larget it suffices to use the types of int and long. We note by x mod m the remainder when x is divided by m. For example 17 % 5 = 2 because 17 = 3*5 + 2. an important property of remainders is that the following formulas hold. 

- (a+b) % m = (a % m  + b % m) % M
- (a-b) % m = (a % m - b % m) % M
- (a · b) % m = (a % m · b % m) % m


This we can take the remainder after every operation and the numbers will never become too large.

for example the following code calculates n!, the factorial of n, mod m 

```python
x = 1
for i in range(1,n):
    x = (x*i) %M
return x
```
Usually we want to remainder to always be between 0,,, m-1. However the remainder of a negative number is either zero or negative. An easy way to make sure thare are no negative remainders is to first caclulate the remainder as usual and add m if the result is negative
```python
x = x %m
if x < 0:
    x += m 
```


## 2.2 Recursive Algorithms
 Recursion often provides an elegant way to implement an algorithm. In this section, we discuss recursive algorithms that systematically go through candiate solutions to a problem . First we fucus on generating subsets && permutations && then discuss the more general backgracking Technique.

 ## 2.2.1 Generating subsets
 Our first application of recursion is generating all subsets of a set of n elements. 

 Given [1,2,3]
 return [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]

 The folling recursive function search can be used to generate the subsets. 

 ```python
 subset = []
 def search(k):
     if k == n + 1:
         # Process subset
     else:
         subset.append(k)
         search(k + 1)
         subset.pop()
         search(k + 1)
```

Thats the general idea. An actual implementation of the algorithm can be seen below
```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first = 0, curr = []):
            # if the combination is done
            if len(curr) == k:  
                output.append(curr[:])
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()
        
        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return output```