def history(operation, n1, n2=None, result=None):
    """Creates a formatted string for the calculation."""
    if operation == "sqrt":
        return f"sqrt {n1} = {result}"
    else:
        return f"{n1} {operation} {n2} = {result}"
