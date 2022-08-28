import one
print("TOP LEVEL NAMEANDMAIN .PY")
one.func()

if __name__ == '__main__':
    print("nameandmain.py is being run directly")
else:
    print("two is being imported")