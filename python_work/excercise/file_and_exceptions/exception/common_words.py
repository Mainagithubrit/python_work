def common_words(filename):
    with open(filename, encoding='utf-8') as f:
        words = f.read()

    total = words.lower().count('the ')
    print(total)


filename = 'raw.txt'
common_words(filename)
