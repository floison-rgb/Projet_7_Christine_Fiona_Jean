"""
utils/ — petites fonctions partagées par les notebooks du repo.

ask(prompt) envoie un prompt au modèle hosted (OpenAI) et renvoie le texte
de la réponse. Le reste du projet (naive_bot, hardened_bot, sweep, etc.)
s'appuie uniquement sur cette fonction.
"""

import os
from openai import OpenAI

# La clé est lue depuis la variable d'environnement OPENAI_API_KEY.
# Ne mettez JAMAIS votre clé API en dur dans le code ou sur GitHub.
_client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

DEFAULT_MODEL = "gpt-4o-mini"


def ask(prompt: str, model: str = DEFAULT_MODEL, temperature: float = 0.0) -> str:
    """
    Envoie `prompt` comme unique message utilisateur au modèle hosted
    et renvoie le texte de la réponse (str).
    """
    resp = _client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
    )
    return resp.choices[0].message.content
