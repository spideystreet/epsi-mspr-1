## Problème de Fuite de Données (Data Leakage) et Résolution

### Le Problème Initial (Score de ~71% trompeur)
Au départ, nous divisions notre jeu de données de manière aléatoire. Cela signifiait que des données de toutes les années (2017, 2022, etc.) se retrouvaient à la fois dans l'ensemble d'entraînement (`train`) et de test (`test`). Le modèle s'entraînait donc sur des exemples de l'année 2022 et était ensuite évalué sur d'autres exemples de la même année.

C'est une forme de **fuite de données (data leakage)** : le modèle obtenait un score d'exactitude artificiellement élevé (~71%) car il était testé sur une période temporelle qu'il connaissait déjà, ce qui ne reflète pas une vraie capacité de prédiction.

### La Solution (Score de ~48% réaliste)
Nous avons résolu ce problème en implémentant une **division temporelle stricte**.
- **Entraînement :** Le modèle s'entraîne désormais **uniquement** sur les données des années antérieures à 2024.
- **Test :** Il est évalué **uniquement** sur les données de l'année 2024, qui sont complètement nouvelles pour lui.

Cette méthode simule correctement une prédiction sur l'avenir. Le score d'exactitude obtenu (autour de 48%) est plus faible, mais il est **honnête, fiable et représentatif** de la réelle capacité du modèle à généraliser sur des données inconnues.

### Hypothèse pour la Prédiction de 2027
Le modèle en lui-même n'a pas conscience du temps (la colonne `YEAR` a été volontairement retirée pour éviter un apprentissage de tendances temporelles simplistes). Il apprend uniquement la corrélation entre des caractéristiques socio-économiques et un résultat d'élection.

Pour prédire le résultat de 2027, nous utilisons les données de 2024 (nos données les plus récentes et complètes) comme un "proxy" ou une estimation. L'hypothèse sous-jacente est que la démographie ne subira pas de bouleversement majeur en 3 ans. Le modèle simule donc le résultat d'une élection de 2027 qui se déroulerait dans les conditions socio-économiques de 2024.