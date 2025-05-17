import pygame
import os
import sys

# === Setup ===
pygame.init()
info = pygame.display.Info()
screen_width, screen_height = 800, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jumping Head Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 48)

# === Load Player Image ===
player_img_path = "player_head.png"
if not os.path.exists(player_img_path):
    print(f"ERROR: '{player_img_path}' not found.")
    pygame.quit()
    sys.exit()

player_image = pygame.image.load(player_img_path).convert_alpha()
player_image = pygame.transform.scale(player_image, (60, 60))

# === Load Obstacle Image ===
obstacle_img_path = "obstacle.png"
if not os.path.exists(obstacle_img_path):
    print(f"ERROR: '{obstacle_img_path}' not found.")
    pygame.quit()
    sys.exit()

obstacle_image = pygame.image.load(obstacle_img_path).convert_alpha()
obstacle_image = pygame.transform.scale(obstacle_image, (50, 50))

# === Game Variables ===
player = pygame.Rect(100, screen_height - 100, 60, 60)
player_vel_y = 0
gravity = 1
jump_strength = -20
is_jumping = False

obstacle = pygame.Rect(screen_width, screen_height - 90, 50, 50)
obstacle_speed = 15

# === Game Loop ===
running = True
while running:
    screen.fill((255, 255, 255))  # White background

    # --- Events ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # --- Input ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not is_jumping:
        player_vel_y = jump_strength
        is_jumping = True

    # --- Physics ---
    player_vel_y += gravity
    player.y += player_vel_y

    if player.y >= screen_height - 100:
        player.y = screen_height - 100
        player_vel_y = 0
        is_jumping = False

    # --- Obstacle Movement ---
    obstacle.x -= obstacle_speed
    if obstacle.x < -50:
        obstacle.x = screen_width + 100  # Reset beyond right edge

    # --- Collision ---
    if player.colliderect(obstacle):
        text = font.render("Game Over!", True, (255, 0, 0))
        screen.blit(text, (screen_width // 2 - 100, screen_height // 2 - 25))
        pygame.display.flip()
        pygame.time.wait(2000)
        obstacle.x = screen_width
        player.y = screen_height - 100
        continue

    # --- Draw ---
    screen.blit(player_image, player)
    screen.blit(obstacle_image, obstacle)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
