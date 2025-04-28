import pygame
import sys
from settings import *
from sounds import load_sounds, play_background_music
from game import Game

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("🔥 Ultra Pong 🔥")

    hit_sound, score_sound, bg_music = load_sounds()
    play_background_music(bg_music)

    game = Game(screen, hit_sound, score_sound)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            game.handle_events(event)

        game.update()
        game.draw()

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()






# import pygame
# import sys
# import random

# # Initialize
# pygame.init()
# clock = pygame.time.Clock()

# # Sound
# hit_sound = pygame.mixer.Sound("assets/mixkit-game-ball-tap-2073.wav")
# score_sound = pygame.mixer.Sound("assets/mixkit-arcade-score-interface-217.wav")
# bg_music = pygame.mixer.Sound("assets/music.mp3")
# bg_music.play(-1)

# # Window
# screen_width, screen_height = 800, 500
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("🔥 Ultra Pong 🔥")

# # Colors
# bg_color = (20, 20, 30)
# white = (240, 240, 240)
# glow_color = (0, 255, 255)

# # Fonts
# font = pygame.font.SysFont("Segoe UI Emoji", 36)
# big_font = pygame.font.SysFont("Segoe UI Emoji", 72)

# # Game elements
# ball = pygame.Rect(screen_width/2-15, screen_height/2-15, 30, 30)
# player = pygame.Rect(screen_width-20, screen_height/2-70, 10, 140)
# opponent = pygame.Rect(10, screen_height/2-70, 10, 140)

# ball_speed_x = 7 * random.choice((1, -1))
# ball_speed_y = 7 * random.choice((1, -1))
# player_speed = 0
# opponent_speed = 7

# player_score = 0
# opponent_score = 0

# # States
# game_state = "menu"  # menu, active, over
# winner = None  # "player" or "opponent"

# # Functions
# def ball_restart():
#     global ball_speed_x, ball_speed_y
#     ball.center = (screen_width/2, screen_height/2)
#     ball_speed_x = 7 * random.choice((1, -1))
#     ball_speed_y = 7 * random.choice((1, -1))

# def ball_animation():
#     global ball_speed_x, ball_speed_y, player_score, opponent_score, game_state, winner
    
#     ball.x += ball_speed_x
#     ball.y += ball_speed_y

#     if ball.top <= 0 or ball.bottom >= screen_height:
#         ball_speed_y *= -1
#         hit_sound.play()

#     if ball.left <= 0:
#         player_score += 1
#         score_sound.play()
#         ball_restart()

#     if ball.right >= screen_width:
#         opponent_score += 1
#         score_sound.play()
#         ball_restart()

#     if ball.colliderect(player) or ball.colliderect(opponent):
#         ball_speed_x *= -1
#         hit_sound.play()
#         ball_speed_x *= 1.05
#         ball_speed_y *= 1.05

#     # Win conditions
#     if player_score >= 10:
#         winner = "player"
#         game_state = "over"
#     if opponent_score >= 10:
#         winner = "opponent"
#         game_state = "over"

# def player_animation():
#     player.y += player_speed
#     if player.top <= 0:
#         player.top = 0
#     if player.bottom >= screen_height:
#         player.bottom = screen_height

# def opponent_ai():
#     if opponent.top < ball.y:
#         opponent.top += opponent_speed
#     if opponent.bottom > ball.y:
#         opponent.bottom -= opponent_speed
#     if opponent.top <= 0:
#         opponent.top = 0
#     if opponent.bottom >= screen_height:
#         opponent.bottom = screen_height

# def draw_glow(surface, rect, color, blur=20):
#     glow = pygame.Surface((rect.width + blur*2, rect.height + blur*2), pygame.SRCALPHA)
#     pygame.draw.ellipse(glow, (*color, 100), glow.get_rect())
#     surface.blit(glow, (rect.x - blur, rect.y - blur))

# # Main loop
# running = True

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#         if game_state == "menu":
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_SPACE:
#                     game_state = "active"
#                     player_score = 0
#                     opponent_score = 0
#                     ball_restart()

#         elif game_state == "active":
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_DOWN:
#                     player_speed += 7
#                 if event.key == pygame.K_UP:
#                     player_speed -= 7
#             if event.type == pygame.KEYUP:
#                 if event.key == pygame.K_DOWN:
#                     player_speed -= 7
#                 if event.key == pygame.K_UP:
#                     player_speed += 7

#         elif game_state == "over":
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_r:
#                     game_state = "active"
#                     player_score = 0
#                     opponent_score = 0
#                     ball_restart()
#                 if event.key == pygame.K_q:
#                     pygame.quit()
#                     sys.exit()

#     if game_state == "active":
#         ball_animation()
#         player_animation()
#         opponent_ai()

#     # Drawing
#     screen.fill(bg_color)

#     if game_state == "menu":
#         title_text = big_font.render("🔥 Ultra Pong 🔥", True, white)
#         start_text = font.render("Press SPACE to Start", True, white)
#         screen.blit(title_text, (screen_width/2 - title_text.get_width()/2, screen_height/2 - 100))
#         screen.blit(start_text, (screen_width/2 - start_text.get_width()/2, screen_height/2 + 20))

#     elif game_state == "active":
#         for i in range(0, screen_height, 20):
#             pygame.draw.rect(screen, (50, 50, 70), (screen_width/2-1, i, 2, 10))

#         draw_glow(screen, ball, glow_color)
#         draw_glow(screen, player, glow_color)
#         draw_glow(screen, opponent, glow_color)

#         pygame.draw.ellipse(screen, white, ball)
#         pygame.draw.rect(screen, white, player)
#         pygame.draw.rect(screen, white, opponent)

#         player_text = font.render(f"{player_score}", True, white)
#         opponent_text = font.render(f"{opponent_score}", True, white)
#         screen.blit(player_text, (screen_width/2 + 20, 20))
#         screen.blit(opponent_text, (screen_width/2 - 40, 20))

#     elif game_state == "over":
#         if winner == "player":
#             end_text = big_font.render("You Win! 🚀", True, white)
#         else:
#             end_text = big_font.render("You Lose 💀", True, white)

#         replay_text = font.render("Press R to Replay", True, white)
#         quit_text = font.render("Press Q to Quit", True, white)

#         screen.blit(end_text, (screen_width/2 - end_text.get_width()/2, screen_height/2 - 100))
#         screen.blit(replay_text, (screen_width/2 - replay_text.get_width()/2, screen_height/2 + 20))
#         screen.blit(quit_text, (screen_width/2 - quit_text.get_width()/2, screen_height/2 + 70))

#     pygame.display.flip()
#     clock.tick(60)
