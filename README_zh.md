# python3-aria2-XML-RPC
Python3 中的 Aria2 RPC 客户端。[aria2，一款强大的开源下载实用程序。](https://aria2.github.io/)。你可以用该代码开发python3连接aria2的小程序。

# 描述
aria2py通过aria2 server 的 xml-RPC接口和功能控制aria2

更多内容请查阅[Aria2 official document](https://aria2.github.io/manual/en/html/aria2c.html#methods)

# 开始
## 启动服务段（可选）
在服务器中以 rpc 开始 aria2，例如：
```
aria2c --enable-rpc --rpc-listen-all=true --rpc-allow-origin-all
```
如果您知道现有的服务器地址及访问密码，则可以跳过此步骤。

## 在python3中创建您自己的客户
克隆此代码。并将 Aria2Py.py 复制到客户端项目目录中。
```
git clone https://github.com/Masterchiefm/python3-aria2-XML-RPC.git
```

# 快速入门
![](https://raw.githubusercontent.com/Masterchiefm/Aria2Py/main/screenshot.png)

# 启动客户端
在您的客户端目录中，按如下方式导入 Aria2Py 以启动客户端：
```
import Aria2Py as a2p
client = a2p.Aria2Client()
```
# 设置服务器信息
默认情况下，服务器信息将设置为server_add="http://127.0.0.1"，server_port=6800，token=""。

如果要更改它们，请使用以下命令设置新信息。客户端将使用这些信息来连接远程 aria2 rpc 服务器。
```
client.setServer(server_add="http://127.0.0.1",server_port=6800,token=1234)
```
如果将参数留空，客户端将不会更改参数的值。

例如，您可以运行以下命令：
```
#set the server info:
client.setServer(server_add="http://127.0.0.1",server_port=6800,token=1234)

#change token only, others will not be change.
client.setServer(server_add="http://127.0.0.1",token='fuckme')
```
# 检查连接
设置服务器后，您只需使用一个函数即可检查连接
```
client.checkConnection()
```
它将返回"Authorized"或"Unauthorized"

# 添加下载链接
设置服务器后，您只需使用一个函数即可添加URL，如下所示：
```
client.addUri("https://example.com/a1.zip")
```
或
```
download_list = ["https://example.com/a1",
                  https://example.com/a2"]
        
client.addUri(download_list)
```
则该函数将返回任务 gid。

# 更多帮助
键入 help（） 以获取更多帮助信息，或阅读 [aria2 官方 rpc 文档](https://aria2.github.io/manual/en/html/aria2c.html#rpc-interface) 以获取更多帮助。


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
