import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen('https://github.com/victorcardosodev')
except urllib.error.URLError:
    print('O site não está acessível')
else:
    print('Site acessado com sucesso')