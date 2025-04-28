import pygame
import random
import sys  # <-- Important fix!

from settings import *

class Game:
    def __init__(self, screen, hit_sound, score_sound):
        self.screen = screen
        self.hit_sound = hit_sound
        self.score_sound = score_sound

        self.ball = pygame.Rect(SCREEN_WIDTH/2-15, SCREEN_HEIGHT/2-15, 30, 30)
        self.player = pygame.Rect(SCREEN_WIDTH-20, SCREEN_HEIGHT/2-70, 10, 140)
        self.opponent = pygame.Rect(10, SCREEN_HEIGHT/2-70, 10, 140)

        self.ball_speed_x = 7 * random.choice((1, -1))
        self.ball_speed_y = 7 * random.choice((1, -1))
        self.player_speed = 0
        self.opponent_speed = 7

        self.player_score = 0
        self.opponent_score = 0

        self.game_state = "menu"  # menu, active, over
        self.winner = None
        self.ball_trail = []

        self.stars = self.generate_stars()

        self.font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)
        self.big_font = pygame.font.SysFont(FONT_NAME, BIG_FONT_SIZE)

    def generate_stars(self):
        stars = []
        for _ in range(100):
            x = random.randint(0, SCREEN_WIDTH)
            y = random.randint(0, SCREEN_HEIGHT)
            size = random.randint(1, 3)
            speed = random.uniform(0.5, 1.5)
            stars.append([x, y, size, speed])
        return stars

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        if self.game_state == "menu":
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.start_game()

        elif self.game_state == "active":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.player_speed += 7
                if event.key == pygame.K_UP:
                    self.player_speed -= 7
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    self.player_speed -= 7
                if event.key == pygame.K_UP:
                    self.player_speed += 7

        elif self.game_state == "over":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.start_game()
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

    def start_game(self):
        self.game_state = "active"
        self.player_score = 0
        self.opponent_score = 0
        self.restart_ball()

    def update(self):
        if self.game_state == "active":
            self.ball_animation()
            self.player_animation()
            self.opponent_ai()

    def draw(self):
        self.screen.fill(BG_COLOR)
        self.draw_stars()

        if self.game_state == "menu":
            self.draw_menu()
        elif self.game_state == "active":
            self.draw_gameplay()
        elif self.game_state == "over":
            self.draw_gameover()

    def ball_animation(self):
        self.ball.x += self.ball_speed_x
        self.ball.y += self.ball_speed_y

        self.ball_trail.append((self.ball.centerx, self.ball.centery))
        if len(self.ball_trail) > 15:
            self.ball_trail.pop(0)

        if self.ball.top <= 0 or self.ball.bottom >= SCREEN_HEIGHT:
            self.ball_speed_y *= -1
            self.hit_sound.play()

        if self.ball.left <= 0:
            self.player_score += 1
            self.score_sound.play()
            self.restart_ball()

        if self.ball.right >= SCREEN_WIDTH:
            self.opponent_score += 1
            self.score_sound.play()
            self.restart_ball()

        if self.ball.colliderect(self.player) or self.ball.colliderect(self.opponent):
            self.ball_speed_x *= -1
            self.hit_sound.play()
            self.ball_speed_x *= 1.05
            self.ball_speed_y *= 1.05

        if self.player_score >= 10:
            self.winner = "Player"
            self.game_state = "over"
        if self.opponent_score >= 10:
            self.winner = "Opponent"
            self.game_state = "over"

    def player_animation(self):
        self.player.y += self.player_speed
        if self.player.top <= 0:
            self.player.top = 0
        if self.player.bottom >= SCREEN_HEIGHT:
            self.player.bottom = SCREEN_HEIGHT

    def opponent_ai(self):
        if self.opponent.top < self.ball.y:
            self.opponent.top += self.opponent_speed
        if self.opponent.bottom > self.ball.y:
            self.opponent.bottom -= self.opponent_speed
        if self.opponent.top <= 0:
            self.opponent.top = 0
        if self.opponent.bottom >= SCREEN_HEIGHT:
            self.opponent.bottom = SCREEN_HEIGHT

    def draw_stars(self):
        for star in self.stars:
            star[0] -= star[3]
            if star[0] < 0:
                star[0] = SCREEN_WIDTH
                star[1] = random.randint(0, SCREEN_HEIGHT)
            pygame.draw.circle(self.screen, (100, 100, 150), (int(star[0]), int(star[1])), star[2])

    def draw_gameplay(self):
        pygame.draw.rect(self.screen, NEON_GREEN, self.player)
        pygame.draw.rect(self.screen, NEON_PURPLE, self.opponent)
        pygame.draw.ellipse(self.screen, NEON_WHITE, self.ball)

        player_text = self.font.render(str(self.player_score), True, NEON_WHITE)
        opponent_text = self.font.render(str(self.opponent_score), True, NEON_WHITE)

        self.screen.blit(player_text, (SCREEN_WIDTH/2 + 20, 20))
        self.screen.blit(opponent_text, (SCREEN_WIDTH/2 - 60, 20))

    def draw_menu(self):
        title = self.big_font.render("🔥 Ultra Pong 🔥", True, NEON_WHITE)
        prompt = self.font.render("Press SPACE to Start", True, NEON_WHITE)

        self.screen.blit(title, (SCREEN_WIDTH/2 - title.get_width()/2, SCREEN_HEIGHT/3))
        self.screen.blit(prompt, (SCREEN_WIDTH/2 - prompt.get_width()/2, SCREEN_HEIGHT/2))

    def draw_gameover(self):
        text = self.big_font.render(f"{self.winner} wins!", True, NEON_WHITE)
        replay_prompt = self.font.render("Press R to Replay", True, NEON_WHITE)
        quit_prompt = self.font.render("Press Q to Quit", True, NEON_WHITE)

        self.screen.blit(text, (SCREEN_WIDTH/2 - text.get_width()/2, SCREEN_HEIGHT/3))
        self.screen.blit(replay_prompt, (SCREEN_WIDTH/2 - replay_prompt.get_width()/2, SCREEN_HEIGHT/2))
        self.screen.blit(quit_prompt, (SCREEN_WIDTH/2 - quit_prompt.get_width()/2, SCREEN_HEIGHT/2 + 50))

    def restart_ball(self):
        self.ball.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.ball_speed_x = 7 * random.choice((1, -1))
        self.ball_speed_y = 7 * random.choice((1, -1))
