# -*- coding: utf-8 -*-
# @Time : 2022/7/3 17:58
# @Author : ZZZZZHHHHH
# @FileName: 1.1.py
# @Software: PyCharm

import collections

Card = collections.namedtuple('Card',['rank','suit'])
class FrenchDeck:
    ranks = [str(n) for n in range(2,11)]+list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    def  __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self,position):
        return self._cards[position]
