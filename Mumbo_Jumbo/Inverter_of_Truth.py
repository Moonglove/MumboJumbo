from random import randint
from math import floor
basic_characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c',
           'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C',
           'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O','P', 'Q',
           'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']



letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

character_list = ['S', 'g', 'v', 'q', ';', ')', 'A', '-', '.', '@', '\\', 'F', 'D', '{', '=', '3', 'z',
                  ']', '1', 'l', 'E', 'x', 'k', 'r', 'p', 'I', 'c', ':', 'N', 'y', 'R', '0', 'L', 'm',
                  '%', 'o', 'a', 'W', 'i', 'B', '~', '/', 'd', 'h', 'u', '$', '2', '|', '[', '5', 'P',
                  '4', '\n', 'K', 'j', '6', 'f', 'X', '_', '}', '\t', 'J', '!', 'C', ',', '"', 'G', 'Z',
                  'b', 's', 'T', 'n', ' ', '(', 'H', 'Q', '+', 'Y', 'U', 'w', '>', '*', "'", '^', '`',
                  '<', 'V', 'M', 'O', '7', '8', '#', '?', 'e', 't', '&', '9']

# Default keys
default_key1 = ('ECd33M1snZWHFzaYIwS4KntJMOTXgmAIQWg431uKra7Pjrk2YD8rwwh97HIqWZ4OQ0pom6fu882nIE7DTeo7vxH'
'yvacSPVwV1Az0lV7bH1zDpJzCWgYHIShpyaxnQ7J2iTmw6WYUq06A3SqDDNnKWqdFKkzhG8uSVe8nvwP8BUqTuiiO7dZ9J5GABHMiQ6D'
'guFQ194zPZ2i3lAUoxTlZimqM70fJjZ5tqQIC7X6yDb6PsscS09F3x2RZo0x1DfqfMpfikbT7TIQvcD4TcGPaWmHCR4U70SLYRcgh2ht'
'srzqKHQIPir2xzTVeF1EyCG226edB6NTigRTEdUJZFUWYwAr63fTdggXPtDpukm9ZeguG6ZVhwG9QCPUs1pTbUwS06AJeFSh9o7PlMfM'
'OrwBGvtetyGwvGcku3WPbakrEZSUKqbBzWMsBSi47a0qAY2StrIjNZxh9eRgNNgLawVMomCjaeKUixegxQziglfhOJMtNyIY6uCjl')

default_key2 = ('IUgPGNLmInOZ024GMXrHwv2RxrKdOhByBtU145xmt17FCkOLEhH6fSM4AlHaxJtxU9mgMx1WH30MlfsSPQHlh0U'
'7rBfoBqd0xDsqRa4SDdYxyR8vSJSGtl0z84f8bvPiqN3TpiYMR0f4iJFA0R54N14QlCXe1CSAgOFZZjtfOllWqKJ3RUu24OGr12gLkBjD'
'FKiHY6cspwAGYx9vD19hIDHCXyojzsfTD8Bm7ituQd4lox9egl0mr1LqZzGwX5nOgoRmiOMNN5zx0fHEOXuhpJSIS7JzKnL5rGvQmclUA'
'A3M1y3mRii4B2YrP1t4mEyJ0Yv2NwEppkoQFeE4R1DPon0uBTEllr5zqc7YfOINnbJHYyS2GXWIqXqsIXCKo8NVKHJFX3Tj2GGs6sCcgs'
'aBgkS9kmwQGTyYrI8mdCeDAsYc3WoL8bxklFBA3RT7Zd7qdFsCaYt7Rljt0ja28BFu8MUhzcmM9FdkYrV5foyHd9fBsB3Sevpd')


