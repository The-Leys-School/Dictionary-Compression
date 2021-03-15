#from termcolor import cprint

original = "Silence. Gradually the sound of distant traffic becomes audible. A LOW ANGLE bounded on one side by a chain-link fence and on the other by the one-story public school buildings. Spray-can hieroglyphics and distant streetlight shadows. This is a Los Angeles public school in a blue collar neighborhood. SLOW PAN as the sound of stray electrical CRACKLING subsides. FRAME comes to rest on the figure of a NAKED MAN kneeling, faced away, in the previously empty yard. He stands, slowly. The man is in his late thirties, tall and powerfully built, moving with graceful precision. CLOSEUP - MAN, his facial features reiterate the power of his body and are dominated by the eyes, which are intense, blue and depthless. His hair is military short. This man is the TERMINATOR."

with open('english10k.txt') as f:
    dictionary = [l.strip() for l in f]

def compress (text):
    buf = []
    for word in text.split():
        suffix = ''
        if word.isupper():
            suffix = suffix + '#'
        elif word[0].isupper():
            suffix = suffix + '!'
        word = word.lower()
        if ',' in word or '.' in word:
                suffix = suffix + word[-1]
                word = word[0:len(word)-1]
        if word == '-':
            suffix = suffix + '?'
        if word in dictionary:
            i = dictionary.index(word)
            if i == 10 or i == 11 or i == 12:
                buf.append(word + suffix)
            else:
                token = '\0' + str(chr(i)+ suffix)
                buf.append(token)
        else:
            buf.append(word + suffix)
    compressed = ' '.join(buf)
    return compressed


def decompress(text):
    ded = text.split()
    new = []
    for word in ded:
        flag1 = True
        flag2 = True
        punc = ''
        if len(word)>2 and (',' in word or '.' in word):
            punc = word[-1]
            word = word[0:len(word)-1]
        if '#' in word:
            flag1 = False
            word = word[0:len(word)-1]
        elif '!' in word:
            flag2 = False
            word = word[0:len(word)-1]
        if '?' in word:
            i = word[0]
        elif not word[0].isalpha():
            if '\0' in word:
                word = word[1:]
            i = dictionary[(ord(word))] 
        else:
            i = word
        if flag1 == False:
            i = i.upper()
        elif flag2 == False:
            i = i.capitalize()
        i = i + punc
        new.append(i)

    ace = ' '.join(new)
    return ace

def test (text):
     data = compress(text)
     assert len(data) < len(text)
     text2 = decompress (data)
     assert text2 == text

if __name__ == '__main__':
    print (decompress(compress(original)))

    compression_ratio = 100 * len(compress(original)) / len(original)

    cprint(original,'cyan')
    cprint('--------------------------------------------------------------','red')
    print(compress(original))
    cprint('--------------------------------------------------------------','red')
    print(f'{len(compress(original))} / {len(original)} ➞ {compression_ratio:.1f}%')

    test(original)



