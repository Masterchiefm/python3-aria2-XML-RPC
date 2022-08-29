# python3-aria2-XML-RPC

Aria2 RPC client in python3.  [aria2,"The next generation download utility."](https://aria2.github.io/)


aria2py是基于Python3 写的 Aria2 RPC 客户端. aria2py通过aria2 server 的 xml-RPC接口和功能控制aria2
[中文介绍文档](https://github.com/Masterchiefm/Aria2Py/blob/main/README_zh.md)
# Description
aria2py controls aria2 via its xml-RPC interface and features.

for more info, please refer to [Aria2 official document](https://aria2.github.io/manual/en/html/aria2c.html#methods)

# Getting started
## Server(Optional)
Start aria2 with rpc in your servcer, example:
```
aria2c --enable-rpc --rpc-listen-all=true --rpc-allow-origin-all
```
If you have an existing server, this step can be skip.

## Creat your own client
clone this code. and copy Aria2Py.py into your client project directory.
```
git clone https://github.com/Masterchiefm/python3-aria2-XML-RPC.git
```
## quick start
![quick start](https://raw.githubusercontent.com/Masterchiefm/Aria2Py/main/screenshot.png)

## initiate a client
In your client directory, import Aria2Py as follow to initiate a client:

```
import Aria2Py as a2p
client = a2p.Aria2Client()
```


## set sever info
The server info will set as  **server_add="http://127.0.0.1",server_port=6800,token=""**  by default.


If you want to change them, use the following to set new info. the client will use these info to connect the remote aria2 rpc server.

```
client.setServer(server_add="http://127.0.0.1",server_port=6800,token=1234)
```

If you leave the parameters blank, the client will not change the parameter's value.

For example, you can run the following:
```
#set the server info:
client.setServer(server_add="http://127.0.0.1",server_port=6800,token=1234)

#change token only, others will not be change.
client.setServer(server_add="http://127.0.0.1",token='fuckme')
```

## Check connection
After setting server, you can simply use one function to check connection
```
client.checkConnection()
```
it will return 'Authorized' or 'Unauthorized'

## add url
After setting server, you can simply use one function to add url as follow:
```
client.addUri("https://example.com/a1.zip")
```
or 
```
download_list = ["https://example.com/a1",
                  https://example.com/a2"]
        
client.addUri(download_list)
```

then the function will return the task gid.

## For more help
type help() to get more help info, or read [aria2 offical rpc documet](https://aria2.github.io/manual/en/html/aria2c.html#rpc-interface) to get more help.


Help on module Aria2Py:
```
Help on Aria2Client in module Aria2Py object:

class Aria2Client(builtins.object)
 |  Default server address is http://127.0.0.1,
 |  default port is 6800, default token is empty
 |  
 |  Methods defined here:
 |  
 |  __init__(self)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  addTorrent(self, torrent_position, save_dir='')
 |      Open local torrent file to download. 
 |      Example:
 |          from Aria2Py import Aria2Client as client
 |          client.setServer(server_add = "http://example.com", server_port = "6800", token = "1234")
 |          client.addTorrent("t1.torrent")
 |          client.addTorrent("t2.torrent", save_dir = "/tmp/downloads")
 |          
 |      t1 will be downloaded to the default path specified in aria2.conf, while t2 will be downloaded to /tmp/downloads.
 |  
 |  addUri(self, uri, save_dir='')
 |      provide the download link (or link list) to donload. Option: provide download position
 |      uri can be a str or a list. If uri is a str, it will be converted to list.
 |      Example:
 |          from Aria2Py import Aria2Client as client
 |          client.setServer(server_add = "http://example.com", server_port = "6800", token = "1234")
 |          client.addUri("http://example.com/file1")
 |          client.addUri(uri = "http://example.com/file2", save_dir = "/tmp/downloads")
 |          client.addUri(uri = ["http://example.com/file3","http://example.com/file4","http://example.com/file5"], save_dir = "/tmp")
 |          
 |          
 |      file1 will be downloaded to the default path specified in aria2.conf, while file2 will be downloaded to /tmp/downloads.
 |      file3,4,5 will be downloaded to /tmp
 |  
 |  changeGlobalOption(self, gid, options)
 |      This method changes options of the download denoted by gid (string) dynamically.
 |      options is a struct. 
 |      option parameter example:  {'max-download-limit':'20K'}
 |  
 |  changeOption(self, gid, options)
 |      This method changes options of the download denoted by gid (string) dynamically.
 |      options is a struct. 
 |      option parameter example:  {'max-download-limit':'20K'}  
 |      
 |      Options are avalible in getOption mehtod.
 |      
 |      Example:
 |          from Aria2Py import Aria2Client as client
 |          client.changeOption("2089b05ecca3d829",{'max-download-limit':'20K'})
 |  
 |  checkConnection(self)
 |      Return connection status between aria2 server and local
 |  
 |  forceRemove(self, gid)
 |      This method removes the download denoted by gid. This method behaves just like aria2.remove()
 |      except that this method removes the download without performing any actions which take time, 
 |      such as contacting BitTorrent trackers to unregister the download first.
 |  
 |  getFiles(self, gid)
 |      This method returns the file list of the download denoted by gid (string). 
 |      The response is an array of structs.
 |  
 |  getGlobalOption(self, gid)
 |      return the global options you can modify.
 |  
 |  getGlobalStatus(self)
 |      This method returns global statistics such as the overall download and upload speeds.
 |      The response is a struct and contains the following keys. Values are strings.
 |      
 |      Speed (byte/sec).
 |      
 |      How to convert? 
 |      1 Mb/s = 1024 kb/s = 1048576 byte/s
 |      1 byte/s = 1/1048576 Mb/s
 |  
 |  getOption(self, gid)
 |      return the options of a specific job you can modify.
 |  
 |  getSessionInfo(self)
 |      This method returns session information. Session ID, which is generated each time when aria2 is invoked.
 |  
 |  getVersion(self)
 |      Return arai2 version
 |  
 |  listMethods(self)
 |      This method returns all the available RPC methods in an array of string. 
 |      This method does nothing for user but for developer.
 |      This method just returns the available methods in remote server.
 |  
 |  listNotifications(self)
 |      This method returns all the available RPC notifications in an array of string. 
 |      Unlike other methods, this method does not require secret token. 
 |      This is safe because this method just returns the available notifications names.
 |  
 |  multicall(self)
 |      This methods encapsulates multiple method calls in a single request. 
 |      methods is an array of structs. The structs contain two keys: methodName and params. 
 |      methodName is the method name to call and params is array containing parameters to the method call.
 |      This method returns an array of responses. 
 |      The elements will be either a one-item array containing the return value of the method call or a struct
 |      of fault element if an encapsulated method call fails.
 |      
 |      Example:
 |          from Aria2Py import Aria2Client as client
 |          client.setServer(server_add = "http://example.com", server_port = "6800", token = "1234")
 |          mc = client.multicall()
 |          mc.aria2.addUri(['http://example.org/file'])
 |          mc.aria2.addTorrent(xmlrpclib.Binary(open('file.torrent', mode='rb').read()))
 |          r = mc()
 |          tuple(r)
 |          
 |      then it will return such result: 
 |      ('2089b05ecca3d829', 'd2703803b52216d1')
 |  
 |  nofification(self, method='', gid='')
 |      future work.不想做
 |  
 |  pause(self, gid='')
 |      Remove a job specified by gid. If parameter gid is empty, this method will pause all.
 |  
 |  remove(self, gid)
 |      remove a job specified by gid.
 |  
 |  removeStopped(self, gid='')
 |      If gid is not specific, this method will remove all stopped jobs.
 |  
 |  saveSession(self)
 |      This method saves the current session to a file specified by the --save-session option. 
 |      This method returns OK if it succeeds.
 |  
 |  setServer(self, server_add='', server_port='6800', token='')
 |      set server info. If you leave the parameters blank, the server info will be unchanged or remained default.
 |      Example:
 |      from Aria2Py import Aria2Client as client
 |      client.setServer(server_add = "http://example.com", server_port = "6800", token = "1234")
 |  
 |  tellActive(self, keys=[])
 |      Show what is currently downloading. you can specific the outputs by giving keys(list), 
 |      or you will get all status infomation. 
 |      
 |      keys is an array of strings. If specified, the response contains only keys in the keys array. 
 |      If keys is empty or omitted, the response contains all keys. This is useful when you just want specific keys and avoid unnecessary transfers. 
 |      
 |      Example:
 |          from Aria2Py import Aria2Client as client
 |          client.setServer(server_add = "http://example.com", server_port = "6800", token = "1234")
 |          client.tellActive("2089b05ecca3d829", ["gid", "status"])
 |  
 |  tellStatus(self, gid='', keys=[])
 |      provide a specific gid to get status. you can specific the outputs by giving keys(list), 
 |      or you will get all status infomation. 
 |      
 |      keys is an array of strings. If specified, the response contains only keys in the keys array. 
 |      If keys is empty or omitted, the response contains all keys. This is useful when you just want specific keys and avoid unnecessary transfers. 
 |      
 |      Example:
 |          from Aria2Py import Aria2Client as client
 |          client.setServer(server_add = "http://example.com", server_port = "6800", token = "1234")
 |          client.tellStatus()
 |          client.tellStatus("2089b05ecca3d829")
 |          client.tellStatus("2089b05ecca3d829", ["gid", "status"])
 |  
 |  tellStopped(self, offset=0, num=512, keys=[])
 |      This method returns a list of waiting downloads, including paused ones.
 |      offset is an integer and specifies the offset from the download waiting at the front.
 |      num is an integer and specifies the max. number of downloads to be returned. 
 |      For the keys parameter, please refer to the aria2.tellStatus() method.
 |  
 |  tellWaiting(self, offset=0, num=512, keys=[])
 |      This method returns a list of waiting downloads, including paused ones.
 |      offset is an integer and specifies the offset from the download waiting at the front.
 |      num is an integer and specifies the max. number of downloads to be returned. 
 |      For the keys parameter, please refer to the aria2.tellStatus() method.
 |  
 |  unpause(self, gid='')
 |      Pause a job specified by gid.if gid is empty, this method will unpause all.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)

    
```
