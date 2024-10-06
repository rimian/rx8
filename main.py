import pygame
import logging
logger = logging.getLogger(__name__)

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 480

logging.basicConfig(
    filename='rx8.log',
    level=logging.INFO
)

def main():
    logger.info('Start')

    data_as_string = '3'

    pygame.init()

    screen = pygame.display.set_mode(
        (WINDOW_WIDTH, WINDOW_HEIGHT),
        pygame.FULLSCREEN
    )

    pygame.display.set_caption('car yo')

    font = pygame.font.SysFont(None, 48)

    img_water_temp = font.render(f"Water temp: {data_as_string}", True, (222,222,222))
    img_oil_pressure = font.render(f"Oil Pressure: {data_as_string}", True, (222,222,222))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.blit(img_water_temp, (40, 20))
        screen.blit(img_oil_pressure, (80, 20))

        pygame.display.update()


if __name__ == '__main__':
    main()
