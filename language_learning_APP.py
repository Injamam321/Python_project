class LanguageLearningApp:
    def __init__(self):
        self.languages = {
            'bangla': {
                'hello': 'হ্যালো',
                'thank you': 'ধন্যবাদ',
                'please': 'অনুগ্রহ করে',
                'goodbye': 'বিদায়',
                'good morning': 'শুভ সকাল',
                'good night': 'শুভ রাত্রি',
                'how are you': 'কেমন আছো?',
                'i am fine': 'আমি ভালো আছি',
                'what is your name': 'তোমার নাম কি?',
                'my name is': 'আমার নাম',
                'welcome': 'স্বাগতম',
                'excuse me': 'মাফ করবেন',
                'sorry': 'দুঃখিত',
                'yes': 'হ্যাঁ',
                'no': 'না',
                'i love you': 'আমি তোমায় ভালোবাসি',
                'help': 'সাহায্য',
                'where is': 'কোথায়',
                'how much': 'কত টাকা',
                'i don’t understand': 'আমি বুঝতে পারছি না'
            },
            'english': {
                'hello': 'hello',
                'thank you': 'thank you',
                'please': 'please',
                'goodbye': 'goodbye',
                'good morning': 'good morning',
                'good night': 'good night',
                'how are you': 'how are you?',
                'i am fine': 'i am fine',
                'what is your name': 'what is your name?',
                'my name is': 'my name is',
                'welcome': 'welcome',
                'excuse me': 'excuse me',
                'sorry': 'sorry',
                'yes': 'yes',
                'no': 'no',
                'i love you': 'i love you',
                'help': 'help',
                'where is': 'where is',
                'how much': 'how much',
                'i don’t understand': 'i don’t understand'
            },
            'spanish': {
                'hello': 'hola',
                'thank you': 'gracias',
                'please': 'por favor',
                'goodbye': 'adios',
                'good morning': 'buenos días',
                'good night': 'buenas noches',
                'how are you': '¿cómo estás?',
                'i am fine': 'estoy bien',
                'what is your name': '¿cómo te llamas?',
                'my name is': 'me llamo',
                'welcome': 'bienvenido',
                'excuse me': 'perdón',
                'sorry': 'lo siento',
                'yes': 'sí',
                'no': 'no',
                'i love you': 'te quiero',
                'help': 'ayuda',
                'where is': '¿dónde está?',
                'how much': '¿cuánto cuesta?',
                'i don’t understand': 'no entiendo'
            },
            'french': {
                'hello': 'bonjour',
                'thank you': 'merci',
                'please': 's\'il vous plaît',
                'goodbye': 'au revoir',
                'good morning': 'bon matin',
                'good night': 'bonne nuit',
                'how are you': 'comment ça va?',
                'i am fine': 'je vais bien',
                'what is your name': 'comment tu t\'appelles?',
                'my name is': 'je m\'appelle',
                'welcome': 'bienvenue',
                'excuse me': 'excusez-moi',
                'sorry': 'désolé',
                'yes': 'oui',
                'no': 'non',
                'i love you': 'je t\'aime',
                'help': 'aidez-moi',
                'where is': 'où est',
                'how much': 'combien ça coûte',
                'i don’t understand': 'je ne comprends pas'
            },
            'german': {
                'hello': 'hallo',
                'thank you': 'danke',
                'please': 'bitte',
                'goodbye': 'auf Wiedersehen',
                'good morning': 'guten Morgen',
                'good night': 'gute Nacht',
                'how are you': 'wie geht\'s?',
                'i am fine': 'mir geht\'s gut',
                'what is your name': 'wie heißt du?',
                'my name is': 'ich heiße',
                'welcome': 'willkommen',
                'excuse me': 'entschuldigung',
                'sorry': 'es tut mir leid',
                'yes': 'ja',
                'no': 'nein',
                'i love you': 'ich liebe dich',
                'help': 'hilfe',
                'where is': 'wo ist',
                'how much': 'wie viel kostet',
                'i don’t understand': 'ich verstehe nicht'
            },
            'korean': {
                'hello': '안녕하세요 (annyeonghaseyo)',
                'thank you': '감사합니다 (gamsahamnida)',
                'please': '제발 (jebal)',
                'goodbye': '안녕히 가세요 (annyeonghi gaseyo)',
                'good morning': '좋은 아침 (joeun achim)',
                'good night': '안녕히 주무세요 (annyeonghi jumuseyo)',
                'how are you': '어떻게 지내세요? (eotteoke jinaeseyo?)',
                'i am fine': '저는 괜찮아요 (jeoneun gwaenchanhayo)',
                'what is your name': '이름이 뭐에요? (ireumi mwoeyo?)',
                'my name is': '제 이름은 (je ireumeun)',
                'welcome': '환영합니다 (hwanyeonghamnida)',
                'excuse me': '죄송합니다 (joesonghamnida)',
                'sorry': '미안합니다 (mianhamnida)',
                'yes': '네 (ne)',
                'no': '아니요 (aniyo)',
                'i love you': '사랑해요 (salanghaeyo)',
                'help': '도와주세요 (dowajuseyo)',
                'where is': '어디에 있어요? (eodie isseoyo?)',
                'how much': '얼마에요? (eolmaeyo?)',
                'i don’t understand': '이해하지 못해요 (ihaehaji mothaeyo)'
            },
            'hindi': {
                'hello': 'नमस्ते (Namaste)',
                'thank you': 'धन्यवाद (Dhanyavaad)',
                'please': 'कृपया (Kripya)',
                'goodbye': 'अलविदा (Alvida)',
                'good morning': 'सुप्रभात (Suprabhat)',
                'good night': 'शुभ रात्रि (Shubh Raatri)',
                'how are you': 'कैसे हो? (Kaise ho?)',
                'i am fine': 'मैं ठीक हूँ (Main theek hoon)',
                'what is your name': 'तुम्हारा नाम क्या है? (Tumhara naam kya hai?)',
                'my name is': 'मेरा नाम है (Mera naam hai)',
                'welcome': 'स्वागत है (Swagat hai)',
                'excuse me': 'माफ़ करें (Maaf karein)',
                'sorry': 'मुझे माफ़ करें (Mujhe maaf karein)',
                'yes': 'हां (Haan)',
                'no': 'नहीं (Nahin)',
                'i love you': 'मैं तुमसे प्यार करता हूँ (Main tumse pyaar karta hoon)',
                'help': 'मदद (Madad)',
                'where is': 'कहाँ है? (Kahan hai?)',
                'how much': 'कितना है? (Kitna hai?)',
                'i don’t understand': 'मुझे समझ में नहीं आता (Mujhe samajh mein nahin aata)'
            },
            # Add more languages as needed
        }

    def show_menu(self):
        print('\n--- Language Learning APP ---')
        print('1. Learn Basic Phrases')
        print('2. Take a Quiz')
        print('3. Exit')

    def learn_phrases(self):
        print('\nChoose a language: ')
        for i, language in enumerate(self.languages.keys(), 1):
            print(f'{i}. {language}')
        
        choice = int(input('Enter your choice: ')) - 1
        selected_language = list(self.languages.keys())[choice]
        
        print(f'\nBasic phrases in {selected_language.capitalize()}:')
        for phrase, translation in self.languages[selected_language].items():
            print(f'{phrase.capitalize()} - {translation.capitalize()}')

    def take_quiz(self):
        print('\nChoose a language for the quiz: ')
        for i, language in enumerate(self.languages.keys(), 1):
            print(f'{i}. {language}')
        
        choice = int(input('Enter your choice: ')) - 1
        selected_language = list(self.languages.keys())[choice]

        print(f'\nQuiz for {selected_language.capitalize()}:')
        # Add quiz functionality here

if __name__ == "__main__":
    app = LanguageLearningApp()
    while True:
        app.show_menu()
        choice = int(input('Enter your choice: '))
        
        if choice == 1:
            app.learn_phrases()
        elif choice == 2:
            app.take_quiz()
        elif choice == 3:
            break
        else:
            print('Invalid choice. Please try again.')

