# Mon 19.jun 10:55:55 - 12017

basic idea in README.md

to start with sobo.py lets figure out some way (best if automatic, but not important now)
to get bookmarks, ideally in json (html too, but that later, other formarts??)

for browsers
* firefox - places sqlite db, should be ok with json too
* chromium/google-chrome local thing, or even exported from google cloud itself
  * meh only html supported, then there is this for JSON https://chrome.google.com/webstore/detail/export-historybookmarks-t/dcoegfodcnjofhjfbhegcgjgapeichlf
    * basic loop done
  * TODO parsing html
  * meh just pass whatver is in ~.config/chromium/Default/Bookmarks
* qutebrowser super simple format for both regular and normal quickmarks
* vivaldi, its chromium

then load them and work with them

# TODO
* do proper investagiation of all bookmarks formats and decide data structure
