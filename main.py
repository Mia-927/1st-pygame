from random import randint
import pygame
#pygame setup
pygame.init()
Window_Width,Window_Hight = 1280,720
disply_surface =pygame.display.set_mode((Window_Width,Window_Hight))
pygame.display.set_caption("Space Shooter")
running=True
clock =pygame.time.Clock()

#surface
surf=pygame.Surface((100,200))
surf.fill(('blue'))
x=100

#imports
player_surf=pygame.image.load(('D:/cs_python/pygame/spaceshoot/image/player.png')).convert_alpha()
player_rect =player_surf.get_rect(center=(Window_Width/2,Window_Hight/2))
player_direction = pygame.math.Vector2(0,0)
player_speed =1000

star_surf=pygame.image.load(('D:/cs_python/pygame/spaceshoot/image/star.png')).convert_alpha()
star_positions=[(randint(0,Window_Width),randint(0,Window_Hight)) for i in range(20)]

metror_surf=pygame.image.load(('D:/cs_python/pygame/spaceshoot/image/meteor.png')).convert_alpha()
metror_rect=metror_surf.get_rect(center=(Window_Width/2,Window_Hight/2))

laser_surf=pygame.image.load(('D:/cs_python/pygame/spaceshoot/image/laser.png')).convert_alpha()
laser_rect=laser_surf.get_rect(bottomleft=(20,Window_Hight-20))

while running:
    dt=clock.tick()/1000  #delta time in seconds
    
    #event loop
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running =False

        
        """if event.type ==pygame.KEYDOWN and event.key == pygame.K_1:
            print(1)
        if event.type == pygame.MOUSEMOTION:
            player_rect.center = event.pos"""
            
    #input
    #print(pygame.mouse.get_rel())
    keys =pygame.key.get_pressed()
    player_direction.x = int(keys[pygame.K_RIGHT]) -int(keys[pygame.K_LEFT])
    player_direction.y = int(keys[pygame.K_DOWN]) -int(keys[pygame.K_UP])
    player_direction = player_direction.normalize() if player_direction else player_direction
    player_rect.center += player_direction*player_speed*dt
    
    
    #DRAW THE GAME
    disply_surface.fill(('gray'))
    for pos in star_positions:
        disply_surface.blit(star_surf,pos)
   

    disply_surface.blit(metror_surf,metror_rect)
    disply_surface.blit(laser_surf,laser_rect)
    disply_surface.blit(player_surf,player_rect)
    
    #player movement

    """if player_rect.bottom >= Window_Hight or player_rect.top <= 0:
        player_rect.bottom >= Window_Hight
        player_direction.y *= -1
    if player_rect.right >= Window_Width or player_rect.left <= 0:
        player_direction.x *= -1
    player_rect.center +=player_direction*player_speed*dt
    disply_surface.blit(player_surf,player_rect)"""


    pygame.display.update()
pygame.quit()

