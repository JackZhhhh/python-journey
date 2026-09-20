def count_frequencies(words):
    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1
    return count

if __name__ == "__main__":
    print(count_frequencies(["a", "b", "a", "c", "b", "a"]))  # expect {'a': 3, 'b': 2, 'c': 1}
    print(count_frequencies([]))                               # expect {}
    print(count_frequencies(["x"]))                             # expect {'x': 1}
    print(count_frequencies(["a", "a", "a"]))                   # expect {'a': 3}
