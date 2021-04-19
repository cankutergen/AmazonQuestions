def longestCommonSubstring(str1, str2):
    matrix = []
    max_val = 0

    for i in range(len(str1)):
        row = []
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                if i > 0 and j > 0:
                    row.append(matrix[i - 1][j - 1] + 1)
                    max_val = max(max_val, matrix[i - 1][j - 1] + 1)
                else:
                    row.append(1)
            else:
                row.append(0)

        matrix.append(row)

    return max_val
