def vowel_count(phrase):
    phrase = phrase.lower()
    from collections import defaultdict
    counter = defaultdict(int)
    counter = {ltr: counter[ltr] + 1 for ltr in phrase}
    return counter

if __name__ == '__main__':
    print(vowel_count('aeiiiou'))

