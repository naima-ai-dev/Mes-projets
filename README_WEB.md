# 🧭 Interface Web Simple - Visualisateur de Labyrinthe

Interface HTML/CSS/JS qui utilise votre fichier Python `Labyrinthe.py` existant !

---

## 📁 Structure des fichiers

```
votre-dossier/
│
├── Labyrinthe.py          # ← Votre fichier Python original (à renommer)
├── app.py                 # ← Serveur Flask (backend)
├── index.html             # ← Interface web (frontend)
└── requirements.txt       # ← Dépendances Python
```

---

## 🚀 Installation rapide

### Étape 1 : Renommer votre fichier

Votre fichier Python doit s'appeler **exactement** `Labyrinthe.py` (avec majuscule).

Si votre fichier a un autre nom, renommez-le :
```bash
mv votre_fichier.py Labyrinthe.py
```

### Étape 2 : Installer Flask

```bash
pip install -r requirements.txt
```

Ou manuellement :
```bash
pip install Flask flask-cors
```

### Étape 3 : Lancer le serveur

```bash
python app.py
```

Vous devriez voir :
```
============================================================
🚀 SERVEUR LABYRINTHE DÉMARRÉ
============================================================
📍 Ouvrez votre navigateur à : http://localhost:5000
⚡ Appuyez sur Ctrl+C pour arrêter le serveur
============================================================
```

### Étape 4 : Ouvrir dans le navigateur

Ouvrez votre navigateur et allez à :
```
http://localhost:5000
```

🎉 **C'est tout !** L'interface devrait s'afficher.

---

## 🎯 Comment utiliser l'interface

1. **Cliquez sur "⚡ BFS (Largeur)"** pour voir l'algorithme de recherche en largeur
   - Explore niveau par niveau
   - Trouve le chemin le plus court
   - Bleues = cases visitées
   - Jaune = chemin final

2. **Cliquez sur "🌲 DFS (Profondeur)"** pour voir l'algorithme de recherche en profondeur
   - Explore en profondeur
   - Trouve un chemin (pas forcément le plus court)

3. **Cliquez sur "🔄 Réinitialiser"** pour effacer et recommencer

4. **Regardez les statistiques** qui s'affichent après chaque recherche :
   - Nombre de cases visitées
   - Longueur du chemin trouvé
   - Algorithme utilisé

---

## 🎨 Ce qui se passe techniquement

### Backend (Python - app.py)
```
┌─────────────────┐
│  Labyrinthe.py  │  ← Vos classes (Pile, Labyrinthe)
└────────┬────────┘
         │
         ↓
┌─────────────────┐
│     app.py      │  ← Serveur Flask
│                 │  
│  Routes:        │
│  /api/labyrinthe │ → Retourne la structure
│  /api/resoudre/bfs │ → Résout avec BFS
│  /api/resoudre/dfs │ → Résout avec DFS
└─────────────────┘
```

### Frontend (HTML/CSS/JS - index.html)
```
┌─────────────────┐
│   index.html    │  ← Interface graphique
│                 │
│  1. Affiche     │
│  2. Anime       │  
│  3. Communique  │ → fetch() → app.py
│     avec Python │
└─────────────────┘
```

### Communication
```
Navigateur          Serveur Python
(index.html)        (app.py)
     │                  │
     │ GET /api/bfs     │
     ├─────────────────>│
     │                  │ Exécute votre
     │                  │ code Python
     │                  │
     │  JSON (chemin)   │
     │<─────────────────┤
     │                  │
   Affiche              │
   et anime             │
```

---

## ⚙️ Personnalisation

### Changer le labyrinthe

Dans `app.py`, modifiez :
```python
LABYRINTHE_DEFAUT = [
    [0, 0, 1, 1, 0],  # ← Votre nouveau labyrinthe
    [0, 0, 0, 1, 0],
    # ...
]

DEPART = (0, 0)      # ← Nouvelle position de départ
ARRIVEE = (4, 4)     # ← Nouvelle position d'arrivée
```

### Changer les couleurs

