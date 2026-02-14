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
