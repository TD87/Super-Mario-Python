SUPER MARIO

All the OOPs principles and guidelines have been followed in this project.

Controls:
	'w' - Jump
	'a' - Move left
	'd' - Move right
	'q' - Quit
	'r' - Restart

For optimal performance, only tap the keys. Don't press and hold.

How to run the game:
	python3 main.py

Types of Enemies:
	1. Regular : Move back and forth on a fixed path. Collision with the enemies result in losing a life.
		Killed by jumping on top of it.
	2. Boss: Moves back and forth as well but can change direction in order to follow the player. Has 2 lives.
		Must be jumped on to lose it's life.

Levels:
	1. Level 1: Ground Level
	2. Level 2: Sky Level

Scoring:
	Killing an enemy = 100 points
	Killing the boss = 200 points
	Collecting coins = 10 points

	At the end of the game - completion of level 2 - points are given based on the time taken. Number of points is inversely
	proportional to time taken.

Winning:
	The user has to kill the boss of the first level to go the second level. The game is completed upon killing boss of the
	second level.

Losing:
	User loses the game when he loses all 3 lives or falls from the platform in level 2.

Bonus:
	1. Color has been implemented
	2. Sounds have been implemented for jumping, collecting coins, moving left or right, game over screen, and game win screen.
		Jumping from the ground and jumping from platforms or pipes have different sounds.
	3. Smart enemies has been implemented in the boss' ability to follow the player.

Miscellaneous:
	1. Mario is invincible for 2 seconds after losing a life.
	2. Both Mario and the boss are invincible for 1 second after boss loses the first life.
