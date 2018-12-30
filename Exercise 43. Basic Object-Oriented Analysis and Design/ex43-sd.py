# Exercise 43. Basic Object-Oriented Analysis and Design - Study Drills

from sys import exit
from random import randint
from textwrap import dedent

############################################
class Scene(object):

    def __init__(self, cheat_code):
        self.cheat_code = cheat_code

    # Override this function in Child classes    
    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

    def battle(self, alien, player):

        print(dedent(f"""
            Gothon {alien.name} has appeared!
            HP = {alien.HP}
            Level = {alien.lvl}
            
            You have {player.HP} health points."""
            ))
        
        cheat_code = input("Press enter to continue.")
        survived = False

        if (cheat_code == self.cheat_code):
            survived = True
            print("Cheat code used. Battle ignored")
            return survived
        
        while True:
            player_damage = player.attack()
            alien.get_hurt(player_damage)
            print(f"\nYou made {player_damage} damage points to that Gothon!")

            if (alien.HP <= 0):
                print("\nYou survived the encounter.")
                survived = True
                break
            
            alien_damage = alien.attack()
            player.get_hurt(alien_damage)
            print(f"{alien.name} has taken {alien_damage} HP with its attack!")

            if (player.HP <= 0):
                print("\nYou are dead.")
                survived = False
                break

            input(">")
        
        return survived


############################################
class Engine(object):   # Game controller

    def __init__(self, scene_map):
        self.scene_map = scene_map
        self.player = Player("Explorer", 100)
    
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter(self.player)
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

############################################
class Death(Scene):
    def __init__(self):
        super(Death, self).__init__("Life")

    quips = [
        "You died.  You kinda suck at this.",
        "Your Mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes."
        ]
    
    def enter(self, player):
        print(Death.quips[randint(0, len(self.quips) - 1)])
        exit(1)

############################################
class CentralCorridor(Scene):

    def __init__(self):
        super(CentralCorridor, self).__init__("You shall not pass!")

    def enter(self, player):
        print(dedent("""
            The Gothons of Planet Percal #25 have invaded your ship and
            destroyed your entire crew.  You are the last surviving
            member and your last mission is to get the neutron destruct
            bomb from the Weapons Armory, put it in the bridge, and
            blow the ship up after getting into an escape pod.

            You're running down the central corridor to the Weapons
            Armory when a Gothon jumps out, red scaly skin, dark grimy
            teeth, and evil clown costume flowing around his hate
            filled body.  He's blocking the door to the Armory and
            about to pull a weapon to blast you.
            """))
        
        action = input("> ")

        if action == "shoot!":
            print(dedent("""
                Quick on the draw you yank out your blaster and fire
                it at the Gothon.  His clown costume is flowing and
                moving around his body, which throws off your aim.
                Your laser hits his costume but misses him entirely.
                This completely ruins his brand new costume his mother
                bought him, which makes him fly into an insane rage
                and blast you repeatedly in the face until you are
                dead.  Then he eats you.
                """))
            return 'death'

        elif action == "dodge!":
            print(dedent("""
                Like a world class boxer you dodge, weave, slip and
                slide right as the Gothon's blaster cranks a laser
                past your head.  In the middle of your artful dodge
                your foot slips and you bang your head on the metal
                wall and pass out.  You wake up shortly after only to
                die as the Gothon stomps on your head and eats you.
                """))
            return 'death'

        elif action == "tell a joke" or action == self.cheat_code:
            print(dedent("""
                    Lucky for you they made you learn Gothon insults in
                    the academy.  You tell the one Gothon joke you know:
                    Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr,
                    fur fvgf nebhaq gur ubhfr.  The Gothon stops, tries
                    not to laugh, then busts out laughing and can't move.
                    While he's laughing you run up and shoot him square in
                    the head putting him down, then jump through the
                    Weapon Armory door.
                    """))
            return 'laser_weapon_armory'

        elif action == "fight!":
            gothon = Alien("Guardian", 25, 1)
            if (self.battle(gothon, player)):
                return 'laser_weapon_armory'
            else:
                return 'death'


        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'

