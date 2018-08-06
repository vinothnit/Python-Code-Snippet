word = "bottles"
for i in range(99,0,-1):
    if i == 1:
        word = "bottle"        
        print(i, word, "of beers on the wall.")
        print(i, word, "of beers.")
        print("Take one down.")
        print("Pass it around.")
        count = i - 1
        print(count, word, "of beers on the wall.")
    else:
        print(i, word, "of beers on the wall.")
        print(i, word, "of beers.")
        print("Take one down.")
        print("Pass it around.")
        count = i - 1
        if count == 1:
                word = "bottle"
                print(count, word, "of beers on the wall.")
        else:
                print(count, word, "of beers on the wall.")

    print()

