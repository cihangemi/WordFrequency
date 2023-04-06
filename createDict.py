def wordCounter(allwords):
    wordCount = {}

    for word in allwords:
        if word in wordCount:
            wordCount[word] += 1
        else:
            wordCount[word] = 1
    return wordCount
