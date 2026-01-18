import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player


def main():
    
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: 1280\nScreen height: 720")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            pass
        screen.fill("black")
        
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        pygame.time.Clock()
        dt = clock.tick(60)/1000
    


if __name__ == "__main__":
    main()
