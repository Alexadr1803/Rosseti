import pygame


# Создание класса кнопок
class Button:

    # инициализация кнопки
    def __init__(self, width, height, pos_x, pos_y, color, text, r, font):
        self.width = width
        self.height = height
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.text = text
        self.r = r
        self.font = font

    # Функция отображения кнопки
    def create(self, screen):
        pygame.draw.rect(screen, self.color,
                         (self.pos_x, self.pos_y, self.width, self.height), 0)
        f1 = pygame.font.Font(self.font, self.r)
        text = f1.render(self.text, True, (0, 0, 0))
        screen.blit(text, (self.pos_x + 10, self.pos_y + self.height // 3))

    # Проверка нажатия - нажата возращает True, если нет False
    def press(self, m_pos):
        m_pos = list(m_pos)
        if self.pos_x <= m_pos[0] <= self.pos_x + self.width and self.pos_y <= m_pos[1] <= self.pos_y + self.height:
            return True
        else:
            return False

    # окрашивание кнопки в серый при наведении курсора
    def on_motion(self, m_pos, screen):
        m_pos = list(m_pos)
        if self.press(m_pos):
            pygame.draw.rect(screen, (100, 100, 100),
                             (self.pos_x, self.pos_y, self.width, self.height), 0)
            f1 = pygame.font.Font(self.font, self.r)
            text = f1.render(self.text, True, (0, 0, 0))
            screen.blit(text, (self.pos_x + 10, self.pos_y + self.height // 2.75))