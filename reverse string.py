def remove_vowels(input_string):
    vowels = "aeiouAEIOU"
    result = ""
    for char in input_string:
        if char not in vowels:
            result += char  # Add non-vowel characters to the result
    return result

# Example usage
string = input("Enter a string: ")
print("String without vowels:", remove_vowels(string))


#def remove_vowels(input_string);
#vowels = "aeiouAEIOU"
# =""
#for char in input_string
#if char not in range
#result += char
#return result
