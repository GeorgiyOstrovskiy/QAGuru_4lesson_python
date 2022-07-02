import inspect


def open_browser():
    pass


def go_to_companyname_homepage(page_url):
    pass


def find_registration_button_on_login_page(page_url, button_text):
    pass


def print_name_and_args(func):
    name_func = func.__name__.split('_')
    args_func = inspect.getfullargspec(func).args
    print('Name function:', end=' ')
    for i in name_func:
        print(i, end=' ')
    print('\nNames arguments:', end=' ')
    if not len(args_func):
        print('no arguments')
    else:
        for i in args_func:
            print(i, end=', ')


print_name_and_args(find_registration_button_on_login_page)
