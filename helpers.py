from os import system


filter_arguments = ["-gs", "-sp", "-mr", "-wr", "-rl", "-rr", "-ci", "-bl"]


def filter_help():
    print()

    system("figlet -c help")

    print()
    print("\t\t+----------------------------------------------+")
    print("\t\t|    python main.py <image_path> -[options]    |")
    print("\t\t+----------------------------------------------+")

    print("\nOPTIONS:")
    print("\t\u2022 -gs: Grayscale")
    print("\t\u2022 -sp: Sepia")
    print("\t\u2022 -mr: Mirror Reflection")
    print("\t\u2022 -wr: Water Reflection")
    print("\t\u2022 -rl: Rotate Left")
    print("\t\u2022 -rr: Rotate Right")
    print("\t\u2022 -ci: Colour InversionHelp")
    print("\t\u2022 -bl: Blur")

    print()
    exit(1)


def check_arguments(args):
    for i in args:
        if i not in filter_arguments:
            return False
    return True
