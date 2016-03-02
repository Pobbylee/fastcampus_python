def isdecimal(string):
    for i in string:
        if i >= ‘0’ and i <= ‘9’:
            continue
        return False

    return True
