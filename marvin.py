paranoid = "Marvin, the parnaoid andriod"
letter = list(paranoid)
for char in letter[:10]:
    print('\t', char)

for char in letter[-7:]:
    print('\t'*2, char)

for char in letter[12:20]:
    print('\t'*3, char)
