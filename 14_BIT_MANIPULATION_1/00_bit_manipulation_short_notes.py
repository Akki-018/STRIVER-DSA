''' 
1. Binary Representation
Every integer is stored in binary.
Rightmost bit = Least Significant Bit (LSB)
Leftmost bit = Most Significant Bit (MSB)

Example:

13 = 1101
2. Bitwise Operators
Operator	Meaning
&	AND
`	`
^	XOR
~	NOT
<<	Left Shift
>>	Right Shift
3. Left Shift
n << i

Means

n × (2^i)

Example

5 << 2

101

↓

10100

=20
4. Right Shift
n >> i

Means

n // (2^i)

(for positive integers)

Example

20 >> 2 = 5
5. Check i-th Bit
if n & (1 << i):

Bit is set.

Else,

Bit is unset.

6. Set i-th Bit
n |= (1 << i)
7. Unset i-th Bit
n &= ~(1 << i)
8. Toggle i-th Bit
n ^= (1 << i)
9. Odd / Even
if n & 1:
    Odd
else:
    Even
10. XOR Properties ⭐
a ^ a = 0

a ^ 0 = a

a ^ b = b ^ a

(a ^ b) ^ c = a ^ (b ^ c)
11. Recover Unknown

If

a ^ x = b

Then

x = a ^ b
12. Count Set Bits (Method 1)
count = 0

while n:

    count += n & 1

    n >>= 1

Time

O(number of bits)
13. Brian Kernighan Algorithm ⭐
count = 0

while n:

    count += 1

    n &= (n - 1)

Removes the rightmost set bit.

Time

O(number of set bits)
14. Power of Two
n > 0 and (n & (n-1)) == 0

Reason:

Power of 2 has exactly one set bit.

15. Rightmost Set Bit
x & (-x)

Returns only the rightmost set bit.

(We'll derive this later using Two's Complement.)

16. Swap Two Numbers
a ^= b

b ^= a

a ^= b
17. Divide Two Integers

Idea

Use Left Shift
Find largest power of 2 multiple
Subtract it
Add (1<<shift) to answer

Time

Better : O((logN)^2)

Optimal : O(logN)
18. Minimum Bit Flips
xor = start ^ goal

Answer = Count Set Bits(xor)
19. Single Number

Every element appears twice.

ans = 0

for num in nums:
    ans ^= num

Reason

x ^ x = 0
20. Single Number II

Every element appears 3 times

Idea

Count set bits for every bit position
Take %3
Reconstruct answer

Time

O(32*N)
21. Single Number III

Two unique numbers.

Algorithm

XOR all numbers
Find rightmost set bit
Divide into two groups
XOR both groups
22. Power Set

Total subsets

2^n

Loop

for mask in range(1<<n):

Check

if mask & (1<<i):

Include

nums[i]

Time

O(n*2^n)
23. Prefix XOR
pref[i]

=

arr[0]^...^arr[i]

Recover

arr[0] = pref[0]

arr[i] = pref[i] ^ pref[i-1]
24. Sieve of Eratosthenes
isPrime = [True]*n

For every prime

Mark multiples

for j in range(i*i,n,i):

Start from

i*i

because smaller multiples are already marked.

Outer loop

for i in range(2,int(sqrt(n))+1):

Time

O(n log log n)
⭐ Most Important Formulae
Check Bit
n & (1<<i)

Set Bit
n | (1<<i)

Unset Bit
n & ~(1<<i)

Toggle Bit
n ^ (1<<i)

Odd Even
n & 1

Count Set Bits
n &= (n-1)

Power of Two
(n&(n-1))==0

Rightmost Set Bit
n & (-n)

Recover XOR
a^x=b
x=a^b

Power Set
for mask in range(1<<n)

Left Shift
n<<i = n*(2^i)

Right Shift
n>>i = n//(2^i)
'''