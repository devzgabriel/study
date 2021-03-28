def iq_test(numbers):
    odd=0
    even=0
    numbers = numbers.split()
    for n in numbers:
        if int(n)%2==0:
            odd+=1
            rodd=numbers.index(n)+1
        else:
            even+=1
            reven=numbers.index(n)+1
    return rodd if odd<even else reven