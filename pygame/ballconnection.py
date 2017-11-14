# please install python3 and pygame

import random
import pygame

def write(screen, text="hello", x=50, y=50, color=(255,0,0), fontsize=24, center=False, bold=True):
    font = pygame.font.SysFont("mono", fontsize, bold)
    fw, fh=font.size(text)
    surface=font.render(text, True, color)
    if center:
        screen.blit(surface, (x-fw//2, y-fh//2))
    else:
            screen.blit(surface, (x, y))

pygame.init()
screen=pygame.display.set_mode((640,480))
background = pygame.Surface(screen.get_size())
background.fill((255,255,255))      
background = background.convert()  



screen.blit(background, (0,0))    

clock = pygame.time.Clock()
mainloop = True
FPS = 60 
playtime = 0.0

#line endpoint 1
hx = 50
hy = 100

hdx = 0
hdy = 0
# line endpoint 2
ix = 200
iy = 100

idx = 0
idy = 0
#minimal distance
minimal_distance = 100
pointfactor = 1

kdx=0
kdy=0

ldx=0
ldy=0


kx = 200
ky = 200

lx=400
ly=400

r = 0
g = 0
b = 0

r1=40
r2=0

d1=1
d2=1

score=0

critical=50

while mainloop:
    milliseconds = clock.tick(FPS)
    playtime += milliseconds / 1000.0
    # ----- event handler -----
    # ----- wandering circles -----
    # k und l
    kdx+=random.choice((-0.1,0,0.1))
    kdy+=random.choice((-0.1,0,0.1))
    ldx+=random.choice((-0.1,0,0.1))
    ldy+=random.choice((-0.1,0,0.1))
    
    kx+=kdx
    ky+=kdy
    lx+=ldx
    ly+=ldy
    
    if kx<0:
        kx=0
        kdx=2
    if kx>640:
        kx=640
        kdx=-2
    if ky<0:
        ky=0
        kdy=2
    if ky>480:
        ky=480
        kdy=-2
    
    if lx<0:
        lx=0
        ldx=5
    if lx>640:
        lx=640
        ldx=-2
    if ly<0:
        ly=0
        ldy=2
    if ly>480:
        ly=480
        ldy=-2
    
    r+=1
    if r>255:
        r=0
        g+=1
        if g>255:
            g=0
            b+=1
            if b>255:
                b=0
    
    r1+=d1
    r2+=d2
    if r1>40:
        r1=40
        d1=-1
    if r1<0:
        r1=0
        d1=1
    if r2>40:
        r2=40
        d2=-1
    if r2<0:
        r2=0
        d2=1
    screen.blit(background, (0,0))  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False # pygame window closed by user
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False # user pressed ESC

    pressed = pygame.key.get_pressed()
    if pressed [pygame.K_i]:
        idy -= 1
    if pressed [pygame.K_k]:
        idy +=1
    if pressed [pygame.K_j]:
        idx -=1
    if pressed [pygame.K_l]:
        idx +=1
    if pressed [pygame.K_w]:
        hdy -= 1
    if pressed [pygame.K_s]:
        hdy +=1
    if pressed [pygame.K_a]:
        hdx -=1
    if pressed [pygame.K_d]:
        hdx +=1
    hx+=hdx
    hy+=hdy
    #hx*=0.95
    #hy*=0.95
    hdx*=0.95
    hdy*=0.95
    ix+=idx
    iy+=idy
    idx*=0.95
    idy*=0.95
    #ix*=0.95
    #iy*=0.95
    
    # ----- out of screen? -----
    if hx < 0:
        hx = 0
        hdx = 0.5
    if hx > 640:
        hx = 640
        hdx = -0.5
    if hy < 0:
        hy = 0
        hdy = 0.5
    if hy > 480:
        hy = 480
        hdy = -0.5
    if ix < 0:
        ix = 0
        idx = 0.5
    if ix > 640:
        ix = 640
        idx = -0.5
    if iy < 0:
        iy = 0
        idy = 0.5
    if iy > 480:
        iy = 480
        idy = -0.5
        
    # ----- critical distance? -----
    dist0 = ((hx-ix)**2 + (hy-iy)**2)**0.5
    if dist0 < minimal_distance:
        pointfactor = -1
        write(screen, "Warning! Line points too close", x=100, y=100)
    else:
        pointfactor = 1
    
    #----- collision detection -----
    #h...k  i...l
    dist1=((hx-kx)**2+(hy-ky)**2)**0.5
    dist2=((ix-lx)**2+(iy-ly)**2)**0.5
    dist3=((hx-lx)**2+(hy-ly)**2)**0.5
    dist4=((kx-ix)**2+(ky-iy)**2)**0.5
    
    if (dist1<critical or dist3<critical) and (dist2<critical or dist4<critical):
        score += 1 * pointfactor
        screen.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        
    pygame.display.set_caption("Punkte: {}".format(score))
    pygame.draw.line(screen, (r,g,b), (hx,hy), (ix, iy), random.randint(1,3))
    pygame.draw.circle(screen, (r,g,b), (int(round(kx,0)),int(round(ky,0))), r1)
    pygame.draw.circle(screen, (g,b,r), (int(round(lx,0)),int(round(ly,0))), r2)
    pygame.display.flip()      # flip the screen like in a flipbook

if score>0:    
    print("Du hast {} Punkte erreicht!".format(score))
else:
    print("Leider 0 Punkte!")
