def suma(*args: float) -> float:
    for i in args:
        if not isinstance(i, (int, float)):
            raise TypeError(f"Argument {i} is not a number")
    return sum(args)
def test_suma():
    assert suma(1, 2, 3) == 6
    assert suma(1.5, 2.5) == 4.0
    assert suma(-1, -2, -3) == -6
    assert suma(0) == 0
    assert suma() == 0
    try:
        suma(1, 'a')
    except TypeError as e:
        assert str(e) == "Argument a is not a number"
    try:
        suma(1, None)
    except TypeError as e:
        assert str(e) == "Argument None is not a number"
    try:
        suma(1, [1, 2])
    except TypeError as e:
        assert str(e) == "Argument [1, 2] is not a number"
    try:
        suma(1, {1: 2})
    except TypeError as e:
        assert str(e) == "Argument {1: 2} is not a number"
if __name__ == "__main__":
    test_suma()
    print("All tests passed.")
    print("Function suma is working correctly.")
    print("You can now use it in your code.")
    print("This function takes any number of arguments and returns their sum.")
    print("It raises a TypeError if any argument is not a number.")
    print("You can call it like this: suma(1, 2, 3) or suma(1.5, 2.5).")
    print("You can also call it with no arguments, and it will return 0.")
    print("This function is useful for adding numbers together.")
    print("You can use it in your projects or scripts.")
    print("Have a great day!")

# This code defines a function `suma` that takes any number of arguments and returns their sum.
# It raises a TypeError if any argument is not a number.
# The code also includes a test function `test_suma` that tests the `suma` function with various cases.
# The test function checks for correct behavior with valid inputs and raises TypeErrors for invalid inputs.
# The script runs the test function and prints messages indicating the success of the tests and the functionality of the `suma` function.
# The script is designed to be run as a standalone program.
# The `suma` function is useful for adding numbers together and can be used in projects or scripts.
# The script also includes a message encouraging the user to have a great day.