#EXPANDED DATABASE Total: 45 Questions
game_data = {
    "1": {  # === EASY LEVEL ===
        "Prepositions": [
            {"q": "The book is ___ the table.", "options": ["A. on", "B. in", "C. at"], "ans": "A"},
            {"q": "I wake up ___ 7 o'clock.", "options": ["A. on", "B. in", "C. at"], "ans": "C"},
            {"q": "She was born ___ 1999.", "options": ["A. on", "B. in", "C. at"], "ans": "B"},
            {"q": "The cat is ___ the box (inside).", "options": ["A. on", "B. in", "C. under"], "ans": "B"},
            {"q": "I go ___ school by bus.", "options": ["A. to", "B. for", "C. at"], "ans": "A"}
        ],
        "Verbs": [
            {"q": "He ___ football every Sunday.", "options": ["A. play", "B. plays", "C. playing"], "ans": "B"},
            {"q": "They ___ students.", "options": ["A. is", "B. am", "C. are"], "ans": "C"},
            {"q": "I ___ an apple yesterday.", "options": ["A. eat", "B. eats", "C. ate"], "ans": "C"},
            {"q": "She is ___ a book now.", "options": ["A. read", "B. reads", "C. reading"], "ans": "C"},
            {"q": "We ___ to the park last week.", "options": ["A. go", "B. went", "C. gone"], "ans": "B"}
        ],
        "Adjectives": [
            {"q": "The sun is very ___.", "options": ["A. hot", "B. cold", "C. soft"], "ans": "A"},
            {"q": "An elephant is a ___ animal.", "options": ["A. small", "B. big", "C. short"], "ans": "B"},
            {"q": "Ice cream tastes ___.", "options": ["A. sweet", "B. salty", "C. spicy"], "ans": "A"},
            {"q": "The turtle is ___.", "options": ["A. fast", "B. slow", "C. loud"], "ans": "B"},
            {"q": "I am ___ because I passed the exam.", "options": ["A. sad", "B. happy", "C. angry"], "ans": "B"}
        ]
    },

    "2": {  # === MEDIUM LEVEL ===
        "Prepositions": [
            {"q": "He is interested ___ learning Python.", "options": ["A. on", "B. in", "C. for"], "ans": "B"},
            {"q": "Are you afraid ___ spiders?", "options": ["A. of", "B. with", "C. about"], "ans": "A"},
            {"q": "It depends ___ the weather.", "options": ["A. from", "B. on", "C. at"], "ans": "B"},
            {"q": "I look forward ___ seeing you.", "options": ["A. to", "B. for", "C. with"], "ans": "A"},
            {"q": "This car belongs ___ me.", "options": ["A. with", "B. for", "C. to"], "ans": "C"}
        ],
        "Verbs": [
            {"q": "I ___ my homework already.", "options": ["A. finish", "B. have finished", "C. finishing"],
             "ans": "B"},
            {"q": "While I was sleeping, the phone ___.", "options": ["A. ring", "B. rang", "C. rings"], "ans": "B"},
            {"q": "You should stop ___ (quit logic).", "options": ["A. smoke", "B. to smoke", "C. smoking"],
             "ans": "C"},
            {"q": "If I ___ rich, I would travel.", "options": ["A. am", "B. was", "C. were"], "ans": "C"},
            {"q": "I used to ___ in London.", "options": ["A. live", "B. living", "C. lived"], "ans": "A"}
        ],
        "Adjectives": [
            {"q": "This movie is very ___.", "options": ["A. bored", "B. boring", "C. bore"], "ans": "B"},
            {"q": "She felt ___ after the run.", "options": ["A. exhausting", "B. exhausted", "C. exhaust"],
             "ans": "B"},
            {"q": "English is ___ than Math.", "options": ["A. easier", "B. more easy", "C. easy"], "ans": "A"},
            {"q": "He is the ___ student in class.", "options": ["A. tall", "B. taller", "C. tallest"], "ans": "C"},
            {"q": "This problem is ___ to solve.", "options": ["A. hard", "B. hardly", "C. harden"], "ans": "A"}
        ]
    },

    "3": {  # === HARD LEVEL ===
        "Prepositions": [
            {"q": "He was accused ___ theft.", "options": ["A. with", "B. of", "C. for"], "ans": "B"},
            {"q": "Please comply ___ the rules.", "options": ["A. to", "B. with", "C. by"], "ans": "B"},
            {"q": "She is amenable ___ change.", "options": ["A. to", "B. for", "C. with"], "ans": "A"},
            {"q": "He was prohibited ___ entering.", "options": ["A. to", "B. from", "C. for"], "ans": "B"},
            {"q": "We must apologize ___ the delay.", "options": ["A. about", "B. for", "C. on"], "ans": "B"}
        ],
        "Verbs": [
            {"q": "Had I known, I ___ have come.", "options": ["A. will", "B. would", "C. can"], "ans": "B"},
            {"q": "It is essential that he ___ present.", "options": ["A. be", "B. is", "C. was"], "ans": "A"},
            {"q": "The evidence ___ the theory.", "options": ["A. corroborates", "B. collaborates", "C. cooperates"],
             "ans": "A"},
            {"q": "Don't let the noise ___ you.", "options": ["A. distract", "B. distruct", "C. district"], "ans": "A"},
            {"q": "The government aims to ___ poverty.", "options": ["A. alleviate", "B. elevate", "C. allocate"],
             "ans": "A"}
        ],
        "Adjectives": [
            {"q": "His speech was ___ (brief).", "options": ["A. concise", "B. verbose", "C. long"], "ans": "A"},
            {"q": "The results were ___ (uncertain).", "options": ["A. ambiguous", "B. clear", "C. obvious"],
             "ans": "A"},
            {"q": "Computers are ___ nowadays (everywhere).", "options": ["A. rare", "B. ubiquitous", "C. unique"],
             "ans": "B"},
            {"q": "He is a ___ worker (careful).", "options": ["A. meticulous", "B. messy", "C. careless"], "ans": "A"},
            {"q": "This technology is now ___ (outdated).", "options": ["A. modern", "B. obsolete", "C. new"],
             "ans": "B"}
        ]
    }
}


