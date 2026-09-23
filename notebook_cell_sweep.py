# --- Cellule à coller dans le notebook, après avoir chargé ATTACKS ---

import sys
sys.path.append(".")
from hireguard import naive_bot, hardened_bot, sweep

print("=== AVANT (naive_bot) ===")
before = sweep(naive_bot, ATTACKS)

print("\n=== APRÈS (hardened_bot) ===")
after = sweep(hardened_bot, ATTACKS)

print("\n=== RÉSUMÉ ===")
print(f"Attack success rate : {before['attack_success_rate']:.0%} -> {after['attack_success_rate']:.0%}")
print(f"False positive rate : {before['false_positive_rate']:.0%} -> {after['false_positive_rate']:.0%}")
