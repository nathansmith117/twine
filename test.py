#! /usr/bin/python3

from twine import Twine

def main():
    test_twine = Twine("Hello world")

    print(test_twine / 2)
    print(test_twine ** 2)
    print(test_twine.sqrt())
    print((test_twine ** 2).sqrt())


if __name__ == "__main__":
    main()
