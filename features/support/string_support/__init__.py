class ExtStr(str):
    def is_include(self, string):
        if string in self:
            return True
        else:
            return False
