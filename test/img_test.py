import play.play


play.set_backdrop('white')

text = play.new_text('text', x=10, y=10, font_size=90)
img = play.new_image('test_image.jpg', 10,10, size=10)
img2 = play.new_image('png_test.png', 70,70, size=10)
img2.turn(40)

img3 = img2.clone()
img3.x = 150
img3.y = 150

circle = play.new_circle()
c2 = circle.clone()


play.start_program()