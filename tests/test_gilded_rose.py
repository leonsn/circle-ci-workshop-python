# -*- coding: utf-8 -*-
import unittest
import sys
sys.path.append("..")
from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)

    def test_old_brie(self):
        items = [Item("Aged Brie", 0, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertTrue("Brie is now of a higher quality", items[0].quality > 1)

    def test_never_over_50(self):
        items = [Item("Aged Brie", 0, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertTrue("Brie should not be able to have a higher quality than 50", items[0].quality == 50)

    def test_bar(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo_bar", items[0].name)





if __name__ == '__main__':
    unittest.main()
