define persistent.mod_anton_pelmeni_endings = set()

init -505 python:
    Mod.episodes.add(ModEpisode("Антон и Пельмени", "_BrenD_", "anton_pelmeni_start", "mod/anton_pelmeni/images/icon.png", "1.0", "https://www.youtube.com/channel/UCATCV8pfte6-lyUy0sjGXUQ"))


image all = im.Scale("mod/anton_pelmeni/images/kitchen/all.jpg", 1920, 1080)
image clear = im.Scale("mod/anton_pelmeni/images/kitchen/clear.jpg", 1920, 1080)
image with_pan = im.Scale("mod/anton_pelmeni/images/kitchen/with_pan.jpg", 1920, 1080)
image with_board = im.Scale("mod/anton_pelmeni/images/kitchen/with_board.jpg", 1920, 1080)

image pelmeni = im.Scale("mod/anton_pelmeni/images/kitchen/pelmeni.png", 1920, 1080)

image fire = Animation(
    "mod/anton_pelmeni/images/kitchen/fire/fire_0.png", 0.30,
    "mod/anton_pelmeni/images/kitchen/fire/fire_1.png", 0.15,
    "mod/anton_pelmeni/images/kitchen/fire/fire_3.png", 0.20,
    "mod/anton_pelmeni/images/kitchen/fire/fire_2.png", 0.25,
) 
image all_turn_on = LiveComposite((1920, 1080), 
    (0, 0), im.Scale("mod/anton_pelmeni/images/kitchen/all_turn_on.jpg", 1920, 1080),
    (0, 0), "fire",
)

image pan = im.Scale("mod/anton_pelmeni/images/kitchen/pan.png", 1920, 1080)
image board_with_pelmeni = im.Scale("mod/anton_pelmeni/images/kitchen/board_with_pelmeni.png", 1920, 1080)

image end_no = im.Scale("mod/anton_pelmeni/images/kitchen/end/no.jpg", 1920, 1080)
image end_early = im.Scale("mod/anton_pelmeni/images/kitchen/end/early.jpg", 1920, 1080)
image end_good = im.Scale("mod/anton_pelmeni/images/kitchen/end/good.jpg", 1920, 1080)
image end_late = im.Scale("mod/anton_pelmeni/images/kitchen/end/late.jpg", 1920, 1080)

image chose_button_none = im.Alpha("interface/intercative_button.png", 0.8)
image plashka = "interface/main_meny/plaska.png"

image results_background = im.Scale("mod/anton_pelmeni/images/kitchen/results_background.jpg", 1920, 1080)

init -506 screen brunch_buton_text(Text):
    text _(Text):
        style "imagemap_text"
        color "#ffffff"
        outlines [ (absolute(1), "#000000", absolute(0), absolute(0)) ]
        at conf_fon

init -506 screen branch_button_fullscreen(Image, Action, Position, Size):
    use branch_button(Image, Action, Position, Size, (0, 0), (1920, 1080)):
        transclude

transform brunch_button_show():
    alpha 0.0
    easeout 0.05 alpha 1.0
transform brunch_button_hide():
    alpha 1.0
    easeout 0.05 alpha 0.0

init -506 screen branch_button(Image, Action, Position, Size, ImagePosition, ImageSize):
    default hover_image = im.MatrixColor(renpy.get_registered_image(Image), im.matrix.brightness(0.20))
    default hover = BoolVaraible(False)

    add hover_image:
        if hover:
            at brunch_button_show
        else: 
            at brunch_button_hide
        
        pos ImagePosition
        xysize ImageSize

    button:
        pos Position
        xysize Size
        hovered hover.true
        unhovered hover.false
        
        hover_sound "sounds/menu/button-click-4.ogg"
        action Action

        transclude

init -506 screen stylized_button_transparent(Text, Position, Action):
    frame:   
        style_prefix "main_menu"
        pos Position
        xsize 300
        ysize 60
        background Null()    
        textbutton _(Text):
            xsize 300
            xoffset -10
            action Action
        button:
            background Frame("plashka")
            xsize 300
            text _(Text):
                xoffset -10
            at mm_but
            action Action

