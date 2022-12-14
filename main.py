# Feel free to use, change the code but please keep Authorship Attribution:
# This app was made by Dennis Rotnov https://github.com/LearnFL

import random

alist = ['rock','paper', 'scissors']

adict = {
    'paper': {
        'scissors': 0,
        'paper': 1,
        'rock': 2
    },
    'rock': {
        'paper': 0,
        'rock': 1,
        'scissors': 2
    },
    'scissors': {
        'rock': 0,
        'scissors': 1,
        'paper': 2
    }
}

winner = ['Human Wins!', 'Good job, you have won!', 'And human wins again!', 'Winner-winner chicken dinner!',
            'Alright, human wins!', 'Congrats you won!', 'You are the winner!', 'Woohooo you won!', 'Computer is in tears, human wins!']
loser = ['Computer wins!', 'AI wins!', 'Skynet wins!', 'Cyber brain wins!', 'There is no shame in loosing! YOU LOST!',
            'Ha-ha you lost!', 'Better luck next time, you lost buddy!', 'You lost!', 'Skynet is rising, T1000 has won!', 'No one is perfect, you lost!']

class Game:
    def __init__(self, alist, adict, winner, loser, game=None):
        self.game = game
        self.alist = alist
        self.adict = adict
        self.winner = winner
        self.loser = loser

    @staticmethod
    def rule(h, c, winner, loser):
        human = adict.get(h)
        computer = adict.get(c)
        hum = computer.get(h)
        comp = human.get(c)
        if hum < comp:
            print(random.choice(winner))
            print('')
        elif comp < hum:
            print(random.choice(loser))
            print('')
        else:
            print('-=Draw=-')
            print('')
    
    @staticmethod
    def depict (x):
        rock = '''
                    _______
                ---'   ____)
                    (_____)
                    (_____)
                    (____)
                ---.__(___)
                '''

        paper = '''
                    _______
                ---'   ____)____
                        ______)
                        _______)
                        _______)
                ---.__________)
                '''

        scissors = '''
                    _______
                ---'   ____)____
                        ______)
                    __________)
                    (____)
                ---.__(___)
                '''
        if x == 0:
            print(rock)
        elif x == 1:
            print(paper)
        else:
            print(scissors)

    def __call__(self):
        if self.game is None:
            print('Enter 0 for Rock, 1 for Paper, 2 for Scissors')
            self.human = input('Human: ')
            while (self.human not in ['0', '1', '2']):
                print('Value must be a number between 0 and 2')
                self.human = input('Human: ')
            self.comp = random.randint(0, 2)
            print(f'Computer:  {alist[self.comp]}')
            self.depict(self.comp)
            self.human_score = alist[int(self.human)]
            self.computer_score = alist[self.comp]
            self.rule(self.human_score, self.computer_score, self.winner, self.loser)

game = Game(alist, adict, winner, loser, game=None)
for i in range(10):
    game()
