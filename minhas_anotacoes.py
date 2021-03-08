def soma(a, b):
  return a + b

def subtracao(a, b):
  return a - b

def is_par(a):
  result = a % 2

  # or = ||
  # or not = !||
  # and = &&
  if result == 0:
    return 'true'
  else:
    return 'false'

def media(a, b, c, d):
  media = (a + b + c + d) / 4

  if a <= 10 and b <= 10 and c <= 10 and d <= 10:
    return 'Sua média é {media}'.format(media=media)
  else:
    return 'Digite valores menor ou igual a 10'

def count_until_x(number):
  for x in range(1, number + 1):
    print('For - Contando até', number, 'o número atual é', x)

def while_count(number):
  x = 0
  while x < number:
    x += 1
    print('While - Contando até', number, 'o número atual é', x)

resultado_soma = soma(5, 2)
resultado_subtracao = subtracao(5, 2)
print('resultado da soma: {sum} \nresultado subtração: {sub}'.format(sum=resultado_soma, sub=resultado_subtracao))

check1 = is_par(10)
check2 = is_par(9)
print('\nResultado se n1 é par {c1}\nResultado se n2 é par {c2}'.format(c1=check1, c2=check2))

check_media = media(10,10,10,9)
print(check_media)

count_until_x(3)
while_count(5)

# aula 05 - Listas
lista = [1, 5, 7, 10]
lista_animal = ['a', 'b', 'c', 'gato', 'cachorro', 'elefante']

if 'gato' in lista_animal:
  print('existe um gato')
else:
  print('não existe um gato na lista')

# incluir novas coisas da lista
lista_animal.append('lobo')

# remover coisas da lista
lista_animal.pop()
lista_animal.pop(1)
lista_animal.remove('elefante')

# ordenando a lista
lista.sort()

# substituindo a lista
lista_animal[0] = 'macaco'

# declarando tuplas
tupla = (1, 10, 12, 14)

# checando o class
type(tupla)

# hash
conjunto = {1, 4, 6, 7}
conjunto.add(8)
conjunto.remove(6)
conjunto_2 = {10, 8}

conjunto.union(conjunto_2)
conjunto.intersection(conjunto_2)
conjunto.difference(conjunto_2)
# semelhante ao union
#conjunto.symetric_difference(conjunto_2)
# retorna um true que ambos tem a mesma informação
conjunto_subset = conjunto_2.issubset(conjunto)
conjunto_subset = conjunto_2.issuperset(conjunto)

# aula classes
class Calculadora:
  def __init__(self, a, b):
    self.a = a
    self.b = b

  def soma(self):
    return self.a + self.b

calculadora = Calculadora(1,3)
print('Teste Calculadora:', calculadora.soma())

# sem init
class Calculadora2:
  def soma(self, a, b):
    return a + b

calculadora2 = Calculadora2()
print('Teste Calculadora2:', calculadora2.soma(1,5))

class Televisao:
  def __init__(self):
    self.ligada = True
    self.desligada = False
    self.canal = 5

  def aumenta_canal(self):
    self.canal += 1

  def diminui_canal(self):
    self.canal -= 1

  def power(self):
    if self.ligada:
      self.ligada = False
    else:
      self.desligada = True

tv = Televisao()
tv.power()
print('A tv está ligada:', tv.ligada)
tv.aumenta_canal()
tv.aumenta_canal()
tv.aumenta_canal()
print('O canal atual é:', tv.canal)
tv.diminui_canal()
print('O canal atual é:', tv.canal)

# imports
#>>> import meu_app
#>>> tv = meu_app.Televisao()
#>>> tv.ligada

# o if abaixo serve para falar "se o arquivo chamar ele mesmo, execute"
# pq ai usando esse if, vc chama a classe nela msm, exemplo:
# class Televisao:
#   def __init__(self):
#     self.ligada = True
#     self.desligada = False
#     self.canal = 5
#
#   def aumenta_canal(self):
#     self.canal += 1
#
#   def diminui_canal(self):
#     self.canal -= 1
#
#   def power(self):
#     if self.ligada:
#       self.ligada = False
#     else:
#       self.desligada = True

