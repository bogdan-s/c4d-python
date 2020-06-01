```
if c4d.threading.GeIsMainThread() == False:
  the_thread = c4d.threading.GeGetCurrentThread()
  Render = c4d.threadingIdentifyThread(thread) == c4d.THREADTYPE_RENDEREXTERNAL
```

### Links
* http://www.plugincafe.com/forum/forum_posts.asp?TID=10986
* https://www.c4dcafe.com/ipb/forums/topic/94605-enable-disable-gui/
* http://www.plugincafe.com/forum/forum_posts.asp?TID=12759 
