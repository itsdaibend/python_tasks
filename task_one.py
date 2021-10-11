# function, that counts all leters in string.
def count_letters(data:str):
    result = {}

    for element in data:
        if element in result.keys():
            result[element] = result.get(element) + 1
        else:
            result[element] = 1
    
    return result 


if __name__ == "__main__":
    while True:
        input_data = input('Enter string to count: ')
        print(count_letters(input_data))

        iteration = input('Count the letters one more time?[y/n]: ')
        if iteration.lower() not in ['y', 'yes']:
            break