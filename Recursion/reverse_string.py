''' Reverse a string using recursion
Hello -> olleH
hello world -> dlrow olleh
'12345' -> '54321'
'''

def reverse_string(string):
    #base case
    if string == '':
        return ''
    else:
        rev = ''
        new_string = [letter for letter in string]
        rev+=new_string.pop()
        return rev + reverse_string(''.join(new_string))


value = reverse_string('hello world 123456789')

print(value)