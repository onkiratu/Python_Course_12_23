# Floating points
def main():
    a = float(input("Enter a: "))
    print("a squared is", square(a) )

def square(n): 
    #return n+n   # intentionally meant to be wrong for testing purposes 
    return n * n
    #return n**2
    #return round(pow(n,2))

if __name__=="__main__":
    main()