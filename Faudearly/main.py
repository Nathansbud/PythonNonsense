import os
import random

num_poems = 4
with open(os.path.join(os.path.dirname(__file__), "data", "dirtyprettythings.txt"), 'r+') as fl:
    lines = [l.strip() for l in fl.readlines()]

def get_poems(count):
    poems = []
    start = 0
    for i, line in enumerate(lines):
        if line == "~": start = i
        if line == "|":
            end = i
            poems.append(lines[start + 1:end])
    return random.choices(poems, k=count)

def generate_faudet(poems, n_per):
    build_poem = ""
    if len(poems) > 0:
        build_poem += poems[0][0].strip()+"\n"
        poems[0] = poems[0][1:]
        for poem in poems:
            random.shuffle(poem)
            if n_per > len(poem):
                build_poem += "\n".join(poem)
            else:
                build_poem += "\n".join(random.sample(poem, k=n_per))
            build_poem+='\n'
    return build_poem

print(generate_faudet(get_poems(3), 2))

