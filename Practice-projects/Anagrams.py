from collections import defaultdict

def anagram_using_defaultdic(words):
    anagram_dic =defaultdict(list)
    for w in words:

        key = "".join(sorted(w)) 
        anagram_dic[key].append(w) 
    print(anagram_dic)  

def anagram_without_defaultdic(words):
    anagram_dic = {}
    for w in words:
        key = ''.join(sorted(w))
        if key not in anagram_dic.keys():
            anagram_dic[key] = []
            anagram_dic[key].append(w) 
        else:
            anagram_dic[key].append(w) 
    print(anagram_dic) 

words = ["tea", "eat", "bat", "ate", "arc", "car"]
anagram_1 = anagram_using_defaultdic(words)
print()
anagram_2 = anagram_without_defaultdic(words) 
