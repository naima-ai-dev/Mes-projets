#--------------------------------------------
# PARTIE 1 : CLASSE PILE (pour stocker le chemin)
# --------------------------------------------
class Pile:
    #une pile est une structure de donnees LIFO (Last In, Last Out)
    
    def __init__(self):
        # On crée une liste vide pour stocker les éléments
        self.elements = []
    
    def empile(self, element):
        # Ajouter un élément au sommet de la pile
        self.elements.append(element) 

    def depile(self):
        # Retirer et retourner l'élément au sommet de la pile
        if len(self.elements) > 0:
            return self.elements.pop()
        return None
    
    def estvide(self):
        # Vérifier si la pile est vide
        return len(self.elements) == 0

#--------------------------------------------
# PARTIE 2 : CLASSE LABYRINTHE
# --------------------------------------------

class Labyrinthe:
    #Cette classe représente un labyrinthe et peut trouver un chemin
    
    def __init__(self, matrice, depart=(0,0), arrivee=None):
        #Initialisation du labyrinthe
        #matrice : une liste de listes avec des 0 (passage) et des 1 (mur)
        #depart : coordonnées de départ (ligne, colonne)
        #arrivee : coordonnées d'arrivée (ligne, colonne)

        # Stocker la matrice du labyrinthe
        self.matrice = matrice
        
        # Nombre de lignes dans le labyrinthe
        self.nb_lignes = len(matrice)
        
        # Nombre de colonnes dans le labyrinthe
        self.nb_colonnes = len(matrice[0])
        
        # Position de départ
        self.depart = depart
        
        # Position d'arrivée 
        if arrivee == None:
            self.arrivee = (self.nb_lignes - 1, self.nb_colonnes - 1)
        else:
            self.arrivee = arrivee
    
    def est_valide(self, ligne, colonne):
        #Vérifie si une case est valide (dans les limites et pas un mur)
        #ligne : numéro de ligne
        #colonne : numéro de colonne
        #Retourne : True si la case est valide, False sinon

        # Vérifier que la ligne est dans les limites
        if ligne < 0 or ligne >= self.nb_lignes:
            return False
        
        # Vérifier que ce n'est pas un mur (0 = passage, 1 = mur)
        if self.matrice[ligne][colonne] == 1:
            return False
        
        # Si toutes les conditions sont OK, la case est valide
        return True
    
    def obtenir_voisins(self, position):
        #Trouve toutes les cases voisines accessibles
        #position : tuple (ligne, colonne)
        #Retourne : liste des positions voisines valides

        ligne, colonne = position 
        voisins = []

        # Les 4 directions possibles : haut, bas, gauche, droite
        directions = [
            (-1, 0),  # Haut
            (1, 0),   # Bas
            (0, -1),  # Gauche
            (0, 1)    # Droite
        ]
        
        # Pour chaque direction
        for d_ligne, d_colonne in directions:
            # Calculer la nouvelle position
            nouvelle_ligne = ligne + d_ligne
            nouvelle_colonne = colonne + d_colonne
            
            # Si la nouvelle position est valide, l'ajouter aux voisins
            if self.est_valide(nouvelle_ligne, nouvelle_colonne):
                voisins.append((nouvelle_ligne, nouvelle_colonne))
        
        return voisins
    
#--------------------------------------------
# MÉTHODE 1 : RECHERCHE EN PROFONDEUR (DFS)
# --------------------------------------------

    def chercher_chemin_profondeur(self, position_actuelle, cases_visitees):
        #Algorithme de recherche en profondeur (Depth-First Search)
        #On explore un chemin jusqu'au bout avant d'essayer un autre chemin
        #position_actuelle : où on est maintenant
        #cases_visitees : liste des cases déjà visitées
        #Retourne : une Pile contenant le chemin (vide si pas de solution)
       
        # Si on est arrivé à destination !
        if position_actuelle == self.arrivee:
            pile = Pile()
            pile.empile(position_actuelle)
            return pile
        
        # Marquer cette case comme visitée
        cases_visitees.append(position_actuelle)
        
        # Explorer tous les voisins
        for voisin in self.obtenir_voisins(position_actuelle):
            # Si ce voisin n'a pas encore été visité
            if voisin not in cases_visitees:
                # Explorer récursivement ce voisin
                pile = self.chercher_chemin_profondeur(voisin, cases_visitees)
                
                # Si on a trouvé un chemin
                if not pile.estvide():
                    # Ajouter la position actuelle au chemin
                    pile.empile(position_actuelle)
                    return pile
        
        # Aucun chemin trouvé depuis cette position
        return Pile()

    def resoudre_profondeur(self):
      #Résoudre le labyrinthe avec l'algorithme de profondeur

        print("\n=== RÉSOLUTION PAR RECHERCHE EN PROFONDEUR ===")
        
        # Lancer la recherche
        chemin_pile = self.chercher_chemin_profondeur(self.depart, [])
        
        # Si aucun chemin trouvé
        if chemin_pile.estvide():
            print("Aucun chemin trouvé du départ à l'arrivée")
            return
        
        # Convertir la pile en liste pour l'affichage
        chemin = []
        while not chemin_pile.estvide():
            chemin.append(chemin_pile.depile())
        
        # Afficher le résultat
        print(f"  Chemin trouvé !")
        print(f"  Départ : {self.depart}")
        print(f"  Arrivée : {self.arrivee}")
        print(f"  Chemin : {chemin}")
        print(f"  Nombre de cases : {len(chemin)}")
    
