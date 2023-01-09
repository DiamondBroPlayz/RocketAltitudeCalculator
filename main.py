import math
import shutil
import os
import time
import random
import pyfiglet

# Math Needed Variables
pi = 3.141592653589793

while True:
    try:
        # Clear screen
        cls = os.system("cls" if os.name == "nt" else "clear")
        cls
        # Get terminal width
        terminal_width, terminal_height = shutil.get_terminal_size()
        # Print banner with ASCII art
        print("*" * terminal_width)
        print("\n")
        print(pyfiglet.figlet_format("Cobalt Spider", font="univers"))
        print("\n")
        print("*" * terminal_width)

        # Declare variables
        M = float(input("Mass of your rocket in kilograms: ").replace(',', ''))  # Mass of rocket in kilograms
        PrevA = float(input("Diameter in inches of your rocket: ").replace(',', ''))  # Diameter of rocket in inches
        A = pi * ((0.5 * (PrevA / 12) * 0.3048) ** 2)  # Cross-sectional area of rocket in meters squared
        rho = 1.2  # Density of air in kg/m^3
        Cd = 0.75  # Drag coefficient of rocket
        k = 0.5 * rho * Cd * A  # Coefficient for wind resistance
        T = float(
        input("Thrust of your rocket's engine in newtons: ").replace(',', ''))  # Thrust of rocket engine in newtons
        I = float(input("Impulse of your rocket's engine in newton-seconds: ").replace(',',''))  # Impulse of rocket engine in newton-seconds
        t = I / T  # Burn time of rocket engine in seconds
        g = 9.8  # Acceleration of gravity in m/s^2

        q = math.sqrt((T - M * g) / k)
        x = 2 * k * q / M

        v = q * (1 - math.exp(-x * t)) / (1 + math.exp(-x * t))
        yb = (-M / (2 * k)) * math.log((T - M * g - k * v ** 2) / (T - M * g))
        yc = (M / (2 * k)) * math.log((T - M * g) / (T - M * g - k * v ** 2))
        total_altitude = yb + yc

        # Make the rocket "launch"
        print("\n" + "*" * terminal_width)
        for i in range(terminal_height - 3):
            print(" " * ((terminal_width - 23) // 2) + "     /\\      _____")
            print(" " * ((terminal_width - 23) // 2) + "    /  \\    /     \\")
            print(" " * ((terminal_width - 23) // 2) + "   /____\\  /       \\")
            print(" " * ((terminal_width - 23) // 2) + "  /      \\/         \\")
            print("*" * terminal_width)
            time.sleep(0.1)

            # Print banner with ASCII art
            print("*" * terminal_width)
            print(pyfiglet.figlet_format("Congrats!", font="univers"))
            print("*" * terminal_width)

            # Print
            print(f"\nYou reached {total_altitude} altitude!")
            print("\nAdditional statistics:")
            print(f"\nVelocity at burnout: {v:.2f} m/s")
            print(f"\nAltitude reached at end of boost phase: {yb:.2f} meters")
            print(f"\nAdditional height achieved during coast phase: {yc:.2f} meters")
        input("\nPress Enter to launch again...")
    except Exception as e:
        with open("errors.txt", "a") as f:
            f.write(str(e) + "\n")
        print("Uh oh! We ran into an error! Press enter to re-try!")
        input()
    except KeyboardInterrupt:
        print("You actually thought you could get a terminal out of me lol")
        input("Press enter to go back to the start")
