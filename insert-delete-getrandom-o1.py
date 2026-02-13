import random


class RandomizedSet:
    def __init__(self):
        self.data_hash_map = {}
        self.data_list = []

    def insert(self, val):
        if val in self.data_hash_map:
            return False
        self.data_hash_map[val] = len(self.data_list)
        self.data_list.append(val)
        return True

    def remove(self, val):
        if val not in self.data_hash_map:
            return False
        to_be_deleted_idx = self.data_hash_map[val]
        self.data_list[to_be_deleted_idx] = self.data_list[-1]

        self.data_hash_map[self.data_list[-1]] = to_be_deleted_idx
        self.data_list.pop()
        del self.data_hash_map[val]
        return True
    def get_random(self):
        return random.choice(self.data_list)
