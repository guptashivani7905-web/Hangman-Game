import random
import os

# 🎯 Custom word categories based on Shivani's interests
WORD_CATEGORIES = {
    "Gaming": ["freefire", "battle", "arena", "loot", "survivor"],
    "Coding": ["python", "variable", "function", "loop", "debug"],
    "Nature": ["river", "mountain", "forest", "sunrise", "rain"]
}

SCORE_FILE = "shivani_scores.txt"

class Hangman:
    def __init__(self, category, max_attempts=6):
        self.category = category
        self.word = random.choice(WORD_CATEGORIES[category])
        self.guessed = set()
        self.attempts_left = max_attempts
        self.hint_used = False

    def show_word(self):
        return ' '.join([ch if ch in self.guessed else '_' for ch in self.word])

    def guess(self, letter):
        letter = letter.lower()
        if not letter.isalpha() or len(letter) != 1:
            return "⚠️ Enter a single alphabet letter."
        if letter in self.guessed:
            return f"🔁 You've already guessed '{letter}'."
        self.guessed.add(letter)
        if letter in self.word:
            return f"✅ '{letter}' is correct!"
        else:
            self.attempts_left -= 1
            return f"❌ '{letter}' is wrong. Attempts left: {self.attempts_left}"

    def give_hint(self):
        if self.hint_used:
            return "❌ Hint already used!"
        self.hint_used = True
        return f"💡 Hint: Word starts with '{self.word[0]}' and is from '{self.category}' category."

    def is_won(self):
        return all(ch in self.guessed for ch in self.word)

    def is_lost(self):
        return self.attempts_left <= 0

def save_score(name, category, word, result):
    with open(SCORE_FILE, "a") as f:
        f.write(f"{name} | {category} | {word} | {result}\n")

def play_game():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("🎮 Welcome to Shivani's Hangman Game!")
    name = input("👤 Enter your name: ").strip()

    print("\n📚 Categories:", ', '.join(WORD_CATEGORIES.keys()))
    category = input("Choose a category: ").capitalize()
    if category not in WORD_CATEGORIES:
        print("⚠️ Invalid category. Defaulting to 'Coding'")
        category = "Coding"

    game = Hangman(category)

    print(f"\n🧩 Word: {game.show_word()}")

    while not game.is_won() and not game.is_lost():
        user_input = input("Enter a letter or type 'hint': ").strip()
        if user_input.lower() == "hint":
            print(game.give_hint())
        else:
            print(game.guess(user_input))
        print(f"Word: {game.show_word()}")

    if game.is_won():
        print(f"\n🎉 Congrats {name}! You guessed the word: {game.word}")
        save_score(name, category, game.word, "Win")
    else:
        print(f"\n😢 Game Over! The word was: {game.word}")
        save_score(name, category, game.word, "Loss")

    again = input("\n🔁 Play again? (yes/no): ").lower()
    if again == "yes":
        play_game()
    else:
        print("👋 Thanks for playing, Shivani!")

if __name__ == "__main__":
    play_game()