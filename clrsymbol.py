def clearSymbols(allwords):
    withoutsymbols=[]
    symbols="!''^+%&/*+()=?_;-,.@\"\"<>:.[]{}½$#£|"
    for word in allwords:
        for symbol in symbols:
            if symbol in word:
                word=word.replace(symbol,"")

        if (len(word)>0):
            withoutsymbols.append(word)
    return withoutsymbols