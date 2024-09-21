import pygame
import random
import math

# Initialisierung von Pygame
pygame.init()

# Bildschirmabmessungen
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jump and Run Game")

# Farben
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Spielfigur
player_size = 50
player_speed = 5
player_jump = -20  # Erhöhte Sprungkraft
gravity = 1
velocity_y = 0

# Plattformen
platform_width = 70
platform_height = 10
platform_gap = 80  # Verringert den Abstand zwischen den Plattformen
platform_speed = 2
platforms = []

# Unsichtbarer Radius um Plattformen
platform_radius = 20  # Radius der Plattformen (Kreise)

# Gelbe Kugeln
yellow_balls = []
yellow_ball_speed = 5  # Geschwindigkeit der gelben Kugeln (erhöht auf 5)

# Schriftarten
font = pygame.font.SysFont(None, 55)
small_font = pygame.font.SysFont(None, 35)

# Spielzustände
start_game = False
game_over = False
can_jump = True  # Variable, um zu verfolgen, ob der Spieler springen kann

# Farbpalette mit 30 verschiedenen Farben
color_palette = [
    (255, 0, 0),     # Rot
    (0, 255, 0),     # Grün
    (0, 0, 255),     # Blau
    (255, 255, 0),   # Gelb
    (255, 165, 0),   # Orange
    (128, 0, 128),   # Lila
    (0, 255, 255),   # Cyan
    (255, 192, 203), # Rosa
    (255, 140, 0),   # Dunkelorange
    (0, 128, 0),     # Dunkelgrün
    (255, 69, 0),    # Rot-Orange
    (139, 69, 19),   # Sattelbraun
    (210, 105, 30),  # Schokolade
    (0, 139, 139),   # Dunkelgrün
    (0, 0, 128),     # Marine
    (123, 104, 238), # Medium Violett
    (218, 112, 214), # Orchidee
    (102, 51, 0),    # Brauner
    (75, 0, 130),    # Indigo
    (0, 0, 139),     # Dunkelblau
    (255, 20, 147),  # Tiefrosa
    (139, 69, 19),   # Sattelbraun
    (139, 0, 0),     # Dunkelrot
    (210, 105, 30),  # Schokolade
    (0, 255, 127),   # Frühlingsgrün
    (0, 100, 0),     # Dunkelgrün
    (0, 255, 255),   # Cyan
    (128, 0, 0),     # Dunkelrot
    (255, 99, 71),   # Tomate
    (160, 82, 45)    # Braun
]

# Zufällige Reihenfolge der Farben in der Palette
random.shuffle(color_palette)

current_color_index = 0
current_platform_color = color_palette[current_color_index]

score = 0  # Score initialisieren
last_score = 0  # Letzten Score initialisieren
high_score = 0  # Höchsten Score initialisieren
coins_collected = 0  # Anzahl der berührten gelben Plattformen

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

