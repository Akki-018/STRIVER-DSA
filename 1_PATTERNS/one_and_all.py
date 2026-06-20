# Pattern 1                                          # ****
for i in range(5):        # rows                     # ****
    for j in range(4):              #columns         # ****
        print("*",end = " ")                         # ****
    print()                                          # ****



#PATTERN 2                                           # *
for i in range(6):                                   # **
    for j in range(i):                               # ***
        print("*" , end = " ")                       # ****
    print()                                          # *****

#PATTERN 3                                           # 1
for i in range(6):                                   # 12
    for j in range(1,i+1):                           # 123
        print(j ,end=" ")                            # 1234
    print()                                          # 12345


#PATTERN 4                                           # 1
for i in range(1,6):                                 # 22
    for j in range(i):                               # 333
        print(i, end = " ")                          # 4444
    print()                                          # 55555


# PATTERN 5                                          # *****
for i in range(1,6):                                 # ****
    for j in range(6-i):                             # ***
        print("*" , end = " ")                       # **
    print()                                          # * 


# PATTERN 6                                          # 12345
for i in range(1,6):                                 # 1234
    for j in range(1,7-i):                           # 123
        print(j , end = " ")                         # 12
    print()                                          # 1

# PATTERN 7                                          #     *
for i in range(1,6):                                 #    ***
    for j in range(5-i):                             #   *****
         print(" ", end= " ")                        #  *******
    for k in range(2*i-1):                           # *********
        print("*",end = " ")
    print()

# PATTERN 8                                          # *********
for i in range(1,6):                                 #  *******
    for j in range(i-1):                             #   *****
        print(" ", end = " ")                        #    ***
    for k in range(2*(5-i)-1):                       #     *
        print("*",end=" ")
    print()

# PATTERN 9
for i in range(1,6):                                    #     *
    for j in range(5-i):                                #    ***
        print(" ",end=" ")                              #   *****
    for k in range(2*i-1):                              #  *******                         
        print("*", end = " ")                           # *********
    print()                                             # *********
for l in range(1,6):                                    #  ******* 
    for m in range(1,l):                                #   *****
        print(" ", end = " ")                           #    ***
    for n in range(2*(6-l)-1):                          #     *
        print("*", end = " ")
    print()


# PATTERN 10                                            # *
for i in range(1,6):                                    # **
    for j in range(i):                                  # ***
        print("*", end = " ")                           # ****
    print()                                             # *****
for k in range(1,5):                                    # ****
    for l in range(5-k):                                # ***
        print("*",end = " ")                            # **
    print()                                             # *


# PATTERN 11                                            # 1
for i in range(5):                                      # 01
    for j in range(i+1):                                # 101
        print((i+j+1)%2 , end =" ")                     # 0101
    print()                                             # 10101


# PATTERN 12    
for i in range(1,5):                                    # 1      1
    for j in range(1,i+1):                              # 12    21
        print(j,end =" ")                               # 123  321
    for k in range(1, 2*(4-i)+1):                       # 12344321
        print(" ", end = " ")
    for l in range(1,i+1):
        print(i-l+1,end =" ")
    print()

    
# PATTERN 13
num = 1                                                 # 1                          
for i in range(1, 6):                                   # 2 3
    for j in range(1,i+1):                              # 4 5 6 
        print(num, end=" ")                             # 7 8 9 10 
        num += 1                                        # 11 12 13 14 15
    print()


# PATTERN 14

#ASCII is used, it is just a number system for characters (A,B..,a,b..)
# 'A' = 65, 'B' = 66 .... 'Z' = 90 ,,, 'a' = 97, 'b' = 98...        # A 
for i in range(1,6):                                                # A B
    for j in range(0,i):                                            # A B C
        print(chr(65 + j), end = " ")                               # A B C D
    print()                                                         # A B C D E 


# PATTERN 15                                                        # A B C D E 
for i in range(1,6):                                                # A B C D 
    for j in range(0,6-i):                                          # A B C
        print(chr(65+j),end =" " )                                  # A B 
    print()                                                         # A 
    
# PATTERN 16
for i in range(0,5):                                                # A 
    char = chr(65+i)                                                # B B 
    for j in range(0,i+1):                                          # C C C 
        print(char , end = " ")                                     # D D D D 
    print()                                                         # E E E E E 

# PATTERN 17 
for i in range(1,5):                                                #       A
    for j in range(1,5-i):                                          #     A B A 
        print(" ", end = " ")                                       #   A B C B A 
    for k in range(1,i+1):                                          # A B C D C B A 
        print(chr(64+k),end = " ")
    for k in range(1,i):
        print(chr(64+k),end = " ")
    print()


# PATTERN 18                                                        # E 
for i in range(1,6):                                                # D E 
    for j in range(1,i+1):                                          # C D E 
        print(chr(65+(4+j-i)), end =" ")                            # B C D E 
    print()                                                         # A B C D E 

# PATTERN 19
for i in range(1,6):                                                # **********
    for j in range(1,7-i):                                          # ****  ****
        print("*" , end = " ")                                      # ***    *** 
    for k in range(1,2*(i-1)+1):                                    # **      **
        print(" ", end = " ")                                       # *        *
    for l in range(1,7-i):                                          # *        *
        print("*", end = " ")                                       # **      **
    print()                                                         # ***    ***
for s in range(1,6):                                                # ****  ****
    for t in range(1,s+1):                                          # **********
        print("*",end  =" ")
    for u in range(1,2*(5-s)+1):
        print(" " ,end = " ")
    for v in range(1,s+1):
        print("*",end = " ")
    print()


# PATTERN 20 
for i in range(1,6):                                                # *        *
    for j in range(1,i+1):                                          # **      **
        print("*" , end = " ")                                      # ***    ***
    for k in range(1,2*(5-i)+1):                                    # ****  ****
        print(" ", end = " ")                                       # **********
    for l in range(1,i+1):                                          # ****  ****
        print("*", end = " ")                                       # ***    ***
    print()                                                         # **      **
for m in range(1,5):                                                # *        *
    for n in range(1,6-m):                                          
        print("*",end =" ")             
    for o in range(1,2*(m-1)+1):
        print(" ",end =" ")
    for p in range(1,6-m):
        print("*",end = " ")
    print()
    

# PATTERN 21
for i in range(1,3):
    for j in range(1,4-i):
      print("*", end = " ")
    for k in range(1,2*(i-1)+1):
        print(" ", end = " ")                                       # * * * * 
    for l in range(1,4-i):                                          # *     *
        print("*",end = " ")                                        # *     *
    print()                                                         # * * * *
for m in range(1,3):
    for n in range(1, m+1):
        print("*", end  =" ")
    for o in range(1,2*(2-m)+1):
        print(" ",end = " ")
    for p in range(1,m+1):
        print("*", end = " ")
    print()

# PATTERN 22 
for i in range(1,5):
     for j in range(1,i+1):
         print(5-j, end = " ")
     for k in range(1,2*(5-i)-1):
         print(5-i,end =" ")
     for l in range(2,i+1):
         print(5-(i-l+1), end = " ")
     print()

for m in range(1,4):
   for n in range(1,5-m):
       print(5-n, end = " ")
   for o in range(1,2*m -1):
       print(m ,end = " ")
   for p in range(1,4-m):
       print( p ,end = " ")
   print()

      
