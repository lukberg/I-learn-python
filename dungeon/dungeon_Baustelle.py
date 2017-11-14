import random

class Monster():
	zoo={}
	number=0
	
	def __init__(self,x=0,y=0,z=0):
		self.x=x
		self.y=y
		self.z=z
		self.char='M'
		self.number=Monster.number
		Monster.number+=1
		Monster.zoo[self.number]=self
		self.hp=random.randint(20,50)
		self.attack=random.randint(5,20)
		self.defense=random.randint(5,15)
		self.waffe=random.choice(('Keule','Schwert','Speer','Messer','Axt','Zahnstocher','Dolch','Stein'))
		self.ruestung=random.choice(('Helm','Brustpanzer','Kettenhemd','Schild'))
		
	def report(self):
		print('Hp:{} Attack:{} Defense:{}'.format(self.hp,self.attack,self.defense))
		print('Meine Waffe:{}'.format(self.waffe))
		print('Meine Rüstung:{}'.format(self.ruestung))		
		
def kampf2():
	gegner=Monster()
	print('Du hast keine Chance gegen mich!')
	gegner.report()
	return 0
		
		
		
def kampf():
	'''kampf zwischen monster und spieler
	return 0 wenn spieler gewinnt
	return 1 wenn spieler verliert'''
	print('Spiele Schere-Stein-Papier gegen das Monster')
	while True:		
		print('Wähle Schere, Stein oder Papier')
		command=input('?')
		if command not in ('Schere','Stein','Papier'):
			return 1
		gegnerzug=random.choice(('Schere','Stein','Papier'))
		print('Du spielst:{} Monster spielt:{}'.format(command,gegnerzug))
		if gegnerzug==command:
			print('Unentschieden!Spiele nochmals!')
			continue
		if (gegnerzug=='Schere' and command=='Papier') or (gegnerzug=='Stein' and command=='Schere') or (gegnerzug=='Papier' and command=='Stein'):
			print('Monster gewinnt und tut dir weh!')
			return 1
		print('Du gewinnst!')
		return 0
		
def shop(geld,semmeln):
	'''tausche geld gegen essen'''
	print()
	print('Wilkommen im Shop')
	print('Eine Wurstsemmel kostet 3 Gold')
	print('Wieviele Wurstsemmeln willst du kaufen?')
	menge=input('? ')
	try:
		menge=int(menge)
	except:
		print('Auf Wiedersehen')
		return geld,semmeln
	#gültige zahl wurde eingegeben
	if menge*3>geld:
		print('Du brauchst mehr Gold')
		return geld,semmeln
	semmeln+=menge
	geld-=menge*3
	print('Vielen Dank für Ihren Einkauf')
	return geld,semmeln
	
def kiste():
	'''gib dem hero ein matherätsel'''
	while True:
		a=random.randint(1,10)
		b=random.randint(1,10)
		c=a*b
		antwort=input('Wieviel ist {}x{}?'.format(a,b))
		try:
			antwort=int(antwort)
		except:
			print('Bitte Zahl eingeben')
			continue
		#error catcher
		if antwort==c:
			print('Bravo')
			return
		print('Falsche Zahl')
		print(a,'x',b,'=',c)
			 
		
dungeon1='''
########################################################################
#..<........*#..M.#......................s..........#.........#.....#...#
#...........#....#.........w.......######..........#.......t.#.........#
#..M.....k..#.w..d....w............?....#.....w....#?#########.....#...#
#.s.........#....#.s......##########....#..........#.........?.....#...#
#...........#..t.#........#€............#..........#?#########.....#...#
######d##############€€####s........M...#.....w....#.........#.....##d##
#.........................#k............#..........#..w.h.w..#.....#...#
#.........................###############..w.......#.........#.....#.<.#
#.........w........w......#...#....................###########.....#####
#.........................#€.?M........................................#
#.........h...............#w..#...w....##########......................#
#..w............M.........#€.?M........#*......h#.....s............s...#
#.<.................w.....#...#........#k...w...?......................#
########################################################################
'''

dungeon2='''
########################################################################
#..<.#...........#.........#..?.....M..............................€..<#
#....#.....#.....#.........#..#.....M..............................€...#
#....#.....#.....#....M....#..##############.###########################
#....#.....#.....#.........#..#s......................................k#
#....#..h..#.....#....M....#..##########################################
#....#.....#.....#.........#......w................................#.w.#
#...s......#.......w..k..€.#............................w......#...#...#
#############d##############.............M.....................#MMM#.>.#
##.*.##........#.w.....#.......................w...............#.w.....#
##...##.......#...#...#...################################.#############
##.*.##......#...#...#.w.#...#.....#..............................#..h.#
##...##.....#...#...#...#....#t................s..............<...d..*.#
##>*.##........#.h.....#.....#.....#..............................#..h.#
########################################################################
'''

dungeon3='''
########################################################################
#....#....#...D.ss.k.d...#................>...#.........k........#....>#
##.??.#...#...########...#....................#..................#.....#
#.#....#..#...D.**.k.d...#...w..M..MM..M..w...#.......s.s.s......#..M..#
#..#....#.#...########...#....................#..................#.....#
#...#...s##..........#...#....................#..................#..M..#
#..#....#.#..........#...##########d####################d###############
#.#....#..#...M...M..#...?...#..............................#>.....#...#
##s...#...#.....k....#...#...#..............................#..........#
#.#....#..#..........#...#k.k#...##?##......................#......#...#
#..#....#.#...M...M..#...#...#...#...#......................#......##d##
#...#....##..........#...#...#...#w.w#......................#......#...#
#....#....#..........#...#...#...#€.€#......................#......#.p.#
#.....#...€..........#.t.#.......#...#......................#......#...#
########################################################################
'''

