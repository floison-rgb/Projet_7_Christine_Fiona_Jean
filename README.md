# Projet_7_Christine_Fiona_Jean — HireGuard

Project 7 — Prompt-injection red-team lab, adapté au cas **HireGuard**, un assistant RH qui présélectionne des CV.

## Contexte

HireGuard lit les CV reçus et répond aux questions des recruteurs ("Ce candidat a-t-il 3 ans d'expérience en Python ?", "Résume son profil"). Le CV est une **donnée non fiable** : elle vient de l'extérieur, n'importe qui peut y écrire n'importe quoi — y compris du texte caché tentant de manipuler le bot. Le recrutement est un usage "à haut risque" selon l'AI Act européen.

## Structure
```
.
├── data/
│   └── attacks.jsonl        # 12 attaques + 5 contrôles bénins (contexte RH)
├── utils/
│   └── __init__.py          # fonction ask() -> appelle Ollama en local
├── project7_injection_redteam.ipynb   # notebook complet (bot, défenses, rapport)
├── requirements.txt
└── .gitignore
```

## Setup (chaque membre de l'équipe, sur sa propre machine)

1. Installer [Ollama](https://ollama.com/download)
2. Télécharger le modèle :
   ```bash
   ollama pull llama3.2
   ```
3. Vérifier qu'Ollama tourne en arrière-plan (icône dans la barre système)
4. Installer les dépendances Python :
   ```bash
   python -m venv venv
   source venv/bin/activate        # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
5. Ouvrir `project7_injection_redteam.ipynb` dans VS Code (extension Jupyter requise) et faire **Run All**

Aucune clé API, aucune inscription : le modèle tourne localement via Ollama.

## Tâches de l'équipe

1. **`succeeded()`** — améliorer le détecteur (fuite de la grille de notation confidentielle, dérive discriminatoire, signaux génériques)
2. **`hardened_bot()`** — fence des données non fiables, input flag, output filter
3. **Mesure & rapport** — comparer attack success rate ET false positive rate avant/après, documenter honnêtement ce qui passe encore

## KPIs mesurés

- **Attack success rate** avant vs après défenses (critère principal du projet)
- **False positive rate** sur les cas bénins (un bot trop paranoïaque bloque des recruteurs légitimes)
