class NvxEndPoint {
    constructor(ipAddress) {
        this.urlHeader = 'https://'
        this.ipAddress = ipAddress
        this.port = ':443'
        this.videoSource = ''
        this.audioSource = ''
        this.audioMode = ''
    }
    createUrl = (urls) => {
        // create url and body
        let url = this.urlHeader + this.ipAddress + this.port + '/'
        for(let urlIndex=0;urlIndex < urls.length;urlIndex++) {
            url = url +  urls[urlIndex] + '/'
        }  
        return url
    }
    createBody = (urls,setting) => {
        let body = {}
        switch(urls.length) {
           case 2: body = {[urls[0]]: {[urls[1]]: {[setting[0]]: setting[1]}}}
        }
        return body
    }
    getDeviceInfo = () => {
        let urls = ['Device','DeviceInfo']
        let request = {
            url: this.createUrl(urls),
            method: 'GET'
        }
        return request
    }  
    getDeviceSpecific = () => {
        let urls = ['Device','DeviceSpecific']
        let request = {
            url: this.createUrl(urls),
            method: 'GET'
        }
    }
    /* VIDEO SOURCE ****************************************************************************************************************************************************/
    getVideoSource = () => {
        let urls = ['Device','DeviceSpecific','VideoSource']
        let request = {
            url: this.createUrl(urls),
            method: 'GET'
        }
        return request
    }
    setVideoSource = (thisVideoSource) => {
        this.videoSource = thisVideoSource 
        let urls = ['Device','DeviceSpecific']
        let request = {
            url: this.createUrl(urls),
            body: this.createBody(urls,['VideoSource',this.videoSource]),
            method: 'SET'
        }
        return request
    }
    /* AUDIO SOURCE ****************************************************************************************************************************************************/
    getAudioSource = () => {
        let urls = ['Device','DeviceSpecific','AudioSource']
        let request = {
            url: this.createUrl(urls),
            method: 'GET'
        }
        return request
    }
    setAudioSource = (thisAudioSource) => {
        this.audioSource = thisAudioSource
        let urls = ['Device','DeviceSpecific']
        let request = {
            url: this.createUrl(urls),
            body: this.createBody(urls,['AudioSource',this.audioSource]),
            method: 'SET'
        }
        return request
    }
    /* AUDIO MODE ******************************************************************************************************************************************************/
    getAudioMode = () => {
        let urls = ['Device','DeviceSpecific','AudioMode']
        let request = {
            url: this.createUrl(urls),
            method: 'GET'
        }
    }
    setAudioMode = (thisAudioMode) => {
        this.audioMode = thisAudioMode 
        let urls = ['Device','DeviceSpecific']
        let request = {
            url: this.createUrl(urls),
            body: this.createBody(urls,['AudioMode',this.audioMode]),
            method: 'SET'
        }
        return request
    }
    /* DEVICE MODE *****************************************************************************************************************************************************/
    getDeviceMode = () => {
        let urls = ['Device','DeviceSpecific','DeviceMde']
        let request = {
            url: this.createUrl(urls),
            method: 'GET'
        }
        return request
    }
    setDeviceMode = (thisDeviceMode) => {
        this.deviceMode = thisDeviceMode
        let urls = ['Device','DeviceSpecific']
        let request = {
            url: this.createUrl(urls),
            body: this.createBody(urls,[])
        }
        return request
    }
}

var fetch = require('fetch').fetchUrl


// testing
nvxEndpoint1 = new NvxEndPoint('192.168.1.71')


console.log(nvxEndpoint1.setVideoSource('Input2'))






