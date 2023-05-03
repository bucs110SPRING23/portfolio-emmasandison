import pygame

BUTTON_SIZE = 25
NUM_BUTTONS = 10

class LED:
    def __init__(self):
        self.on = False
        self.color = (10,10,10)
        self.rect = pygame.Rect(0, 0, BUTTON_SIZE, BUTTON_SIZE)

#Driver
def main():

    # initialize display and models
    pygame.init()
    display = pygame.display.set_mode()
    machine_rect = pygame.Rect(0, 0,
                               BUTTON_SIZE * NUM_BUTTONS * 2 + BUTTON_SIZE,
                               BUTTON_SIZE * 3)
    machine_rect.center = (display.get_width() / 2, display.get_height() / 2)

    leds = []
    for i in range(NUM_BUTTONS):
        led = LED()
        led.rect.x = machine_rect.x + BUTTON_SIZE + (BUTTON_SIZE * 2 * len(leds))
        led.rect.y = machine_rect.y + BUTTON_SIZE
        leds.append(led)

    #mainloop
    while True:
        #eventloop
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for led in leds:
                    if led.rect.collidepoint(event.pos):
                        if led.on:
                            led.on = False
                            led.color = (190, 0, 0)
                        else:
                            led.on = True
                            led.color = (0, 255, 0)

        #Redraw
        pygame.draw.rect(display, "grey", machine_rect)
        for led in leds:
            pygame.draw.circle(display, led.color, led.rect.center, BUTTON_SIZE / 2)
        #display updates
        pygame.display.flip()


main()

