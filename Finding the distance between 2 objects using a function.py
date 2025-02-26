from math import sqrt

def distance(x1, y1, x2, y2):
    return sqrt( (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2) )

def main():
    a1, b1 = map(int, input("Enter cordinates of first object:").split())
    a2, b2 = map(int, input("Enter cordinates of second object:").split())
    
    result = distance(a1, b1, a2, b2)
    print(f"The distance between 2 object is: {result:.2f}")
if __name__ == '__main__':
    main() 