# Convert input into shifted verison of base 24 using all letters
# Used for character identifiers later
def base_converter(base, num):

    # Use only letters in the result, used to generate the prefix lists
    if base == 24:
        character_list = letter_list
    # Use only numbers in the result, used to turn a message into only numbers
    else:
        character_list = num_list
        
    for i in range(1, num + 1):
            if base**i > num:
                digit_count = i
                break
    final_string = ''
    for i in range(digit_count, 0, -1):
        current_digit_value = base ** (i-1)
        new_digit = floor(num / current_digit_value)
        num = num - new_digit * current_digit_value
        new_digit = character_list[new_digit]
        final_string += str(new_digit)
    return final_string


# Check if a character or string contains a letter (other than i or q, which are used as salt)
def is_letter(string):
    for character in string:
        if character in letter_list:
            return True
    return False


# Use a polyalphabetic cipher to encode using a key
# Also can be used to reverse the cipher
def poly_cipher(message, key = default_key1, mode='encrypt', encryption_list=character_list):    
    polyed_message = []

    # Turn the key and message into list format
    message_list = [x for x in message]
    key_list = [x for x in key]

    # Iterate throught each character of the message, shifting it an approporate value
    # to create a poly-alphabetic cipher
    x = -1
    for i in message_list:
        x += 1
        key_digit = key_list[x]
        key_value = encryption_list.index(key[x])
        if x == len(key_list)-1: # <-- Resuse the key if it is shorter than the message
            x = -1

        try:
            letter_value = encryption_list.index(i)

            if mode == 'encrypt':
                new_character = key_value + letter_value
                
            elif mode == 'decrypt':
                new_character = letter_value - key_value
            
            if new_character >= len(encryption_list): # <-- Use a wrap-around if a character exceeds the list
                new_character -= len(encryption_list)

            shifted_digit = encryption_list[new_character]
            polyed_message.append(shifted_digit)
            
        except:
            polyed_message.append(i)
            x -= 1

    # Convert the output back into string format
    polyed_message_string = ''
    for i in polyed_message:
        polyed_message_string += i
        
    return polyed_message_string

# Create number system lists
# Call base_lists[your_number_system - 2] to access the correct list
base_lists = [[], [], [], [], [], [], []]
for i in range(1, len(character_list)+1):
    base_lists[0].append(base_converter(2, i))
    base_lists[1].append(base_converter(3, i))
    base_lists[2].append(base_converter(4, i))
    base_lists[3].append(base_converter(5, i))
    base_lists[4].append(base_converter(6, i))
    base_lists[5].append(base_converter(7, i))
    base_lists[6].append(base_converter(8, i))




# Main Encryption function
def encrypt(code, user_key=''):

    # Create basic poly cipher with default key
    code = poly_cipher(code, default_key1)
    if user_key != '':
        code = poly_cipher(code, key=user_key)
        
    # Convert code string to list with LIST COMPREHENSION
    code_list = [x for x in code]

    list_choice = randint(0, 6) #(base_lists[list_choice])

    # Hash_Browns. A hash loop for transforming characters into numerical values
    # The number system is chosen at random from 2 - 8
    for i in range(0, len(code_list)):
        index_value = character_list.index(code_list[i])
        code_list[i] = base_lists[list_choice][index_value]


    # Compile letter prefix list
    prefix_list = []
    for i in range(0, len(code_list)):
        prefix_list.append(base_converter(24, i+1))


    # Convert list to string
    final_code_list = []
    code_string = ''
    special_insert = str(randint((10**(list_choice+1)), (10**(list_choice+2))-1)) # <-- Trigonmetric differential calculus

    # Find the the sum of the digits of special_insert for later use
    total_of_special_insert = 0
    for digit in special_insert:
        total_of_special_insert += int(digit)
    
    # Randomize prefix list
    for total in range(0, total_of_special_insert):
        moving_letter = prefix_list[-1]
        prefix_list.pop()
        prefix_list.insert(0, moving_letter)

    # Assemble full string
    for i in range(0, len(code_list)):
        # Generate the numbers used as spacers between the item in code_list
        divider_num = str(randint(list_choice+2, list_choice+5))
        if int(divider_num) > 9: # <-- Prevent the number from being two-digit
            divider_num = str(randint(8, 9))
            
        new_addition = prefix_list[i] + str(code_list[i]) + divider_num
        insert_position = randint(0, len(final_code_list))
        final_code_list.insert(insert_position, new_addition)

    # Insert the iq string into the final list
    insert_position = randint(0, len(final_code_list))
    final_code_list.insert(insert_position, ('i'+special_insert+'q'))

    # Convert the list to a string
    for i in final_code_list:
        code_string += i

    # Create a final ploy cipher to hide the i & q insert.        
    # If a key was used, it is implemented here, or use a default key if one was not provided
    code_string = poly_cipher(code_string, key=default_key2, encryption_list=basic_characters)
    return code_string


