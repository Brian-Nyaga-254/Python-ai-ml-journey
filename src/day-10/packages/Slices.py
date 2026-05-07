import sys
if len(sys.argv) < 2:
    print("Too few arguments")
    sys.exit()
for arg in sys.argv[1:-1]:
    print("Hello my name is,",arg)