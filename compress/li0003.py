with open('english10k.txt') as f:
    Standard_Dictionary = [l.strip() for l in f]

def compress(text):
    return compress_with_dict(text, Standard_Dictionary)

def compress_with_dict(text, dict):
    punctuation = [',', '...', '.', '!', '?', ':']
    buf = []
    for word in text.split():
        egg = False
        for punk in punctuation:
            if punk in word:
                word = word.rstrip(punk)
                egg = True
                end = punk
        if word in dict:
            i = dict.index(word)
            token = '\0' + str(i)
        elif word.lower() in dict and word[1:].islower():
            i = dict.index(word.lower())
            token = '\u2603' + str(i)
        else:
            token = word
        if egg == True:
            token = token + end
        buf.append(token)
    compressed = ' '.join(buf)
    return compressed

def decompress(compressed):
    return decompress_with_dict(compressed, Standard_Dictionary)

def decompress_with_dict(compressed, dict):
    punctuation = [',', '...', '.', '!', '?', ':']
    buf = []
    text = compressed.split()
    for word in text:
        egg = False
        for punk in punctuation:
            if punk in word:
                word = word.rstrip(punk)
                egg = True
                end = punk
        if '\u2603' in word:
            temp = word[1:]
            new = dict[int(temp)]
            firstLetter = new[0]
            new = new.replace(firstLetter, firstLetter.upper())
        elif '\x00' in word:
            temp = word[1:]
            new = dict[int(temp)]
        else:
            new = word
        if egg == True:
            new += end
        buf.append(new)
    result = ' '.join(buf)
    return result

