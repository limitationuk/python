def add (a, b):
    return a + b

def sub (a, b):
    return a - b

def mul (a, b):
    return a * b

def div (a, b):
    return a / b

def module_name():
    print(f"My __name__ is {__name__}")
    if __name__ == "__main__":
        print("직접실행됨")
    else:
        print("호출됨")
module_name()