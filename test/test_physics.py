import play

sprite = play.new_circle(color='gray', radius=20)
sprite.start_physics(obeys_gravity=True, bounciness=0,stable=True, friction=0)

rect = play.new_box(color='blue', width=20, height=30, x=50, y=50)
rect.start_physics(obeys_gravity=True, stable=False)

img = play.new_image('test_image.jpg', 10,10, size=10)
img.start_physics(obeys_gravity=True, stable=False)

play.new_text()

play.start_program()