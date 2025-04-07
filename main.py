for i in range(32, 128):
    print(str(i).ljust(3), ": " + chr(i), end="      ")
    if i % 4 == 0:
        print()
