import wrap, time
from wrap_mENdRU.actions import set_size_percent

wrap.world.create_world(1000, 900)
wrap.add_sprite_dir('sprites')
z = wrap.sprite.add('zastavka', 500, 500, 'заставка')

# k=wrap.sprite.add('zastavka',500,400,'img')
# wrap.sprite.set_size_percent(k,40,30)
t = wrap.sprite.add_text(' МИССИЯ ', 500, 400, font_size=50, italic=True, text_color=(255, 250, 0),
                         back_color=(0, 250, 250))


# wrap.sprite.set_size_percent(t,300,300)
@wrap.on_mouse_up(wrap.BUTTON_LEFT)
def poxod_na_missiyo(pos_x, pos_y):
    t_p = wrap.sprite.is_collide_point(t, pos_x, pos_y)
    if t_p == True:
        wrap.sprite.hide(t)
        wrap.sprite.set_costume(z, 'new_okno')


@wrap.on_mouse_up(wrap.BUTTON_LEFT)
def perehod_pric(pos_x, pos_y):
    c=wrap.sprite.get_costume(z)

    if c=='new_okno' and :
        wrap.sprite.set_costume(z, 'игра')

    #     wrap.sprite,set_size_percent(k,35,25)
    #     time.sleep(0.1)
    #     wrap.sprite,set_size_percent(k,40,30)
    #     print(5)
