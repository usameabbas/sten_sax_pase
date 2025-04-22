import random

class StenSaxPase:
    def __init__(self):
        self.alternativ = ["sten", "sax", "påse"]
        self.spelarens_poäng = 0
        self.datorns_poäng = 0

    def datorns_val(self):
        return random.choice(self.alternativ)

    def avgör_vinnare(self, spelarens_val, datorns_val):
        if spelarens_val == datorns_val:
            return "Oavgjort!"
        elif (spelarens_val == "sten" and datorns_val == "sax") or \
             (spelarens_val == "sax" and datorns_val == "påse") or \
             (spelarens_val == "påse" and datorns_val == "sten"):
            self.spelarens_poäng += 1
            return "Du vann!"
        else:
            self.datorns_poäng += 1
            return "Du förlorade!"