# -*- coding: utf-8 -*-


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):
    def __init__(self, items: list[Item]):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if (
                item.name != "Aged Brie"
                and item.name != "Backstage passes to a TAFKAL80ETC concert"
            ):
                if item.name != "Sulfuras, Hand of Ragnaros":
                    self._decrease_item_quality(item)
            else:
                self._increment_item_quality(item)
                if item.name == "Backstage passes to a TAFKAL80ETC concert":
                    if item.sell_in < 11:
                        self._increment_item_quality(item)
                    if item.sell_in < 6:
                        self._increment_item_quality(item)
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.name != "Sulfuras, Hand of Ragnaros":
                            self._decrease_item_quality(item)
                    else:
                        self._kill_item_quality(item)
                else:
                    self._increment_item_quality(item)

    def _increment_item_quality(self, item: Item) -> None:
        item.quality = min(item.quality + 1, 50)

    def _decrease_item_quality(self, item: Item) -> None:
        item.quality = max(0, item.quality - 1)

    def _kill_item_quality(self, item: Item) -> None:
        item.quality = 0
