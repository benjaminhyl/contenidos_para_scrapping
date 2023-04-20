from dataclasses import dataclass


@dataclass
class DataClassCard:
    rank: str
    suit: str


reina = DataClassCard("12", "trebol")
# print(reina.rank)
# print(type(DataClassCard("12", "trebol")))
# print(type(reina))
# print(reina == DataClassCard("12", "trebol"))


class RegularCard:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit


queen_of_hearts = RegularCard('Q', 'Hearts')
print(queen_of_hearts.rank)

print(queen_of_hearts)

print(queen_of_hearts == RegularCard('Q', 'Hearts'))