#--------------------------------------------
# MÉTHODE 2 : RECHERCHE EN LARGEUR (BFS)
# --------------------------------------------  
    def chercher_chemin_largeur(self):
        #Algorithme de recherche en largeur (Breadth-First Search)
        #On explore niveau par niveau, comme des vagues
        #Retourne : une Pile contenant le chemin (vide si pas de solution)
    
        # Liste des cases à explorer (on commence par le départ)
        a_explorer = [self.depart]
        
        # Pour chaque case, on mémorise d'où on vient
        # -1 signifie "case de départ, pas de parent"
        parent = {self.depart: -1}
        
        # Cases déjà visitées
        visitees = [self.depart]
        
        # Index de la case qu'on examine actuellement
        index = 0
        
        # Tant qu'il reste des cases à explorer
        while index < len(a_explorer):
            # Prendre la case actuelle
            case_actuelle = a_explorer[index]
            
            # Si on a trouvé l'arrivée !
            if case_actuelle == self.arrivee:
                # Reconstruire le chemin en remontant les parents
                pile = Pile()
                position = case_actuelle
                
                # Remonter jusqu'au départ
                while position != -1:
                    pile.empile(position)
                    position = parent.get(position, -1)
                
                return pile
            
            # Explorer tous les voisins de la case actuelle
            for voisin in self.obtenir_voisins(case_actuelle):
                # Si ce voisin n'a pas encore été visité
                if voisin not in visitees:
                    # L'ajouter à la liste à explorer
                    a_explorer.append(voisin)
                    
                    # Mémoriser d'où on vient
                    parent[voisin] = case_actuelle
                    
                    # Marquer comme visité
                    visitees.append(voisin)
            
            # Passer à la case suivante
            index += 1
        
        # Aucun chemin trouvé
        return Pile()
    
    def resoudre_largeur(self):
        #Résoudre le labyrinthe avec l'algorithme de largeur (plus court chemin)
    
        print("\n=== RÉSOLUTION PAR RECHERCHE EN LARGEUR (PLUS COURT CHEMIN) ===")
        
        # Lancer la recherche
        chemin_pile = self.chercher_chemin_largeur()
        
        # Si aucun chemin trouvé
        if chemin_pile.estvide():
            print("Aucun chemin trouvé du départ à l'arrivée")
            return
        
        # Convertir la pile en liste pour l'affichage
        chemin = []
        while not chemin_pile.estvide():
            chemin.append(chemin_pile.depile())
        
        # Afficher le résultat
        print(f" Plus court chemin trouvé !")
        print(f"  Départ : {self.depart}")
        print(f"  Arrivée : {self.arrivee}")
        print(f"  Chemin : {chemin}")
        print(f"  Longueur : {len(chemin)} cases")
    
    def afficher_labyrinthe(self, chemin=None):
        """
        Afficher le labyrinthe de manière visuelle
        
        chemin : optionnel, liste de positions à marquer sur le chemin
        """
        print("\n=== LABYRINTHE ===")
        print("█  = mur, · = passage, D = départ, A = arrivée, * = chemin")
        print()
        
        # Pour chaque ligne
        for ligne in range(self.nb_lignes):
            # Pour chaque colonne
            for colonne in range(self.nb_colonnes):
                position = (ligne, colonne)
                
                # Départ
                if position == self.depart:
                    print("D", end=" ")
                # Arrivée
                elif position == self.arrivee:
                    print("A", end=" ")
                # Sur le chemin (si fourni)
                elif chemin and position in chemin:
                    print("*", end=" ")
                # Mur
                elif self.matrice[ligne][colonne] == 1:
                    print("█ ", end=" ")
                # Passage
                else:
                    print("·", end=" ")
            
            print()  # Nouvelle ligne

#============================================
# PROGRAMME PRINCIPAL
# ============================================

if __name__ == "__main__":
    # Définition du labyrinthe
    # 0 = passage (on peut passer)
    # 1 = mur (on ne peut pas passer)
    laby = [
        [0, 0, 1, 1, 0, 1, 1, 1, 1],
        [0, 0, 0, 1, 0, 1, 1, 1, 1],
        [1, 0, 0, 1, 1, 1, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [1, 0, 1, 0, 0, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 1, 0, 0, 1],
        [0, 0, 1, 1, 0, 1, 0, 0, 1],
        [1, 1, 0, 1, 0, 0, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 0, 0]
    ]
    
    # Créer un objet Labyrinthe
    # Départ : case (0, 0) en haut à gauche
    # Arrivée : case (10, 8)
    mon_labyrinthe = Labyrinthe(laby, depart=(0, 0), arrivee=(10, 8))
    
    # Afficher le labyrinthe vide
    mon_labyrinthe.afficher_labyrinthe()
    
    # Résoudre avec la méthode en profondeur
    mon_labyrinthe.resoudre_profondeur()
    
    # Résoudre avec la méthode en largeur (plus court chemin)
    mon_labyrinthe.resoudre_largeur()
    
    print("\n" + "="*50)
    print("Programme terminé !")
    print("="*50)

    