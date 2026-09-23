"""
utils/ — petites fonctions partagées par les notebooks du repo.

ask(prompt) envoie un prompt au modèle et renvoie le texte de la réponse.
Le reste du projet (naive_bot, hardened_bot, sweep, etc.) s'appuie
uniquement sur cette fonction.

On utilise Ollama ici : le modèle tourne EN LOCAL sur votre machine,
aucune inscription, aucun compte, aucune donnée envoyée sur internet.
- installez Ollama : https://ollama.com/download
- puis dans un terminal : ollama pull llama3.2
- assurez-vous qu'Ollama tourne en arrière-plan (il démarre automatiquement
  après installation ; sinon lancez l'appli Ollama une fois)

Chaque membre de l'équipe doit installer Ollama + faire "ollama pull llama3.2"
sur SA machine : le modèle tourne en local, il n'est pas partagé via une clé.
"""

from openai import OpenAI

# Ollama expose une API compatible OpenAI en local, sur le port 11434.
# Pas besoin de vraie clé API : Ollama n'en vérifie pas, mais le SDK
# OpenAI exige qu'on passe une valeur non vide.
_client = OpenAI(
    api_key="ollama",  # valeur factice, non vérifiée par Ollama
    base_url="http://localhost:11434/v1",
)

DEFAULT_MODEL = "llama3.2"


def ask(prompt: str, model: str = DEFAULT_MODEL, temperature: float = 0.0) -> str:
    """
    Envoie `prompt` comme unique message utilisateur au modèle local
    (via Ollama) et renvoie le texte de la réponse (str).
    """
    resp = _client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
    )
    return resp.choices[0].message.content
