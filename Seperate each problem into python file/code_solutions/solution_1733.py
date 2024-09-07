def find_overlapping_substrings(s, t):
    # Write your code here
    # return [i for i in range(len(s)) if s[i:i+len(t)] == t]
    return [i for i in range(len(s)) if s[i:i+len(t)] == t]

if __name__ == '__main__':
    print(find_overlapping_substrings('abc', 'ab'))
    print(find