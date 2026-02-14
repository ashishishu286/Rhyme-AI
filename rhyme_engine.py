from cmu_loader import load_cmu_dict
phoneme_list = load_cmu_dict()

def extract_rhyme_part(phoneme_list):
    rhyme_words = {}

    for x in phoneme_list:
        clean_word = x.split("(")[0]

        for parts in phoneme_list[x]:
            ind = len(parts)-1
            found = False
            for y in range(ind, -1, -1):
                if parts[y].endswith(("1", "2")):
                    ind = y
                    found = True
                    break

            if not found:
                continue

            phonemeKey = " ".join(parts[ind:]) # cleaner and faster instead of phonemeKey += part

            if phonemeKey in rhyme_words:
                rhyme_words[phonemeKey].append(clean_word)
            else:
                rhyme_words[phonemeKey] = [clean_word]  #underdstand it

    return rhyme_words


extract_rhyme_part(phoneme_list)
