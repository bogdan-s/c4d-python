```
if c4d.threading.GeIsMainThread() == False:
  the_thread = c4d.threading.GeGetCurrentThread()
  Render = c4d.threadingIdentifyThread(thread) == c4d.THREADTYPE_RENDEREXTERNAL
```
