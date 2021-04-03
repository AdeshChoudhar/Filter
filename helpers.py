from os import system


def filter_help():
    print()

    system("figlet -c help")

    print()
    print("\t\t+----------------------------------------------+")
    print("\t\t|    python main.py <image_path> -[filter]    |")
    print("\t\t+----------------------------------------------+")

    print("\nFILTERS:")
    print("\t\u2022 -gs: Grayscale")
    print("\t\u2022 -sp: Sepia")
    print("\t\u2022 -mr: Mirror Reflection")
    print("\t\u2022 -wr: Water Reflection")
    print("\t\u2022 -rl: Rotate Left")
    print("\t\u2022 -rr: Rotate Right")
    print("\t\u2022 -ci: Colour Inversion")
    print("\t\u2022 -bl: Blur")

    print("\n* Multiple filters can be applied simultaneously!")
    print()
    exit(1)
