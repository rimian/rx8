import pygame
import logging
import obd
logger = logging.getLogger(__name__)

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 480

logging.basicConfig(
    filename='rx8.log',
    level=logging.INFO
)

connection = obd.Async()
connection.watch(obd.commands.COOLANT_TEMP)
connection.watch(obd.commands.OIL_TEMP)
connection.start()

def main():
    logger.info('Start')

    water_temp = connection.query(obd.commands.COOLANT_TEMP)
    oil_temp = connection.query(obd.commands.OIL_TEMP)

    pygame.init()

    screen = pygame.display.set_mode(
        (WINDOW_WIDTH, WINDOW_HEIGHT),
        pygame.FULLSCREEN
    )

    pygame.display.set_caption('car yo')

    font = pygame.font.SysFont(None, 48)

    img_water_temp = font.render(f"Water Temp: {water_temp}", True, (222,222,222))
    img_oil_temp = font.render(f"Oil Temp: {oil_temp}", True, (222,222,222))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                connection.stop()
                pygame.quit()

        screen.blit(img_water_temp, (40, 20))
        screen.blit(img_oil_temp, (80, 20))

        pygame.display.update()


if __name__ == '__main__':
    main()
