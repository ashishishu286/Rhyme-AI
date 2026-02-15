import re
from cmu_loader import load_cmu_dict
phoneme_list = load_cmu_dict()

def find_last_stressed_vowel(phenome):
    index = len(phenome)-1
    for x in range(index, -1, -1):
        if phenome[x].endswith(("1","2")):
            return x
    return -1

def extract_rhyme_part(phoneme_list):
    rhyme_words = {}

    for word, pronunciations in phoneme_list.items():
        for phonemes in pronunciations:
            index = find_last_stressed_vowel(phonemes)

            if index == -1:
                continue

            phoneme_key = " ".join(phonemes[index:])

            if phoneme_key not in rhyme_words:
                rhyme_words[phoneme_key] = []

            rhyme_words[phoneme_key].append(word)

    return rhyme_words


rhymeDict = extract_rhyme_part(phoneme_list)

def get_rhymes(word):
    word = re.sub(r'[^a-z]', '', word.lower())
    pronounciations = phoneme_list.get(word)
    if not pronounciations:
        print("Sorry, this word is not present in the dictionary")
    else:
        ans = set()
        for phenome in pronounciations:
            index = find_last_stressed_vowel(phenome)
            if index == -1:
                continue
            wordKey = " ".join(phenome[index:])
            for x in rhymeDict.get(wordKey, []):
                if x!=word:
                    ans.add(x)
        return sorted(ans)