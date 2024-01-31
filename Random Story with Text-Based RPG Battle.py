#By Felin
import random 
when=['once upon a time,','A thousand years ago,','In the last year,','In the last century,']
where=['in Egypt','in India','in South Africa','in south America','in Poland']
name=['Alan','Dave','Joe','Max','Ben']
feel=['adored','loved','liked','respected']
day=['monday','tuesday','wednesday','thursday','friday']
dragonhouse=['abode','den','lair','hideout','castle']
aim=['avenge his kingdom','destroy the dragon','kill the dragon','eradicate the dragon']
Dragon=['destroyed the agriculture','destroyed the village','looted the treasury of the kingdom','kidnapped the princess of the kingdom','killed many villagers']
print(random.choice(when)+random.choice(where),' there was a player by the '
'name of '+ random.choice(name)+'.''The villagers '+random.choice(feel)+' the player.'
'One '+random.choice(day)+',''a dragon flew into the village and '+random.choice(Dragon)+'.'
'The player decided to '+random.choice(aim)+'.''The player went to the '+random.choice(dragonhouse),'of the dragon.'
'The player saw the dragon and fought the dragon.')
DragonHealth=100
PlayerHealth=100
DamagetoDragon=random.randint(0,20)
DamagetoPlayer=random.randint(0,20)
while DragonHealth<=100 and PlayerHealth<=100: 
      
       DamagetoDragon=random.randint(0,20)
       DamagetoPlayer=random.randint(0,20)
       if DragonHealth<0:
             print('Dragon has',DragonHealth,'HP')
             print('Dragon was killed.Player has won')
             break
       if PlayerHealth<0:
             print('Player has',PlayerHealth,'HP')
             print('Player was killed.Dragon has won')
             
             break
       print('Dragon has',DragonHealth,'HP')
       print('Player has',PlayerHealth,'HP')
       if DragonHealth<0:
            print('Dragon was killed.Player has won')
       if PlayerHealth<0:
            print('Player was killed.Dragon has won')
  
       DragonHealth=DragonHealth-DamagetoDragon
       PlayerHealth=PlayerHealth-DamagetoPlayer

    
