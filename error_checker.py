def check_if_is_none(*arguments):
    for a in arguments:
        if a is None:
            raise TypeError(f"Error! Mandatory argument {a} not passed.")