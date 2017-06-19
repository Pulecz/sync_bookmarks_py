# sync_bookmarks_py - Bookmarks Synchronization using python

Maybe alternative for Xmarks?
Simplified one, probably will not support removing bookmarks from current session.

Similarly like with KeePassX, this tool should allow you to share your main bookmarks:

* in whatever format (write it yourself)
* in one (or more) file
* encrypted (or not)
* ..

Idea is you import your current bookmarks (html flavours, json,...)...
#TODO study formats a bit

... then after you do some browsing and have some bookmarks to add, you pass it
to the script again which will eat it.

This will obviously require either manual work because when adding sync you need to:

### Adding stuff

export to the bookmarks and pass it to the script
```pythonified_`bash
supported_browsers='firefox','chromium','vivaldi'
${supported_browsers[0]} --export bookmarks.json #or html
sybo.py --crunch bookmark.json -O synced_bookmarks.json
```

### Getting stuff

get your synced_bookmarks.json on different device either with git, gdrive, whateverBOX, etc.

```pythonified_bash
${supported_browsers[0]} --import synced_bookmarks.json #or html
```

PROBLEM: how do browsers behave when you constantly import them bookmarks?

Isn't it better to just delete the bookmarks and "reflash" it with new ones?

# Extension

Since I have no idea yet if most browsers supports --export --import and
majority of people don't have some bash scripts to automate stuff for
themselves, the idea of extension is which would probably work best.

Ext could either be semi-automatic, so you would just click button and select
import/export or totally automatic, by selecting which file to look for and
replace curent bookmarks with the new ones.

Ideally the extension should compare those two bookmarks and tell user which
will be removed and what will be added.

But if user is sure that they only want to get the synced_bookmarks and dump
whatever is on local, just force it.

# Ideas

working with bookmarks, sorting, removing duplicates
