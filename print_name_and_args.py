import inspect


def print_name_and_args(func):
    name_func = func.__name__.split('_')
    args_func = inspect.getfullargspec(func).args
    print('Name function: ', *name_func)
    print('\nNames arguments:', end=' ')
    if not len(args_func):
        print('no arguments')
    else:
        print(*args_func, sep=', ')
