"""    Assuming the 'top10' and 'rest' are already tokenized.    """

def jaccard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union if union != 0 else 0

def distance (top10, rest):
    return jaccard_similarity(top10, rest)

