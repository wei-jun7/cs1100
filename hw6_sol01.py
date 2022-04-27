def clean_word(word):
    ''' clean word, remove non alphabet character '''
    cleaned_word = ''
    for ch in word.lower():
        if ch.isalpha():
            cleaned_word += ch
    return cleaned_word


def parsing_file(filename, stop_words):
    ''' parsing file words '''
    words = []
    f = open(filename, 'r')
    for line in f.readlines():
        for word in line.split(' '):
            word = clean_word(word)
            # word not empty and not stop words
            if word and word not in stop_words:
                words.append(word)
    f.close()
    return words


def load_stop_word():
    ''' load stop words '''
    stop_words = set()
    f = open('stop.txt', 'r')
    for line in f.readlines():
        stop_words.add(clean_word(line.strip()))
    f.close()
    return stop_words


def calculate_average_word_length(words):
    ''' Q1 '''
    total = 0.0
    for word in words:
        total += len(word)
    average = total / len(words)
    print('1. Average word length: %.2f' % round(average, 2))
    return average


def calculate_distinct_word(words):
    ''' Q2 '''
    ratio = round(len(set(words)) / len(words), 3)
    print('2. Ratio of distinct words to total words: %.3f' % ratio)
    return ratio


def calculate_length_of_words(words, filename):
    ''' Q3 '''
    print('3. Word sets for document', filename + ":")
    d = {}
    max_length = 0
    for word in words:
        length = len(word)
        # create set
        if length not in d:
            d[length] = set()
        # update max length
        if length > max_length:
            max_length = length
        # add word
        d[length].add(word)
    # print result
    for i in range(1, max_length + 1):
        length = 0
        if i in d:
            length = len(d[i])
        print('%4d:%4d:' % (i, length), end='')
        if length != 0:
            words = list(d[i])
            words.sort()
            if len(words) <= 6:
                for word in words:
                    print(' ' + word, end='')
            else:
                print(' {} {} {} ... {} {} {}'.format(words[0], words[1], words[2], words[-3], words[-2], words[-1]), end='')
        print()
    return d, max_length


def create_pair(word1, word2):
    if word1 < word2:
        return (word1, word2)
    else:
        return (word2, word1)


def find_distinct_word_pairs(words, maximum_separation, filename):
    ''' Q4 '''
    print('4. Word pairs for document', filename)
    pairs = set()
    for i in range(len(words)):
        word = words[i]
        # find pairs
        for j in range(i - maximum_separation, i + maximum_separation + 1):
            if j >= 0 and j < len(words) and word != words[j]:
                pairs.add(create_pair(word, words[j]))
    print('  {} distinct pairs'.format(len(pairs)))
    pairs = list(pairs)
    pairs.sort()
    # print result
    if len(pairs) <= 10:
        for pair in pairs:
            print('  {} {}'.format(pair[0], pair[1]))
    else:
        print('  {} {}'.format(pairs[0][0], pairs[0][1]))
        print('  {} {}'.format(pairs[1][0], pairs[1][1]))
        print('  {} {}'.format(pairs[2][0], pairs[2][1]))
        print('  {} {}'.format(pairs[3][0], pairs[3][1]))
        print('  {} {}'.format(pairs[4][0], pairs[4][1]))
        print('  ...')
        print('  {} {}'.format(pairs[-5][0], pairs[-5][1]))
        print('  {} {}'.format(pairs[-4][0], pairs[-4][1]))
        print('  {} {}'.format(pairs[-3][0], pairs[-3][1]))
        print('  {} {}'.format(pairs[-2][0], pairs[-2][1]))
        print('  {} {}'.format(pairs[-1][0], pairs[-1][1]))
    ratio = round(len(pairs) / len(pairs), 3)
    print('5. Ratio of distinct word pairs to total: %.3f' % ratio)
    return ratio


if __name__ == '__main__':
    first_file = input('Enter the first file to analyze and compare ==> ')
    print(first_file)
    second_file = input('Enter the second file to analyze and compare ==> ')
    print(second_file)
    maximum_separation = int(input('Enter the maximum separation between words in a pair ==> '))
    print(maximum_separation)
    stop_words = load_stop_word()
    first_words = parsing_file(first_file, stop_words)
    second_words = parsing_file(second_file, stop_words)
    
    print('\nEvaluating document ' + first_file)
    a1 = calculate_average_word_length(first_words)
    r1 = calculate_distinct_word(first_words)
    d1, m1 = calculate_length_of_words(first_words, first_file)
    p1 = find_distinct_word_pairs(first_words, maximum_separation, first_file)
    
    print('\nEvaluating document ' + second_file)
    a2 = calculate_average_word_length(second_words)
    r2 = calculate_distinct_word(second_words)
    d2, m2 = calculate_length_of_words(second_words, second_file)
    p2 = find_distinct_word_pairs(second_words, maximum_separation, second_file)

    print('Summary comparison')
    if a1 >= a2:
        print('1. {} on average uses longer words than {}'.format(first_file, second_file))
    else:
        print('1. {} on average uses longer words than {}'.format(second_file, first_file))
    print('2. Overall word use similarity: %.3f' % abs(r1 - r2))
    print('3. Word use similarity by length:')
    i = 1
    while i <= max(m1, m2):
        similarity = 0
        if i in d1 and i in d2:
            similarity = len(d1[i] & d2[i]) / len(d1[i] | d2[i])
        print('%4d: %.4f' % (i, similarity))
        i += 1
