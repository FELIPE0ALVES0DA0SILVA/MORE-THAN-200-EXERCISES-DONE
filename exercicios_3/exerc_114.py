import urllib.request

while True:
    try:
        page = urllib.request.urlopen('http://www.pudim.com.br')
    except:
        print('Não está conectado.')
        break
    else:
        print('Está conectado.')
        print(page.read())
        break

