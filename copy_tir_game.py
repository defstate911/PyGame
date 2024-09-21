import pygame
import random
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))

pygame.display.set_caption('Игра ТИР')
icon = pygame.image.load('img/tir1.jpg')
pygame.display.set_icon(icon)

target_image = pygame.image.load('img/tir2.png')
target_width = 80
target_hight = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HIGHT - target_hight)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

pygame.font.init()
font = pygame.font.SysFont('Arial', 36)  # Выбор шрифта и размера
small_font = pygame.font.SysFont('Arial', 24)  # Шрифт для счётчика

text_surface = None
text_timer = 0

count = 0
total_shots = 0
running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            total_shots += 1
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_hight:
                text_surface = font.render('В яблочко!', True, (255, 255, 255))
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HIGHT - target_hight)
                text_timer = 360
                count += 1
            else:
                text_surface = font.render('Мимо!', True, (255, 0, 0))  # Красный текст
                text_timer = 360
    screen.blit(target_image, (target_x, target_y))

    if text_timer > 0:
        screen.blit(text_surface, (SCREEN_WIDTH // 2 - text_surface.get_width() // 2, 50))  # Отцентрированный текст
        text_timer -= 1  # Уменьшаем таймер

    count_surface = small_font.render(f'Попаданий: {count}', True, (255, 255, 255))
    total_shots_surface = small_font.render(f'Всего выстрелов: {total_shots}', True, (255, 255, 255))
    screen.blit(count_surface, (10, 10))  # Показываем счётчик в левом верхнем углу
    screen.blit(total_shots_surface, (10, 40))  # Показываем счётчик всех выстрелов

    pygame.display.update()

# После завершения игры выводим итоговое сообщение
screen.fill((0, 0, 0))  # Чёрный фон
final_message = font.render(f'Вы попали {count} раз из {total_shots} выстрелов.', True, (255, 255, 255))
game_over_message = font.render('GAME OVER', True, (255, 0, 0))  # Отдельное сообщение для "GAME OVER"
screen.blit(final_message, (SCREEN_WIDTH // 2 - final_message.get_width() // 2, SCREEN_HIGHT // 2 - final_message.get_height() // 2))
screen.blit(game_over_message, (SCREEN_WIDTH // 2 - game_over_message.get_width() // 2, SCREEN_HIGHT // 2 + 40))  # Чуть ниже центра

pygame.display.update()
pygame.time.wait(3000)  # Ждём 3 секунды, чтобы показать итоговое сообщение



pygame.quit()