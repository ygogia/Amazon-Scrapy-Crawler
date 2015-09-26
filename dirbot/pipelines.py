from scrapy.exceptions import DropItem
class FilterWordsPipeline(object):
    """A pipeline for filtering out items which contain certain words in their
    description"""

    # put all words in lowercase
    words_to_filter = [',', ',']
    
    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['title']:
            return item
        else:
            raise DropItem("Wrong Link %s" % item)
