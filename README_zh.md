# Aria2Py
Python3 中的 Aria2 RPC 客户端。[aria2，一款强大的开源下载实用程序。](https://aria2.github.io/)。你可以用该代码开发python3连接aria2的小程序。

# 描述
aria2py通过aria2 server 的 xml-RPC接口和功能控制aria2

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
git clone https://github.com/Masterchiefm/Aria2Py.git 
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
client.set_server(server_add="http://127.0.0.1",server_port=6800,token=1234)
```
如果将参数留空，客户端将不会更改参数的值。

例如，您可以运行以下命令：
```
#set the server info:
client.set_server(server_add="http://127.0.0.1",server_port=6800,token=1234)

#change token only, others will not be change.
client.set_server(server_add="http://127.0.0.1",token='fuckme')
```
# 检查连接
设置服务器后，您只需使用一个函数即可检查连接
```
client.check_connection()
```
它将返回"授权"或"未经授权"

# 添加下载链接
设置服务器后，您只需使用一个函数即可添加URL，如下所示：
```
client.add_uri("https://example.com/a1.zip")
```
或
```
download_list = ["https://example.com/a1",
                  https://example.com/a2"]
        
client.add_uri(download_list)
```
则该函数将返回任务 gid。

# 更多帮助
键入 help（） 以获取更多帮助信息，或阅读 [aria2 官方 rpc 文档](https://aria2.github.io/manual/en/html/aria2c.html#rpc-interface) 以获取更多帮助。

模块 Aria2Py 上的帮助：
```
   class Aria2Client(builtins.object)
     |  Default server address is http://127.0.0.1,
     |  default port is 6800, default token is empty
     |  
     |  Methods defined here:
     |  
     |  __init__(self)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  add_Torrent(self, torrent_position, position='')
     |      upload torrent file to download. 
     |      <<WARING>>
     |      This function is not tested!!!
     |  
     |  add_uri(self, uri, position='')
     |      provide the download link (or link list) to donload. Option: provide download position
     |  
     |  change_global_option(self, gid, options)
     |      This method changes options of the download denoted by gid (string) dynamically.
     |      options is a struct. 
     |      option parameter example:  {'max-download-limit':'20K'}
     |  
     |  change_option(self, gid, options)
     |      This method changes options of the download denoted by gid (string) dynamically.
     |      options is a struct. 
     |      option parameter example:  {'max-download-limit':'20K'}
     |  
     |  check_connection(self)
     |  
     |  force_remove(self, gid)
     |      This method removes the download denoted by gid. This method behaves just like aria2.remove()
     |      except that this method removes the download without performing any actions which take time, 
     |      such as contacting BitTorrent trackers to unregister the download first.
     |  
     |  get_files(self, gid)
     |      This method returns the file list of the download denoted by gid (string). 
     |      The response is an array of structs.
     |  
     |  get_global_option(self, gid)
     |      return the global options you can modify.
     |  
     |  get_global_status(self)
     |      speed (byte/sec).
     |  
     |  get_option(self, gid)
     |      return the options of a specific job you can modify.
     |  
     |  get_session_info(self)
     |  
     |  get_version(self)
     |  
     |  list_methods(self)
     |  
     |  list_notifications(self)
     |  
     |  multicall(self, method)
     |      This methods encapsulates multiple method calls in a single request. 
     |      methods is an array of structs. The structs contain two keys: methodName and params. 
     |      methodName is the method name to call and params is array containing parameters to the method call.
     |      This method returns an array of responses. 
     |      The elements will be either a one-item array containing the return value of the method call or a struct
     |      of fault element if an encapsulated method call fails.
     |  
     |  nofification(self, method='', gid='')
     |      future work.不想做
     |  
     |  pause(self, gid='')
     |      if gid is empty, this method will pause all.
     |  
     |  remove(self, gid)
     |      remove a downloading or waiting, paused job.
     |  
     |  remove_stopped(self, gid='')
     |      If gid is not specific, this method will remove all stopped jobs.
     |  
     |  save_session(self)
     |      This method saves the current session to a file specified by the --save-session option. 
     |      This method returns OK if it succeeds.
     |  
     |  set_server(self, server_add='', server_port='6800', token='')
     |      set server info. If you leave the parameters blank, the server info will be unchanged or remained default.
     |  
     |  tell_active(self, keys=[])
     |      Show what is currently downloading. you can specific the outputs by giving keys(list), 
     |      or you will get all status infomation.
     |  
     |  tell_status(self, gid='', keys=[])
     |      provide a specific gid to get status. you can specific the outputs by giving keys(list), 
     |      or you will get all status infomation.
     |  
     |  tell_stopped(self, offset=0, num=50, keys=[])
     |      This method returns a list of waiting downloads, including paused ones.
     |      offset is an integer and specifies the offset from the download waiting at the front.
     |      num is an integer and specifies the max. number of downloads to be returned. 
     |      For the keys parameter, please refer to the aria2.tellStatus() method.
     |  
     |  tell_waiting(self, offset=0, num=50, keys=[])
     |      This method returns a list of waiting downloads, including paused ones.
     |      offset is an integer and specifies the offset from the download waiting at the front.
     |      num is an integer and specifies the max. number of downloads to be returned. 
     |      For the keys parameter, please refer to the aria2.tellStatus() method.
     |  
     |  unpause(self, gid='')
     |      if gid is empty, this method will unpause all.
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
