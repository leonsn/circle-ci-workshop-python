# -*- coding: utf-8 -*-
import unittest
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/code/")
from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_old_brie(self):
        items = [Item("Aged Brie", 0, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertTrue("The quality of the Aged Brie should " \
                "increase during quality update", items[0].quality > 1)

    def test_never_over_50(self):
        items = [Item("Aged Brie", 0, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertTrue("Brie should not be able to have a higher " \
                "quality than 50", items[0].quality == 50)



if __name__ == '__main__':
    unittest.main()
