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
graceful precision. CLOSEUP - MAN, his facial features
reiterate the power of his body and are dominated by the
eyes, which are intense, blue and depthless. His hair is
military short. This man is the TERMINATOR.'''




with open('english10k.txt') as f:
    dictionary = [l.strip() for l in f]



def processor (word):
    suffix = ''
    origin = word
    if len(word)>1:
        if word.isupper():
            word = word.lower()
            suffix = suffix + "#"
        elif word[0].isupper():
            word = word.lower()
            suffix = suffix + "^"
    
    if ','in word or '.' in word:
        suffix = suffix + word[-1]
        word = word[0:len(word)-1]

    if word in dictionary:
        i = dictionary.index(word)
        token = '\0' + str(i) + suffix 
        if len(token) > len(origin):
            token = origin

    else:
        token = origin
    buf.append(token)

    
    

buf = []
for word in original.split():
    processor(word)

compressed = ' '.join(buf)
 
compression_ratio = 100 * len(compressed) / len(original)

print(original)
print('––')
print(compressed)
print('––')
print(f'{len(compressed)} / {len(original)} ➞ {compression_ratio:.1f}%')

