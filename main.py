import asyncio
import random
from Toads import BasicToad, Assassin, Adventurer, Craftsman, Fatality


async def conduct_battles(num_battles):
    victories_toad1 = 0
    victories_toad2 = 0

    for _ in range(num_battles):
        toad1 = random.choice([BasicToad(), Assassin(), Adventurer(), Craftsman(), Fatality()])
        toad2 = random.choice([BasicToad(), Assassin(), Adventurer(), Craftsman(), Fatality()])

        toad1.health = toad1.health
        toad2.health = toad2.health

        winner = await toad1.battle(toad2)
        if winner == 1:
            victories_toad1 += 1
        else:
            victories_toad2 += 1

    return victories_toad1, victories_toad2


async def main():
    battles = 100
    results1 = conduct_battles(battles)
    results2 = conduct_battles(battles)

    victories1, victories2 = await asyncio.gather(results1, results2)

    print(f"Победы первой жабы: {victories1[0] + victories2[0]}")
    print(f"Победы второй жабы: {victories1[1] + victories2[1]}")


if __name__ == "__main__":
    asyncio.run(main())
