

from random import randint
import pygame

#pygame setup
pygame.init()
Window_Width,Window_Hight = 1280,720
disply_surface =pygame.display.set_mode((Window_Width,Window_Hight))
pygame.display.set_caption("Space Shooter")
running=True

#surface
surf=pygame.Surface((100,200))
surf.fill(('blue'))
x=100

#imports
player_surf=pygame.image.load(('D:/cs_python/pygame/spaceshoot/image/player.png')).convert_alpha()
player_rect =player_surf.get_rect(center=(Window_Width/2,Window_Hight/2))
player_direction = 1
star_surf=pygame.image.load(('D:/cs_python/pygame/spaceshoot/image/star.png')).convert_alpha()
star_positions=[(randint(0,Window_Width),randint(0,Window_Hight)) for i in range(20)]

metror_surf=pygame.image.load(('D:/cs_python/pygame/spaceshoot/image/meteor.png')).convert_alpha()
metror_rect=metror_surf.get_rect(center=(Window_Width/2,Window_Hight/2))

laser_surf=pygame.image.load(('D:/cs_python/pygame/spaceshoot/image/laser.png')).convert_alpha()
laser_rect=laser_surf.get_rect(bottomleft=(20,Window_Hight-20))

while running:
    #event loop
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running =False

    #DRAW THE GAME
    disply_surface.fill(('gray'))
    for pos in star_positions:
        disply_surface.blit(star_surf,pos)
   

    disply_surface.blit(metror_surf,metror_rect)
    disply_surface.blit(laser_surf,laser_rect)
    
    #player movement
    player_rect.x+=player_direction*0.8
    if player_rect.right >  Window_Width or player_rect.left <0:
        player_direction*=-1
    disply_surface.blit(player_surf,player_rect.topleft)

    pygame.display.update()
pygame.quit()
