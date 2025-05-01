import wrap, time
from wrap_mENdRU.actions import set_size_percent

wrap.world.create_world(1000, 900)
wrap.add_sprite_dir('sprites')
u= wrap.sprite.add('zastavka', 500, 500, 'new_okno',visible=False)
wrap.sprite.set_size_percent(u,250,250)
z = wrap.sprite.add('zastavka', 500, 500, 'заставка')


# k=wrap.sprite.add('zastavka',500,400,'img')
# wrap.sprite.set_size_percent(k,40,30)
t = wrap.sprite.add_text(' МИССИЯ ', 500, 400, font_size=50, italic=True, text_color=(255, 250, 0),
                         back_color=(0, 250, 250))


# wrap.sprite.set_size_percent(t,300,300)
@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def poxod_na_missiyo(pos_x, pos_y):
    c=wrap.sprite.get_costume(z)

    if wrap.sprite.exist(t)==True:
        t_p = wrap.sprite.is_collide_point(t, pos_x, pos_y)
        if t_p == True:
            wrap.sprite.remove(t)
            wrap.sprite.set_costume(z, 'new_okno')

    if c=='new_okno':
        wrap.sprite.set_costume(z, 'игра')
        wrap.sprite.show(u)



@wrap.on_mouse_up(wrap.BUTTON_LEFT)
def spusk_pric(pos_x,pos_y):
    if wrap.sprite.exist(t)==False:
        wrap.sprite.set_costume(z,'new_okno')

