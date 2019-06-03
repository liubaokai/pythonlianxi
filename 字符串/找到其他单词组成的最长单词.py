class LongestWord():
    def find_str(self, str_array, strs):
        i = 0
        while i < len(str_array):
            if strs == str_array[i]:
                return True
            i += 1
        return False

    def is_contain(self, str_array, word, length):
        lens = len(word)
        if lens == 0:
            return True
        i = 1
        while i <= lens:
            if i == length:
                return False
            strs = word[0:i]
            if self.find_str(str_array, strs):
                if self.is_contain(str_array, word[i:], length):
                    return True
            i += 1
        return False

    def getLongest(self, str_array):
        str_array = sorted(str_array, key=len, reverse=True)
        i = 0
        while i < len(str_array):
            if self.is_contain(str_array, str_array[i], len(str_array[i])):
                return str_array[i]
            i += 1
        return None
