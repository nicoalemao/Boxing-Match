# -*- coding: utf-8 -*-
"""game.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19gX27d3F1YyOGS6zWdIoRI9iX4yB5CYv
"""

#Jogo bala
import random

print ("Insira seu nome")
nome = input()

print ("Insira a quantidade de vidas")
vidaP1 = int(input())
vidaP2 = vidaP1

preparo1 = 0
preparo2 = 0

rounds = 1

while (vidaP1>0 and vidaP2>0):


  roundsText = str(rounds)
  vidaP1Text = str(vidaP1)
  vidaP2Text = str(vidaP2)



  print (" ")
  print ("-----------------")
  print (" ")
  print ("Round " + roundsText)
  print (" ")
  print ("Vida de " + nome + ": " + vidaP1Text)
  print (" ")
  print ("Vida de Inimigo: " + vidaP2Text)
  print (" ")
  print ("-----------------")
  print ("1 - Golpe")
  print ("2 - Defesa")
  print ("3 - Preparo")
  print ("0 - Desistir")
  print (" ")
  print ("Ação:")


  acaoP1 = int(input())
  print (" ")
  if (rounds == 1):
    acaoP2 = "3"
    preparo2 = 1
  else:
    if (preparo2 == 0):
      acaoP2 = random.choice("2" "3")
    else:
      acaoP2 = random.choice("1" "2")

  #começo soco
  if (acaoP1 == 1):
    
    if (acaoP2 == "1"):
      if (preparo1 == 0 and preparo2 == 1):
        print ("Você não tinha um soco preparado e tomou uma porrada")
        vidaP1 = vidaP1 - 1
        preparo1 = 0
        preparo2 = 0
      if (preparo1 == 1 and preparo2 == 1):
        print ("Vocês dois se dão um soco.")
        vidaP2 = vidaP2 - 1
        vidaP1 = vidaP1 - 1
        preparo1 = 0
        preparo2 = 0
    
    if (acaoP2 == "2"):
      if (preparo1 == 0):
        print ("Você não tinha um soco preparado e seu inimigo se defende")
      else:
        print ("Você tenta dar um soco em seu inimigo, mas ele se denfende")
        preparo1 = 0
    
    if (acaoP2 == "3"):
      if (preparo1 == 0):
        print ("Você não tinha um soco preparado e seu inimigo prepara um soco")
      else:
        print ("Você soca seu inimigo enquanto ele prepara um soco")
        preparo1 = 0
        vidaP2 = vidaP2 - 1

  #começo defesa
  if (acaoP1 == 2):
    if (acaoP2 == "1"):
      print ("Seu inimigo tenta te socar, mas você defende")
      preparo2 = 0

    if (acaoP2 == "2"):
      print ("Vocês dois se defendem")

    if (acaoP2 == "3"):
      print ("Você se defende enquanto seu inimigo prepara um soco")
      preparo2 = 1

  #começo preparo
  if (acaoP1 == 3):
    if (preparo1 == 1):
      if (acaoP2 == "1"):
        print ("Você já tinha um soco preparado e toma um soco")
        vidaP1 = vidaP1 - 1
        preparo2 = 0
      if (acaoP2 == "2"):
        print ("Você já tinha um soco preparado e seu inimigo se defende")
      if (acaoP2 == "3"):
        print ("Você já tinha um soco preparado e seu inimigo prepara um soco")
        preparo2 = 1
    else:
      if (acaoP2 == "1"):
        print ("Você tenta preparar um soco, mas toma um soco")
        vidaP1 = vidaP1 - 1
        preparo2 = 0
      if (acaoP2 == "2"):
        print ("Você prepara um soco e seu inimigo se defende")
        preparo1 = 1
      if (acaoP2 == "3"):
        print ("Vocês dois preparam um soco")
        preparo1 = 1
        preparo2 = 1

    #começo destisir
  if (acaoP1 == 0):
    print ("você desiste da luta")
    vidaP1 = 0

  rounds = rounds + 1



if (vidaP1 == 0):
  print ("Vida de " + nome + ": 0")
  print ("Vida de Inimigo: " + vidaP2Text)
  print (nome + " perdeu")

if (vidaP2 == 0):
  print ("Vida de " + nome + ": " + vidaP1Text)
  print ("Vida de Inimigo: 0")
  print ("Inimigo perdeu")