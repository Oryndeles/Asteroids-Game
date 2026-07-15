import pygame, constants
from logger import log_state

pygame.init()
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()

# game_loop
while True:
    log_state()
    for event in pygame.event.get():
        pass
    screen.fill("black")
    pygame.display.flip()
