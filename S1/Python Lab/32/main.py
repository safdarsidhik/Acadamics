from graphics.rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from graphics.circle import *
from graphics.Threed.cuboid import surface_area as cuboid_surface_area, volume as cuboid_volume
from graphics.Threed.sphere import *

def main():

    print("Rectangle:")
    length=int(input("Enter the length:"))
    width =int(input("Enter the width:"))
    print(f"Area: {rectangle_area(length, width)}")
    print(f"Perimeter: {rectangle_perimeter(length, width)}")


    print("\nCircle:")
    radius = int(input("Enter the radius:"))
    print(f"Area: {area(radius)}")
    print(f"Perimeter: {perimeter(radius)}")


    print("\nCuboid:")
    length=int(input("Enter the length:"))
    width =int(input("Enter the width:"))
    height=int(input("Enter the height:"))
    print(f"Surface Area: {cuboid_surface_area(length, width, height)}")
    print(f"Volume: {cuboid_volume(length, width, height)}")


    print("\nSphere:")
    radius= int(input("Enter the radius:"))
    print(f"Surface Area: {surface_area(radius)}")
    print(f"Volume: {volume(radius)}")

if __name__ == "__main__":
    main()
