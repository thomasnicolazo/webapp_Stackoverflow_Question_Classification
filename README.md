# StackOverflow tag suggestion

Cette API est le résultat du projet suggestion de tags pour la plateforme stackoverflow. Elle est à destination des utilisateurs qui souhaitent avoir une suggestion de tags pour leurs questions. Cette API fonctionne avec l'encodeur USE et un classificateur de regression logistique.
## fonctionement 
L'API est réalisé avec Flask. Les diffèrentes étapes se composent de la manière suivante:
  - l'utilisateur entre la question
  - Tokenization de la question avec l'API [NLTK](https://www.nltk.org/)
  - supression des des stop words
  - lemmatization du texteavec [en_core_web_sm](https://spacy.io/models/en#en_core_web_sm) de la librairie spaCy
  - utilisation de l'encodeur [USE](https://tfhub.dev/google/collections/universal-sentence-encoder/1) sur les lemmas
  - application du modèle de regression logistique 
  - transformation des résultats obtenus par le classificateur avec des dictionaires de passage. Ils sont contenus dans le fichier labels 
  - l'application renvoie une suggestions de tags pour l'utilisateur
---
## Docker
Un dockerfile est disponible pour l'API. Pour le lancer une fois dans le dossier de l'application:\
`docker build -t stack .`\
`docker run stack`\
