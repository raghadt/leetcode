class Solution:
    def removeVowels(self, S: str) -> str:
        chars_to_remove = ['a','e','o','i','u'] #-- Create list of vowel
        set_char = set(chars_to_remove)
        new_S = "".join([c for c in S if c not in set_char])
        return new_S