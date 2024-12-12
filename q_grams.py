def generate_qgrams(string, q):
    qgrams = []
    for i in range(len(string) - q + 1):
        qgram = string[i:i+q]
        qgrams.append(qgram)
    return qgrams

def find_common_qgrams(string1, string2, q):
    qgrams1 = generate_qgrams(string1, q)
    qgrams2 = generate_qgrams(string2, q)
    
    common_qgrams = set(qgrams1) & set(qgrams2)
    
    return common_qgrams

def distance (word1, word2):
    return len(find_common_qgrams(word1, word2, 2)) # changed the return value from a 'set' to the 'number of the elements in the set' (default: 2-grams)
