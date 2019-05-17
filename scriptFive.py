inputs = ['words','going','backwards']
def reverseWords(array):
    for x in array:

        arrayIndex = array.index(x)
        
        print(array.index(arrayIndex+1))


reverseWords(inputs)