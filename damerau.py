def damerau_levenshtein_distance(str1, str2):
    m, n = len(str1), len(str2)

    # Initialize a matrix to store distances
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the first row and column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Fill in the rest of the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if str1[i - 1] == str2[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1, # Deletion
                dp[i][j - 1] + 1, # Insertion
                dp[i - 1][j - 1] + cost # Substitution
            )

            # Check for transposition
            if i > 1 and j > 1 and str1[i - 1] == str2[j - 2] and str1[i - 2] == str2[j - 1]:
                dp[i][j] = min(dp[i][j], dp[i - 2][j - 2] + cost)

    # The bottom-right cell contains the Damerau-Levenshtein distance
    return dp[m][n]

def distance (word1, word2):
    res = damerau_levenshtein_distance(word1, word2)
    return res
