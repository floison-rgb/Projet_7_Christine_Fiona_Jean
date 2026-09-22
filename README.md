# Projet_7_Christine_Fiona_Jean

Project 7 — Prompt-injection red-team lab (Track B, hosted OpenAI)

## Structure
```
.
├── data/
│   └── attacks.jsonl        # 12 attaques + 1 contrôle bénin
├── utils/
│   └── __init__.py          # fonction ask() -> appelle l'API OpenAI
├── project7_injection_redteam.ipynb   # notebook de départ
└── requirements.txt
```

## Setup

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
export OPENAI_API_KEY="votre-clé"   # Windows: set OPENAI_API_KEY=votre-clé
jupyter notebook project7_injection_redteam.ipynb
```

## Tâches
1. Améliorer `succeeded()` — le check actuel (`"pwned" in reply`) est trop grossier.
2. Construire un `hardened_bot` : isoler les données non fiables, marquer l'input, filtrer l'output.
3. Comparer le taux de succès des attaques avant / après défenses, et documenter honnêtement ce qui passe encore.
