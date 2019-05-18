# Data normalization
# -- Len and Count
def letterCount(word,letter):
    # Loop through word if i = letter wordCount + 1
    counter = 0
    for x in word:
        if x == letter :
            counter = counter+1
    return print(counter)
missisipiCount = letterCount("missisipi", "m")
print(missisipiCount)
