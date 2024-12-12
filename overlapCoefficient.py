def overlap_coefficient(set1, set2):
    common_elements = len(set1.intersection(set2))
    total_unique_elements = min(len(set1),len(set2))
    
    if total_unique_elements == 0:
        return 0.0 # Avoid division by zero
    
    coefficient = common_elements / total_unique_elements
    return coefficient

def distance (top10, rest):
    return overlap_coefficient(top10, rest)
