import edge_tts
import asyncio
import csv
import os
import time
import sounddevice as sd
import numpy as np
import speech_recognition as sr
from datetime import datetime

class AgentVocal:
    def __init__(self, voice="fr-FR-DeniseNeural"):
        self.voice = voice
        self.csv_file = f"conversation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        # Créer le fichier CSV avec les en-têtes
        with open(self.csv_file, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "Type", "Contenu"])
        
        # Initialiser le recognizer pour la reconnaissance vocale
        self.recognizer = sr.Recognizer()
    
    async def text_to_speech(self, text, output_file="output.mp3"):
        """Convertit du texte en audio avec Edge-TTS et sauvegarde en MP3"""
        communicate = edge_tts.Communicate(text, self.voice)
        await communicate.save(output_file)
        self.save_to_csv("agent", text)
        return output_file
    
    def play_audio(self, file_path):
        """Joue un fichier audio"""
        if os.name == 'nt':  # Windows
            os.system(f"start {file_path}")
        else:  # Unix/Mac
            os.system(f"afplay {file_path}")
        
        # Attendre que le fichier soit joué (approximativement)
        # Pour une démo plus robuste, vous pourriez utiliser pygame ou un autre module
        duration = 1 + (len(file_path.split()) * 0.5)  # Estimation grossière
        time.sleep(duration)
    
    def listen_and_recognize(self, timeout=10):
        """Écoute l'utilisateur et retourne le texte reconnu"""
        print("🎤 Écoute en cours...")
        
        try:
            with sr.Microphone() as source:
                # Ajustement pour le bruit ambiant
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                print("Parlez maintenant...")
                
                # Écouter
                audio = self.recognizer.listen(source, timeout=timeout)
                
                # Reconnaître en utilisant Google Speech Recognition
                text = self.recognizer.recognize_google(audio, language="fr-FR")
                print(f"✓ Texte reconnu: {text}")
                self.save_to_csv("utilisateur", text)
                return text
        except sr.RequestError:
            print("❌ Erreur: Impossible de se connecter au service de reconnaissance")
            return "Désolé, je n'ai pas pu me connecter au service de reconnaissance vocale."
        except sr.UnknownValueError:
            print("❌ Impossible de reconnaître la parole")
            return "Je n'ai pas compris ce que vous avez dit."
        except Exception as e:
            print(f"❌ Erreur: {e}")
            return "Une erreur s'est produite lors de la reconnaissance vocale."
    
    def save_to_csv(self, speaker, content):
        """Sauvegarde un dialogue dans le CSV"""
        with open(self.csv_file, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            timestamp = datetime.now().strftime("%H:%M:%S")
            writer.writerow([timestamp, speaker, content])
    
    def show_conversation_history(self):
        """Affiche l'historique de la conversation depuis le CSV"""
        try:
            with open(self.csv_file, mode="r", encoding="utf-8") as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                print("\n--- HISTORIQUE DE LA CONVERSATION ---")
                for row in reader:
                    if len(row) >= 3:
                        timestamp, speaker, content = row
                        speaker_display = "🤖 Agent:" if speaker == "agent" else "👤 Utilisateur:"
                        print(f"[{timestamp}] {speaker_display} {content}")
                print("-----------------------------------\n")
        except Exception as e:
            print(f"Erreur lors de l'affichage de l'historique: {e}")

async def run_demo():
    agent = AgentVocal()
    
    # Script de conversation (questions prédéfinies)
    questions = [
        "Bonjour, je suis un assistant virtuel qui effectue une enquête de satisfaction. Pouvez-vous me donner votre nom et prénom ?", 
        "Merci. Sur une échelle de 1 à 10, comment évalueriez-vous la qualité de nos services ?",
        "Pourriez-vous me dire quels aspects de nos services vous appréciez le plus ?",
        "Y a-t-il des points que nous pourrions améliorer selon vous ?",
        "Merci beaucoup pour votre temps et vos réponses. Avez-vous d'autres commentaires à ajouter ?"
    ]
    
    # Introduction
    print("=== DÉMO D'AGENT IA VOCAL ===")
    print("L'agent va poser 5 questions. Parlez clairement après chaque question.")
    print("Mode alternatif (si la reconnaissance vocale ne fonctionne pas): répondez par texte")
    print("=============================================")
    input("Appuyez sur Entrée pour commencer...")
    
    # Boucle de conversation
    for question in questions:
        # Générer et jouer la question
        audio_file = await agent.text_to_speech(question)
        print(f"\n🤖 Agent: {question}")
        agent.play_audio(audio_file)
        
        # Mode reconnaissance vocale
        try:
            response = agent.listen_and_recognize()
        except Exception:
            # Fallback sur mode texte si la reconnaissance échoue
            print("Mode texte (fallback):")
            response = input("Votre réponse: ")
            agent.save_to_csv("utilisateur", response)
        
        # Pause
        time.sleep(1)
    
    # Conclusion
    conclusion = "Merci pour votre participation à cette enquête. Toutes vos réponses ont été enregistrées. Passez une excellente journée!"
    audio_file = await agent.text_to_speech(conclusion)
    print(f"\n🤖 Agent: {conclusion}")
    agent.play_audio(audio_file)
    
    # Afficher l'historique
    agent.show_conversation_history()
    print("\nLes réponses ont été sauvegardées dans:", agent.csv_file)

if __name__ == "__main__":
    # Installation des dépendances si nécessaire
    # pip install edge-tts SpeechRecognition sounddevice numpy pyaudio
    asyncio.run(run_demo())