words = ['sad','shit','hello','yes','nothing','every','boom']
wordDict = {}
for i in range(1,len(words)):
    if words[i-1] not in wordDict:
         #为单词新建一个辞典
        wordDict[words[i-1]] = {}
    if words[i] not in wordDict[words[i-1]]:
        wordDict[words[i-1]][words[i-1]] = 0
        wordDict[words[i-1]][words[i]] = wordDict[words[i-1]][words[i]] + 1
print(wordDict)
