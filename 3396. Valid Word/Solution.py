class Solution:
    def isValid(self, word: str) -> bool:

        if len(word) < 3:
            return False
        #if not word.isalnum():
        #    return False


        vowels = set("aeuoiAEUOI")
        digits = set("0123456789")
        consonants = set("bcdfghjklmnpqrstvwxyzBCDEFGHJKLMNPQRSTVWXYZ")

        has_vowel = False
        has_consonant = False

        for letter in word:
            if letter in vowels:
                has_vowel = True
            elif letter in consonants:
                has_consonant = True
            elif letter not in digits:
                return False
        #print(has_vowel, has_consonant)

        return has_vowel and has_consonant

        