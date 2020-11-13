# Le Jeu de la vie

Ce programme est le fruit de plusieurs heures libres intelligemment employé en classes préparatoire. Il n'est donc absolument pas parfait aux vues des connaissances en programmation que j'avais à l'époque.

## TODO

- Réparer Suivant x20
- Ajouter bouton toggle suivant
- Choix positionnement des formes
- Modification interaction avec les bords?

## Introduction

### Description

> Le jeu de la vie est un automate cellulaire imaginé par *John Horton Conway* en 1970 et qui est probablement le plus connu de tous les automates cellulaires. Malgré des règles très simples, le jeu de la vie est **Turing-complet**.
> Le jeu de la vie est un jeu de simulation au sens mathématique plutôt que ludique. Bien que n'étant pas décrit par la théorie des jeux, certains le décrivent comme un *"jeu à zéro joueur"*.  
> Source: [Wikipédia](https://fr.wikipedia.org/wiki/Jeu_de_simulation)

### Règles

Le jeu se déroule sur une grille à deux dimensions, théoriquement infinie (mais de longueur et de largeur finies et plus ou moins grandes dans la pratique), dont les cases, qu’on appelle des "cellules" peuvent prendre deux états distincts : "vivante" ou "morte".

Évolution:

- une cellule *morte* possédant **exactement trois** voisines vivantes devient vivante,  
- une cellule *vivante* possédant **deux ou trois** voisines vivantes le reste, sinon elle meurt.

## Programme

Ce programme utilise la librairie python [**tkinter**](https://docs.python.org/3/library/tkinter.html). Il s'agit d'une librairie graphique libre.

### Description

A l’exécution du programme (`python3 Jeu_de_la_vie.py` sous Linux) une fenêtre apparaît. Elle est constituée comme suit:

- En haut on voit le numéro de la génération en cours
- En bas à Gauche on dispose d'une liste de formes intéressantes (planeurs, canon, etc.)
- En bas à droite on a accès aux boutons:

    + Suivant: Passer a la génération suivante
    + Clear: Nettoyer la grille
    + Suivant X20: Passer 20 génération d'un coup
    + Stop: Fermer la fenêtre


