import random;


class Character_Demo:
    BODY_PARTS = ["Head", "Torso", "Left hand", "Right hand", "Legs"]
    health = 100
    health_shield = 100
    state = False

    def __init__(self, name, race):
        self.name = name
        self.race = race

    def hit(self, target):
        if target == 0:
            self.health -= 15
        elif target == 1:
            self.health -= 10
        elif 2 <= target <= 3:
            self.health -= 5
        elif target == 4:
            self.health -= 15

    def attack(self, enemy):
        if self.target != enemy.block_part:
            enemy.hit(self.target)

    def choice_target(self, target):
        self.target = target

    def body_block(self, block_part):
        self.block_part = block_part

    # user: test0
    # passwd: asdfgh12345
    #
    # test1
    # zxcvbn12345
    #
    # test2
    # poiuy09876

    #test3
    #lkjhg54321

    #test4
    #

    #test5
    #789456123q

    #test6
    #123456789q

    #test7
    #qazwsxedc123

    #test8
    #edcrfv456

    #test9
    #tgbyhn789

    #test10
    #q1w2e3r4





















# orc = Character_Demo ("Carl","orc")
# name = input ("Whats your name?:")
# race = input ("Input race:")
# player = Character_Demo (name,race)
# exit = False
# while True:
# 	if (player.health <=0) or (orc.health<=0) or (exit):
# 		print("GameOver")
# 		break
# 	else:
# 		target = input("Choose target attack: ")
# 		block_part = input("Choose your block part")

# 		if target == "Exit" or block_part == "Exit":
# 			exit = True
# 		else:
# 			orc.choice_target(random.randint(0,4))
# 			orc.body_block(random.randint(0,4))
# 			player.choice_target(Character_Demo.BODY_PARTS.index(target))
# 			player.body_block(Character_Demo.BODY_PARTS.index(block_part))
# 			orc.attack(player)
# 			player.attack(orc)
# 		print("Player")
# 		print("Target:",player.BODY_PARTS[player.target])
# 		print("Block:",player.BODY_PARTS[player.block_part])
# 		print("Health:", player.health)
# 		print("Orc")
# 		print("Target:",orc.BODY_PARTS[orc.target])
# 		print("Block:",orc.BODY_PARTS[orc.block_part])
# 		print("Health:", orc.health)
