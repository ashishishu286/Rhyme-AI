import re
from cmu_loader import load_cmu_dict
cmu_dict = load_cmu_dict()

def find_last_stressed_vowel(phenome):
    index = len(phenome)-1
    for x in range(index, -1, -1):
        if phenome[x].endswith(("1","2")):
            return x
    return -1

def extract_rhyme_part(cmu_dict):
    rhyme_words = {}

    for word, pronunciations in cmu_dict.items():
        for phonemes in pronunciations:
            index = find_last_stressed_vowel(phonemes)

            if index == -1:
                continue

            phoneme_key = " ".join(phonemes[index:])

            if phoneme_key not in rhyme_words:
                rhyme_words[phoneme_key] = []

            rhyme_words[phoneme_key].append(word)

    return rhyme_words


rhymeDict = extract_rhyme_part(cmu_dict)

def get_rhymes(word):
    word = re.sub(r'[^a-z]', '', word.lower())
    pronunciations = cmu_dict.get(word)
    if not pronunciations:
        print("Sorry, this word is not present in the dictionary")
    else:
        ans = set()
        for phoneme in pronunciations:
            index = find_last_stressed_vowel(phoneme)
            if index == -1:
                continue
            wordKey = " ".join(phoneme[index:])
            for x in rhymeDict.get(wordKey, []):
                if x != word:
                    ans.add(x)
        return sorted(ans)

def rhyme_score(p1, p2):
    if len(p1) <= len(p2):
        shorter = p1
        longer = p2
    else:
        shorter = p2
        longer = p1

    max_score = 0
    n = len(shorter)
    m = len(longer)

    # Slide shorter across longer
    for start in range(m - n + 1):
        score = 0
        for i in range(n):
            if shorter[i] == longer[start + i]:
                score += 1
            else:
                break
        max_score = max(max_score, score)

    return max_score


def get_similar_rhymes(word):
    word = re.sub(r'[^a-z]', '', word.lower())
    phoneme = cmu_dict.get(word)
    ans = set()
    for pronunciation in phoneme:
        lastStressIndex = find_last_stressed_vowel(pronunciation)
        if(lastStressIndex==-1):
            continue
        trimmedPhoneme = pronunciation[lastStressIndex:]
        for cmuWord, cmuPronunciations in cmu_dict.items():
            for cmuPronunciation in cmuPronunciations:
                cmuLastStressIndex = find_last_stressed_vowel(cmuPronunciation)
                if (cmuLastStressIndex == -1):
                    continue
                cmuTrimmedPhoneme = cmuPronunciation[cmuLastStressIndex:]
                score = rhyme_score(trimmedPhoneme, cmuTrimmedPhoneme)
                if score>=2:
                    if cmuWord == word:
                        continue
                    ans.add(cmuWord)

    return sorted(ans)

def analyze_line(line):
    words = line.split()
    lineDict = {}
    for word in words:
        word = re.sub(r'[^a-z]', '', word.lower())
        wordPhonemes = cmu_dict.get(word)
        if not wordPhonemes:
            continue
        for wordPhoneme in wordPhonemes:
            wordLastStressedIndex = find_last_stressed_vowel(wordPhoneme)
            if wordLastStressedIndex == -1:
                continue
            wordPhoneme = wordPhoneme[wordLastStressedIndex:]
            if word not in lineDict:
                lineDict[word] = []
            lineDict[word].append(wordPhoneme)
    items = list(lineDict.items())
    ans = set()

    for i in range(len(items) - 1):
        word1, segs1 = items[i]
        for j in range(i + 1, len(items)):
            word2, segs2 = items[j]
            found = False
            for pseg1 in segs1:
                for pseg2 in segs2:
                    if rhyme_score(pseg1, pseg2) >= 2:
                        ans.add((word1, word2))
                        found = True
                        break
                if found:
                    break

    return ans

print(analyze_line("I smoke fire while the mic gets stoked"))