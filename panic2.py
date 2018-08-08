phrase = "don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

#for i in range(4):
#    plist.pop()
#plist.remove('d')
#plist.remove("'")
#plist.extend([plist.pop(),plist.pop()])
#plist.insert(2, plist.pop(3))

Newphrase = ''.join(plist[1:3:1]) + ''.join([plist[5],plist[4],plist[7],plist[6]
                                             ])
#print(Nlist)
#new_prase = ''.join(Nlist)
print(Newphrase)

