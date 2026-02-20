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

def rhyme_section(p1, p2):
    if len(p1) <= len(p2):
        shorter = p1
        longer = p2
    else:
        shorter = p2
        longer = p1

    max_score = 0
    n = len(shorter)
    m = len(longer)

    best_segment = []

    for start in range(m - n + 1):
        score = 0
        temp = []

        for i in range(n):
            if shorter[i] == longer[start + i]:
                score += 1
                temp.append(shorter[i])
            else:
                break

        if score > max_score:
            max_score = score
            best_segment = temp

    return best_segment

def weighted_rhyme_section(p1, p2):
    p1Last = find_last_stressed_vowel(p1)
    p2Last = find_last_stressed_vowel(p2)

    if p1Last == -1 or p2Last == -1:
        return [], 0

    p1 = p1[p1Last:]
    p2 = p2[p2Last:]

    if(len(p1)>len(p2)):
        longer = p1
        shorter = p2
    else:
        longer = p2
        shorter = p1

    max_score = 0
    bestSegment = []

    for start in range(len(longer)-len(shorter)+1):
        score = 0
        tempList = []
        for i in range(len(shorter)):
            if shorter[i] == longer[start+i]:
                phoneme = shorter[i]
                tempList.append(phoneme)
                if phoneme.endswith(('1', '2')):
                    score += 3
                elif phoneme.endswith('0'):
                    score += 2
                else:
                    score += 1
            else:
                break
        if score > max_score:
            max_score = score
            bestSegment = tempList

    return bestSegment, max_score

def analyze_line(line):
    words = line.split()
    instances = []

    # Build token instances (duplicates preserved)
    for word in words:
        clean = re.sub(r'[^a-z]', '', word.lower())
        wordPhonemes = cmu_dict.get(clean)
        if not wordPhonemes:
            continue

        segments = []
        for phoneme in wordPhonemes:
            idx = find_last_stressed_vowel(phoneme)
            if idx == -1:
                continue
            segments.append(phoneme[idx:])

        if segments:
            instances.append({
                "word": clean,
                "segments": segments
            })
    print(instances)

    ans = {}
    pair_count = 0

    # Token-based pair comparison
    for i in range(len(instances) - 1):
        word1 = instances[i]["word"]
        segs1 = instances[i]["segments"]

        for j in range(i + 1, len(instances)):
            word2 = instances[j]["word"]
            segs2 = instances[j]["segments"]

            found = False

            for pseg1 in segs1:
                for pseg2 in segs2:
                    segment, score = weighted_rhyme_section(pseg1, pseg2)

                    if score >= 4:
                        pair_count += 1
                        key = " ".join(segment)

                        if key not in ans:
                            ans[key] = {
                                "words": [],
                                "score": score
                            }
                        else:
                            ans[key]["score"] = max(ans[key]["score"], score)

                        # store actual pair occurrence
                        ans[key]["words"].append((word1, word2))

                        found = True
                        break
                if found:
                    break
    print(ans)
    result = {}

    for key, data in ans.items():
        score = data["score"]

        if score >= 6:
            strength = "strong"
        elif score >= 4:
            strength = "medium"
        else:
            strength = "weak"

        result[key] = {
            "pairs": data["words"],   # list of pair occurrences
            "strength": strength,
            "score": score
        }

    n = len(instances)

    return result, pair_count, n

def rhyme_density(line):
    clusters, pair_count, n = analyze_line(line)

    if n < 2:
        return 0

    total_possible_pairs = (n * (n - 1)) / 2

    return pair_count / total_possible_pairs