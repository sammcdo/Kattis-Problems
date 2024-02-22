class Trie:
    def __init__(self):
        self.children = {}

    def add(self, word):
        current_dict = self.children
        for letter in word:
            current_dict = current_dict.setdefault(ord(letter), {})
        if ord('_') in current_dict:
            current_dict[ord('_')] += 1
        else:
            current_dict[ord('_')] = 1

    def starts_with(self, prefix, rev=False):
        '''
        Returns a list of all words beginning with the given prefix, or
        an empty list if no words begin with that prefix.
        '''
        words = list()
        current = self.children
        t = ""
        for char in prefix:
            if ord(char) not in current:
                # Could also just return words since it's empty by default
                return list()
            current = current[ord(char)]
            if rev:
                t = char + t

        # Step 2
        if rev:
            self.__child_words_for(current, words, t, rev=True)
        else:
            self.__child_words_for(current, words, prefix)
        return words

    def __child_words_for(self, current, words, stem, rev=False):
        if ord('_') in current:
            if current[ord('_')] > 1:
                words.extend([stem]*current[ord('_')])
            else:
                words.append(stem)
        for letter in current:
            if chr(letter) != '_':
                if rev:
                    self.__child_words_for(current[letter], words, chr(letter) + stem, rev=True)
                else:
                    self.__child_words_for(current[letter], words, stem+chr(letter))


words = Trie()

for i in range(int(input())):
    word = input()

    words.add(word)

    print(len(words.starts_with(word))-1)