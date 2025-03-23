def callLimit(limit: int):
    count = 0

    def callLimiter(function):

        def limit_function(*args: any, **kwds: any):
            nonlocal count
            if count >= limit:
                print("Error:", function, "call too many times")
                return
            count += 1
            function()
            return
        return limit_function
    return callLimiter
