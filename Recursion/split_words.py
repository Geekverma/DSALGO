''' Given a string phrase and list of words,
create function word_split() to split a strind in a way words can be made out of list of words
'''


def word_split(string, list):
    #base case
    if string == '' or len(list) == 0:
        return ''

    else:
        letter = [word for word in list if word in string]

    return letter



value = word_split('themanrang fhsgathe',['the','ran','man',' ','fgh','54','fd','89'])
print(value)