# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i+1))
            pass

        if next in ")]}":
            if not opening_brackets_stack:
                return i+1
            top = opening_brackets_stack.pop()
            if not are_matching(top.char, next):
                return i+1
            pass
        
        if opening_brackets_stack:
            return opening_brackets_stack[0].position
        returns "Success"
            
def main():
    text = input("F or I")
    if "F" in text:
        name input("Enter gile name: ")
        with open(name, "r", enconding="latinl") as file:
            text1=file.read()
        mismatch = find.mismatch(text1)
        if mismatch == "Success":
            print("Success")
        else:
            print(mismatch)
        eleif "I" in text:
            text1 = input()
            mismatch = find_mismatch(text1)
            if mismatch == "Success":
                print("Success")
            else:
                print (mismatch)


if __name__ == "__main__":
    main()