############################################
class LaserWeaponArmory(Scene):

    def __init__(self):
        super(LaserWeaponArmory, self).__init__("Heavy Machine Gun")

    def enter(self, player):
        print(dedent("""
            You do a dive roll into the Weapon Armory, crouch and scan
            the room for more Gothons that might be hiding.  It's dead
            quiet, too quiet.  You stand up and run to the far side of
            the room and find the neutron bomb in its container.
            There's a keypad lock on the box and you need the code to
            get the bomb out.  If you get the code wrong 10 times then
            the lock closes forever and you can't get the bomb.  The
            code is 3 digits.
            """))
        
        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        #print("CODE: ", code)
        guess = input("[keypad]> ")
        guesses = 1 # First attempt already done

        while guess != code and guesses < 10 and guess != self.cheat_code:
            print("BZZZZEDDD!")
            guesses += 1
            guess = input("[keypad]> ")
        
        if guess == code or guess == self.cheat_code:
            print(dedent("""
                The container clicks open and the seal breaks, letting
                gas out.  You grab the neutron bomb and run as fast as
                you can to the bridge where you must place it in the
                right spot.
                """))
            return 'the_bridge'
        else:
            print(dedent("""
                The lock buzzes one last time and then you hear a
                sickening melting sound as the mechanism is fused
                together.  You decide to sit there, and finally the
                Gothons blow up the ship from their ship and you die.
                """))
            return 'death'

############################################
class TheBridge(Scene):

    def __init__(self):
        super(TheBridge, self).__init__("Pass of Caradhras")

    def enter(self, player):
        print(dedent("""
            You burst onto the Bridge with the netron destruct bomb
            under your arm and surprise 5 Gothons who are trying to
            take control of the ship.  Each of them has an even uglier
            clown costume than the last.  They haven't pulled their
            weapons out yet, as they see the active bomb under your
            arm and don't want to set it off.
            """))

        action = input("> ")

        if action == "throw the bomb":
            print(dedent("""
                In a panic you throw the bomb at the group of Gothons
                and make a leap for the door.  Right as you drop it a
                Gothon shoots you right in the back killing you.  As
                you die you see another Gothon frantically try to
                disarm the bomb. You die knowing they will probably
                blow up when it goes off.
                """))
            return 'death'
 
        elif action == "slowly place the bomb" or action == self.cheat_code:
            print(dedent("""
                You point your blaster at the bomb under your arm and
                the Gothons put their hands up and start to sweat.
                You inch backward to the door, open it, and then
                carefully place the bomb on the floor, pointing your
                blaster at it.  You then jump back through the door,
                punch the close button and blast the lock so the
                Gothons can't get out.  Now that the bomb is placed
                you run to the escape pod to get off this tin can.
                """))

            return 'escape_pod'
        
        elif action == "fight!":
            player.HP += 10
            gothon = Alien("All in one", 30, 3)
            if (self.battle(gothon, player)):
                return 'escape_pod'
            else:
                return 'death'

        else:
            print("DOES NOT COMPUTE!")
            return "the_bridge"    

############################################
class EscapePod(Scene):

    def __init__(self):
        super(EscapePod, self).__init__("Grievous")
 
    def enter(self, player):
        print(dedent("""
            You rush through the ship desperately trying to make it to
            the escape pod before the whole ship explodes.  It seems
            like hardly any Gothons are on the ship, so your run is
            clear of interference.  You get to the chamber with the
            escape pods, and now need to pick one to take.  Some of
            them could be damaged but you don't have time to look.
            There's 5 pods, which one do you take?
            """))

        good_pod = randint(1,5)
        guess = input("[pod #]> ")

        if int(guess) != good_pod or guess != self.cheat_code:
            print(dedent(f"""
                    You jump into pod {guess} and hit the eject button.
                    The pod escapes out into the void of space, then
                    implodes as the hull ruptures, crushing your body into
                    jam jelly.
                    """))
            return 'death'
        
        else:
            print(dedent(f"""
                    You jump into pod {guess} and hit the eject button.
                    The pod easily slides out into space heading to the
                    planet below.  As it flies to the planet, you look
                    back and see your ship implode then explode like a
                    bright star, taking out the Gothon ship at the same
                    time.  You won!
                    """))

            return 'finished'

############################################
class Finished(Scene):

    def __init__(self):
        super(Finished, self).__init__("Start")

    def enter(self, player):
        print("You won! Good job.")
        return 'finished'

############################################
class Map(object):
    # Initialize the static dictionary of the scenes
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

############################################

# A very basic combat system approach
 
class Character(object):
    def __init__(self, name, HP):
        self.name = name
        self.HP = HP
    
    def attack(self):
        pass

    def get_hurt(self, damage):
        self.HP -= damage

class Player(Character):

    def __init__(self, name, HP):
        super(Player, self).__init__(name, HP)

    def attack(self):
        return randint(1,10)

    def restore_health(self, hp=100):
        self.HP = hp

class Alien(Character):

    def __init__(self, name, HP, lvl):
        super(Alien, self).__init__(name, HP)
        self.lvl = lvl

    def attack(self):
        return randint( (1 * self.lvl), ((10 * self.lvl) / 2))

# Start of the game

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()