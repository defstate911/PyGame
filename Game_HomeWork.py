import pygame
import random

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Фруктовый рай")

AQUAMARINE = (127, 255, 212)
#BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
#RED = (255, 0, 0)
#YELLOW = (255, 255, 0)
#ORANGE = (255, 165, 0)
#PURPLE = (160, 32, 240)

font = pygame.font.SysFont(None, 36)

basket_speed = 10

TARGET_SCORE = 500

def load_image(name, width=None, height=None):
        image = pygame.image.load(f'img1/{name}')
        if width and height:
            image = pygame.transform.scale(image, (width, height))
        return image


class Fruit:
    def __init__(self, fruit_type):
        self.fruit_type = fruit_type
        self.size = 80  # Размер изображения фрукта после масштабирования
        self.x = random.randint(0, WINDOW_WIDTH - self.size)
        self.y = -self.size  # Начальная позиция за верхней границей
        self.speed = random.randint(3, 7)

        if self.fruit_type == "banana":
            self.image = load_image("banana.png", self.size, self.size)
            self.points = 10
        elif self.fruit_type == "apple":
            self.image = load_image("apple.png", self.size, self.size)
            self.points = 15
        elif self.fruit_type == "kiwi":
            self.image = load_image("kiwi.png", self.size, self.size)
            self.points = 20
        elif self.fruit_type == "pineapple":
            self.image = load_image("pineapple.png", self.size, self.size)
            self.points = 25
        elif self.fruit_type == "strawberry":
            self.image = load_image("strawberry.png", self.size, self.size)
            self.points = 30
        elif self.fruit_type == "carrot":
            self.image = load_image("carrot.png", self.size, self.size)
            self.points = -500  # Морковка сбрасывает счет

    def move(self):
        self.y += self.speed

    def draw(self, surface):
        # Отрисовка изображения фрукта
        surface.blit(self.image, (self.x, self.y))


class Basket:
    def __init__(self):
        self.size = 80  # Размер корзинки после масштабирования
        self.image = load_image("basket.png", self.size, self.size)
        self.x = (WINDOW_WIDTH - self.size) // 2
        self.y = WINDOW_HEIGHT - self.size - 10  # Располагаем корзинку чуть выше нижней границы
        self.speed = basket_speed

    def move_left(self):
        self.x -= self.speed
        if self.x < 0:
            self.x = 0

    def move_right(self):
        self.x += self.speed
        if self.x > WINDOW_WIDTH - self.size:
            self.x = WINDOW_WIDTH - self.size

    def draw(self, surface):
        # Отрисовка изображения корзинки
        surface.blit(self.image, (self.x, self.y))


def main():
    basket = Basket()

    fruits = []

    score = 0

    game_over = False

    clock = pygame.time.Clock()

    # Период появления нового фрукта (в миллисекундах)
    spawn_event = pygame.USEREVENT + 1
    pygame.time.set_timer(spawn_event, 1000)  # Новый фрукт каждые 1 секунду

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == spawn_event and not game_over:
                # Случайный выбор типа фрукта
                fruit_type = random.choice(["banana", "apple", "kiwi", "pineapple", "strawberry", "carrot"])
                fruits.append(Fruit(fruit_type))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            basket.move_left()
        if keys[pygame.K_RIGHT]:
            basket.move_right()

        if not game_over:
            # Перемещение фруктов
            for fruit in fruits[:]:
                fruit.move()
                # Проверка на столкновение с корзинкой
                if (basket.x < fruit.x + fruit.size and
                    basket.x + basket.size > fruit.x and
                    basket.y < fruit.y + fruit.size and
                    basket.y + basket.size > fruit.y):
                    score += fruit.points
                    fruits.remove(fruit)
                    if fruit.fruit_type == "carrot":
                        score = 0  # Обнуляем счет при ловле морковки
                    if score >= TARGET_SCORE:
                        game_over = True

                # Удаление фруктов, которые упали за нижнюю границу
                elif fruit.y > WINDOW_HEIGHT:
                    fruits.remove(fruit)

        # Заполнение окна
        window.fill(AQUAMARINE)

        # Отрисовка корзинки
        basket.draw(window)

        # Отрисовка фруктов
        for fruit in fruits:
            fruit.draw(window)

        # Отображение счета
        score_text = font.render(f"Счет: {score}", True, WHITE)
        window.blit(score_text, (10, 10))

        # Проверка на победу
        if game_over:
            win_text = font.render("Поздравляем! Вы победили!", True, GREEN)
            window.blit(win_text, (WINDOW_WIDTH // 2 - win_text.get_width() // 2, WINDOW_HEIGHT // 2))

        # Обновление дисплея
        pygame.display.flip()

        # Ограничение частоты кадров до 60 FPS
        clock.tick(60)

    # Завершение работы Pygame
    pygame.quit()


if __name__ == "__main__":
    main()
