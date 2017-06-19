# coding: utf-8
import json

def open_json(json_file):
    with open(json_file) as json_file_wrapper:
        bookmarks_dict = json.loads(json_file_wrapper.read())
    return bookmarks_dict

def search_by_id_in(bookmarks_dict, input_id, failed_return=None):
    for bookmark in bookmarks_dict:
        if bookmark.get('id') == str(input_id):
            return bookmark
    if not failed_return is None:
        return '{} {}'.format(failed_return, input_id)

def search_by_parentId_in(bookmarks_dict, parrentId):
    for bookmark in bookmarks_dict:
        if bookmark.get('parrentId') == str(parentId):
            return bookmark

def parse_chrome_json(chrome_bookmarks_json_file):
    """using this extens:
    https://chrome.google.com/webstore/detail/export-historybookmarks-t/dcoegfodcnjofhjfbhegcgjgapeichlf
    """
    bookmarks_dict = open_json(chrome_bookmarks_json_file)
    #bookmarks_dict is a list
    for bookmark in bookmarks_dict:
        #bookmarks is dict, with keys..
        ##for key, value in bookmark.items():
        #if it has not url, so its probably a FOLDER
        if not bookmark.get('url'):
            print('FOLDER')
            print(bookmark)
            print('parrentId', search_by_id_in(bookmarks_dict, bookmark.get('parentId'), 'No id'))
            input('hit enter to continue...')
            ##break #nothing else to do here
        else:
            print('URL')
            print(bookmark)
            input('hit enter to continue...')

def get_highest_id_in(bookmarks_dict, limit=9999, break_limit=100):
    for_max = []
    for index in range(0, limit):
        bookmark = search_by_id_in(bookmarks_dict, index)
        if bookmark:
            for_max.append(int(bookmark.get('id')))
        else:
            #if too many Nones, just break
            if break_limit == 0:
                break
            break_limit -= 1

    return max(for_max)

def print_ids_in_order():
    bookmarks_dict = open_json('research/chrome_bookmarks.json')
    highest = get_highest_id_in(bookmarks_dict)
    print('got highest id:',highest,'\n hit enter to print every url')
    input()
    for index in range(0, highest):
        print(search_by_id_in(bookmarks_dict, index))
