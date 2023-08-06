import random
# print(random.randint(1, 10))

# coin = random.choice(  ["heads", "tails"]  ) 
# print(coin)

cards = ["Jack", "Queen", "King", "Ace"]
random.shuffle(cards)
for card in cards:
    print(card)


 