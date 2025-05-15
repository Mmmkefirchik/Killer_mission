import wrap, time
from wrap_mENdRU.actions import set_size_percent

wrap.world.create_world(1000, 900)
wrap.add_sprite_dir('sprites')
u= wrap.sprite.add('zastavka', 500, 500, 'new_okno',visible=False)
p_p=wrap.sprite.add('zastavka', 500, 500, 'pric_in_pric',visible=False)
wrap.sprite.set_size_percent(u,250,250)
z = wrap.sprite.add('zastavka', 500, 500, 'заставка')


# k=wrap.sprite.add('zastavka',500,400,'img')
# wrap.sprite.set_size_percent(k,40,30)
nadpis = wrap.sprite.add_text(' МИССИЯ ', 500, 400, font_size=50, italic=True, text_color=(255, 250, 0), back_color=(0, 250, 250))
posledniy_pos_y = 0
posledniy_pos_x = 0


# wrap.sprite.set_size_percent(t,300,300)
@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def poxod_na_missiyo(pos_x, pos_y):
    global posledniy_pos_x,posledniy_pos_y
    c=wrap.sprite.get_costume(z)


    if wrap.sprite.exist(nadpis)==True:
        n_p = wrap.sprite.is_collide_point(nadpis, pos_x, pos_y)
        if n_p == True:
            wrap.sprite.remove(nadpis)
            wrap.sprite.set_costume(z, 'new_okno')

    if c=='new_okno':
        wrap.sprite.set_costume(z, 'игра')
        wrap.sprite.show(p_p)
        posledniy_pos_x=pos_x
        posledniy_pos_y=pos_y
        wrap.sprite.show(u)




@wrap.on_mouse_up(wrap.BUTTON_LEFT)
def spusk_pric(pos_x,pos_y):
    wrap.sprite.move_to(u,500,450)
    if wrap.sprite.exist(nadpis)==False:

        wrap.sprite.set_costume(z,'new_okno')

@wrap.on_mouse_move()
def pricelivanie(pos_x,pos_y):
    #x
    global posledniy_pos_y,posledniy_pos_x

    r=wrap.sprite.get_costume(z)
    if r!='игра' :

        return
    rasstoyanie=posledniy_pos_x-pos_x
    rasstoyanie=rasstoyanie*2.5

    wrap.sprite.move(u, rasstoyanie, 0)
    centrt_pric = wrap.sprite.get_centerx(u)

    if centrt_pric>1750:
        wrap.sprite.move_centerx_to(u,1750)

    elif centrt_pric<-1100:
        wrap.sprite.move_centerx_to(u,-1100)

    posledniy_pos_x=pos_x

    #y

    rasstoyanie=posledniy_pos_y-pos_y
    rasstoyanie=rasstoyanie*2.5
    print(rasstoyanie)

    wrap.sprite.move(u,0,rasstoyanie)
    centrt_pric = wrap.sprite.get_centery(u)


    if centrt_pric>1800:
        wrap.sprite.move_centery_to(u,1800)

    elif centrt_pric<-800:
        wrap.sprite.move_centery_to(u,-800)


    posledniy_pos_y=pos_y