def initialize_game():
    global player, velocity_y, platforms, can_jump, current_color_index, current_platform_color, score, yellow_balls, coins_collected
    player = pygame.Rect(WIDTH // 2, HEIGHT - 100 - player_size, player_size, player_size)
    velocity_y = 0
    platforms = [pygame.Rect(WIDTH // 2 - platform_width // 2, HEIGHT - 100, platform_width, platform_height)]
    while len(platforms) < 10:  # Weniger Plattformen
        new_platform = pygame.Rect(random.randint(0, WIDTH - platform_width), random.randint(0, HEIGHT - player_size - platform_gap), platform_width, platform_height)
        if all(not new_platform.colliderect(existing) and
               math.sqrt((new_platform.centerx - existing.centerx) ** 2 + (new_platform.centery - existing.centery) ** 2) > platform_radius
               for existing in platforms):
            platforms.append(new_platform)
    score = 0
    can_jump = True  # Hinzugefügt: Setze die Sprungmöglichkeit beim Start des Spiels
    current_color_index = 0
    current_platform_color = color_palette[current_color_index]
    yellow_balls = []  # Liste für gelbe Kugeln zurücksetzen
    coins_collected = 0  # Zurücksetzen der Anzahl berührter gelber Plattformen

initialize_game()

# Hauptspiel Schleife
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not start_game:
                    start_game = True
                    game_over = False
                    initialize_game()
                if game_over:
                    start_game = True
                    game_over = False
                    initialize_game()
                elif can_jump:
                    velocity_y = player_jump
                    can_jump = False  # Hinzugefügt: Deaktiviere die Sprungmöglichkeit nach einem Sprung

    if start_game:
        # Bewegung der Spielfigur
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.left > 0:
            player.x -= player_speed
        if keys[pygame.K_RIGHT] and player.right < WIDTH:
            player.x += player_speed

        # Schwerkraft
        velocity_y += gravity
        player.y += velocity_y

        # Plattform-Kollision
        if player.y >= HEIGHT:
            game_over = True
            start_game = False
            last_score = score  # Aktualisiere den letzten Score
            if score > high_score:
                high_score = score  # Aktualisiere den höchsten Score
        for platform in platforms:
            if player.colliderect(platform) and velocity_y > 0:
                player.y = platform.y - player_size
                velocity_y = 0
                score += 1  # Ein Punkt für jede Plattformberührung
                can_jump = True  # Hinzugefügt: Erlaube dem Spieler erneut zu springen, wenn er eine Plattform erreicht

        # Überprüfe Kollision mit gelber Kugel
        for ball in yellow_balls[:]:
            if player.colliderect(ball['rect']):
                yellow_balls.remove(ball)
                coins_collected += 1

        # Plattformen bewegen
        for platform in platforms:
            platform.y += platform_speed
            if platform.y >= HEIGHT:
                platform.y = -platform_height
                platform.x = random.randint(0, WIDTH - platform_width)
                while any(platform.colliderect(existing) and
                          math.sqrt((platform.centerx - existing.centerx) ** 2 + (platform.centery - existing.centery) ** 2) <= platform_radius
                          for existing in platforms if existing != platform):
                    platform.x = random.randint(0, WIDTH - platform_width)

        # Erzeuge gelbe Kugeln zufällig von oben nach unten
        if random.random() < 0.01:  # Wahrscheinlichkeit von 1% pro Frame
            new_ball = {
                'rect': pygame.Rect(random.randint(0, WIDTH - 2 * platform_radius), -2 * platform_radius, 2 * platform_radius, 2 * platform_radius),
                'speed': yellow_ball_speed
            }
            yellow_balls.append(new_ball)

        # Farbwechsel bei jedem hundertsten Punkt
        if score % player_size == 0 and score > 0:
            current_color_index = (current_color_index + 1) % len(color_palette)
            current_platform_color = color_palette[current_color_index]

        # Update Position der gelben Kugeln
        for ball in yellow_balls:
            ball['rect'].y += ball['speed']

        # Entferne gelbe Kugeln, die den Bildschirm verlassen haben
        yellow_balls = [ball for ball in yellow_balls if ball['rect'].top <= HEIGHT]

        # Bildschirm zeichnen
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, player)
        for platform in platforms:
            pygame.draw.rect(screen, current_platform_color, platform)  # Plattformen in aktueller Farbe zeichnen
        for ball in yellow_balls:
            pygame.draw.circle(screen, YELLOW, ball['rect'].center, platform_radius)  # Gelbe Kugeln als Kreis zeichnen

        draw_text(f'Score: {score}', small_font, BLACK, screen, WIDTH // 2, 20)

        pygame.display.flip()
        pygame.time.Clock().tick(60)

    else:
        screen.fill(WHITE)
        if game_over:
            draw_text('Game Over', font, RED, screen, WIDTH // 2, HEIGHT // 2)  # Farbe zu Rot geändert
            draw_text(f'Last Score: {last_score}', small_font, BLACK, screen, WIDTH // 2, HEIGHT // 2 + 60)
            draw_text(f'High Score: {high_score}', small_font, BLACK, screen, WIDTH // 2, HEIGHT // 2 + 100)
            draw_text(f'Coins Collected: {coins_collected}', small_font, BLACK, screen, WIDTH // 2, HEIGHT // 2 + 140)
            draw_text('Press Space to Restart', small_font, BLACK, screen, WIDTH // 2, HEIGHT // 2 + 180)
        else:
            draw_text('Press Space to Start', font, BLACK, screen, WIDTH // 2, HEIGHT // 2)
        pygame.display.flip()

pygame.quit()
