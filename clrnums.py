def clearNums(allwords):
    withoutnums=[]
    nums="0123456789"
    for word in allwords:
        for num in nums:
            if num in word:
                word=word.replace(num,"")

        if (len(word)>0):
            withoutnums.append(word)
    return withoutnums