Dans `index.html`, section `<style>`, modifiez :
```css
.cell.visited {
    background: #93c5fd;  /* ← Couleur des cases visitées */
}

.cell.path {
    background: #fbbf24;  /* ← Couleur du chemin */
}
```

### Changer la vitesse d'animation

Dans `index.html`, fonction `resoudre()`, modifiez :
```javascript
await sleep(30);  // ← Cases visitées (en millisecondes)
await sleep(50);  // ← Chemin final
```

Plus petit = plus rapide, plus grand = plus lent.

### Changer la taille des cellules

Dans `index.html`, section `<style>`, modifiez :
```css
.cell {
    width: 45px;   /* ← Largeur */
    height: 45px;  /* ← Hauteur */
}
```

---

## 🐛 Dépannage

### Erreur : "Module 'Labyrinthe' not found"
**Solution :** Votre fichier Python doit s'appeler **exactement** `Labyrinthe.py` (avec majuscule) et être dans le même dossier que `app.py`.

### Le navigateur affiche "Le serveur Python n'est pas démarré"
**Solution :** Vérifiez que vous avez lancé `python app.py` dans le terminal et qu'il tourne toujours.

### Erreur : "Port 5000 already in use"
**Solution :** Un autre programme utilise le port 5000. Changez le port dans `app.py` :
```python
app.run(debug=True, port=5001)  # ← Utilisez 5001 au lieu de 5000
```
Puis ouvrez `http://localhost:5001`

### L'interface ne se met pas à jour
**Solution :** Rafraîchissez la page (Ctrl+F5 ou Cmd+Shift+R)

### Erreur : "ModuleNotFoundError: No module named 'flask'"
**Solution :** Installez Flask :
```bash
pip install Flask flask-cors
```

---

## 📚 Fichiers inclus

| Fichier | Description |
|---------|-------------|
| `app.py` | Serveur Flask qui expose vos algorithmes Python via API |
| `index.html` | Interface web complète (HTML + CSS + JavaScript) |
| `requirements.txt` | Dépendances Python nécessaires |
| `Labyrinthe.py` | **Votre fichier** (à renommer si nécessaire) |

---

## 💡 Avantages de cette solution

✅ **Simple** : Seulement 3 fichiers (+ votre Python existant)  
✅ **Réutilise votre code** : Aucune modification de votre `Labyrinthe.py`  
✅ **Interface moderne** : HTML/CSS/JS avec animations  
✅ **Facile à personnaliser** : Couleurs, vitesse, taille...  
✅ **Portable** : Fonctionne sur n'importe quel ordinateur avec Python  

---

## 🎓 Pour aller plus loin

### Ajouter d'autres algorithmes

Dans `app.py`, ajoutez une nouvelle route :
```python
@app.route('/api/resoudre/astar')
def resoudre_astar():
    # Votre algorithme A*
    pass
```

Dans `index.html`, ajoutez un bouton :
```html
<button onclick="resoudre('astar')">🌟 A*</button>
```

### Permettre de dessiner son propre labyrinthe

Ajoutez du JavaScript pour cliquer sur les cellules et créer des murs, puis envoyez le nouveau labyrinthe au serveur Flask.

---

## ❓ Questions ?

**Q: Dois-je modifier mon fichier Labyrinthe.py ?**  
R: Non ! L'interface utilise votre code tel quel.

**Q: Est-ce que ça fonctionne sur mobile ?**  
R: Oui, tant que votre téléphone peut accéder au serveur local.

**Q: Puis-je héberger ça sur Internet ?**  
R: Oui ! Utilisez des services comme Heroku, Render, ou PythonAnywhere.

**Q: Combien de temps pour installer ?**  
R: 2 minutes si vous avez Python et pip installés.

---

**Bon code ! 🚀**

Si vous avez des questions ou des problèmes, vérifiez que :
1. ✅ Flask est installé (`pip install Flask flask-cors`)
2. ✅ Votre fichier s'appelle exactement `Labyrinthe.py`
3. ✅ Le serveur est lancé (`python app.py`)
4. ✅ Vous ouvrez `http://localhost:5000` dans le navigateur
