### Geral

* Python GUI libraries (such as PyQt and PySide) is not official supported. I am also unable to find any reference or someone who was successful integrating th GUI libraries/
* Accessing Data http://www.plugincafe.com/forum/forum_posts.asp?TID=5428
* Populate User Data http://www.plugincafe.com/forum/forum_posts.asp?TID=11606
* Creating User Data http://www.plugincafe.com/forum/forum_posts.asp?TID=8420
* using user data buttons in python [SOLVED] http://www.plugincafe.com/forum/forum_posts.asp?TID=11938
* Getting the description of a user ID https://plugincafe.maxon.net/topic/7851/10167_getting-user-data-descid-issue-resolved/3
* Adding User Data http://blog.grooff.eu/?p=224
https://plugincafe.maxon.net/topic/11469/add-remove-groups-of-user-data/4
* IMO. It’s very important to understand how UD works. And that requires seeing the containers in their raw form without any python covering them up.
* Once you know how the containers work. Then the users can write code in a more pythonic manner if they wish. But they need to know how it works first.
* If you are referring to the “Default Open” option for UD groups.
* The ID for that one isn’t: c4d.DESC_GUIOPEN
* It’s: c4d.DESC_DEFAULT the interface drop down is referring to the descriptions customgui flag. be sure to pass valid data, you can crash c4d with invalid description elements.
* You don’t need to retrieve the userdataIDcontainer.
* Just have it as op[userdatacontainer] and it should work

### Links
http://www.plugincafe.com/forum/forum_posts.asp?TID=13629 (Iterate user data Iterate)
Dynamic Real Input Xpresso ( https://forums.cgsociety.org/t/python-real-input-xpresso/1586911/3)
Add Port
http://www.plugincafe.com/forum/forum_posts.asp?TID=13268 (Boolean User Data but the GUI is Button)
Botton Press again http://www.plugincafe.com/forum/forum_posts.asp?TID=12182
http://www.plugincafe.com/forum/forum_posts.asp?TID=10986
https://www.c4dcafe.com/ipb/forums/topic/94605-enable-disable-gui/
 
http://www.plugincafe.com/forum/forum_posts.asp?TID=12759 
