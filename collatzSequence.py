def ruth(number):
    if number > 5:
        number += 2
        print(number)
        return int(number)
    else:
        number -= 3
        print(number)
        return int(number)

ruth(12)


# collatz
def collatz(number):
    
    if number % 2 == 0:
        number = (number // 2)
        print(number)
        return (print(int(number)))
            
    elif number % 2 == 1:
        number = (3 * number + 1)
        print(number)
        return (print(int(number)))
               
        
integer = int(input())

collatz(integer)
while collatz != 1:
    continue
    



