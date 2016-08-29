@Grab(group='org.gperfutils', module='gbench', version='0.4.2-groovy-2.3')
import groovyx.gbench.Benchmark

import Parser

def loginPath    = '/a-logon/'
def searchPath   = '/a-search/'
def baseUrl     = 'http://loveplanet.ru'
def login       = '<login>'
def password    = '<password>'

// def proxyHost   // = 'serviceproxy.avangard.ru'
// def proxyPort   // = 8080

def pageRegex   = /<a href="(\/page\/.*\/frl-2\/)" target="_blank" class="buser_usname">/
def nameRegex   = /<div class="fsize17 mt3 mb11 fl">(.*)<\/div>/
def horoRegex   = /<a href="http:\/\/horo.qip.ru\/signs\/.*" target="_blank">(.*)<\/a>/

def parser


def exit = { System.exit(0) } // debug thing
def File debug = new File("output.html") // one more
debug.delete()

//if (proxyHost && proxyPort) {
//    parser = new Parser (proxyHost: proxyHost, proxyPort: proxyPort, baseUrl: baseUrl)
//} else {
    parser = new Parser (baseUrl: baseUrl)
//}


parser.post path:loginPath,
            data:[
                a:          'logon',
                login:      login,
                password:   password,
            ]

data =      [
                a:      'search',
                d:      '1',
                foto:   '1',
                pol:    '1',
                spol:   '2',
                bage:   '20',
                tage:   '28',
                geo:    '3159,4312,4400',
                p:      '0',
            ]
for (age in 21..30) {
data.tage=age
data.bage=age
for (p in 0..190) {
    data.p = p
    parser.get data: data,path:searchPath
    parser.search(regex:pageRegex).each {
    def link = it.replaceAll ('frl-2','frl-4')
        parser.get path:link
        parser.get path:it
    }
}



}

