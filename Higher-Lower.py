from random import randint
from game_data import data
from art import logo, vs
from replit import clear


def hasard (donnees) :
  long = len(donnees)
  n = randint(0,long-1)
  return donnees[n]

def phrase1 (choix) :
  print ('Compare A: '+choix['name']+' a '+ choix['description']+', from '+choix['country'])

def phrase2 (choix) :
  print ('Against B: '+choix['name']+', a '+ choix['description']+', from '+choix['country']+'.') 


def jeu (donnees):
  score = 0
  print(logo)
  choix1=hasard(donnees)
  choix2=hasard(donnees)
  while choix2 == choix1 :
    choix2=hasard(donnees)
  phrase1(choix1)
  print('\n'+vs+'\n')
  phrase2(choix2)
  rep=input('Who has more followers? Type "A" or "B": ')
  clear()

  while (rep == 'A' and choix1['follower_count']>choix2['follower_count']) or (rep == 'B' and choix2['follower_count']>choix1['follower_count']) :
    choix1=choix2
    choix2=hasard(donnees)
    while choix2 == choix1 :
      choix2=hasard(donnees)
    print(logo)
    phrase1(choix1)
    print('\n'+vs+'\n')
    phrase2(choix2)
    rep=input('Who has more followers? Type "A" or "B": ')
    score+=1
    clear()
  print ("Sorry, that's wrong. Final score: "+str(score))
    
jeu(data)
  