# Main decrypt function
def decrypt(code, user_key=''):

    # Reverse the last ploy cipher used on the code with the default key
    code = poly_cipher(code, key=default_key2, mode='decrypt', encryption_list=basic_characters)


    # Turn string into list (and re-group letter pairs)
    code_list = []
    floating_letters = ''
    for i in code:
        if i in letter_list:
            floating_letters += i
        else:
            if floating_letters != '':
                code_list.append(floating_letters)
                floating_letters = ''
            code_list.append(i)
            
    # Find and remove i & q from the code_list
    i_position = code_list.index('i') + 1
    q_position = code_list.index('q')
    number_system_list = code_list[i_position:q_position]
    x = 0
    for i in range(i_position-1, q_position+1):
        del code_list[i-x]
        x += 1
    number_system = len(number_system_list)-2

               
    # Re-order list
    # Identify number of letters
    number_of_spaces = 0
    big_num_range = num_list[(number_system)+2:10]
    for unit in code_list:
        if unit in big_num_range:
            number_of_spaces += 1
##        for i in big_num_range:
##            if i == code_list[code_list.index(unit)]:
##                number_of_spaces += 1

    
    # Re-order list (also deleting identifier letters and spacer numbers)
    sorted_list = []
    reorder_list = []
    new_addition = ''
    for i in range(0, number_of_spaces):
        reorder_list.append(base_converter(24, i+1))

    # (Un)Randomize re-order list (using total of i-q)
    total_of_number_system = 0
    for digit in number_system_list:
        total_of_number_system += int(digit)
    
    for total in range(0, total_of_number_system):
        moving_letter = reorder_list[-1]
        reorder_list.pop()
        reorder_list.insert(0, moving_letter)

    for i in range(0, number_of_spaces):
        index_pos = code_list.index(reorder_list[i])
        x = 0
        while True:
            x += 1
            if index_pos+x != len(code_list):
                if is_letter(code_list[index_pos+x]) == True:
                    sorted_list.append(new_addition[:-1])
                    new_addition = ''
                    break
                else:
                    new_addition += code_list[index_pos+x]
            else:
                sorted_list.append(new_addition[:-1])
                new_addition = ''
                break
            
    # Convert numerical values into letter equivelents
    number_system = base_lists[number_system]
    
    for i in range(0, len(sorted_list)):
        for num in range(0, len(character_list)):
            if sorted_list[i] == str(number_system[num]):
                sorted_list[i] = character_list[num]
                
    # Convert list to string
    final_string = ''
    for i in sorted_list:
        final_string += str(i)

    # Reverse poly chipher with default key
    # If a key is used, first use the key decryption
    if user_key != '':
        final_string = poly_cipher(final_string, key=user_key, mode='decrypt')
    final_string = poly_cipher(final_string, key=default_key1, mode='decrypt')

    return final_string


# Function calls to be exported
def encrypt_text(text, mode, key=''):
    try:
        if mode == 'encrypt':
            return encrypt(text, key)
        elif mode == 'decrypt':
            return decrypt(text, key)
    except:
        return None

### Test
##message = encrypt_text('All of the bugs are out!', mode='encrypt', key='we\'ll see')
##solution = encrypt_text(message, mode='decrypt', key='we\'ll see')
##print(solution)
