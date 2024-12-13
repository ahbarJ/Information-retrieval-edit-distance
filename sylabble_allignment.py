import nltk 

def get_syllables(word):
    syllables = []
    phones = nltk.corpus.cmudict.dict().get(word.lower())
    if phones:
        for phone_list in phones:
            syllables.extend(phone_list)
    return syllables

def align_syllables(word1, word2):
    syllables1 = get_syllables(word1)
    syllables2 = get_syllables(word2)

    min_len = min(len(syllables1), len(syllables2))
    
    alignment = list(zip(syllables1[:min_len], syllables2[:min_len]))

    return alignment

def distance (word1, word2):
    return len(align_syllables(word1, word2)) # changed the return value from a list to the number of elements in that list
