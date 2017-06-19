# coding: utf-8
import json
import chrome_json_extens_handler as extens

def open_json(json_file):
    with open(json_file) as json_file_wrapper:
        bookmarks_dict = json.loads(json_file_wrapper.read())
    return bookmarks_dict

#working with chrome Bookmarks
d = open_json('research/Bookmarks')
#bar
#d.get('roots').get('bookmark_bar')
#main
#d.get('roots').get('other')
#mobile networks
##d.get('roots').get('synced')
#much better then that extens

#TODO look on other bookmarks and decide the structure


if __name__ == '__main__':
    extens.parse_chrome_json('research/chrome_bookmarks.json')
    #extens.print_ids_in_order()
