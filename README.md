# Qu'est-ce qu'un Blueprint ?

Un blueprint est un moyen de diviser une application Flask en segments plus petits et plus gérables. Chaque blueprint peut avoir ses propres routes, vues, modèles, formulaires, fichiers statiques, et templates. Cette approche est particulièrement utile pour les grandes applications où la séparation des préoccupations améliore la maintenabilité et la lisibilité du code.

## Avantages des Blueprints
* **Modularité** : Permet de diviser l'application en modules distincts.
* **Réutilisabilité** : Facilite la réutilisation de segments de code entre différentes applications.
* **Organisation** : Améliore la structure et la lisibilité du code.
* **Collaboration** : Facilite le travail collaboratif en permettant à différentes équipes de travailler sur différents segments de l'application.


```
blueprint/
│
├── project/
│   ├── __init__.py
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── forms.py
│   │   └── routes.py
│   │
│   ├── main/
│   │   ├── __init__.py
│   │   └── routes.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py
│   │
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── img/
│   │
│   └── templates/
│       ├── auth/
│       │   ├── signup.html
│       │   └── login.html
│       ├── main/
│       │   ├── index.html
│       │   └── profile.html
│       └── base.html
│
├── .venv
├── db.sqlite
├── .gitignore
├── README.md
├── create_db.py
├── run.py
└── requirements.txt
```


