def square(x: int | float) -> int | float:
    """
    Returns the square of the given number.

    Parameters:
    x (int | float): The number to be squared.

    Returns:
    int | float: The squared value of x.
    """
    return x ** 2


def pow(x: int | float) -> int | float:
    """
    Raises the given number to the power of itself.

    Parameters:
    x (int | float): The base number.

    Returns:
    int | float: The result of x raised to the power of x.
    """
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Creates a closure that repeatedly applies a function to a stored value.

    Parameters:
    x (int | float): The initial value.
    function (callable): A function that takes a number and returns a
    transformed number.

    Returns:
    object: A function (inner) that, when called, applies the given function to
            the stored value and returns the updated value.
    """
    count = 0

    def inner() -> float:
        """
        Applies the function to the stored value and returns the updated res.

        Returns:
        float: The updated value after applying the function.
        """
        nonlocal count
        if count == 0:
            count = x
        count = function(count)
        return count
    return inner