init -506 screen stylized_button_filled(Text, Position, Action):
    frame:   
        style_prefix "main_menu"
        pos Position
        xsize 300
        ysize 60
        background Null() 
        button:
            background Frame("plashka")
            xsize 300
            text _(Text):
                xoffset -10
            at filepic_but
            action Action

define state = set()
define stage = 0
define put_pelmeni_time = -1

transform alpha(Delay):
    alpha 0.0
    linear Delay
    linear 1 alpha 1.0
    linear 2
    linear 0.5 alpha 0.0

screen intro():
    use stylized_button_transparent("Пропустить", (1610, 20), [ Return() ])

    text _("{color=#e4422d}{size=+20}ДИСКЛЕЙМЕР:{/size}{/color}\nЭто неофициальный фрагмент и его сюжет не имеет никакого отношенния к оригинальной истории и реальным событиям. Также разработчики дали добро на разработку и распространение данной подделки."):
        at alpha(0.5)
        xalign 0.5
        yalign 0.5
        text_align 0.5
        xysize (1000, 600)
        size 70

    button:
        at alpha(4)
        xalign 0.5
        yalign 0.5
        yoffset -250
        text _("Мод создал:\n{size=+20}_BrenD_{/size}"):
            size 70
            text_align 0.5
            hover_underline True
            hover_color "#285999"
        action OpenURL("https://www.youtube.com/channel/UCATCV8pfte6-lyUy0sjGXUQ")
    image "mod/anton_pelmeni/images/brend.png":
        at alpha(4)
        xalign 0.5
        yalign 0.5
        yoffset 50
        xysize (409, 401)

    text _("Эпизод: Антон и Пельмени"):
        at alpha(7.5)
        xalign 0.5
        yalign 0.5
        text_align 0.5
        size 120

    timer 12 action Return()


screen bring_choose(has_pelmeni, has_pan):
    if "pelmeni" in state and "pan" in state:
        on "show" action Jump("anton_pelmeni_start.brought_all")

    if not has_pelmeni:
        use branch_button("chose_button_none", [ Jump("anton_pelmeni_start.bring_pelmeni") ], (955, 305), (647, 254), (955, 285), (647, 300)):
            use brunch_buton_text("ДОСТАТЬ ПЕЛЬМЕНИ")
    
    if not has_pan:
        use branch_button("chose_button_none", [ Jump("anton_pelmeni_start.bring_pan") ], (380, 300), (460, 345), (360, 300), (500, 345)):
            use brunch_buton_text("ДОСТАТЬ КАСТРЮЛЮ")

screen trun_on_cooker():
    use branch_button("chose_button_none", [ Jump("anton_pelmeni_start.turn_on") ], (645, 640), (360, 276), (605, 640), (400, 276)):
        use brunch_buton_text("ВКЛЮЧИТЬ")

screen wait_or_put_pelmeni():
    use branch_button("chose_button_none", [ Jump("anton_pelmeni_start.wait") ], (425, 285), (360, 276), (405, 285), (400, 276)):
        use brunch_buton_text("ПОДОЖДАТЬ")

    use branch_button_fullscreen("board_with_pelmeni", [ Jump("anton_pelmeni_start.put_pelmeni") ], (1075, 285), (360, 276)):
        use brunch_buton_text("ЗАКИНУТЬ")

screen wait_or_end():
    use branch_button("chose_button_none", [ Jump("anton_pelmeni_start.wait") ], (1075, 285), (360, 276), (1055, 285), (400, 276)):
        use brunch_buton_text("ПОДОЖДАТЬ")

    use branch_button_fullscreen("pan", [ Jump("anton_pelmeni_start.end") ], (425, 285), (360, 276)):
        use brunch_buton_text("ДОСТАТЬ")


transform time_background:
    alpha 0.0
    linear 0.5 alpha 1.0
    linear 2
    linear 0.5 alpha 0.0

