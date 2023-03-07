from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup


try:
    html = urlopen('http://pythonscraping.com/pages/page1.html')
except HTTPError as e:
    print(e)
    #devolve null, executa um break ou algum outro 'Plano B'
except URLError as e:
    print('The server could not be found!')
else:
    print('It Worked!')
    #o programa continua. Nota: Se você retornar ou executar um break no
    #catch da execeção, não será necessário usar a instrução 'else'
    bs = BeautifulSoup(html.read(),'lxml')
    try:
        badContent = bs.find('nonExisting')  #nonExistingTag atributo depreciado
    except AttributeError as e:
        print('Tag was not found!')
    else:
        if badContent == None:
            print('Tag was not found!')
        else:
            print(badContent)
    print(bs.h1)