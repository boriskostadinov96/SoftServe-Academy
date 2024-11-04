def len_longest_chain(chain_pairs):
    if not chain_pairs:
        return 0

    chain_pairs.sort(key=lambda x: x[1])

    max_len = 1
    dp = [1] * len(chain_pairs)

    for i in range(1, len(chain_pairs)):
        for j in range(i):
            if chain_pairs[j][1] < chain_pairs[i][0]:
                dp[i] = max(dp[i], dp[j] + 1)
                max_len = max(max_len, dp[i])

    return max_len


print(len_longest_chain([(2, 3), (3, 4), (3, 5)]))
print(len_longest_chain([(2, 3), (3, 4), (1, 2)]))
print(len_longest_chain([(-15, -11), (17, 22), (8, 12), (-11, -10), (-4, -1)]))
print(len_longest_chain([(-5, 0), (-4, 0), (4, 5), (3, 4), (-1, 1), (-6, -2)]))