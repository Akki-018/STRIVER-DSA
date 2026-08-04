### BITWISE OPERATORS - Bitwise operators work bit by bit on binary representation of numbers 
## AND - (&)
'''This operator return 1 only both the bits are 1, else 0 
ex - 5&3 -> 5 = 101 , 3 - 011
now after comparing each bits - we get 001 i.e. 1 
therefore 5&3 = 1
'''
print(5&9)
print(14&11) 

''' 
Important properties 
1-  x&x == x 
2-  x&0 == 0 
3-  x&1 -- Checks the LSB of the bit - last bit 1 - odd , last bit 0 - even

'''
''' 
USES - 
1. Check if a number is odd or even 
2. Check if the ith - bit is set 
3. Bit masking 

'''
## OR(|) 
'''
only returns 1 if atleast one bit is 1 - otherwise 0 
ex - 5|3 -> 5=101,3=011 , taking or of it gives - 111 i.e. 7 
ex - 12|10 -> 12=1100,10 = 1010 , taking or of it gives - 1110 ie.e 14 

'''
print(5|3)
print(12|10)

''' 
Important Properties:
1- x|x = x 
2- x|0 = x 
3- x|1 => only gurantees that the lsb becomes 1 , it doesn't simply add 1

'''
''' 
USES: 
1- Set bits 
2- Bit masking 

'''
## XOR(^) 
''' 
The XOR(exclusive OR) returns - 1 ( if both bits are diff) , 0 - (if both bits are same)
Same - 0 
diff - 1 

ex - 5^3 -> 5 = 101 , 3 = 011 -> 6 
ex - 12^10 -> 12 = 1100, 10 = 1010 -> 6 

'''
print(5^3)
print(12^10)

'''
Imp prop:
1- x^0 = x 
2- x^x = 0
3- x^y^x = y  

USES:
1- So many problems
2- Toggle bits 
'''

## BITWISE NOT(~)
''' 
It works only on one operand, the not operator inverts every bit
ex - 0->1,1->0 

impnote - ~5 == -6 .. but why ? 
because computers dont store negatie numbers with a minus sign - they use a representation called two complement 
the identity is -> ~n = -(n+1)
'''
print(~5)
''' 
Uses: 
1- Create masks
2- Clear bits 
3- Bit manipulation tricks

'''
### SHIFT OPERATORS 
## LEFT SHIFT(<<)
''' 
n<<i - tells that shift the binary number of n to the left by i positions 
ex - 5<<1 -> 5=101 shift 5 to left by 1 position - i.e. we have 1010 i.e 10 
therefore 5<<1 = 10 

ex - 5<<2 -> 10100 i.. 20
'''
print(5<<1)
print(5<<2)

''' 
imp point - Every shift doubles the number

'''
'''
1<<i
creates a binary number where only the ith - bit is set to 1
'''

## Right Shift(n>>i)
'''
This is the opp of left shift i.e.
every bit shifts to the right by i positions - the bits that falls off on the right are discarded
ex - 5>>1
101 - 10 ==2  ... 5>>1 == 2 

ex - 20>>2 - 11100 shifts to right 2 times give - 111 i.e 7

'''
print(5>>1)
print(20>>2)    
print(15>>3)

''' 
Right shift divides the number by 2 

for non -negative numbers - formula => n>>i = floor(n/2*i)

'''


