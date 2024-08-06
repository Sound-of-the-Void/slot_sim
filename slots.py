import random

class Slot_machine:
    def __init__(self, NumReel, DictWin):
        self.reels = [[i for i in range(10)]] * NumReel
        self.wins = DictWin

    def spin_slot(self):
        spin_result = ''
        for reel in self.reels:
            spin_result += str(random.choice(reel))
            print(spin_result)
        return spin_result

    def spin_simulation(self, spinCount, potAmt, betAmt):
        self.spinCount, self.potAmt, self.betAmt = spinCount, potAmt, betAmt
        jackpots = 0
        startingPot = potAmt
        totalPaid = 0
        winSpins = 0

        for i in range(self.spinCount):
            potAmt += betAmt
            currSpin = self.spin_slot()
            hits = [item for item in self.wins.keys() if item in currSpin]
            if hits:
                multiplier = self.wins[max(hits)]
                payout = (betAmt * multiplier)
                potAmt -= payout
                totalPaid += payout
                winSpins += 1
                if multiplier == self.wins[max(self.wins.keys())]:
                    jackpots += 1

        returnToPlayer = float(f"{totalPaid / (betAmt * spinCount)}")
        profit = potAmt - startingPot

        if totalPaid == 0:
            profit = f"{float(profit):,.2f}"
            return f"{winSpins} wins/{spinCount} запусков.  Казино в выигрыше на: {profit}. RTP: 0.0"
        if profit > 0:
            profit = f"{float(profit):,.2f}"
            return f"{winSpins} wins/{spinCount} запусков.  Казино в выигрыше на: {profit}.  " \
                   f"RTP: {returnToPlayer:.2f}"
        elif profit < 0:
            profit = f"{float(profit):,.2f}"
            profit = str(profit).replace("-", "-$")
            return f"{winSpins} wins/{spinCount} запусков.  Казино в проигрыше на: {profit}. " \
                   f"RTP: {returnToPlayer:.2f}"
        else:
            return f"{winSpins} wins/{spinCount} запусков.  Все остались при своём: {profit}. " \
                   f"RTP: {returnToPlayer:.2f}"


slot1 = Slot_machine(3, {'777': 200, '888': 100, '999': 90, '666': 80, '555': 70, '444': 60,
                    '333': 50, '222': 40, '111': 30, '000': 666})

# print(slot1.reels)
# print(slot1.wins)
print(slot1.spin_simulation(40000, 200000, 5))