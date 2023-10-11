
def angles(n):    # n is the number of sides
    sum =0
    if n==0:
        sum = 0
    else:
        sum = (n-2)*180  #calculates the total sum of the interior angles.
    return sum

def noOfSides(ang): # ang is the total interior angle
    sides = 0
    if ang == 0:
        sides = 0
    else:
        sides = (ang +360)/180   #calcualates how many sides the shape has
    return sides



if __name__ == "__main__":
    n = int(input("Enter a number: "))
    if n < 0:
        print("Angle are not defined for negative numbers.")
    else:
        result = angles(n)
        print(f"The total angle of {n} sides  is {result}")
    
    totAng = int(input("Enter a total interior angle for a shape: "))
    if totAng<0:
        print(" shapes are not defined for negative numbers.")
    else:
        display = noOfSides(totAng)
        print(f"The total sides of {totAng} angles is {display}")





