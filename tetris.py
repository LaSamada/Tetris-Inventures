import pygame, sys
from game_logic import Game
from miscellaneous import Colors as colors

pygame.init()

title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score:", True, colors.white)
level_surface = title_font.render("Level:", True, colors.white)
next_surface = title_font.render("Next", True, colors.white)
game_over_surface = pygame.font.Font(None, 55).render("Game Over", True, colors.red)

screen = pygame.display.set_mode((900, 620))

pygame.display.set_caption("Python Tetris Inventures")

clock = pygame.time.Clock()

game = Game()

game_refresh = pygame.USEREVENT
pygame.time.set_timer(game_refresh, game.time)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.game_over == True and event.key == pygame.K_r:
                game.game_over = False
                game.reset()
            elif event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            elif event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            elif event.key == pygame.K_DOWN and game.game_over == False:
                game.soft_drop()
                game.update_score(0, 1, 0)
            elif event.key == pygame.K_SPACE and game.game_over == False:
                hard_drop = game.hard_drop()
                game.update_score(0, 0, hard_drop)
            elif event.key == pygame.K_UP and game.game_over == False:
                game.rotate()
        if event.type == game_refresh and game.game_over == False:
            game.soft_drop()
            pygame.time.set_timer(game_refresh, game.time)

    score_value = title_font.render(str(game.score), True, colors.white)
    level_value = title_font.render(str(game.level), True, colors.white)

    pygame.draw.rect(screen, colors.gray, (0, 0, 900, 620))


    screen.blit(score_surface, (20, 20, 100, 100))
    screen.blit(score_value, (150, 20, 100, 100))
    screen.blit(level_surface, (620, 20, 50, 50))
    screen.blit(level_value, (750, 20, 100, 100))
    screen.blit(next_surface, (20, 200, 100, 100))

    if game.game_over == True:
        screen.blit(game_over_surface, (650, 310, 300, 300))

    
    game.paint(screen)
    pygame.display.update()
    clock.tick(60)