text = "mang kasir aplikasi sederhana"

word_count = 0
char_count = 0
in_word = False

for ch in text:
    if ch != ' ':
        char_count += 1
        if not in_word:
            word_count += 1
            in_word = True
    else:
        in_word = False

print("Words:", word_count)
print("Characters (no spaces):", char_count)