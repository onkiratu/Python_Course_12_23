import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("Helllo, " + sys.argv[1])