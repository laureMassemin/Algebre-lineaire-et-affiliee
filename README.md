# Algèbre Linéaire et Affiliée

Une bibliothèque Python complète pour les opérations d'algèbre linéaire, incluant les vecteurs, matrices, systèmes linéaires, espaces vectoriels, applications linéaires et programmation linéaire.

## Fonctionnalités

### Vecteurs (`vector.py`)
- Création et manipulation de vecteurs
- Opérations : addition, soustraction, multiplication scalaire
- Produit scalaire et norme
- Méthodes utilitaires (longueur, accès aux coordonnées)

### Matrices (`matrix.py`)
- Créations de matrices par dimensions ou liste de listes
- Opérations matricielles : addition, soustraction, multiplication
- Transposition
- Calcul du déterminant
- Inversion de matrice

### Systèmes Linéaires (`linearSystem.py`)
- Représentation de systèmes linéaires Ax = b
- Création de matrice augmentée
- Résolution par élimination gaussienne
- Support pour les systèmes sur- et sous-déterminés

### Espaces Vectoriels (`VectorielSpace.py`)
- Définition d'espaces vectoriels par une base
- Vérification de l'indépendance linéaire
- Calcul de dimensions
- Opérations sur les espaces vectoriels

### Applications Linéaires (`linearApplication.py`)
- Représentation d'applications linéaires par des matrices
- Application d'une transformation à un vecteur
- Composition d'applications linéaires
- Calcul de noyau et image

### Programmation Linéaire (`linearProgramming.py`)
- Formulation de problèmes de programmation linéaire
- Maximisation ou minimisation sous contraintes
- Algorithme du simplexe
- Gestion des contraintes d'inégalité

## Installation

### Prérequis
- Python 3.6+

## Architecture

```
.
├── vector.py              # Classe Vector
├── matrix.py              # Classe Matrix
├── linearSystem.py        # Classe LinearSystem
├── VectorielSpace.py      # Classe VectorielSpace
├── linearApplication.py   # Classe ApplicationLineaire
├── linearProgramming.py   # Classe LinearProgram
├── __init__.py            # Module init
└── README.md              # Cette documentation
```
