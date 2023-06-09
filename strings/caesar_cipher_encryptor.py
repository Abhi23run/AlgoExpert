def caesarCipherEncryptor(string, key):
    # Write your code here.
    #code_abhinav
    final_string=''
    for letter in string:
        final_string+=(chr(((ord(letter)-ord('a')+key)%26)+ord('a')))
    return final_string
