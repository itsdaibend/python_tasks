"""
Function, that backwards each word in text. For instance: DAY
<<< Y
<<< A
<<< D
"""
def get_backward_string(text:str):
    print(text[-1])
    try:
        get_backward_string(text[:-1])
    except IndexError:
        pass

if __name__ == "__main__":
    while True:
        input_data = input('Enter text: ')
        get_backward_string(str(input_data))

        iteration = input('Make string backward again?[y/n]: ')
        if iteration.lower() not in ['y', 'yes']:
            break