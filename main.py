import pygame
from button_class import Button
pygame.init()
win_width = 540
win_height = 900
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption('Заправки')
font = "fonts//Black Bamboo DK.ttf"
# Зададим цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
BLUE = (0, 0, 255)

# Зададим размер и положение кнопки
button_width = 300
button_height = 50
button_x = (win_width - button_width) // 5
button_y = (win_height - button_height) // 1.5

button_start = Button(button_width, button_height, button_x, button_y, BLUE,"Найти заправку", 12, font)
# Основной цикл
running = True
while running:
    window.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if button_start.press(event.pos):
            running = False
    button_start.create(window)
    # Отрисовка кнопки


    # Отрисовка текста на кнопк


    pygame.display.update()

pygame.quit()