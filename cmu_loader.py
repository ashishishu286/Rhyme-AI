def load_cmu_dict():
    dictMap = {}

    with open("cmudict.dict", "r") as mainFile:
        for line in mainFile:
            if line.startswith(";;;"):
                continue

            parts = line.split()
            word = parts[0].split("(")[0].lower()   # remove (1), (2) etc.
            phonemes = parts[1:]

            if word in dictMap:
                dictMap[word].append(phonemes)
            else:
                dictMap[word] = [phonemes]

    return dictMap

#Problems Faced in this
# -> First I didn't knew about split function, so I implemented it using for loop, which
# was logically correct but since original function of python are written in C or C++
# they are comparatively faster, even if the logic is same
# -> CMU dictionary contains multiple pronunciations of same word. for example read
# has two different pronunciation, which in the file are written as read(1) and
# read(2), so it took me sometime to figure out. My solution to this problem was
# while looping we can check if the word ends with ")", if yes then then we iterate
# and remove "(1)" part and store its phenome in as a second list by using append
# function, but to my surprise even this could have been done with the help of
# inbuild function split()
# -> I also didnt knew I can directly do  phonemes = parts[1:], initially I used for
# loop for that