import requests

class NvxEndPoint:
    header = 'https://'
    port = ':443'
    videoSource = ''
    audioSource = ''
    audioMode = ''
    deviceMode = ''
    videoWallMode = ''
    autoInitiationMode = False
    autoInputRoutingEnabled = False
    macAddress = ''
    model = ''
    name = ''
    version = ''
    serialNumber = ''
    streamLocationsTx = ['','','','']
    streamLocationsRx = ['','','','']
    multicastAddressesTx = ['','','','']
    multicastAddressesRx = ['','','','']
    def __init__(self, ip_address, username, password):
        self.ip_address = ip_address
        self.username = username
        self.password = password
    # CREATE URL/BODY ================================================================================
    def createUrl(self,urls):
        new_url = self.header + self.ip_address + self.port + '/'
        for url in urls:
            new_url = new_url + url + '/'
        return new_url
    def createBody(self,body_type,urls,body_key,body_value):            # work with ARGS and KARGS to simplify this
        if body_type == 1:
            body = {urls[0]: {urls[1]: {body_key: body_value}}}
        elif body_type == 2:
            body = {urls[0]: {urls[1]: {urls[2]: [{body_key: body_value}]}}}
        return body
    # AUTHENTICATION =================================================================================
    def authenticate_step1(self):
        url = 'http://' + self.ip_address + '/userlogin.html'
        req = requests.get(url=url)
        if req.status_code == 200:
            res = req.text
            cookies = req.cookies
            return cookies

    def authenticate_step2(self):
        urls = ['userlogin.html']
        data = {
            'login': 'admin',
            'passwrd': 'admin'
        }
        req = requests.post(url=self.createUrl(urls), data=data)
        if req.status_code == 200:
            res = req.text
            return res

    def session(self):
        url = 'http://' + self.ip_address + '/userlogin.html'
        data = {
            'login': 'admin',
            'passwrd': 'admin'
        }
        urls = ['userlogin.html']
        session = requests.Session()
        session.get(url=url)
        cookies = session.cookies
        print(cookies)
        req = session.post(url=self.createUrl(urls), cookies=cookies, data=data)
        return req.text


        
    # DEVICE INFO ====================================================================================
    def getDeviceInfo(self):
        urls = ['Device','DeviceInfo']
        req = requests.get(url = self.createUrl(urls), verify=False)
        if req.status_code == 200:
            res = req.json()
            self.macAddress = res[urls[0]][urls[1]]['MacAddress']
            self.model = res[urls[0]][urls[1]]['Model']
            self.name = res[urls[0]][urls[1]]['Name']
            self.version = res[urls[0]][urls[1]]['PufVersion']
            self.serialNumber = res[urls[0]][urls[1]]['SerialNumber']
        return req.status_code
    # DEVICE OPERATIONS ==============================================================================
    # REBOOT
    def reboot(self):
        urls = ['Device','DeviceOperations']
        request = {
            'url': self.createUrl(urls),
            'body': self.createBody(1,urls,'Reboot', 'true'),
            'method': 'POST'
        }
        return request
    # DEVICE SPECIFIC ================================================================================
    def getDeviceSpecfic(self):
        urls = ['Device','DeviceSpecific']
        req = requests.get(url=self.createUrl(urls), verify=False)
        if req.status_code == 200:
            res = req.json()
            self.videoSource = res[urls[0]][urls[1]]['VideoSource']
            self.audioSource = res[urls[0]][urls[1]]['AudioSource']
            self.audioMode = res[urls[0]][urls[1]]['AudioMode']
            self.deviceMode = res[urls[0]][urls[1]]['DeviceMode']
            self.videoWallMode = res[urls[0]][urls[1]]['VideoWallMode']
            self.autoInitiationMode = res[urls[0]][urls[1]]['AutoInitiationMode']
            self.autoInputRoutingEnabled = res[urls[0]][urls[1]]['AutoInputRoutingEnabled']
        return req.status_code
    # VIDEO SOURCE
    def getVideoSource(self):
        urls = ['Device','DeviceSpecific','VideoSource']
        req = requests.get(url=self.createUrl(urls), verify=False)
        if req.status_code == 200:
            res = req.json()
            self.videoSource = res[urls[0]][urls[1]][urls[2]]
        return req.status_code
    def setVideoSource(self,video_source):
        urls = ['Device','DeviceSpecific']
        request = {
            'url': self.createUrl(urls),
            'body': self.createBody(1,urls,'VideoSource',video_source),
            'method': 'POST'
        }
        return request
    # AUDIO SOURCE 
    def getAudioSource(self):
        urls = ['Device','DeviceSpecific','AudioSource']
        req = requests.get(url=self.createUrl(urls), verify=False)
        if(req.status_code == 200):
            res = req.json()
            self.audioSource = res[urls[0]][urls[1]][urls[2]]
        return req.status_code
    def setAudioSource(self,audio_source):
        urls = ['Device','DeviceSpecific']
        request = {
            'url': self.createUrl(urls),
            'body': self.createBody(1,urls,'AudioSource',audio_source),
            'method': 'POST'
        }
        return request
    # AUDIO MODE 
    def getAudioMode(self):
        urls = ['Device','DeviceSpecific','AudioMode']
        req = requests.get(url=self.createUrl(urls), verify=False)
        if(req.status_code == 200):
            res = req.json()
            self.audioMode = res[urls[0]][urls[1]][urls[2]]
        return req.status_code
    def setAudioMode(self,audio_mode):
        urls = ['Device','DeviceSpecific']
        request = {
            'url': self.createUrl(urls),
            'body': self.createBody(1,urls,'AudioMode',audio_mode),
            'method': 'POST'
        }
        return request
    # DEVICE MODE
    def getDeviceMode(self):
        urls = ['Device','DeviceSpecific','DeviceMode']
        req = requests.get(url=self.createUrl(urls), verify=False)
        if req.status_code == 200:
            res = req.json()
            self.deviceMode = res[urls[0]][urls[1]][urls[2]]
        return req.status_code
    def setDeviceMode(self,device_mode):
        urls = ['Device','DeviceSpecific']
        request = {
            'url': self.createUrl(urls),
            'body': self.createBody(1,urls,'DeviceMode',device_mode),
            'method': 'POST'
        }
        return request
    # STREAM TRANSMIT ====================================================================================
    def getStreamTransmit(self,stream):
        urls = ['Device', 'StreamTransmit',"Streams"]
        req = requests.get(url=self.createUrl(urls), verify=False)
        if req.status_code == 200:
            res = req.json()
            streams = res[urls[0]][urls[1]][urls[2]]
            self.streamLocationsTx[stream] = streams[stream]['StreamLocation']
            self.multicastAddressesTx[stream] = streams[stream]['MulticastAddress']
        return req.status_code
    def setMulticastAddress(self,stream,multicast_address):
        urls = ['Device','StreamTransmit','Streams',str(stream)]
        body_urls = ['Device','StreamTransmit','Streams']
        request = {
            'url': self.createUrl(urls),
            'body': self.createBody(2,body_urls,'MulticastAddress',multicast_address),
            'method': 'POST'
        }
        return request
    # STREAM RECEIVE =====================================================================================
    def getStreamReceive(self,stream):
        urls = ['Device','StreamReceive','Streams']
        req = requests.get(url=self.createUrl(urls), verify=False)
        if req.status_code == 200:
            res = req.json()
            streams = res[urls[0]][urls[1]][urls[2]]
            self.streamLocationsRx[stream] = streams[stream]['StreamLocation']
            self.multicastAddressesRx[stream] = streams[stream]['MulticastAddress']
        return req.status_code
    def setStreamReceive(self,stream_location):
        urls = ['Device','StreamReceive','Streams','0']
        body_urls = ['Device','StreamReceive','Streams']
        request = {
            'url': self.createUrl(urls),
            'body': self.createBody(2,body_urls,'StreamLocation',stream_location),
            'method': 'POST'
        }
        return request
    # AUDIO VIDEO INPUT OUTPUT ===========================================================================
    def getAudioVideoInput(self):
        urls = ['Device','AudioVideoInputOutput','Inputs']
        req = requests.get(url=self.createUrl(urls), verify=False)
        if req.status_code == 200:
            res = req.json()
            return res
        
    def getAudioVideoOutput(self):
        urls = ['Device','AudioVideoInputOutput','Outputs']
        request = {
            'url': self.createUrl(urls),
            'method': 'GET'
        }
        return request


# defining endpoints
encoder_01 = NvxEndPoint("192.168.1.51",'admin','admin')
decoder_01 = NvxEndPoint("192.168.1.71",'admin','admin')


print(decoder_01.session())
















