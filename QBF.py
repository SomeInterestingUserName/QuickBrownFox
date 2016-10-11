#QuBrFx--"Quick Brown Fox Test"--Searches a string and returns whether or not it contains all letters of the alphabet.
#
#Revision History
#   -1.0 Initial Release

def QuBrFx(string_in, charset="abcdefghijklmnopqrstuvwxyz"):
    letters = list(charset)
    lettercount = 0
    string_in = string_in.lower()
    for items in letters:
        if items.lower() in string_in:
            lettercount += 1
        else:
            break
    return lettercount == len(letters)

if __name__ == '__main__': #Executes a test case if program is directly run. Just to test.
    import time
    start = time.clock()
    result = QuBrFx("The quick brown fox jumps over the lazy dog.")
    print(time.clock() - start)
    print(result)