#QUESTION FUNCTION
def ask_question(question_obj):
    print(f"\n[Question]: {question_obj['q']}")

    for option in question_obj['options']:
        print(option)

    #Answer
    user_ans = input("Your Answer (A/B/C): ").upper().strip()

    #Conditional structure
    if user_ans == question_obj['ans']:
        print(">>> Correct! Great job!")
        return 1  # right-->1 point
    else:
        print(f">>> Wrong! The correct answer was {question_obj['ans']}")
        return 0  # wrong-->0 point



#LOGIC
import random
import time


def start_game():
    total_score = 0
    questions_to_ask = 10  #question number

    #difficulty choose
    print("\n" + "=" * 40)
    print("   ENGLISH VOCABULARY CHALLENGE 2025    ")
    print("=" * 40)
    print("Select Difficulty:")
    print("1. Level 1 (Easy)")
    print("2. Level 2 (Medium)")
    print("3. Level 3 (Hard)")


    while True:
        choice = input("Enter choice (1-3): ").strip()
        if choice in ["1", "2", "3"]:
            break
        else:
            print("Invalid input! Please enter 1, 2, or 3.")


    #gain data form database
    current_level_dict = game_data[choice]

    print(f"\n---> Loading Level {choice}... Mixing Questions... <---")
    time.sleep(1)


    question_pool = []   #new question dictionary

    for topic, q_list in current_level_dict.items():
        for q in q_list:
            question_pool.append((topic, q))


    selected_batch = random.sample(question_pool, questions_to_ask)

    current_q_num = 1

    for topic_name, question_obj in selected_batch:
        print(f"\n" + "-" * 30)
        print(f"Question {current_q_num}/{questions_to_ask} [Topic: {topic_name}]")
        print("-" * 30)

        score = ask_question(question_obj)
        total_score += score
        current_q_num += 1
        time.sleep(0.5)

        #Ask if player wants to restart after each question
        if current_q_num % 6 == 0:
            while True:
                restart = input("\nDo you want to restart the game? (yes/no): ").lower()

                if restart in ["yes", "y"]:
                    print("Restarting game...")
                    return 999

                elif restart in ["no", "n"]:
                    print("Continuing game...")
                    break

                else:
                    print("Invalid input! Please enter yes or no.")




    print("\n" + "=" * 40)
    print(f" COMPLETED! Final Score: {total_score} / {questions_to_ask}")

    # --- Easter Egg Trigger ---
    if total_score < 2:
        print("\n=== Easter Egg Unlocked!!! ===")
        print("Do you love this game? (Answer: What is 500 + 21?)")

        egg_ans = input("Your Answer: ").lower().strip()

        # Accept many correct formats
        valid_answers = [
            "521",
            "five hundred and twenty one",
            "five hundred twenty one",
            "five hundred & twenty one",
            "5 hundred 21",
            "five hundred twenty-one",
            "five hundred and twenty-one"
        ]

        if egg_ans in valid_answers:
            print("\n🎉 Correct! You found the secret bonus! +6 points!")
            total_score += 6
        else:
            print("\nAlright, let's see your score...")
    elif total_score >= 8:
        print("Rating: S (Outstanding!)")
    elif total_score >= 6:
        print("Rating: A (Good Job!)")
    else:
        print("Rating: B (Keep Practicing!)")
    print("=" * 40)

    return 0

#Replay Loop
if __name__ == "__main__":
    game_running = True

    while game_running:
        result = start_game()

        if result == 999:
            continue  # restart instantly



        while True:
            replay = input("\nDo you want to play again or challenge other level? (yes/no): ").lower()

            if replay in ["yes", "y"]:
                game_running = True
                break

            elif replay in ["no", "n"]:
                print("Thanks for playing. Goodbye!")
                print("Game: English Vocabulary Challenge 1.0 Crafted by 3ZXW")
                game_running = False
                break

            else:
                print("Invalid input! Please enter yes or no.")