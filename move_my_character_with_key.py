from pico2d import *


TUK_WIDTH,TUK_HEIGHT = 1280,1024
open_canvas(TUK_WIDTH,TUK_HEIGHT)
tuk_ground=load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
frame = 0
dir_hori=0
dir_vert=0
face_dir=1

x,y=TUK_WIDTH//2,TUK_HEIGHT//2


def key_events():
    global running,dir_hori,dir_vert,x,y

    events=get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key==SDLK_ESCAPE:
                running = False
            elif event.key==SDLK_RIGHT:
                dir_hori+=1
                face_dir=1
            elif event.key==SDLK_LEFT:
                dir_hori-=1
                face_dir = -1
            elif event.key==SDLK_UP:
                dir_vert+=1
            elif event.key==SDLK_DOWN:
                dir_vert-=1
        elif event.type == SDL_KEYUP:
            if event.key==SDLK_ESCAPE:
                running = False
            elif event.key==SDLK_RIGHT:
                dir_hori-=1
            elif event.key==SDLK_LEFT:
                dir_hori+=1
            elif event.key==SDLK_UP:
                dir_vert-=1
            elif event.key==SDLK_DOWN:
                dir_vert+=1


    pass


while running:
    clear_canvas()

    tuk_ground.draw(TUK_WIDTH//2,TUK_HEIGHT//2)
    if dir_hori==0 and dir_vert==0:
        if face_dir==1:
            character.clip_draw(frame*100,300,100,100,x,y)
        else:
            character.clip_draw(frame * 100, 200, 100, 100, x, y)
    else:
        if face_dir==1:
            character.clip_draw(frame * 100, 100, 100, 100, x, y)
        else:
            character.clip_draw(frame * 100, 0, 100, 100, x, y)

    key_events()
    update_canvas()
    frame = (frame + 1) % 8
    x+=dir_hori*5
    y+=dir_vert*5
    delay(0.05)


close_canvas()