class MyException(Exception):
    pass
def error(ErrTitle):
    raise MyException(ErrTitle)