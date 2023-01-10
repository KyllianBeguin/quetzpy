def log(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}({args}, {kwargs}) -> {result}')
        return result
    return wrapper