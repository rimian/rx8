import can
import pygame

bus1 = can.interface.Bus('test', interface='virtual')
bus2 = can.interface.Bus('test', interface='virtual')

msg1 = can.Message(arbitration_id=0xabcde, data=[1,2,3])
bus1.send(msg1)
msg2 = bus2.recv()

# Convert the data payload to a string representation
data_as_string = ''.join(format(byte, '02x') for byte in msg2.data)

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

pygame.init()

screen = pygame.display.set_mode(
    (WINDOW_WIDTH, WINDOW_HEIGHT),
    pygame.FULLSCREEN
)

pygame.display.set_caption(data_as_string)

sysfont = pygame.font.get_default_font()
font = pygame.font.SysFont(None, 48)
img = font.render(f"Temp: {data_as_string}", True, (222,222,222))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.blit(img, (40, 20))
    pygame.display.update()
