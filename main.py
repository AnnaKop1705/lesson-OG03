import time
import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background_img = pygame.image.load('img/fone.jpg')

pygame.display.set_caption('Охота на уточек')
icon = pygame.image.load('img/icon.jpg')
pygame.display.set_icon(icon)

target_img = pygame.image.load('img/target.png')
target_width = 80
target_height = 80

font = pygame.font.Font(None, 36)

def show_score(score):
    score_text = font.render('Очки: ' + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

def show_timer(timer):
    timer_text = font.render('Время: ' + str(timer), True, (255, 255, 255))
    screen.blit(timer_text, (SCREEN_WIDTH - 150, 10))

def show_best_score(best_score):
    best_score_text = font.render('Лучший результат: ' + str(best_score), True, (255, 255, 255))
    screen.blit(best_score_text, (10, 50))

def show_round_result(score, best_score):
    round_result_text = font.render('Результат раунда: ' + str(score), True, (255, 255, 255))
    screen.blit(round_result_text, (SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2 - 20))
    best_score_text = font.render('Лучший результат: ' + str(best_score), True, (255, 255, 255))
    screen.blit(best_score_text, (SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2 + 20))

def show_restart_button():
    restart_text = font.render('Новый раунд', True, (0, 255, 0))
    screen.blit(restart_text, (SCREEN_WIDTH // 2 - 90, SCREEN_HEIGHT // 2 + 80))

def game():
    target_x = random.randint(0, SCREEN_WIDTH - target_width)
    target_y = random.randint(0, SCREEN_HEIGHT - target_height)
    score = 0
    best_score = 0
    start_time = time.time()
    round_time = 5
    game_over = False

    running = True
    while running:
        screen.blit(background_img, (0, 0))
        show_score(score)
        show_best_score(best_score)
        time_left = round_time - int(time.time() - start_time)
        show_timer(max(0, time_left))

        if not game_over:
            screen.blit(target_img, (target_x, target_y))
        if game_over:
            show_round_result(score, best_score)
            show_restart_button()
        if time_left <= 0:
            if score > best_score:
                best_score = score
            game_over = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if not game_over and target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                    score += 1
                    target_x = random.randint(0, SCREEN_WIDTH - target_width)
                    target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                elif game_over and SCREEN_WIDTH // 2 - 90 < mouse_x < SCREEN_WIDTH // 2 + 90 and SCREEN_HEIGHT // 2 + 80 < mouse_y < SCREEN_HEIGHT // 2 + 120:
                    game_over = False
                    start_time = time.time()
                    score = 0

        pygame.display.update()

    pygame.quit()

game()