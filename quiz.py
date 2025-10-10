import tkinter as tk
from tkinter import messagebox
import random
import time

from questions import questions

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz wielokrotnego wyboru")
        self.score = 0
        self.current_q = 0
        self.selected_vars = []
        self.current_options = []
        self.correct_indices = []
        self.user_answers = [None] * len(questions)
        self.checked_questions = [False] * len(questions)

        # Zegar
        self.start_time = time.time()
        self.running = True

        # Górny pasek
        top_frame = tk.Frame(root)
        top_frame.pack(pady=5)

        self.progress_label = tk.Label(top_frame, text="", font=("Arial", 12, "italic"))
        self.progress_label.pack(side=tk.LEFT, padx=20)

        self.timer_label = tk.Label(top_frame, text="Czas: 00:00", font=("Arial", 12, "bold"))
        self.timer_label.pack(side=tk.RIGHT, padx=20)

        # Pytanie
        self.question_label = tk.Label(root, text="", wraplength=500, font=("Arial", 14, "bold"))
        self.question_label.pack(pady=20)

        # Odpowiedzi
        self.options_frame = tk.Frame(root)
        self.options_frame.pack()

        # Poprawna odpowiedź (na dole)
        self.correct_label = tk.Label(root, text="", font=("Arial", 11, "italic"), fg="blue")
        self.correct_label.pack(pady=5)

        # Przyciski
        button_frame = tk.Frame(root)
        button_frame.pack(pady=15)

        self.back_button = tk.Button(button_frame, text="Cofnij", command=self.prev_question, state=tk.DISABLED)
        self.back_button.grid(row=0, column=0, padx=5)

        self.check_button = tk.Button(button_frame, text="Sprawdź", command=self.check_answer)
        self.check_button.grid(row=0, column=1, padx=5)

        self.next_button = tk.Button(button_frame, text="Dalej", command=self.next_question, state=tk.DISABLED)
        self.next_button.grid(row=0, column=2, padx=5)

        # W __init__ dodaj przycisk "Od nowa"
        self.restart_button = tk.Button(root, text="Od nowa", command=self.restart_quiz)
        self.restart_button.pack(pady=5)

        self.end_button = tk.Button(root, text="Sprawdź wynik (skończysz quiz)", command=self.end_quiz)
        self.end_button.pack(pady=10)

        self.show_question()
        self.update_buttons()
        self.update_timer()

    def show_question(self):
        for widget in self.options_frame.winfo_children():
            widget.destroy()

        q = questions[self.current_q]

        if self.user_answers[self.current_q] is None:
            indices = list(range(len(q["options"])))
            random.shuffle(indices)
            self.current_options = [q["options"][i] for i in indices]
            self.correct_indices = [indices.index(i) for i in q["correct"]]
        else:
            self.current_options = self.user_answers[self.current_q]["options"]
            self.correct_indices = self.user_answers[self.current_q]["correct"]

        self.progress_label.config(text=f"Pytanie {self.current_q + 1}/{len(questions)}")
        self.question_label.config(text=q["question"])
        self.correct_label.config(text="")  # wyczyść poprzednią poprawną odpowiedź

        self.selected_vars = []
        for option in self.current_options:
            var = tk.IntVar()
            chk = tk.Checkbutton(self.options_frame, text=option, variable=var, font=("Arial", 12))
            chk.pack(anchor="w")
            self.selected_vars.append(var)

        # Przywracanie wcześniejszych zaznaczeń
        if self.user_answers[self.current_q] is not None:
            selected = self.user_answers[self.current_q]["selected"]
            for i in selected:
                self.selected_vars[i].set(1)
            if self.checked_questions[self.current_q]:
                self.color_answers(selected)

        self.update_buttons()

    def check_answer(self):
        selected = [i for i, v in enumerate(self.selected_vars) if v.get() == 1]
        correct = set(self.correct_indices)
        selected_set = set(selected)

        # Dynamiczne kolorowanie:
        for i, widget in enumerate(self.options_frame.winfo_children()):
            if i in selected_set and i in correct:
                widget.config(bg="pale green")  # dobrze zaznaczone
            elif i in selected_set and i not in correct:
                widget.config(bg="lightcoral")  # źle zaznaczone
            elif i not in selected_set and i in correct:
                widget.config(bg="lightcoral")  # brak zaznaczenia poprawnej

        self.user_answers[self.current_q] = {
            "options": self.current_options,
            "correct": self.correct_indices,
            "selected": selected
        }
        self.checked_questions[self.current_q] = True

        if selected_set == correct:
            self.score += 1

        # Wyświetlenie poprawnych odpowiedzi:
        # Wyświetlenie poprawnych odpowiedzi w nowej linii:
        correct_answers = [self.current_options[i] for i in self.correct_indices]
        answers_text = "Poprawne odpowiedzi:\n" + "\n".join(f"- {ans}" for ans in correct_answers)
        self.correct_label.config(text=answers_text, justify="left")

        self.update_buttons(after_check=True)

    def update_buttons(self, after_check=False):
        # Przycisk cofania działa, jeśli nie jesteśmy na pierwszym pytaniu
        if self.current_q == 0:
            self.back_button.config(state=tk.DISABLED)
        else:
            self.back_button.config(state=tk.NORMAL)

        # Przycisk dalej działa zawsze, jeśli nie jesteśmy na ostatnim pytaniu
        if self.current_q < len(questions) - 1:
            self.next_button.config(state=tk.NORMAL)
        else:
            self.next_button.config(state=tk.DISABLED)

        # "Sprawdź" pozostaje dostępny zawsze, dopóki pytanie nie zostało sprawdzone
        if self.checked_questions[self.current_q]:
            self.check_button.config(state=tk.DISABLED)
        else:
            self.check_button.config(state=tk.NORMAL)


    def next_question(self):
        if self.current_q < len(questions) - 1:
            self.current_q += 1
            self.show_question()

    def prev_question(self):
        if self.current_q > 0:
            self.current_q -= 1
            self.show_question()

    def update_timer(self):
        if self.running:
            elapsed = int(time.time() - self.start_time)
            minutes = elapsed // 60
            seconds = elapsed % 60
            self.timer_label.config(text=f"Czas: {minutes:02}:{seconds:02}")
            self.root.after(1000, self.update_timer)

    def end_quiz(self):
        if not self.running:
            return
        self.running = False

        elapsed = int(time.time() - self.start_time)
        minutes = elapsed // 60
        seconds = elapsed % 60

        self.back_button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.DISABLED)
        self.check_button.config(state=tk.DISABLED)
        self.end_button.config(state=tk.DISABLED)

        messagebox.showinfo(
            "Koniec quizu",
            f"Twój wynik: {self.score}/{len(questions)}\n"
            f"Czas: {minutes:02} min {seconds:02} sek"
        )

    def restart_quiz(self):
        # Resetujemy zmienne
        self.score = 0
        self.current_q = 0
        self.selected_vars = []
        self.current_options = []
        self.correct_indices = []
        self.user_answers = [None] * len(questions)
        self.checked_questions = [False] * len(questions)
        
        # Tasujemy pytania ponownie
        random.shuffle(questions)
        
        # Resetujemy timer
        self.start_time = time.time()
        self.running = True
        
        # Wczytujemy pierwsze pytanie
        self.show_question()
        
        # Przywracamy aktywność przycisków
        self.back_button.config(state=tk.DISABLED)
        self.check_button.config(state=tk.NORMAL)
        self.end_button.config(state=tk.NORMAL)
        self.update_buttons()
        self.update_timer()



# Uruchomienie
root = tk.Tk()
app = QuizApp(root)
root.mainloop()