transform time_text:
    alpha 0.0
    linear 0.25
    linear 0.5 alpha 1.0
    linear 1.75
    linear 0.5 alpha 0.0

define time_pass_map = [
    [ 5, "" ],
    [ 5, "" ],
    [ 5, "" ],
    [ 4, "ы" ],
    [ 4, "ы" ],
]

screen time_pass(Time, Sufix):
    add "#000": 
        at time_background

    text _("Спустя " + str(Time) + " минут" + Sufix):
        style "imagemap_text"
        color "#fff"
        size 80
        at time_text

    timer 3 action Return()

transform results_alpha:
    alpha 0.0
    linear 1.0 alpha 1.0

screen results(Ending_name, Rating):
    default endings_count = 4
    
    default revealed_endings_count = len(persistent.mod_anton_pelmeni_endings)

    image "results_background":
        at results_alpha

    button:
        pos (20, 980)
        text _("Мод создал: _BrenD_"):
            size 70
            hover_underline True
            hover_color "#285999"
        action OpenURL("https://www.youtube.com/channel/UCATCV8pfte6-lyUy0sjGXUQ")
        at results_alpha

    default text_color = "#fff"
    if Rating == "Отлично":
        $ text_color = "#42d042"
    elif Rating == "Плохо":
        $ text_color = "#d06842"
    elif Rating == "Очень плохо":
        $ text_color = "#d04242"
    elif Rating == "Сойдёт":
        $ text_color = "#d0af42"

    text _("Концовка:\n{vspace=-40}{size=+30}[Ending_name]{/size}\n{vspace=30}{size=-20}{color=[text_color]}[Rating]{/color}\nОткрыто концовок: [revealed_endings_count]/[endings_count]"):
        xalign 0.5
        yalign 0.5
        text_align 0.5
        yoffset -50
        size 90
        at results_alpha

    hbox:
        xalign 0.5
        yalign 0.5
        yoffset 230
        spacing 50
        use stylized_button_filled("Переиграть", (0, 0), [ Jump("anton_pelmeni_start") ])
        use stylized_button_filled("Меню", (0, 0), [ MainMenu(confirm=False) ])
        at results_alpha


