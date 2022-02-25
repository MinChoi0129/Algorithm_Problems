class PPAP:
    default_PPAP_strings = [['P', 'P', 'A', 'P'], ['P']]
    
    def __init__(self, text : str):
        self.text = text
    
    def isPPAP(self):
        check_list = []
        for char in self.text:
            check_list.append(char)
            if check_list[-4:] == PPAP.default_PPAP_strings[0]:
                for _ in range(3): check_list.pop()
                
        return True if check_list in PPAP.default_PPAP_strings else False

print("PPAP" if PPAP(input()).isPPAP() else "NP")