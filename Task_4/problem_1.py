def count_words(filename):
    with open(filename, 'r') as f:
        words = f.read().lower().split()
    word_count = {}
    for word in words:
        word = ''.join(char for char in word if char.isalnum())
        if word:
            word_count[word] = word_count.get(word, 0) + 1
    for word, count in word_count.items():
        print(word, count)

count_words('Sample.txt')
