class Filecounter:
    def __init__(self, filename):
        try:
            self.file = filename
        except:
            self.text = ''

    def count_chars(self):
        text = open(self.file, 'r')
        sum = 0
        for line in text:
            formated = list(line)
            for char in formated:
                if not char:
                    formated.remove(char)
            sum += len(formated)
        text.close()
        return sum

    def count_words(self):
        text = open(self.file, 'r')
        sum = 0
        for line in text:
            formated = line.split(' ')
            for word in formated:
                if not word:
                    formated.remove(word)
            sum += len(formated)
        text.close()
        return sum

    def count_sentences(self):
        text = open(self.file, 'r')
        sum = 0
        for line in text:
            if not '.' in line:
                pass
            else:
                formated = line.split('.')
                for sent in formated:
                    if not sent:
                        formated.remove(sent)
                sum += len(formated)
        text.close()
        return sum

    def printfile(self):
        text = open(self.file, 'r')
        for line in text:
            print(line, end='')
        text.close()


examle = Filecounter('example.txt')
examle.printfile()
print()
print(examle.count_chars())
print(examle.count_words())
print(examle.count_sentences())
