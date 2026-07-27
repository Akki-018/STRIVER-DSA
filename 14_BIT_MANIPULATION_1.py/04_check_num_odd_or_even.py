## TO CHECK IF THE NUMBER IS ODD OR EVEN 
def odd_even(n):
    if n&1==1:
        return f"The number is odd"
    return f"The number is even"
print(odd_even(17))