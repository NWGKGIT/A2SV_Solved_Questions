class FrequencyTracker:
    def __init__(self):
        self.freqmap = {} 
        self.counts = {} 
    def add(self, number: int) -> None:
        f = self.freqmap.get(number, 0)
        
        if f > 0:
            self.counts[f] -= 1
        
        self.freqmap[number] = f + 1
        self.counts[f + 1] = self.counts.get(f + 1, 0) + 1

    def deleteOne(self, number: int) -> None:
        f = self.freqmap.get(number, 0)
        if f > 0:
            self.counts[f] -= 1
            self.freqmap[number] = f - 1
            if f - 1 > 0:
                self.counts[f - 1] = self.counts.get(f - 1, 0) + 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.counts.get(frequency, 0) > 0