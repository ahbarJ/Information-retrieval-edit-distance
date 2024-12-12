def dice_coefficient(set1, set2):
    intersection = len(set1.intersection(set2))
    dice = (2.0 * intersection) / (len(set1) + len(set2))
    return dice

def distance (top10, rest):
    return dice_coefficient(top10, rest)
