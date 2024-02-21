# NAME: Sheena Watson
# COURSE NUMBER: CIS261
# LAB TITLE: Week 8 Lab Rectangle
def printRectangle():
    height = int(input("\nHeight: "))
    width = int(input("Width: "))
    print("Perimeter: "+str(2*(height + width)))
    print("Area: "+str(height * width))
    for i in range(0, height):
        diagram = "* "
        c = "  "
        if i == 0 or i == height-1:
            c="* "
        for j  in range(0, width-2):
            diagram = diagram+c   
        diagram = diagram+"* "    
        print(diagram)

    
print("Rectangle Calculator")
while True:
    printRectangle()
    repeat = input("Continue? (y/n): ")
    repeat = repeat.lower()
    if repeat == "n":
        print("Bye....")
        exit()
    