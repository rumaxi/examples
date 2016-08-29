@Grab(group='org.codehaus.groovy.modules.http-builder', module='http-builder', version='0.7.2' )
import groovyx.net.http.HTTPBuilder
import static groovyx.net.http.ContentType.*
import static groovyx.net.http.Method.*


class Parser {
    def userAgent = 'Mozilla/5.0 (X11; Linux x86_64; rv:23.0) Gecko/20100101 Firefox/23.0'
    def location, status, content, baseUrl, path
    def proxyHost, proxyPort
    def cookies = [:]

    String toString(){
        [location, cookies]
    }

    def post = { params ->
                        this.path = params.path ?: '/'
                        this.location = baseUrl+this.path
                        def http = new groovyx.net.http.HTTPBuilder (baseUrl)
                        cookies.each {println ">>> $it"}
                        def headers = [
                                    'User-Agent': userAgent,
                                    'Referer'   : location,
                                    'Cookie'   : ''
                        ]
                        cookies.each {headers.Cookie += "$it; "}
                        if (proxyHost && proxyPort) { http.setProxy (proxyHost, proxyPort, 'http') }
                        http.setHeaders (headers)
                        print "${location} : "
                        try {
                        http.post ( path: path, body: params.data,  requestContentType: URLENC, response)
                        } catch (groovyx.net.http.HttpResponseException e) { println "$e" }
                        http.shutdown()
    }

    def get = { params ->
                        this.path = params.path ?: '/'
                        this.location = baseUrl+path
                        def http = new groovyx.net.http.HTTPBuilder (baseUrl)
                        def cookie = ''
                        def headers = [
                                    'User-Agent': userAgent,
                                    'Referer': location,
                                    'Cookie': '',
                        ]
                        cookies.each {headers.Cookie += "$it; "}
                        if (proxyHost && proxyPort) { http.setProxy (proxyHost, proxyPort, 'http') }
                        http.setHeaders (headers)
                        print "${location} : "
                        try {
                        if (params.data) {
                            http.get ( path: path, contentType : TEXT, query: params.data, response)
                        } else { http.get ( path: path, contentType : TEXT, response) }
                        } catch (groovyx.net.http.HttpResponseException e) { println "$e" }
                        http.shutdown()
            }

    def search = { params ->
                        def output = []
                        def temp = content

                        if (params.substring) {
                            temp = []
                            content.eachLine {
                                if (it.contains(params.substring)) {
                                    temp << it+'\n'
                                }
                            }
                            println temp
                        }
                        if (params.regex) {
                            output = []
                            def match = temp =~ params.regex
                            match.findAll() { output << it[1]; }
                        }
                        output
    }
    
    
    private response = { resp, content ->
                            println "${resp.getStatusLine()}"
                            def thisCookies = resp.getHeaders('Set-Cookie');
                            if (thisCookies) {
                                thisCookies.each {
                                    def cookieName = it.getValue().split(';')[0].split('=')[0]
                                    def cookieValue = it.getValue().split(';')[0].split('=')[1]
                                    cookies[cookieName] = cookieValue
                                }
                            }
                            def thisLocation = resp.getHeaders('Location').value.join();
                            if (resp.getStatus() == 302 && thisLocation) {
                                println "302 Redirect to: $thisLocation"
                                get url:baseUrl+thisLocation
                            }
                           this.content = content.text
    }
}

