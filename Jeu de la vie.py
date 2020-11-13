import tkinter as tk
from time import sleep

"""
Regles:
Surive: Une cellule survie si elle a 2 ou 3 voisines sinon elle meurt
Nait: Un cellule nait si elle a exactement 3 voisines

"""
#On demande la taille de la grille
taille=40
k=0
temp=0

'''
while type(taille)!=int or int(taille)<=0: #On exclue une grille de 0 par 0 cases et les entrées non entieres
	try:
		taille=int(input("Donnez une taille convenable pour la grille\n"))
	except:
		print("Ce n'est pas un entier")
		ValueError
'''

def creerGrille(taille): #On creer une liste de liste constituant la grille
	G=[]	
	
	for i in range(taille):
		G.append([])
	for i in range(taille):
		for j in range(taille):
			G[j].append(0)
	return G

def voisin(case,grille,taille): #On calcule le nombre de voisin d'une cellule donnee
	ligne=int(case[0])
	colonne=int(case[1])
	voisin = 0
	#Cas en haut a gauche
	if ligne-1>=0:
		if colonne-1>=0:
			if grille[ligne-1][colonne-1]==1:
				voisin+=1
	#Cas en haut au milieu
	if ligne-1>=0:
		if grille[ligne-1][colonne]==1:
			voisin+=1
	#Cas en haut a droite
	if ligne-1>=0:
		if colonne+1<taille:
			if grille[ligne-1][colonne+1]==1:
				voisin+=1
	#Cas au milieu a gauche
	if colonne-1<taille:
		if grille[ligne][colonne-1]==1:
			voisin+=1
	#Cas au milieu a droite
	if colonne+1<taille:
		if grille[ligne][colonne+1]==1:
			voisin+=1
	#Cas en bas a gauche
	if ligne+1<taille:
		if colonne-1>=0:
			if grille[ligne+1][colonne-1]==1:
				voisin+=1
	#Cas en bas au milieu
	if ligne+1<taille:
		if grille[ligne+1][colonne]==1:
			voisin+=1
	#Cas en bas a droite
	if ligne+1<taille:
		if colonne+1<taille:
			if grille[ligne+1][colonne+1]==1:
				voisin+=1
	return(voisin)#On revoi le nombre de voisin

def grilleBeau(taille,grille): #Fonction bonus servant a afficher la grille de maniere propre en console
    for i in range(taille):
        #Déclaration des compteurs
        k=0
        p=0
        #On régle le nombre de -
        while k<taille*6+1: 
            print('-',end='')
            k=k+1
        print()
        print('| ',end='')
        for j in range(taille):
            #On rempli
            print(grille[i][j],"| ", end='')
        print()

    #On régle le nombre de - a la fin
    while p<taille*6+1: 
        print('-',end='')
        p=p+1   
    print()
    return grille

def liveOrdies(): #On calcule a partir d'une grille les cellules qui meurent et celles qui vivent
	global grille
	global taille
	newgrille=creerGrille(taille)

	for i in range(taille):
		for j in range(taille):
			case=[i,j]

			if grille[i][j]==0:
				if voisin(case,grille,taille)==3:
					#print("La cellule sur la case " + str(case) + " nait")
					newgrille[i][j]=1
				else:
					newgrille[i][j]=0

			elif grille[i][j]==1:
				if voisin(case,grille,taille)==2 or voisin(case,grille,taille)==3:
					#print("La cellule sur la case " + str(case) + " survie")
					newgrille[i][j]=1

				elif voisin(case,grille,taille)<=1:
					#print("La cellule sur la case " + str(case) + " meurt")
					newgrille[i][j]=0

				elif voisin(case,grille,taille)>=4:
					#print("La cellule sur la case " + str(case) + " meurt")
					newgrille[i][j]=0

			else:
				print("Il y a un soucis")
	return(newgrille) #On revoie la grille vieilli d'une generation

