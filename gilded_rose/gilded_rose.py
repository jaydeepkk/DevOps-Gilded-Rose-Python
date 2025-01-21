class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self.update_item_quality(item)
            print(f"Item after update: {item}")

    def update_item_quality(self, item):
        if item.name == "Aged Brie":
            self.update_aged_brie(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            self.update_backstage_passes(item)
        elif item.name == "Sulfuras, Hand of Ragnaros":
            pass  # Sulfuras doesn't change
        else:
            self.update_normal_item(item)

    def update_aged_brie(self, item):
        if item.quality < 50:
            item.quality += 1
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality < 50:
            item.quality += 1

    def update_backstage_passes(self, item):
        if item.quality < 50:
            item.quality += 1
            if item.sell_in < 11 and item.quality < 50:
                item.quality += 1
            if item.sell_in < 6 and item.quality < 50:
                item.quality += 1
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = 0

    def update_normal_item(self, item):
        if "Conjured" in item.name:
            degrade_rate = 2  
        else:
            degrade_rate = 1
        if item.quality > 0:
            item.quality -= degrade_rate
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= degrade_rate
