def read_dictionary(dictionary_file):
    ''' read dictionary file'''
    d = {}
    f = open(dictionary_file, 'r')
    for line in f.readlines():
        kv = line.strip().split(',')
        if len(kv) == 2:
            d[kv[0]] = float(kv[1])
    f.close()
    return d


def read_words(input_file):
    ''' read words file '''
    w = []
    f = open(input_file, 'r')
    for line in f.readlines():
        word = line.strip()
        if word:
            w.append(word)
    f.close()
    return w


def read_keyboard(keyboard_file):
    ''' read keyboard file '''
    d = {}
    f = open(keyboard_file, 'r')
    for line in f.readlines():
        letters = line.strip().split(' ')
        letter = letters.pop(0)
        d[letter] = letters
    f.close()
    return d


def correct_words(d, w, k):
    ''' correct words '''
    for word in w:
        freq = []
        if word in d:
            print('%15s -> FOUND' % word)
        else:
            freq.extend(drop(word, d))
            freq.extend(insert(word, d))
            freq.extend(swap(word, d))
            freq.extend(replace(word, d, k))
            # sort result
            freq.sort(reverse=True)
            freq = freq[:3]
            # display result
            if len(freq) == 0:
                print('%15s -> NOT FOUND' % word)
            else:
                words = []
                for f in freq:
                    if f[1] not in words:
                        words.append(f[1])
                print('%15s -> FOUND  %d:  %s' % (word, len(freq), ' '.join(words)))


def drop(word, d):
    ''' try drop '''
    freq = []
    for i in range(len(word)):
        w = word[:i] + word[i + 1:]
        if w in d:
            freq.append((d[w], w))
    return freq


def insert(word, d):
    ''' try insert '''
    freq = []
    for i in range(len(word) + 1):
        for j in range(97, 123):
            ch = chr(j)
            w = word[:i] + ch + word[i:]
            if w in d:
                freq.append((d[w], w))
    return freq


def swap(word, d):
    ''' try swap '''
    freq = []
    for i in range(len(word) - 1):
        w = word[:i] + word[i + 1] + word[i] + word[i + 2:]
        if w in d:
            freq.append((d[w], w))
    return freq


def replace(word, d, k):
    ''' try replace '''
    freq = []
    for i in range(len(word)):
        for r in k[word[i]]:
            w = word[:i] + r + word[i + 1:]
            if w in d:
                freq.append((d[w], w))
    return freq

if __name__ == '__main__':
    dictionary_file = input('Dictionary file => ').strip()
    print(dictionary_file)
    input_file = input('Input file => ').strip()
    print(input_file)
    keyboard_file = input('Keyboard file => ').strip()
    print(keyboard_file)

    d = read_dictionary(dictionary_file)
    w = read_words(input_file)
    k = read_keyboard(keyboard_file)
    correct_words(d, w, k)