# if __name__ == '__main__':
  # tv = Televisao()
  # tv.power()
  # print('A tv está ligada:', tv.ligada)
  # tv.aumenta_canal()
  # tv.aumenta_canal()
  # tv.aumenta_canal()
  # print('O canal atual é:', tv.canal)
  # tv.diminui_canal()
  # print('O canal atual é:', tv.canal)

# outra forma de acessar a classe televisão
# >>> from meu_app import Televisao, Calculadora
# >>> tv = Televisao()
# >>> tv.ligada

# lambda
contador_letras = lambda lista: [len(x) for x in lista]
contador_letras(['gato', 'cachorro'])
#>>> [4, 8]

calculadora = {
  'soma': lambda a, b: a + b,
  'subtracao': lambda a, b: a - b
}

teste = calculadora['soma']
teste(1, 5)

# aula 9 - abrir arquivos e ler
# 'w' sobreescreve no arquivo
arquivo = open('teste.csv', 'w')
arquivo.write('primeira escrita')
arquivo.close()

# 'a' escreve nas linhas de baixo
arquivo = open('teste.csv', 'a')
arquivo.write('\nsegunda escrita')
arquivo.close()

# 'r' apenas lê
arquivo = open('teste.csv', 'r')
texto = arquivo.read()
print(texto)

# iteração em arquivos
arquivo = open('teste.csv', 'r')
texto = arquivo.read()
texto.split('\n')
#>>> ['primeira escrita', 'segunda escrita']

# exemplo de recursividade
arquivo = open('teste.csv', 'w')
arquivo.write('Fabio,7,10,8,9')
arquivo = open('teste.csv', 'a')
arquivo.write('\nFran,4,4,0,1')
arquivo.close()
arquivo = open('teste.csv', 'r')
texto = arquivo.read()
alunos = texto.split('\n')
lista_media = []
for aluno in alunos:
  make_split = aluno.split(',')
  nome = make_split.pop(0)
  notas = make_split
  make_media = lambda notas: sum([int(i) for i in notas]) / 4
  media = make_media(notas)

  print('O nome do aluno é:', nome, 'e sua média é:', media)
  print('==========================================')
  lista_media.append({nome: media})
print(lista_media)

# copiando arquivos
import shutil
shutil.copy('teste.csv', '/home/fsoares/meta/fabio/curso-python/copia_teste.csv')
shutil.move('teste.csv', '/home/fsoares/')

# aula 10 - manipulação de data e hora
from datetime import date, time, datetime
date = date.today()
teste = date.strftime('%d/%m/%Y')
teste2 = date.strftime('%A %B %Y')
print(teste)
print(teste2)

hora = time(hour=15, minute=10, second=30)
print(hora.strftime('%H:%M:%S'))
print(hora)

print(datetime.now())
print(datetime.now().day)
print(datetime.now().year)

# aula 11 - tratamentos de exceções e customizações
try:
  #divisao = 10 / 0
  lista = [1,2]
  lista[1]
except ZeroDivisionError:
  print('não é possivel realizar essa divisão')
except IndexError:
  print('error de index')
except:
  print('error')
# aqui é possível capturar exatamente o erro
except BaseException as ex:
  print(ex)
# https://docs.python.org/3/tutorial/errors.html
else:
  print('executa quando não houver exceção')
finally:
  print('sempre executa esse bloco')

# exemplos
class Error(Exception):
  pass

class InputError(Error):
  def __init__(self, message):
    self.message = message

while True:
  try:
    x = int(input('Digite um número de 0 a 10:'))
    print(x)
    if x > 10:
      raise InputError('Esse é um erro que não pode ser maior que 10')
    break
  except ValueError:
    print('Digite apenas números!')

# última aula - pacotes python
# pip3 install requests

import requests
response = requests.get('https://viacep.com.br/ws/18805280/json/')
print(response.status_code)
print(response.text)
teste = response.json()
teste['cep']
