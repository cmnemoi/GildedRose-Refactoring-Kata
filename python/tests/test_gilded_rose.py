# -*- coding: utf-8 -*-

from gilded_rose import Item, GildedRose


def test_perempted_item_should_degrade_twice_as_fast() -> None:
    # given perempted item
    perempeted_item = Item("product", -1, 2)

    # when i update item quality
    guilded_rose = GildedRose([perempeted_item])
    guilded_rose.update_quality()

    # then perempted item quality should be 0
    assert perempeted_item.quality == 0


def test_item_quality_cannot_be_negative() -> None:
    # given item
    items = [Item(f"product", sell_in=50, quality=0)]

    GildedRose(items).update_quality()

    assert items[0].quality == 0


def test_aged_brie_raises_quality() -> None:
    aged_brie = Item("Aged Brie", sell_in=50, quality=0)

    GildedRose([aged_brie]).update_quality()

    assert aged_brie.quality == 1


def test_quality_cannot_be_more_than_fifty() -> None:
    aged_brie = Item("Aged Brie", sell_in=0, quality=50)

    GildedRose([aged_brie]).update_quality()

    assert aged_brie.quality == 50


def test_sulfuras_does_not_lose_quality() -> None:
    sulfuras = Item("Sulfuras, Hand of Ragnaros", sell_in=0, quality=50)

    GildedRose([sulfuras]).update_quality()

    assert sulfuras.quality == 50


def test_backstage_quality_raises_quality() -> None:
    backstage = Item("Backstage passes to a TAFKAL80ETC concert", sell_in=50, quality=0)

    GildedRose([backstage]).update_quality()

    assert backstage.quality == 1


def test_backstage_quality_raises_two_quality_when_sell_in_less_than_10() -> None:
    backstage = Item("Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=0)

    GildedRose([backstage]).update_quality()

    assert backstage.quality == 2


def test_backstage_quality_raises_three_quality_when_sell_in_less_than_5() -> None:
    backstage = Item("Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=0)

    GildedRose([backstage]).update_quality()

    assert backstage.quality == 3


def test_backstage_quality_is_zero_when_sell_in() -> None:
    backstage = Item("Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=10)

    GildedRose([backstage]).update_quality()

    assert backstage.quality == 0
