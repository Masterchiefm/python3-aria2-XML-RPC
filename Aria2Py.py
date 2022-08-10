#!/usr/bin/env python
# coding: utf-8
import os
import xmlrpc.client as xmlrpc_client
class Aria2Client:
    """Default server address is http://127.0.0.1,
    default port is 6800, default token is empty"""
    #print("ss")
    def __init__(self):
        #print("初始化信息")
        self.server_add = "http://127.0.0.1"
        self.server_port = "6800"
        rpc = "rpc"
        self.server_url = self.server_add + ":" + self.server_port + "/" + rpc
        self.server = xmlrpc_client.ServerProxy(self.server_url)
        self.token = ''

    
    
    def setServer(self,server_add = '',server_port = '6800', token = ''):
        """set server info. If you leave the parameters blank, the server info will be unchanged or remained default.
            Example:
            from Aria2Py import Aria2Client as client
            client.setServer(server_add = "http://example.com", server_port = "6800", token = "1234")
        """
        #server信息更改
        rpc = "rpc"
        
        #更改服务器地址
        if server_add == '':
            pass
        else:
            if server_add[-1] == "/":
                server_add = server_add[:-1]
            self.server_add = server_add
        
        #更改端口
        if server_port == '':
            pass
        else:
            self.server_port = str(server_port)
            

        
        if token == '':
            pass
        else:
            self.token = str(token)
       
    
        self.server_url = self.server_add + ":" + self.server_port + "/" + rpc
        self.server = xmlrpc_client.ServerProxy(self.server_url)
    
    
    def getVersion(self):
        """Return arai2 version"""
        try:
            version = self.server.aria2.getVersion("token:%s"%self.token)
            return str(version)
        except Exception as e:
            return str(e)
        
    def checkConnection(self):
        """Return connection status between aria2 server and local"""
        try:
            version = self.getVersion()
            if "Unauthorized" in version:
                return "Unauthorized"
            elif "version" in version:
                return "Authorized"
            else:
                return version
        except Exception as e:
            return e
        
        
    def addUri(self,uri,save_dir=''):
        """provide the download link (or link list) to donload. Option: provide download position
        uri can be a str or a list. If uri is a str, it will be converted to list.
        Example:
            from Aria2Py import Aria2Client as client
            client.setServer(server_add = "http://example.com", server_port = "6800", token = "1234")
            client.addUri("http://example.com/file1")
            client.addUri(uri = "http://example.com/file2", save_dir = "/tmp/downloads")
            client.addUri(uri = ["http://example.com/file3","http://example.com/file4","http://example.com/file5"], save_dir = "/tmp")
            
            
        file1 will be downloaded to the default path specified in aria2.conf, while file2 will be downloaded to /tmp/downloads.
        file3,4,5 will be downloaded to /tmp
        
        """
        
        # convert uri to list.
        if type(uri) == type([1]):
            uri_list = uri
        else:
            uri_list = [uri]
        
        if save_dir != "":
            save_dir = dict(dir =save_dir)
            try:
                pid = self.server.aria2.addUri("token:%s"%self.token,uri_list,save_dir)
                return pid
            except Exception as e:
                return e
        else:
            try:
                #print("no")
                pid = self.server.aria2.addUri("token:%s"%self.token,uri_list)
                return pid
            except Exception as e:
                return e
            
    def addTorrent(self,torrent_position,save_dir=''):
        '''Open local torrent file to download. 
        Example:
            from Aria2Py import Aria2Client as client
            client.setServer(server_add = "http://example.com", server_port = "6800", token = "1234")
            client.addTorrent("t1.torrent")
            client.addTorrent("t2.torrent", save_dir = "/tmp/downloads")
            
        t1 will be downloaded to the default path specified in aria2.conf, while t2 will be downloaded to /tmp/downloads.
            
            '''
        torrent = xmlrpc_client.Binary(open(torrent_position, mode='rb').read())
        if torrent_file_position != "":
            download_dir = dict(dir=save_dir)
            try:
                pid = self.server.aria2.addTorrent("token:%s"%self.token,torrent,save_dir)
                return pid
            except Exception as e:
                return e
        else:
            try:
                #print("no")
                pid = self.server.aria2.addTorrent("token:%s"%self.token,torrent)
                return pid
            except Exception as e:
                return e
    
    def remove(self,gid):
        """remove a job specified by gid."""
        try:
            result = self.server.aria2.remove("token:%s"%self.token,gid)
            return result
        except Exception as e:
            return e
        
        
    def forceRemove(self,gid):
        """This method removes the download denoted by gid. This method behaves just like aria2.remove()
        except that this method removes the download without performing any actions which take time, 
        such as contacting BitTorrent trackers to unregister the download first."""
        
        try:
            result = self.server.aria2.forceRemove("token:%s"%self.token,gid)
            return result
        except Exception as e:
            return e
        
    def pause(self,gid = ''):
        """Remove a job specified by gid. If parameter gid is empty, this method will pause all."""
        if gid == '':
            try:
                result = self.server.aria2.pauseAll("token:%s"%self.token)
                return result
            except Exception as e:
                return e
        
        try:
            result = self.server.aria2.pause("token:%s"%self.token,gid)
            return result
        except Exception as e:
            return e
    
    def unpause(self,gid = ''):
        """Pause a job specified by gid.if gid is empty, this method will unpause all."""
        if gid == '':
            try:
                result = self.server.aria2.unpauseAll("token:%s"%self.token)
                return result
            except Exception as e:
                return e
        
        try:
            result = self.server.aria2.unpause("token:%s"%self.token,gid)
            return result
        except Exception as e:
            return e
    
    
    def tellStatus(self,gid = '',keys = []):
        """provide a specific gid to get status. you can specific the outputs by giving keys(list), 
        or you will get all status infomation. 
        
        keys is an array of strings. If specified, the response contains only keys in the keys array. 
        If keys is empty or omitted, the response contains all keys. This is useful when you just want specific keys and avoid unnecessary transfers. 
        
        Example:
            from Aria2Py import Aria2Client as client
            client.setServer(server_add = "http://example.com", server_port = "6800", token = "1234")
            client.tellStatus()
            client.tellStatus("2089b05ecca3d829")
            client.tellStatus("2089b05ecca3d829", ["gid", "status"])
            
        
        """
        if type(keys) == type('string'):
            keys = [keys]
        try:
            status = self.server.aria2.tellStatus("token:%s"%self.token,gid,keys)
            return status
        except Exception as e:
            return e
        
    def tellActive(self,keys = []):
        """Show what is currently downloading. you can specific the outputs by giving keys(list), 
        or you will get all status infomation. 
        
        keys is an array of strings. If specified, the response contains only keys in the keys array. 
        If keys is empty or omitted, the response contains all keys. This is useful when you just want specific keys and avoid unnecessary transfers. 
        
        Example:
            from Aria2Py import Aria2Client as client
            client.setServer(server_add = "http://example.com", server_port = "6800", token = "1234")
            client.tellActive("2089b05ecca3d829", ["gid", "status"])
        """
        if type(keys) == type('string'):
            keys = [keys]
        try:
            active_jobs = self.server.aria2.tellActive("token:%s"%self.token,keys)
            return active_jobs
        except Exception as e:
            return e
        
    def tellWaiting(self,offset = 0, num = 512, keys = []):
        """This method returns a list of waiting downloads, including paused ones.
        offset is an integer and specifies the offset from the download waiting at the front.
        num is an integer and specifies the max. number of downloads to be returned. 
        For the keys parameter, please refer to the aria2.tellStatus() method."""
        if type(keys) == type('string'):
            keys = [keys]
        try:
            waiting_jobs = self.server.aria2.tellWaiting("token:%s"%self.token,offset,num,keys)
            return waiting_jobs
        except Exception as e:
            return e
        
    def tellStopped(self,offset = 0, num = 512, keys = []):
        """This method returns a list of waiting downloads, including paused ones.
        offset is an integer and specifies the offset from the download waiting at the front.
        num is an integer and specifies the max. number of downloads to be returned. 
        For the keys parameter, please refer to the aria2.tellStatus() method."""
        if type(keys) == type('string'):
            keys = [keys]
        try:
            stopped_jobs = self.server.aria2.tellStopped("token:%s"%self.token,offset,num,keys)
            return stopped_jobs
        except Exception as e:
            return e
        
    def listMethods(self):
        """This method returns all the available RPC methods in an array of string. 
        This method does nothing for user but for developer.
        This method just returns the available methods in remote server."""
        
        try:
            methods = self.server.system.listMethods("token:%s"%self.token)
            return methods
        except Exception as e:
            return e
        
    def listNotifications(self):
        """This method returns all the available RPC notifications in an array of string. 
        Unlike other methods, this method does not require secret token. 
        This is safe because this method just returns the available notifications names."""
        try:
            notifications = self.server.system.listNotifications()
            return notifications
        except Exception as e:
            return e
        
    def getFiles(self,gid):
        """This method returns the file list of the download denoted by gid (string). 
        The response is an array of structs."""
        try:
            files = self.server.aria2.getFiles("token:%s"%self.token,gid)
            return files
        except Exception as e:
            return e
        
    def multicall(self):
        """This methods encapsulates multiple method calls in a single request. 
        methods is an array of structs. The structs contain two keys: methodName and params. 
        methodName is the method name to call and params is array containing parameters to the method call.
        This method returns an array of responses. 
        The elements will be either a one-item array containing the return value of the method call or a struct
        of fault element if an encapsulated method call fails.
        
        Example:
            from Aria2Py import Aria2Client as client
            client.setServer(server_add = "http://example.com", server_port = "6800", token = "1234")
            mc = client.multicall()
            mc.aria2.addUri(['http://example.org/file'])
            mc.aria2.addTorrent(xmlrpclib.Binary(open('file.torrent', mode='rb').read()))
            r = mc()
            tuple(r)
            
        then it will return such result: 
        ('2089b05ecca3d829', 'd2703803b52216d1')
        """
        try:
            mc = xmlrpc_client.MultiCall(self.server)
            return mc
        except Exception as e:
            return e
    
    def getSessionInfo(self):
        """This method returns session information. Session ID, which is generated each time when aria2 is invoked."""
        try:
            info = self.server.aria2.getSessionInfo("token:%s"%self.token)
            return info
        except Exception as e:
            return e
        
    def removeStopped(self,gid = ''):
        """If gid is not specific, this method will remove all stopped jobs."""
        if gid == '':
            try:
                result = self.server.aria2.purgeDownloadResult("token:%s"%self.token)
                return result
            except Exception as e:
                return e
        
        else:
            try:
                result = self.server.aria2.removeDownloadResult("token:%s"%self.token,gid)
                return result
            except Exception as e:
                return e
            
    def getOption(self,gid):
        """return the options of a specific job you can modify."""
        try:
            option = self.server.aria2.getOption("token:%s"%self.token,gid)
            return option
        except Exception as e:
                return e
            
            
    def changeOption(self,gid,options):
        """This method changes options of the download denoted by gid (string) dynamically.
        options is a struct. 
        option parameter example:  {'max-download-limit':'20K'}  
        
        Options are avalible in getOption mehtod.
        
        Example:
            from Aria2Py import Aria2Client as client
            client.changeOption("2089b05ecca3d829",{'max-download-limit':'20K'})
        """
        try:
            option = self.server.aria2.changeOption("token:%s"%self.token,gid,options)
            return option
        except Exception as e:
                return e
            
            
    def getGlobalOption(self,gid):
        """return the global options you can modify."""
        try:
            option = self.server.aria2.getGlobalOption("token:%s"%self.token,gid)
            return option
        except Exception as e:
                return e
            
    def changeGlobalOption(self,gid,options):
        """This method changes options of the download denoted by gid (string) dynamically.
        options is a struct. 
        option parameter example:  {'max-download-limit':'20K'}  """
        try:
            option = self.server.aria2.changeGlobalOption("token:%s"%self.token,gid,options)
            return option
        except Exception as e:
                return e
    
    
    def getGlobalStatus(self):
        """This method returns global statistics such as the overall download and upload speeds.
        The response is a struct and contains the following keys. Values are strings.
        
        Speed (byte/sec).
        
        How to convert? 
        1 Mb/s = 1024 kb/s = 1048576 byte/s
        1 byte/s = 1/1048576 Mb/s
        
        """
        try:
            status = self.server.aria2.getGlobalStat("token:%s"%self.token)
            return status
        except Exception as e:
            return e
        

    
    def saveSession(self):
        """This method saves the current session to a file specified by the --save-session option. 
        This method returns OK if it succeeds."""
        try:
            result = self.server.aria2.saveSession("token:%s"%self.token)
            return result
        except Exception as e:
            return e
    
    def nofification(self,method = '',gid=''):
        """future work.不想做"""
        if method == '':
            methods = []
            result = self.listNotifications()
            for i in result:
                m = i.replace("aria2.","")
                methods.append(m)
            
            return methods
        
        
        
        
        else:
            #未完成。不想做。
            pass  
            


