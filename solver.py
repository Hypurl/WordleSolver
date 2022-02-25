import string,operator
from pathlib import Path
from collections import Counter
from itertools import chain
alchar,wl,aa=set(string.ascii_letters),5,6
wor={word.lower()for word in Path("./wordlewo.txt").read_text().splitlines()if len(word)==wl and set(word)<alchar} #wordlewo.txt
lc=Counter(chain.from_iterable(wor))
lf={character: value/sum(lc.values())for character,value in lc.items()}
def sbwc(words):return sorted([(word,cwc(word))for word in words],key=operator.itemgetter(1),reverse=True)
def dwt(worcc):
    for(word,freq)in worcc:print(f"{word:<10} | {freq:<5.2}")
def cwc(word):
    score=0.0
    for char in word:score+=lf[char]
    return score/(wl-len(set(word))+1)
def input_word():
    while True:
        word=input("Input the word you entered> ")
        if len(word)==wl and word.lower()in wor:break
    return word.lower()
def mwv(word,wv):
    assert len(word)==len(wv)
    for letter,v_letter in zip(word,wv):
        if letter not in v_letter:return False
    return True
def inpres():
    while True:
        resp=input("Type the color-coded reply from Wordle:\n  G for Green\n  Y for Yellow\n  ? for Gray\nResponse from Wordle> ")
        if len(resp)==wl and set(resp)<={"G","Y","?"}:break
        else:print(f"Error - invalid answer {resp}")
    return resp
def match(wv,pw):return [word for word in pw if mwv(word, wv)]
def solve():
    pw,wv=wor.copy(),[set(string.ascii_lowercase)for _ in range(wl)]
    for attempt in range(1,aa + 1):
        print(f"Attempt {attempt} with {len(pw)} possible words")
        dwt(sbwc(pw)[:15])
        word,resp=input_word(),inpres()
        for idx,letter in enumerate(resp):
            if letter=="G":wv[idx]={word[idx]}
            elif letter=="Y":
                try:wv[idx].remove(word[idx])
                except KeyError:pass
            elif letter=="?":
                for vector in wv:
                    try:vector.remove(word[idx])
                    except KeyError:pass
        pw=match(wv,pw)
solve()
