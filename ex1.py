DIGIT_WORDS = [
  'zero',
  'one',
  'two',
  'three',
  'four',
  'five',
  'six',
  'seven',
  'eight',
  'nine',
]

def number_to_words(num):
    worded_numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '10']
    return  ' '.join(worded_numbers[int(digit)] for digit in str(num))



def words_to_number(words):
    word_to_number_dict = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    full_number = ''

    for line in  words.split('\n'):
        for word in line.split(' '): 
            full_number += str(word_to_number_dict.get(str(word)))
        return full_number

print(number_to_words(69))
print(number_to_words(752))
print(number_to_words(24))
print(number_to_words(54985304))

print('----------')

print(words_to_number("two three five six"))
print(words_to_number("one zero zero"))
print(words_to_number("six nine"))