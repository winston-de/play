import play.play

cat = play.new_text('=^.^=', font_size=70)

play.screen.width = 500
play.screen.height = 500

cat_sound = play.new_sound("meow.mp3")

@play.repeat_forever
async def move_cat():
    cat.x = play.random_number(-200, 200)
    cat.y = play.random_number(-200, 200)
    cat.color = play.random_color()

    cat.show()
    await play.timer(seconds=0.4)
    cat.hide()
    await play.timer(seconds=0.4)


@cat.when_clicked
def win_function():
    cat.show()
    cat.words = 'You won!'
    cat_sound.play()


play.start_program()