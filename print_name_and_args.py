import inspect


def open_browser(browser_name):
    pass


def go_to_companyname_homepage(page_url):
    pass


def find_registration_button_on_login_page(page_url, button_text):
    pass


def print_name_and_args(func):
    name_func = func.__name__.split('_')
    args_func = inspect.getfullargspec(func).args
    print('Name function: ', *name_func)
    print('Names arguments:', end=' ')
    if not len(args_func):
        print('no arguments\n')
    else:
        print(*args_func, '\n', sep=', ')


print_name_and_args(open_browser)
print_name_and_args(go_to_companyname_homepage)
print_name_and_args(find_registration_button_on_login_page)
