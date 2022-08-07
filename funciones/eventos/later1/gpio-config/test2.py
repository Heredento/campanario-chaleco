

owo = input(f"Escribe lo que sea:\n")
def uwu (var):
    print(type(var))
    match type(var):
        case "<class 'int'>":
            print("Integer")
        case "<class 'float'>":
            print("Flotante")
        case "<class 'str'>":
            print("String")
        case other:
            print(type(var))

uwu(owo)





# command = 'Hello, World!'
# >>> match command:
# ...     case 'Hello, World!':
# ...         print('Hello to you too!')
# ...     case 'Goodbye, World!':
# ...         print('See you later')
# ...     case other:
# ...         print('No match found')