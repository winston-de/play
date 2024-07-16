import play.play

cat = play.new_text('=^.^=', font_size=70)

play.screen.width = 849
play.screen.height = 812
play.screen.title = "Meow!"
play.screen.show_grid = True
play.set_backdrop("white")

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
    play.send_message("hi")


@play.when_messaged_received("hi")
def test():
    print("Got it!")

@play.when_any_message_received
def message(name):
    print(name)


play.start_program()