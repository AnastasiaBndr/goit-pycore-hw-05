def input_error(func):
    def inner(*args, **kwargs):
        try:
            print(args)
            return func(*args, **kwargs)
        except ValueError:
            return "Enter the argument for the command"
        except KeyError:
            return "KeyError"
        except IndexError:
            return "IndexError"

    return inner
