def xor_and_convert_to_ascii(hex_numbers):
    result = []
    for hex_num in hex_numbers:
        # Convert hexadecimal string to integer
        num = int(hex_num, 16)
        # XOR result is already in integer form, so no need to XOR again
        # Convert the XOR result to ASCII and add to the result list
        ascii_char = chr(num)
        result.append(ascii_char)
    return ''.join(result)

# Example usage:
original_hex_numbers =  [
    '00', 'ec', '9b', '9e', 'c3', 'ef', 'af', 'ab', 'e8', 'e4', '95', 'cf', 'db', 'ed', 'b3', 'cb', 
    'dc', 'f2', 'b3', 'ca', 'c5', 'ae', '80', '93', '9b', 'c0', '82', 'cc', '9d', 'fb', 'b3', 'ce', 'c3', 
    'ef', '9e', 'cf', 'd8', 'ac', '81', 'cc', 'c0', 'a8', 'b3', 'c9', 'cd', 'fb', 'df', '99', '9b', 'e2'
]

xored_ascii = xor_and_convert_to_ascii(original_hex_numbers)
print(len(original_hex_numbers))
print(xored_ascii)