def remplirGrille(grille): #Fonction bonus servant a remplir en console la grille
	taille=len(grille[0])
	print("Debut du remplissage de la grille\n")

	for i in range(taille):
		for j in range(taille):
			grille[i][j]=int(input("Quel est l'etat de la cellule "  + str([i,j]) + " tapez 1 si elle est vivante 0 sinon:\n"))
			print(grille)
			
grille=creerGrille(taille) #On initialise la grille
##################################################################################

taillePix=800

def case(event): #On calcule les coordonnee d'une case a partir d'une action sur la fenetre
	global taille

	ligne=event.x
	colonne=event.y
	return[event.x//(taillePix/taille),colonne//(taillePix/taille)]

def leftClic(event): #Action declanchee lorsque l'on utilise le clic gauche sur la fenetre
	try:
		ligne=int(case(event)[0])
		colonne=int(case(event)[1])
		grille[colonne][ligne]=1 #On fait naitre une cellule sur la case cliquee
		refreshColor() #On recolorie la grille en fonction de cette modification
		
	except IndexError:
		print("Une erreur est survenue, veuillez relancer le programme")

def rightClic(event): #Action declanchee lorsque l'on utilise le clic droit sur la fenetre
	try:

		ligne=int(case(event)[0])
		colonne=int(case(event)[1])
		grille[colonne][ligne]=0 #On tue la cellule sur la case cliquee
		refreshColor() #On recolorie la grille en fonction de cette modification

	except IndexError:
		print("Une erreur est survenue, veuillez relancer le programme")
'''
def refreshColor(): #Fonction graphique qui colorie en vert les cellule vivantes et blanc les mortes
	global grille, taille

	for i in range(taille):
		for j in range(taille):
			if grille[j][i]==1:
				tissus.create_rectangle(taillePix/taille*i,taillePix/taille*j,taillePix/taille*(i+1),taillePix/taille*(j+1),fill='green')
			elif grille[j][i]==0:
				tissus.create_rectangle(taillePix/taille*i,taillePix/taille*j,taillePix/taille*(i+1),taillePix/taille*(j+1),fill='white')
	#print(str(grille)+'\n')
'''
def refreshColor():
	global grille, taille
	tissus.delete(fenetre,'tag1')
	for i in range(taille):
		for j in range(taille):
			if grille[j][i]==1:
				tissus.create_rectangle(taillePix/taille*i,taillePix/taille*j,taillePix/taille*(i+1),taillePix/taille*(j+1),fill='green',tags='tag1')
			elif grille[j][i]==0:
				tissus.create_rectangle(taillePix/taille*i,taillePix/taille*j,taillePix/taille*(i+1),taillePix/taille*(j+1),fill='white',tags='tag1')

def tracerGrille(): #Fonction créant le quadrillage de la fenetre
	global taille
	for i in range(taille):
		for j in range(taille):
			tissus.create_rectangle(taillePix/taille*i,taillePix/taille*j,taillePix/taille*(i+1),taillePix/taille*(j+1),fill='white',tags='tag1')

def nextGrille(): #Lie au bouton elle appelle les fonction necessaire pour la grille suivante
	global grille,k
	k+=1
	label1.configure(text="Generation  " + str(k))
	grille=liveOrdies() #On calcul la nouvelle grille (avec les naissances et les morts)
	refreshColor() #On recolorie la grille en fonction de cette modification
 
def clearGrille():
	global grille,taille,k
	k=0
	label1.configure(text="Generation  " + str(k))
	grille=creerGrille(taille)
	refreshColor()
	return grille

def nextGrilleRepeat():
	global temp
	if temp<20:
		temp+=1
		nextGrille()
		nextGrilleRepeat()
		sleep(1)
	else:
		temp=0






def clic(event):
    i=choix.curselection()
    valeur=choix.get(i)
    if valeur=='Planeur':
    	setPlaneur()
    elif valeur=='Canon':
    	setCanon()
    elif valeur=='Joli':
    	setJoli()
    elif valeur=='Rigolo':
    	setRigolo()
    elif valeur=='Oscillateur':
    	setOscillateur()

def setPlaneur():
	global taille,grille
	clearGrille()
	if taille==40:
		grille[11][9]=1
		grille[11][10]=1
		grille[11][11]=1
		grille[12][11]=1
		grille[13][10]=1
		refreshColor()
	else:
		print("La taille n'est pas adaptee!")

def setCanon():
	global taille,grille
	clearGrille()
	if taille==40:
		grille[19][1]=1
		grille[20][1]=1
		grille[19][2]=1
		grille[20][2]=1
		grille[19][11]=1
		grille[20][11]=1
		grille[21][11]=1
		grille[18][12]=1
		grille[22][12]=1
		grille[17][13]=1
		grille[23][13]=1
		grille[17][14]=1
		grille[23][14]=1
		grille[20][15]=1
		grille[18][16]=1
		grille[22][16]=1
		grille[19][17]=1
		grille[20][17]=1
		grille[21][17]=1
		grille[20][18]=1
		grille[17][21]=1
		grille[18][21]=1
		grille[19][21]=1
		grille[17][22]=1
		grille[18][22]=1
		grille[19][22]=1
		grille[16][23]=1
		grille[20][23]=1
		grille[15][25]=1
		grille[16][25]=1
		grille[20][25]=1
		grille[21][25]=1
		grille[17][35]=1
		grille[18][35]=1
		grille[17][36]=1
		grille[18][36]=1
		refreshColor()
	else:
		print("La taille n'est pas adaptee!")

def setJoli():
	global taille,grille
	clearGrille()
	if taille==40:
		grille[18][18]=1
		grille[18][19]=1
		grille[18][20]=1
		grille[18][21]=1
		grille[19][18]=1
		grille[19][19]=1
		grille[19][20]=1
		refreshColor()
	else:
		print("La taille n'est pas adaptee!")

def setRigolo():
	global taille,grille
	clearGrille()
	if taille==40:
		grille[18][17]=1
		grille[18][18]=1
		grille[18][19]=1
		grille[18][20]=1
		grille[18][21]=1
		grille[19][18]=1
		grille[19][19]=1
		grille[19][20]=1
		refreshColor()
	else:
		print("La taille n'est pas adaptee!")

def setOscillateur():
	global taille,grille
	clearGrille()
	if taille==40:
		grille[19][18]=1
		grille[19][19]=1
		grille[19][20]=1
		refreshColor()
	else:
		print("La taille n'est pas adaptee!")

#############################################################
#Partie concernant la fenetre tkinter

fenetre=tk.Tk() #On creer le cadre
fenetre.resizable(width=False,height=False)
label1=tk.Label(fenetre, text="Generation  " + str(k))
label1.pack()
tissus=tk.Canvas(width=taillePix,height=taillePix,bg="white") #On creer le tissus
tissus.pack() #On accroche le tissus sur le cadre
tracerGrille() #On creer le quadrillage de la fenetre

choix = tk.Listbox(fenetre,bg="white",height=5,width=10)
choix.bind('<ButtonRelease-1>',clic)
choix.pack(side='left')
choix.insert(1,"Planeur")
choix.insert(2,"Canon")
choix.insert(3,"Oscillateur")
choix.insert(4,"Joli")
choix.insert(5,"Rigolo")

tissus.bind("<Button-1>",leftClic) #En cas de clic gauche on appelle la fonction lefClic
tissus.bind("<Button-3>",rightClic) #En cas de clic droit on appelle la fonction rightClic

button1=tk.Button(fenetre,text='Stop',command=fenetre.destroy).pack(side='right') #Bouton pour detruire la fenetre
button2=tk.Button(fenetre,text='Suivant',command=nextGrille).pack(side='left') #Bouton pour afficher la grille suivante
button3=tk.Button(fenetre,text='Clear',command=clearGrille).pack(side='left') #Bouton pour afficher la grille suivante
button4=tk.Button(fenetre,text='Suivant X20',command=nextGrilleRepeat).pack(side='left') #Bouton pour afficher la grille suivante

tk.mainloop()