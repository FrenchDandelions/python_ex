def callLimit(limit: int):
    """
    A decorator factory that limits the nb of times a function can be called.

    Parameters:
    limit (int): The maximum nb of times the decorated function can be called.

    Returns:
    function: A decorator that enforces the call limit on the wrapped function.

    Behavior:
    - When the decorated function is called more than `limit` times,
        it prints an error message and does not execute the function.
    - Maintains an internal count of function calls.
    """
    count = 0

    def callLimiter(function):
        """
        Decorates a function to limit its number of calls.

        Parameters:
        function (callable): The function to be limited.

        Returns:
        function: A wrapped function that enforces the call limit.
        """

        def limit_function(*args: any, **kwds: any):
            """
            Executes the function if the call limit has not been reached.

            Parameters:
            *args: Positional arguments passed to the function.
            **kwds: Keyword arguments passed to the function.

            Returns:
            None
            """
            nonlocal count
            if count >= limit:
                print("Error:", function, "call too many times")
                return
            count += 1
            function()
            return
        return limit_function
    return callLimiter
