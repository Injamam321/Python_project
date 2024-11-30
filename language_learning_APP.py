class LanguageLearningApp:
    def __init__(self):
        self.languages = {
            'spanish': {
                'hello': 'hola',
                'thank you': 'gracias',
                'please': 'por favor',
                'goodbye': 'adios'
            },
            'french': {
                'hello': 'bonjour',
                'thank you': 'merci',
                'please': 's\'il vous plaît',
                'goodbye': 'au revoir'
            },
            'german': {
                'hello': 'hallo',
                'thank you': 'danke',
                'please': 'bitte',
                'goodbye': 'auf Wiedersehen'
            }
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
        
        print(f'\nQuiz in {selected_language.capitalize()}:')
        score = 0
        
        for phrase, translation in self.languages[selected_language].items():
            answer = input(f'What is "{phrase}" in {selected_language}? ').strip().lower()
            if answer == translation:
                print('Correct!')
                score += 1
            else:
                print(f'Wrong. The correct answer is "{translation}".')
        
        print(f'\nYour score: {score}/{len(self.languages[selected_language])}')

    def run(self):
        while True:
            self.show_menu()
            choice = input('\nEnter your choice: ')
            
            if choice == '1':
                self.learn_phrases()
            elif choice == '2':
                self.take_quiz()
            elif choice == '3':
                print('Goodbye! Keep learning languages!')
                break
            else:
                print('Invalid choice. Please try again.')

# Run the Language Learning APP
if __name__ == '__main__':
    app = LanguageLearningApp()
    app.run()
