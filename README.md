🤖 Agent Vocal IA - Enquête de Satisfaction 🗣️

🚀 Introduction

Bienvenue dans le projet Agent Vocal IA ! Ce projet implémente un agent vocal interactif qui pose des questions, écoute les réponses des utilisateurs, et enregistre les dialogues dans un fichier CSV pour une analyse ultérieure. Le tout se fait à l'aide de la synthèse vocale et de la reconnaissance vocale. 🤖🎤

⚙️ Fonctionnalités

Synthèse vocale (TTS) : L'agent pose des questions à l'utilisateur en utilisant des voix humaines grâce à Edge-TTS.
Reconnaissance vocale : L'agent écoute les réponses de l'utilisateur et les enregistre à l'aide de la bibliothèque SpeechRecognition.
Enregistrement des réponses : Les réponses de l'utilisateur sont sauvegardées dans un fichier CSV pour une analyse future.
Interaction en temps réel : L'agent et l'utilisateur peuvent discuter pendant l'enquête avec des échanges en temps réel.

🛠️ Technologies utilisées

Edge-TTS pour la synthèse vocale
SpeechRecognition pour la reconnaissance vocale
Sounddevice et Numpy pour la gestion audio
CSV pour l'enregistrement des dialogues
Python 3.x

📥 Installation

1. Cloner le dépôt Git
bash
Copier
Modifier
git clone https://github.com/ton-utilisateur/nom-du-repository.git
cd nom-du-repository
2. Créer un environnement virtuel
bash
Copier
Modifier
python -m venv venv
3. Activer l'environnement virtuel
Windows :
bash
Copier
Modifier
venv\Scripts\activate
Mac/Linux :
bash
Copier
Modifier
source venv/bin/activate
4. Installer les dépendances
Installe les bibliothèques nécessaires :

bash
Copier
Modifier
pip install -r requirements.txt
5. Lancer le script
Tu peux maintenant lancer le script principal pour démarrer l'agent vocal :

bash
Copier
Modifier
python edge.py

🧑‍💻 Comment ça marche ?

L'agent vocal pose des questions (par exemple, "Quel est votre nom ?").
L'utilisateur répond à voix haute.
L'agent enregistre la réponse et l'ajoute à un fichier CSV avec un horodatage.
L'agent continue avec la question suivante, jusqu'à ce que toutes les questions soient posées.
À la fin de la session, l'agent vocal remercie l'utilisateur et affiche un résumé de l'historique des conversations.
📊 Exemple de fichier CSV généré
Timestamp	Type	Contenu
12:01:23	Agent	Bonjour, quel est votre nom ?
12:01:45	Utilisateur	Jean Dupont
12:02:05	Agent	Merci, sur une échelle de 1 à 10, comment évaluez-vous la qualité de nos services ?
12:02:35	Utilisateur	9
📑 Améliorations possibles
Voix plus naturelles : Tester différentes voix et ajuster les paramètres pour obtenir des voix plus naturelles.
Ajouter plus de questions et personnaliser les dialogues.
Améliorer la gestion des erreurs de reconnaissance vocale et de lecture audio.
