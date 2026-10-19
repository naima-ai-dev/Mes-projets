from flask import Flask, jsonify, render_template, send_from_directory
from flask_cors import CORS
import sys
import os

# Importer classes depuis le fichier Labyrinthe.py
# Assurez-vous que Labyrinthe.py est dans le même dossier
try:
    from Labyrinthe import Pile, Labyrinthe
except ImportError:
    print("ERREUR: Impossible d'importer Labyrinthe.py")
    print("Assurez-vous que le fichier Labyrinthe.py est dans le même dossier que app.py")
    sys.exit(1)

app = Flask(__name__, static_folder='.')
CORS(app)  # Permettre les requêtes depuis le navigateur

# Le labyrinthe par défaut 
LABYRINTHE_DEFAUT = [
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

DEPART = (0, 0)
ARRIVEE = (10, 8)

@app.route('/')
def index():
    """Page d'accueil - retourne le fichier HTML"""
    return send_from_directory('.', 'index.html')

@app.route('/api/labyrinthe')
def get_labyrinthe():
    """Retourne la structure du labyrinthe"""
    return jsonify({
        'matrice': LABYRINTHE_DEFAUT,
        'depart': DEPART,
        'arrivee': ARRIVEE,
        'nb_lignes': len(LABYRINTHE_DEFAUT),
        'nb_colonnes': len(LABYRINTHE_DEFAUT[0])
    })

@app.route('/api/resoudre/dfs')
def resoudre_dfs():
    """Résoudre avec DFS (profondeur)"""
    laby = Labyrinthe(LABYRINTHE_DEFAUT, depart=DEPART, arrivee=ARRIVEE)
    
    # Lancer la recherche
    cases_visitees = []
    chemin_pile = laby.chercher_chemin_profondeur(DEPART, cases_visitees)
    
    # Convertir la pile en liste
    chemin = []
    while not chemin_pile.estvide():
        chemin.append(chemin_pile.depile())
    
    return jsonify({
        'algorithme': 'DFS (Profondeur)',
        'chemin': chemin,
        'visitees': cases_visitees,
        'longueur_chemin': len(chemin),
        'cases_visitees': len(cases_visitees),
        'trouve': len(chemin) > 0
    })

@app.route('/api/resoudre/bfs')
def resoudre_bfs():
    """Résoudre avec BFS (largeur)"""
    laby = Labyrinthe(LABYRINTHE_DEFAUT, depart=DEPART, arrivee=ARRIVEE)
    
    # Lancer la recherche
    chemin_pile = laby.chercher_chemin_largeur()
    
    # Pour BFS, on doit aussi récupérer les cases visitées
    # On refait l'algorithme pour capturer les visitées
    a_explorer = [DEPART]
    parent = {DEPART: -1}
    visitees = [DEPART]
    index = 0
    
    while index < len(a_explorer):
        case_actuelle = a_explorer[index]
        
        if case_actuelle == ARRIVEE:
            break
        
        for voisin in laby.obtenir_voisins(case_actuelle):
            if voisin not in visitees:
                a_explorer.append(voisin)
                parent[voisin] = case_actuelle
                visitees.append(voisin)
        
        index += 1
    
    # Convertir la pile en liste
    chemin = []
    while not chemin_pile.estvide():
        chemin.append(chemin_pile.depile())
    
    return jsonify({
        'algorithme': 'BFS (Largeur)',
        'chemin': chemin,
        'visitees': visitees,
        'longueur_chemin': len(chemin),
        'cases_visitees': len(visitees),
        'trouve': len(chemin) > 0
    })

if __name__ == '__main__':
    print("\n" + "="*60)
    print(" SERVEUR LABYRINTHE DÉMARRÉ")
    print("="*60)
    print(f" Ouvrez votre navigateur à : http://localhost:5000")
    print(f" Appuyez sur Ctrl+C pour arrêter le serveur")
    print("="*60 + "\n")
    
    app.run(debug=True, port=5000)
