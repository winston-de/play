import unittest
import play
import sys
import pygame

from play import Oops


class TestScreenMethods(unittest.TestCase):
    def test_title(self):
        t = "Hello!"
        play.screen.title = t
        self.assertEqual(t, play.screen.title)

    def test_width(self):
        w = 400
        play.screen.width = w
        self.assertEqual(w, play.screen.width)

    def test_height(self):
        h = 900
        play.screen.height = h
        self.assertEqual(h, play.screen.height)

    def test_grid(self):
        play.screen.show_grid = True
        self.assertEqual(True, play.screen.show_grid)


def test_sprite(sp : play._SpriteBase, tst : unittest.TestCase):
    """Tests cloning of sprites"""
    sp.turn(90)
    b2 = sp.clone()
    b2.x += 20
    b2.y += 20
    tst.assertEqual(sp.x + 20, b2.x)
    tst.assertEqual(sp.y + 20, b2.y)
    tst.assertEqual(sp.angle, b2.angle)

class TestSprites(unittest.TestCase):
    def test_box(self):
        box = play.new_box("blue", 20, 20, width=20, height=20)
        box.width = 30
        box.height = 30
        self.assertEqual(35, box.right)
        self.assertEqual(5, box.bottom)
        test_sprite(box, self)

    def test_circle(self):
        cir = play.new_circle("black", 40, 40, radius=10)
        cir.radius = 15
        test_sprite(cir, self)

    def test_image(self):
        img = play.new_image("test_image.jpg", 30, 30, 100)
        img.image_filename = "png_test.png"
        test_sprite(img, self)

    def test_line(self):
        line = play.new_line("black", 30, 30, 10, 30)
        test_sprite(line, self)

class SayTests(unittest.TestCase):
    def test_line(self):
        box = play.new_box()
        txt = "a"*100
        box.say(txt)

    def test_line_spaces(self):
        box = play.new_box()
        txt = "aaaa "*10
        box.say(txt)

    def test_massive_line(self):
        box = play.new_box()
        txt = "a"*256
        with self.assertRaises(Oops):
            box.say(txt)

    def test_empty(self):
        box = play.new_box()
        box.say("")
    def test_inf(self):
        box = play.new_box()
        box.say_forever("hi")
        box.say_end()

    def test_end(self):
        box = play.new_box()
        box.say_end()

@play.when_program_starts
def start():
    # play must be initialized before we can start our tests
    unittest.main()


if __name__ == '__main__':
    play.start_program()