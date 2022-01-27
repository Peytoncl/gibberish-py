import string
from zalgo_text import zalgo

english = string.ascii_lowercase
galactic = ["ᔑ", "ʖ", "ᓵ", "↸", "ᒷ", "⎓","⊣","⍑",'╎','⋮','ꖌ','ꖎ','ᒲ','リ','𝙹','!','¡','ᑑ','∷','ᓭ','ℸ','⚍','⍊','∴','̇/','||','⨅']

def Galactic(word):
    galacticString = ""
    for letter in word:
        if(letter == " "):
            galacticString = galacticString + letter
            continue
        galacticString = galacticString + galactic[english.index(letter)]  
    return galacticString

def Glitch(text):
    return zalgo.zalgo().zalgofy(text)

def Gibberish(word):
    return Glitch(Galactic(word))