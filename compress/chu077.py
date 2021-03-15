with open('english10k.txt') as f:
    dictionary = [l.strip() for l in f]

def remove_pun(text):
    text = text.split()
    new_text = []
    for each_word in text:
        full_stop = 0
        comma = 0
        hyphen = 0
        all_upper = 0
        first_upper = 0
        if each_word.isupper():
            all_upper = 1
        elif each_word[:1].isupper() and len(each_word) != 1:
            first_upper = 1
# Make a note of where there is a capital charater or a punctuation
        for each_charater in each_word:
            if each_charater == '.':
                full_stop = 1
            elif each_charater == ',':
                comma = 1
# Changing the hyphens make it longer for some reason
            elif each_charater == '-':
                hyphen = 1
                x = each_word.index('-')
        if all_upper == 1:
            each_word = '~'+ each_word.lower()
        elif first_upper == 1:
            each_word = '`'+ each_word.lower()

        if full_stop == 1:
            new_text.append(each_word[:-1])
            new_text.append('//')
        elif comma == 1:
            new_text.append(each_word[:-1])
            new_text.append('///')
        # elif hyphen == 1:
        #     new_text.append(each_word[0:x])
        #     new_text.append('////')
        #     new_text.append(each_word[x+1:])
        else:
            new_text.append(each_word)
    return new_text

def compress(text):
    buf = []
    new_text = remove_pun(text)
# Store the words without capitals and punctuation
    for word in new_text:
        #print(word)
        if word[:1] == '`'or word[:1] == '~':
            if word[1:] in dictionary:
                i = dictionary.index(word[1:])
                if i == 10 or i == 11 or i == 12 or i == 13 or i == 96 or i == 126:
                    i += 10000
                token = '\0' + word[:1] + chr(i)
                buf.append(token)
            else:
                buf.append(word)
        elif word in dictionary:
            i = dictionary.index(word)
            if i == 10 or i == 11 or i == 12 or i == 13 or i == 96 or i == 126:
                i += 10000
            token = '\0' + chr(i)
            buf.append(token)
        else:
            buf.append(word)

# Turning the notes back in to what they are before
    for x in range (len(buf)):
        try:
            if buf[x+1] == '//':
                buf[x] = buf[x]+'.'
                buf.pop(x+1)
            elif buf[x+1] == '///':
                buf[x] = buf[x]+','
                buf.pop(x+1)
            elif buf[x+1] == '////':
                buf[x] = buf[x]+'-'+ buf[x+2]
                buf.pop(x+1)
        except IndexError:
            pass
    compressed = ' '.join(buf) 
    return compressed

def decompress(text):
    text = text.split()
    new_text = []
    for x in range (0,len(text)):
        if '\x00' in text[x]:
            try:
                if text[x] == '\x00,':
                    word = dictionary[44]
                elif (text[x][1] == '`' or text[x][1] == '~') and (text[x][-1] == '.' or text[x][-1] == ','):
                    i = ord(text[x][2])
                    if i > 10000:
                        i -= 10000
                    word = text[x][1] + dictionary[i] + text[x][3]
                elif (text[x][1] == '`' or text[x][1] == '~'):
                    i = ord(text[x][2])
                    if i > 10000:
                        i -= 10000
                    word = text[x][1] + dictionary[i]
                elif text[x][-1] == '.' or text[x][-1] == ',':
                    i = ord(text[x][1])
                    if i > 10000:
                        i -= 10000
                    word = dictionary[i] + text[x][-1]
                else:
                    i = ord(text[x][1])
                    if i > 10000:
                        i -= 10000
                    word = dictionary[i]
            except IndexError:
                pass
            new_text.append(word)
        else:
            new_text.append(text[x])

# Changing the words back to uppercase if needed
    for x in range (0,len(new_text)):
        if new_text[x][0] == '`':
            new_text[x] = new_text[x][1].upper() + new_text[x][2:]
        elif new_text[x][0] =='~':
            new_text[x] = new_text[x][1:].upper()
    compressed = ' '.join(new_text)
    return compressed

def test(text):
    compressed = compress(text)
    decompressed = decompress(compressed)
    assert text == decompressed

def stats(text):
    compressed = compress(text)
    compression_ratio = 100 * len(compressed) / len(text)

    cprint('––---------------------------------------------------','blue')
    cprint(f'{len(compressed)} / {len(text)} ➞  {compression_ratio:.1f}%', 'green', 'on_red', attrs = ['bold'])
    cprint('––---------------------------------------------------','blue')

