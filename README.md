# python3-aria2-XML-RPC

Aria2 RPC client in python3.  [aria2,"The next generation download utility."](https://aria2.github.io/)


aria2py是基于Python3 写的 Aria2 RPC 客户端. aria2py通过aria2 server 的 xml-RPC接口和功能控制aria2
[中文介绍文档](https://github.com/Masterchiefm/Aria2Py/blob/main/README_zh.md)
# Description
aria2py controls aria2 via its xml-RPC interface and features

# Getting started
## Server(Optional)
Start aria2 with rpc in your servcer, example:
```
aria2c --enable-rpc --rpc-listen-all=true --rpc-allow-origin-all
```
If you know an existing server, this step can be skip.

## Creat your own client
clone this code. and copy Aria2Py.py into your client project directory.
```
git clone https://github.com/Masterchiefm/Aria2Py.git 
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
client.set_server(server_add="http://127.0.0.1",server_port=6800,token=1234)
```

If you leave the parameters blank, the client will not change the parameter's value.

For example, you can run the following:
```
#set the server info:
client.set_server(server_add="http://127.0.0.1",server_port=6800,token=1234)

#change token only, others will not be change.
client.set_server(server_add="http://127.0.0.1",token='fuckme')
```

## Check connection
After setting server, you can simply use one function to check connection
```
client.check_connection()
```
it will return 'Authorized' or 'Unauthorized'

## add url
After setting server, you can simply use one function to add url as follow:
```
client.add_uri("https://example.com/a1.zip")
```
or 
```
download_list = ["https://example.com/a1",
                  https://example.com/a2"]
        
client.add_uri(download_list)
```

then the function will return the task gid.

## For more help
type help() to get more help info, or read [aria2 offical rpc documet](https://aria2.github.io/manual/en/html/aria2c.html#rpc-interface) to get more help.


Help on module Aria2Py:
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
