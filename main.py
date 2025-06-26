import wrap, time
mode = 'menu'#igra,pric,popadanie,prpoigresh,pabada

wrap.world.create_world(1000, 900)
wrap.add_sprite_dir('sprites')
#okno 2
u= wrap.sprite.add('zastavka', 500, 500, 'new_okno',visible=False)
wrap.sprite.set_size_percent(u,250,250)
#siluats
s_bol=wrap.sprite.add('zastavka', 500, 500, 'siluat')
wrap.sprite.set_size_percent(s_bol, 112.5, 112.5)

s_bol_shir_orig=wrap.sprite.get_width_percent(s_bol)
print(s_bol_shir_orig)
wrap.sprite.set_reverse_x(s_bol,True)
# r1=wrap.sprite.add('zastavka', 500, 100, 'Ric', visible=False)
# s_p1=wrap.sprite.add('zastavka',200,200,'siluat_p')

p_p=wrap.sprite.add('zastavka', 500, 500, 'pric_in_pric',visible=False)
zastavka = wrap.sprite.add('zastavka', 500, 500, 'заставка')

#siluats big/2
# r2=wrap.sprite.add('zastavka', 500, 100, 'Ric')
# s_p2=wrap.sprite.add('zastavka',200,200,'siluat_p')
s_smal=wrap.sprite.add('zastavka', 725, 780, 'siluat',visible=False)
wrap.sprite.set_reverse_x(s_smal,True)
wrap.sprite.set_size_percent(s_smal,45,45)
s_smal_shir_orig=wrap.sprite.get_width_percent(s_smal)
print(s_smal_shir_orig)

nadpis = wrap.sprite.add_text(' МИССИЯ ', 500, 400, font_size=50, italic=True, text_color=(255, 250, 0), back_color=(0, 250, 250))

posledniy_pos_y = 0
posledniy_pos_x = 0
m = wrap.sprite.add_text('ВАША ЦЕЛЬ НА СЕГОДНЯ: ЧЕЛОВЕК В ЧЕРНОМ', 500, 250,visible=False)

n_p=None
@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def poxod_na_missiyo(pos_x, pos_y):
    global posledniy_pos_x,posledniy_pos_y,n_p,mode


    if mode=='menu':
        n_p = wrap.sprite.is_collide_point(nadpis, pos_x, pos_y)
        if n_p == True:
            mode = 'igra'
            wrap.sprite.remove(nadpis)
            wrap.sprite.set_costume(zastavka, 'new_okno')
            wrap.sprite.show(m)
            return

    if mode=='igra':
        mode='pric'
        wrap.sprite.set_costume(zastavka, 'игра')
        wrap.sprite.hide(m)
        # wrap.sprite.hide(r2)
        wrap.sprite.hide(s_smal)
        # wrap.sprite.hide(s_p2)

        print(s_smal_shir_orig)
        # wrap.sprite.show(r1)
        # wrap.sprite.show(s_p1)

        wrap.sprite.show(p_p)
        posledniy_pos_x=pos_x
        posledniy_pos_y=pos_y
        wrap.sprite.show(u)





@wrap.on_mouse_up(wrap.BUTTON_LEFT)
def spusk_pric(pos_x,pos_y):
    global  mode
    wrap.sprite.move_to(u,500,450)

    if mode!='menu':
        mode='igra'
        wrap.sprite.set_costume(zastavka, 'new_okno')
        wrap.sprite.show(s_smal)
        mesto_spr_na_krane(s_smal, s_bol)



@wrap.on_mouse_move()
def pricelivanie(pos_x,pos_y):
    #x
    global posledniy_pos_y,posledniy_pos_x,m

    l=wrap.sprite.get_costume(zastavka)
    if l!='игра' :
        return

    rasstoyanie=posledniy_pos_x-pos_x
    rasstoyanie=rasstoyanie*5

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

    wrap.sprite.move(u,0,rasstoyanie)
    centrt_pric = wrap.sprite.get_centery(u)


    if centrt_pric>1800:
        wrap.sprite.move_centery_to(u,1800)

    elif centrt_pric<-800:
        wrap.sprite.move_centery_to(u,-800)


    posledniy_pos_y=pos_y

    mesto_spr_na_krane(s_smal, s_bol)
    # mesto_spr_na_krane(r2, r1)
    # mesto_spr_na_krane(s_p2, s_p1)
def mesto_spr_na_krane(sprite_m,sprite_b):
    l=wrap.sprite.get_left(zastavka)
    v=wrap.sprite.get_top(zastavka)
    mal_kran_spr1=wrap.sprite.get_centerx(sprite_m)-l
    mal_kran_spr2=wrap.sprite.get_centery(sprite_m)-v
    mal_kran1=mal_kran_spr1*2.5
    mal_kran2=mal_kran_spr2*2.5

    ramki_bol_kran_x1=wrap.sprite.get_left(u)
    ramki_bol_kran_x2=wrap.sprite.get_top(u)

    mesto_spr_bol_kran1=ramki_bol_kran_x1+mal_kran1
    mesto_spr_bol_kran2=ramki_bol_kran_x2+mal_kran2

    wrap.sprite.move_to(sprite_b,mesto_spr_bol_kran1,mesto_spr_bol_kran2)

popatka = 15
j=False
@wrap.on_mouse_down(wrap.BUTTON_RIGHT)
def strelba():
    global j
    if j==True:
        return
    c_pricx=wrap.sprite.get_centerx(p_p)
    c_pricy=wrap.sprite.get_centery(p_p)
    j=wrap.sprite.is_collide_point(s_bol,c_pricx,c_pricy)


# @wrap

@wrap.always(30)
def szhatie():
    if j==True:
        crutilka(s_bol,s_smal,s_smal_shir_orig)




x=None
def crutilka(sprite_big,sprite_smal,orig_shir_smal):
    global x
    if x==None:
        x=orig_shir_smal*-0.05

    now_shir=wrap.sprite.get_width_percent(sprite_smal)
    print(now_shir)
    if x<0  and now_shir<=0:
        revers = wrap.sprite.get_reverse_x(sprite_smal)
        wrap.sprite.set_reverse_x(sprite_smal, not revers)
        wrap.sprite.set_reverse_x(sprite_big, not revers)
        x=orig_shir_smal*0.05

    #
    if x==orig_shir_smal*0.05 and now_shir>=orig_shir_smal:
        x=orig_shir_smal*-0.05
    p=now_shir+x
    #
    #
    wrap.sprite.set_width_percent(sprite_smal,p)

    wrap.sprite.set_width_percent(sprite_big,p*2.5)

q = wrap.sprite.add_text(str(popatka), 500, 100,False)


@wrap.always(1000)
def timer():
    global popatka
    if popatka <= 15 and popatka != -1 and n_p==True:
        wrap.sprite.show(q)
        wrap.sprite_text.set_text(q, str(popatka))
        popatka = popatka - 1

    print(popatka)



@wrap.always
def debug():
    wrap.world.set_title(mode)























# @wrap.always(1000)
# def dvig():

    # wrap.sprite.move(r2,5,0)
    # mesto_spr_na_krane(r2, r1)







import wrap_py
wrap_py.app.start()