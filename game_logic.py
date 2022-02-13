from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.modalview import ModalView
from kivy.uix.label import Label
from random import randint
from board import coordinate

# size gaming window
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '500')


class MainApp(App):
    def __init__(self):
        super().__init__()
        self.switch = True

    def winner(win, str_win):
        """ end game - popup """
        popup = ModalView(size_hint=(0.75, 0.5))
        victory_label = Label(text=str_win, font_size=40)
        popup.add_widget(victory_label)
        popup.open()

    def game(self, arg):
        """ gomoku logic """
        end_game = False
        arg.disabled = True
        arg.text = 'X'
        while True:
            rand_choice = randint(0, 100)
            if self.buttons[rand_choice].disabled == False:
                self.buttons[rand_choice].text = 'O'
                self.buttons[rand_choice].disabled = True
                break
        vector = lambda item: [self.buttons[x].text for x in item]
        for item in coordinate:
            winning_combination_X = ('X', 'X', 'X', 'X', 'X')
            winning_combination_O = ('O', 'O', 'O', 'O', 'O')
            if str(winning_combination_X).strip('()') in str(vector(item)).strip('[]'):
                str_win = 'You Winn!'
                end_game = True
                MainApp.winner(end_game,str_win)
            elif (str(winning_combination_O).strip('()') in str(vector(item)).strip('[]')):
                str_win = 'You Lose!'
                end_game = False
                MainApp.winner(end_game, str_win)
                end_game = True
            if end_game:
                for button in self.buttons:
                    button.disabled = True
                break
    
    def restart(self, arg):
        """ restart game """
        self.switch = True
        for button in self.buttons:
            button.text = ''
            button.disabled = False
    
    def build(self):
        """ build plaing board """
        self.title = 'Gomoku game'
        root = BoxLayout(orientation="vertical", padding=10)
        grid = GridLayout(cols=10)
        self.buttons = []
        for _ in range(100):
            button = Button(
                background_color= '#ffffff',
                color=[252, 141, 141, 1],
                font_size=24,
                disabled=False,
                on_press = self.game
            )
            self.buttons.append(button)
            grid.add_widget(button)
        root.add_widget(grid)

        # restart game
        root.add_widget(
            Button(
                text='Restart',
                size_hint=[1, .1],
                background_color='red',
                font_size=28,
                on_press=self.restart
            )
        )
        return root


if __name__ == "__main__":
    MainApp().run()