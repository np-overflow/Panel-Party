import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self.color = color

    def changeColor(self, color):
        self.image.fill(color)
        self.color = color


class Player(pygame.sprite.Sprite):
    def __init__(self, path, height, width):
        super().__init__()
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, (height, width))
        self.rect = self.image.get_rect()

        if self.rect.x <= 25:
            self.rect.x = 25

    def border(self):
        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.x >= 550:
            self.rect.x = 550
        if self.rect.y <= 0:
            self.rect.y = 0
        if self.rect.y >= 550:
            self.rect.y = 550

    def moveRight(self, dist):
        self.rect.x += dist

    def moveLeft(self, dist):
        self.rect.x -= dist

    def moveDown(self, dist):
        self.rect.y += dist

    def moveUp(self, dist):
        self.rect.y -= dist


# General setup
pygame.init()

# Main window
screen_width = 600
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Panel Party')

# Variables
dist = 1
p1_points = 0
p2_points = 0
timer = 40
tile_size = 30
my_font = pygame.font.SysFont('Comic Sans MS', 30)
text = my_font.render(str(timer), True, (0, 0, 0))
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 1000)

# Game Objects
all_group = pygame.sprite.Group()
tile_group = pygame.sprite.Group()
for row in range(40, screen_width, 35):
    for col in range(40, screen_width, 35):
        tile = Tile(tile_size, tile_size, row, col, (128, 128, 128))
        tile_group.add(tile)
        tile_group.draw(screen)
        all_group.add(tile)

player_group = pygame.sprite.Group()

# Create player1
player1 = Player("game\\super-mario.png", 50, 50)
player1.rect.x = 0
player1.rect.y = 0
player_group.add(player1)
all_group.add(player1)

# Create player2
player2 = Player("game\\ghost.png", 50, 50)
player2.rect.x = screen_width - 25
player2.rect.y = screen_height - 25
player_group.add(player2)
all_group.add(player2)


# Game Loop
while timer >= 0:
    p1_points = 0
    p2_points = 0
    my_font = pygame.font.SysFont('Comic Sans MS', 30)

    # end game criteria
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            pygame.quit()
        elif event.type == timer_event:
            timer -= 1
            if timer == 0:
                pygame.time.wait(4000)
                pygame.time.set_timer(timer_event, 0)
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(0, 0, 600, 600), 2)

    keys = pygame.key.get_pressed()
    # Player 1 movements
    player1.border()
    if keys[pygame.K_a]:
        player1.moveLeft(dist)
    if keys[pygame.K_d]:
        player1.moveRight(dist)
    if keys[pygame.K_s]:
        player1.moveDown(dist)
    if keys[pygame.K_w]:
        player1.moveUp(dist)
    # Player 2 movements
    player2.border()
    if keys[pygame.K_LEFT]:
        player2.moveLeft(dist)
    if keys[pygame.K_RIGHT]:
        player2.moveRight(dist)
    if keys[pygame.K_DOWN]:
        player2.moveDown(dist)
    if keys[pygame.K_UP]:
        player2.moveUp(dist)

    # Collision detection
    p1_hit_list = pygame.sprite.spritecollide(player1, tile_group, False)
    p2_hit_list = pygame.sprite.spritecollide(player2, tile_group, False)

    for i in p1_hit_list:
        i.changeColor((255, 0, 0))
    for i in p2_hit_list:
        i.changeColor((0, 0, 255))

    # Calculate score
    for i in tile_group:
        if i.color == (255, 0, 0):
            p1_points += 1
        if i.color == (0, 0, 255):
            p2_points += 1

    # Display score
    text_surface = my_font.render(
        "Mario: " + str(p1_points), False, (0, 255, 0))
    screen.blit(text_surface, (100, 600))
    text_surface = my_font.render(
        "Ghost: " + str(p2_points), False, (0, 255, 0))
    screen.blit(text_surface, (400, 600))
    all_group.draw(screen)
    all_group.update()
    pygame.display.update()

pygame.quit()