label anton_pelmeni_start:
    scene black with Dissolve(0.3)
    call ._reset
    jump .intro

    label ._reset:
        $ stage = 0
        $ put_pelmeni_time = -1
        $ state.clear()
        stop fon
        stop music

        return
    
    label .intro:
        scene black with Dissolve(0.3)
        call screen intro
        jump .begin

    label .begin:
        play music "music/1_Melancholy(Tiny_Bunny).ogg" fadein 0.5
        scene clear with Dissolve(1)

        "Школа выматывает."
        "Очень хочется есть, но на плите ничего не было."
        "Странно. Мама всегда приготовит то пюрешку, то солянку или хоть ту же кашу."
        "Может она считает, что я уже самостоятелен и смогу себя накормить?"
        "Помню, в холодильнике лежат пельмени."
        "Так и хочется их съесть."
        "Ладно, хватит мечтать, нужно приступать."

        $ state.clear()
        call screen bring_choose(False, False)

    label .current_background():
        $ has_pan = "pan" in state;
        $ has_pelmeni = "pelmeni" in state;

        if has_pan and has_pelmeni:
            scene all 
            show pelmeni
            with Dissolve(0.3)
        elif has_pan:
            scene with_pan with Dissolve(0.3)
        else:
            scene with_board 
            show pelmeni
            with Dissolve(0.3)

        return

    label .bring_pan:
        $ state.add("pan")
        "Набираем кастрюлку воды. Вот так до середины."
        play sound "sounds/Krizka.ogg"
        call .current_background
        "Готово. "

        call screen bring_choose(False, True)

    label .bring_pelmeni:
        $ state.add("pelmeni")
        play sound "sounds/desk-close-00.ogg"
        call .current_background
        "Пельмешки. Ручная работа!"

        call screen bring_choose(True, False)

    label .brought_all:
        scene all
        show pelmeni

        "Все на месте. Можно приступать."
        call screen trun_on_cooker()

    label .turn_on:
        window hide
        play sound "mod/anton_pelmeni/sounds/podzhiganie-gazovoj-plity.mp3"
        scene all_turn_on
        show pelmeni
        with Dissolve(0.3)
        play fon "mod/anton_pelmeni/sounds/zvuk-utechki-gaza.mp3" loop volume 0.7

        $ renpy.pause(0.7)
        window auto
        
        call screen wait_or_put_pelmeni()

    label .wait:
        $ stage += 1

        $ renpy.jump("anton_pelmeni_start.wait_" + str(stage))

    label .put_pelmeni:
        $ stage += 1
        $ put_pelmeni_time = stage

        play sound "mod/anton_pelmeni/sounds/Splash-8CloseDistance-www.FesliyanStudios.com.mp3"
        hide pelmeni with Dissolve(0.3)

        if put_pelmeni_time == 1:
            "Сразу закинул пельмени."
            "А чего ждать?"
        elif put_pelmeni_time == 2:
            "Закинул пельмени в тёплую воду."
        elif put_pelmeni_time == 3:
            "Вода хорошо закипела. Должны получится отличные пельмени."
        else:
            "Осталось очень мало воды."
        
        "Посолил и добавил специй."
        "Ждём..."

        jump .next_stage

    label .wait_1:
        "Нужно подождать, дать воде нагреться"

        jump .next_stage

    label .after_1():
        if put_pelmeni_time == -1:
            "Начинает закипать."
        else:
            "Пельмешки осели на дно."
            "Начинают появляться пузырьки."

        return

    label .wait_2:
        if put_pelmeni_time == -1:
            "Подожду ещё немного. Пусть хорошо закипит."
        else:
            "Подожду. Пельмешкам нужно время, чтобы сварится."
            "Не буду ж я их сырыми есть."

        jump .next_stage

    label .after_2():
        if put_pelmeni_time == -1:
            "Кипит."
            "Стоит ли сейчас кидать пельмени?"
        elif put_pelmeni_time == 1:
            "Ещё не всплывают."
            "Помню мама говорила, что их нужно доставать когда они все всплывут."
            "Может я ошибаюсь?"
        else:
            "Всё выглядит нормально. Только..."
            "Не мопню, их нужно кидать в теплую воду или когда она закипит?"
            "В любом случаии, не буду ж я их выкидывать."
            "Не может же такая мелочь испортить Домашние мамины пельмени."

        return

    label .wait_3:
        if put_pelmeni_time == -1:
            "Думаю, нет."
            "Набирал ледяную воду. Дам ей ещё времени."
        elif put_pelmeni_time == 1:
            "НЕТ! Не может такого быть!"
            "Я точно помню мамины слова."
            "Лучше ещё подождать."
        else:
            "Жду пока не всплывут."
            "Главное, чтобы не убежали"

        jump .next_stage

    label .after_3():
        if put_pelmeni_time == -1:
            "Половина воды выкипела."
        elif put_pelmeni_time == 1:
            "Начали всплывать. Но..."
            "Некоторые пельмени потеряли свою тестовую защиту."
            "Может их уже стоит доставать, чтобы минимизировать потери?"
        elif put_pelmeni_time == 2:
            "Все на месте. Потихоньку начали всплывать."
            "Что делать дальше? Ждать?"
            play sound "mod/anton_pelmeni/sounds/zvuk-urchanija-v-zhivote.mp3"
            "{i}*урчания желудка*"
            "Выбор не из прочтых"
        else:
            "Очень хочется есть."
            "Заглянул в кастрюлю - все на месте."
            play sound "mod/anton_pelmeni/sounds/zvuk-urchanija-v-zhivote.mp3"
            "{i}*урчания желудка*"
            "Поскорее б они сварились"

        return

    label .wait_4:
        if put_pelmeni_time == -1:
            "Ждём..."
        elif put_pelmeni_time == 1:
            "Смерившысь с потерями решил: \nНужно подождать, чтобы гарантировать, что все пельмени были готовыми, и, что сырых нету"
        elif put_pelmeni_time == 2:
            "Как бы сильно не бурчал жылудок, решил подождать ещё чуток."
            "Пусть все всплывут."
        else:
            "Пельмени должны вариться 7-9 минут. Тогда можно добится истиного вкуса пельмений."
            "Нужно лишь потерпеть."
            "Пусть ребята ещё полежат."

        jump .next_stage

    label .after_4():
        if put_pelmeni_time == -1:
            "В кастрюле закончилась вода."
            jump .end
        elif put_pelmeni_time == 1:
            "Потери слишком велики, нужно срочно доставать"
            jump .end
        elif put_pelmeni_time == 2:
            "Все всплыли. Видно как плавает тесто."
            "Может стоит уже достать?"
        elif put_pelmeni_time == 3:
            "Наши ребята уже всплыли. Видимо не понравилось на дне лежать."
            "Выглядит аппетитно."
            "Может достать и приютить их в желудке?"
        else:
            "Слабо верится, что получится сварить пельмени. Слишком мало воды осталось."

        return

    label .wait_5:
        if put_pelmeni_time == 2:
            "НЕТ."
            "Незная почему, я решил подождать ещё какое-то время"
        elif put_pelmeni_time == 3:
            "Я не мог отвести от них взгляд. Они были слишком апетитными."
            "В мыслях я представлял как кладу в рот один пельмень за другим."
        else:
            "Остается только ждать."

        jump .next_stage

    label .after_5():
        if put_pelmeni_time == 2:
            "Уже нет времени ждать. Пора доставать."
        elif put_pelmeni_time == 3:
            "Не заметел как протело время."
            "Тесто полопалось, нужно доставать."
        else:
            "Вода закончилась. Нужно доставать."

        return

    label .next_stage:
        play sound "mod/anton_pelmeni/sounds/tikanie.ogg"
        call screen time_pass(*time_pass_map[stage - 1])

        $ renpy.call("anton_pelmeni_start.after_" + str(stage))

        if stage >= 5:
            jump .end


        if put_pelmeni_time == -1:
            call screen wait_or_put_pelmeni()
        else:
            call screen wait_or_end()

    label .end:
        play sound "sounds/sfx_sit_down.ogg"
        stop fon
        play music "music/11_Poryadok.ogg"
        if put_pelmeni_time == -1:
            jump .end_no_water
        elif stage == 4 and put_pelmeni_time == 3:
            jump .end_good
        elif stage - put_pelmeni_time <= 1:
            jump .end_early
        else:
            jump .end_late

    label .end_early:
        scene end_early with Dissolve(0.3)
        "Твердые!"
        "Видимо не доварились."
        "Рано достал и испортил пельмени."
        "В следующий раз точно получится."

        call ._save_ending("Рано достал", "Плохо")

    label .end_good:
        "Хорошая идея"
        scene end_good with Dissolve(0.3)
        "Получились отличные пельмени."
        "Вкусные, сочные!"
        "То, что нужно было для хорошего обеда."

        call ._save_ending("Идеальный пельмень", "Отлично")

    label .end_late:
        scene end_late with Dissolve(0.3)
        "Тесто сильно розмякло."
        "Немного переварил."
        "Думаю, есть можно."

        call ._save_ending("Передержал", "Сойдёт")

    label .end_no_water:
        scene end_no with Dissolve(0.3)
        "Дождался! Останусь голодным."
        "В следующий раз точно получится."

        call ._save_ending("Дождался", "Очень плохо")

    label ._save_ending(Ending_name, Rating):
        if (Ending_name in persistent.mod_anton_pelmeni_endings) == False:
            $ persistent.mod_anton_pelmeni_endings.add(Ending_name)
            $ renpy.save_persistent()

        scene black with Dissolve(0.3)
        call screen results(Ending_name, Rating)
        return
