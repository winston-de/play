import play.play


play.set_backdrop('white')

text = play.new_text('text', x=10, y=10, font_size=90)
img = play.new_image('test_image.jpg', 10,10, size=10)
img2 = play.new_image('png_test.png', 70,70, size=10)
img2.turn(40)

img3 = img2.clone()
img3.x = 150
img3.y = 150

sp = play.new_sprite(x=-100, y=-100, costume_files=["test_image.jpg", "png_test.png"])

@play.when_any_key_pressed
def switch(key):
    sp.next_costume()
    sp.size = 10
    sp.say("Switched costume!")

# img.say("Hello!Hello!Hello!Hello!Hello!Hello!Hello !Hello!Hello!Hello!Hello!Hello!Hello!Hello!")
# circle = play.new_circle()
# c2 = circle.clone()


play.start_program()