level=[]
for d in (dungeon1,dungeon2,dungeon3):
	dungeon=[]
	for line in d.splitlines():
		dungeon.append(list(line))
	level.append(dungeon)

#hero='@'
hero=Monster(1,2,0)
hero.gold=0
hero.wurst=0
hero.hunger=0
hero.char='@'
herox=1
heroy=2
heroz=0
herogold=0
herowurst=0
herohunger=0
herohp=100
key=0

# --- monster erschaffen ---
for z,dungeon in enumerate(level):
	for y,line in enumerate(dungeon):
		for x,char in enumerate(line):
			if char=='M':
				Monster(x,y,z)
				level[z][y][x]='.'

while True:
	for z,dungeon in enumerate(level):
		if z !=heroz:
			continue
		for y,line in enumerate(dungeon):
			#if y !=heroy:
			#	print(line)
			#else:		
			for x,b in enumerate(line):
				#if x==herox and y==heroy:
				for m in Monster.zoo.values():
					if m.x==x and m.y==y and m.z==z:
						print(m.char,end='')
						break
				else:
					print(b,end='')
			print()
			
	print('Hunger:{}'.format(herohunger))
	print('Wurstsemmeln:{}'.format(herowurst))
	print('Schlüssel:{}'.format(key))
	print('Gold:{}'.format(herogold))
	#herox=int(input())
	command=input('Hp:{} ??? '.format(herohp))
	#herohunger+=1
	#steigt der hunger? 20% chance
	if random.random()<0.2:
		herohunger+=random.randint(5,10)
		print('Mein Magen knurrt!')
	#bewegung
	dx=0
	dy=0
	if command=='a':
		dx=-1
	if command=='d':
		dx=1
	if command=='up':
		if level[heroz][heroy][herox]=='>':
			heroz-=1
			continue
		else:
			print('Finde erst ein Stiegenhaus >')
	if command=='down':
		if level[heroz][heroy][herox]=='<':
			heroz+=1
			continue
		else:
			print('Finde erst ein Stiegenhaus <')	
	if command=='w':
		dy=-1
	if command=='s':
		dy=1	
	#if command=='jump':
		#dx=5
		#herohunger+=3
	if command=='heal':
		herohp=100
	if herohp>100:
		herohp=100
	if command=='#':
		print()
		print()
		print('Spiel wurde beendet')
		break
	# --- in mauer gelaufen ---
	ziel=level[heroz][heroy+dy][herox+dx]
	if ziel=='#':
		print('Aua')
		dx=0
		dy=0
	# --- tür ---
	if ziel=='d':
		if key<1:
			print('Dir fehlt ein Schlüssel!')
			dx=0
			dy=0
		if key>0:
			print('Die Tür wurde geöffnet!')
			key-=1
			level[heroz][heroy+dy][herox+dx]='.'
	# --- verschlossene tür ---
	if ziel=='D':
		if key<1:
			print('Dir fehlt ein Schlüssel')
			dx=0 
			dy=0
		if key>0:
			print('Die Tür wurde geöffnet!')
			key-=1	
	# --- monster ---
	if ziel=='M':
		print('Ein Monster blockiert deinen Weg')
		resultat=kampf2()
		if resultat==0:
			level[heroz][heroy+dy][herox+dx]=random.choice(('w','€','?','.','h'))
		else:
			herohp-=random.randint(10,20)
			print('Das Monster tut dir weh')
			if  herohp<1:
				break
		dx=0
		dy=0
	# --- bewegung! ---
	herox+=dx
	heroy+=dy
	hero.y += dy
	hero.x += dx
	
	if command=='eat':
		if herowurst>0:
			herowurst-=1
			herohunger-=random.randint(5,10)
		if herohunger<0:
			print()
			print()
			print('Du bist geplatzt!')
			break
	if herohunger>100:
		print()
		print()
		print('Du bist verhungert!')
		break
	#------------------Auswertung-------------------------
	stuff=level[heroz][heroy][herox]
	if stuff=='€':
		print('Hurra, Gold!')
		herogold+=random.randint(1,5)
		level[heroz][heroy][herox]='.'
	if stuff=='?':
		print('Oh, ein Rätsel.')
		kiste()
	if stuff=='p':
		print()
		print()
		print('Die Prinzessin ist gerettet!')
		break
	if stuff=='w':
		print('Oh, eine Wurstsemmel!')
		herowurst+=1
		level[heroz][heroy][herox]='.'
	if stuff=='*':
		print('Hurra, ein Diamant')
		herogold+=random.randint(5,25)
		level[heroz][heroy][herox]='.'
	if stuff=='s':
		print('Eine Schokolade')
		herowurst+=5
		level[heroz][heroy][herox]='.' 
	if stuff=='t':
		herogold,herowurst=shop(herogold,herowurst)
	if stuff=='k':
		key+=1
		level[heroz][heroy][herox]='.'
	if stuff=='h':
		print('Hurra ein Heiltrank!')
		herohp+=random.randint(5,10)
		level[heroz][heroy][herox]='.'
		if herohp>100:
			herohp=100			


print('Game Over')
	
