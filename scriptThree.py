# Given a word
# Have the program remove the given suffix
# Use the strip method

# Strip Method
def suffixStrip(suffix, word):
    return print(word.rstrip(suffix))

suffixStrip('ed',"murdered")
