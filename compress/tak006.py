with open('english10k.txt') as f:
    dictionary = [l.strip() for l in f]

punctuation = ['.', ',', ';', '-']

buf = []

def punc(t):
    for x in range(len(punctuation)):
        if punctuation[x] in t:
            if punctuation[x] == '-':
                return t.split("-")
            return [t.rstrip(punctuation[x])]
    return [t]

def compress(t):
    for word in t.split():
        for sub_word in punc(word):
            if sub_word.lower() in dictionary and not sub_word.isdigit():
                i = dictionary.index(sub_word.lower()) + 1
                token = chr(i)
                buf.append(token)
            else:
                buf.append("0" + sub_word + "0")
    return ''.join(buf)

def toggle(bole):
    if bole:
        return False
    return True 

def decompress(t):
    thing = False
    final_text = ''
    i = 0
    for x in t:
        if x == '0':
            thing = toggle(thing)
            if not thing:
                final_text += ' '
        elif thing:
            final_text += t[i]
        else:
            if dictionary[(ord(x)) -1] == 'will':
                print([x], ord(x) -1, "test")
            final_text += dictionary[(ord(x)) -1] + " "
        i += 1
    return final_text

if __name__ == '__main__':
    original = '''Silence. Gradually the sound of distant traffic
    becomes audible. A LOW ANGLE bounded on one side by a
    chain-link fence and on the other by the one-story public
    school buildings. Spray-can hieroglyphics and distant
    streetlight shadows. This is a Los Angeles public school in
    a blue collar neighborhood. SLOW PAN as the sound of stray
    electrical CRACKLING subsides. FRAME comes to rest on the
    figure of a NAKED MAN kneeling, faced away, in the
    previously empty yard. He stands, slowly. The man is in his
    late thirties, tall and powerfully built, moving with
    graceful precision. CLOSE UP - MAN, his facial features
    reiterate the power of his body and are dominated by the
    eyes, which are intense, blue and depthless. His hair is
    military short. This man is the TERMINATOR.'''


    compressed = compress(original)
    decompressed = decompress(compressed)

    compression_ratio = 100 * len(compressed) / len(original)

    print(f'{len(compressed)} / {len(original)} ➞ {compression_ratio:.1f}%')
    print(decompressed)
