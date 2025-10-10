import tkinter as tk
from tkinter import messagebox
import random
import time

# Lista pytań
questions = [
    {
        "question": "Naturalne przetwarzanie obrazu, przewyższające jego sztuczny odpowiednik, charakteryzuje:",
        "options": [
            "powtarzalność wyników",
            "większa skuteczność rozpoznawania obrazów dwuznacznych",
            "szybka analiza obrazów złożonych",
            "szybsze rozpoznawanie prostych obiektów w czasie rzeczywistym"
        ],
        "correct": [1,2]
    },
    {
        "question": "Czy na podstawie składowej luminancji (Y) i dwóch składowych chrominancji (Cr, Cb) możliwe jest odtworzenie barw podstawowych RGB:",
        "options": ["tak", "nie"],
        "correct": [0]
    },
    {
        "question": "Luminancja Y niesie informację o:",
        "options": [
            "obecności koloru czerwonego w pikselach",
            "poziomie jasności piksela",
            "obecności koloru zielonego w pikselach",
            "obecności koloru niebieskiego w pikselach"
        ],
        "correct": [1]
    },
    {
        "question": "Do układu optycznego oka można zaliczyć:",
        "options": ["tęczówkę", "siatkówkę", "rogówkę", "soczewkę"],
        "correct": [2, 3]
    },
    {
        "question": "Dla obrazu czarno-białej szachownicy wykonujemy przeskalowanie do dwukrotnie większej rozdzielczości. "
                    "Stosujemy metody: „najbliższego sąsiada” oraz interpolację. Która da lepszy rezultat?",
        "options": ["interpolacja", "najbliższego sąsiada"],
        "correct": [1]
    },
    {
        "question": "Histogram skumulowany obrazu po operacji wyrównania histogramu ma w przybliżeniu postać:",
        "options": ["funkcji liniowej", "funkcji pierwiastkowej", "funkcji kwadratowej", "nie da się wyznaczyć histogramu skumulowanego"],
        "correct": [0]
    },
    {
        "question": "W metodzie BBHE (Bi-Histogram Equalization) za kryterium podziału przyjmuje się średnią jasność w obrazie.",
        "options": ["prawda", "fałsz"],
        "correct": [0]
    },
    {
        "question": "Operacja wyrównania histogramu w RGB (osobno dla każdej ze składowych) nie powoduje znaczącej zmiany kolorów w obrazie.",
        "options": ["prawda", "fałsz"],
        "correct": [1]
    },
    {
        "question": "Kiedy jednopunktowe przekształcenie obrazu jest odwracalne:",
        "options": [
            "zawsze",
            "tylko jeśli funkcja przekształcająca jest rosnąca",
            "jeśli funkcja przekształcająca jest ściśle monotoniczna",
            "tylko jeśli funkcja przekształcająca jest malejąca",
            "nigdy"
        ],
        "correct": [2]
    },
    {
        "question": "Które z podanych przekształceń nie są operacjami kontekstowymi:",
        "options": ["konwolucja", "LUT", "binaryzacja", "filtracja medianowa"],
        "correct": [1, 2]
    },
    {
        "question": "Wybierz z poniższych filtry liniowe:",
        "options": ["filtr medianowy", "filtr konwolucyjny", "filtr maksymalny"],
        "correct": [1]
    },
    {
        "question": "W pokazanym na wykładzie filtrze adaptacyjnym uśrednianiu w drugim kroku nie podlegają:",
        "options": ["punkty obiektów", "minima lokalne", "maksima lokalne", "punkty krawędzi"],
        "correct": [3]
    },
    {
        "question": "Cechą charakterystyczną maski filtru górnoprzepustowego jest:",
        "options": [
            "suma współczynników > 0",
            "suma współczynników = 0",
            "suma współczynników < 0"
        ],
        "correct": [1]
    },
    {
        "question": "Które z poniższych filtrów służą do wyostrzania obrazu?",
        "options": ["filtr uśredniający", "filtr dolnoprzepustowy", "filtr górnoprzepustowy", "filtr medianowy"],
        "correct": [2]
    },
    {
        "question": "Zakładając rozmiar filtru dolnoprzepustowego na 3x3 przy operacji zmiany rozdzielczości, "
                    "o ile pikseli należy powielić brzeg obrazu, aby zlikwidować zakłócenia?",
        "options": ["3", "1", "2", "0"],
        "correct": [1]
    },
    {
        "question": "Czy operacja dolnoprzepustowości pozwala usunąć zakłócenia typu impulsowego?",
        "options": ["prawda", "fałsz"],
        "correct": [1]
    },
    {
        "question": "Wyznaczono dwuwymiarową transformatę Fouriera obrazu. Gdzie będą znajdowały się niskie częstotliwości F-obrazu (po transformacji optycznej)?",
        "options": ["jest to zależne od obrazu", "na krawędziach F-obrazu", "w centrum F-obrazu", "w rogach F-obrazu"],
        "correct": [2]
    },
    {
        "question": "Czy następujące zdanie jest poprawne? Konwolucja w dziedzinie F-obrazu odpowiada mnożeniu w dziedzinie przestrzennej?",
        "options": ["tak", "nie", "tak, ale tylko gdy rozdzielczość F-obrazu jest potęgą liczby 2", "tak, ale tylko gdy rozdzielczość obrazu jest potęgą liczby 2"],
        "correct": [0]
    },
    {
        "question": "Czy bazując tylko na fazie F-obrazu można dokonać pełnej rekonstrukcji obrazu rzeczywistego?",
        "options": ["tak", "nie", "tak, ale pod warunkiem że amplituda jest liniowa", "tak, ale pod warunkiem że amplituda jest opisana funkcją analityczną"],
        "correct": [1]
    },
    {
        "question": "Dany jest obraz lekko nieostry. Jakie podejście powinno umożliwić poprawienie jego jakości?",
        "options": [
            "dodanie/odjęcie od obrazu rezultatu filtracji dolnoprzepustowej",
            "dodanie/odjęcie od obrazu rezultatu filtracji medianowej",
            "dodanie/odjęcie od obrazu rezultatu filtracji górnoprzepustowej",
            "dodanie/odjęcie od obrazu rezultatu filtracji maksymalnej"
        ],
        "correct": [2]
    },
        {
            "question": "Dany jest obraz wejściowy. Zaproponuj maskę 3x3, która pozwoli na wykrycie krawędzi poziomych. Następnie dokonaj filtracji splotowej z wybraną maską. Na wyniku zaznacza poszukiwaną krawędź. Uwaga: piksele brzegowe pozostaw bez zmian. Pomiń normalizację.\nObraz wejściowy:\n1 1 2 1 1\n1 1 2 1 1\n2 2 4 2 2\n4 4 6 4 4\n4 4 6 4 4",
            "options": [
                "[-1 -1 -1; 0 0 0; 1 1 1]",
                "[1 1 1; 0 0 0; -1 -1 -1]",
                "[0 1 0; 1 -4 1; 0 1 0]",
                "[1 0 -1; 2 0 -2; 1 0 -1]"
            ],
            "correct": [1]
        },
#??
  
    {
        "question": "Czy konwersja RGB -> odcienie szarości jest operacją odwracalną?",
        "options": ["tak", "nie"],
        "correct": [1]
    },
    {
        "question": "Które z podanych akronimów nie są oznaczeniem przestrzeni kolorów:",
        "options": ["CMYK", "RGB", "YYU", "HSV", "Lac", "HSI"],
        "correct": [2, 4]
    },
   
    {
        "question": "Dwukrotną redukcję rozdzielczości obrazu można osiągnąć stosując kolejno:",
        "options": [
            "filtrację dolnoprzepustową i podpróbkowanie",
            "filtracje dolnoprzepustową i nadpróbkowanie",
            "podpróbkowanie i filtrację dolnoprzepustową",
            "filtrację górnoprzepustową i podpróbkowanie"
        ],
        "correct": [0]
    },
    {
        "question": "Histogram obrazu po operacji wyrównania histogramu powinien mieć rozkład:",
        "options": ["normalny", "chi-kwadrat", "dla takiego obrazu nie da się wyznaczyć histogramu", "jednostajny", "binarny (tylko dwie wartości)"],
        "correct": [3]
    },
    {
        "question": "W metodzie DSIHE (Dualistic Sub-Image Histogram Equalization) obraz dzieli się na dwa podzbiory o takiej samej liczbie pikseli.",
        "options": ["prawda", "fałsz"],
        "correct": [0]
    },
    {
        "question": "Wyrównanie histogramu w przestrzeni barw HSV, z wykorzystaniem tylko składowej V pozwala zachować kolory na obrazie.",
        "options": ["prawda", "fałsz"],
        "correct": [0]
    },
    {
        "question": "Operacje geometryczne to operacje, w których:",
        "options": [
            "położenie pikseli (x,y) zmieniane jest zgodnie z dana relacją matematyczną",
            "jasność pikseli, których położenie jest zmienne, nie ulega zmianie",
            "jasność pikseli dla tych samych współrzędnych w obrazie sprzed operacji i po niej może się różnić",
            "nowa wartość jasności piksela obliczana jest na podstawie jego poprzedniej wartości zgodnie z przyjętą relacją matematyczną"
        ],
        "correct": [0, 1, 2]
    },
    {
        "question": "Które z poniższych operacji są operacjami bezkontekstowymi?",
        "options": ["negacja", "filtr konwolucyjny", "LUT", "filtr medianowy"],
        "correct": [0, 2]
    },
    {
        "question": "Wybierz z poniższych filtr nieliniowy:",
        "options": ["filtr medianowy", "filtr konwolucyjny", "filtr logiczny"],
        "correct": [0, 2]
    },
    {
        "question": "Filtr adaptacyjny to taki, który...",
        "options": [
            "podczas filtracji zmienia swoje współczynniki",
            "podczas filtracji zmienia przefiltrowane już wartości",
            "podczas filtracji zmienia swoje współczynniki oraz już przefiltrowane wartości",
            "podczas filtracji „wybiera” punkty obrazu, które następnie filtruje"
        ],
        "correct": [0, 3]
    },
    {
        "question": "Filtr kombinowany:",
        "options": [
            "to złożenie dwóch lub więcej masek filtrów prostych (np. Sobel, Prewitt)",
            "służy np. do wykrywania krawędzi",
            "do łącznie filtrów stosuje się formułę Euklidesową lub modułową"
        ],
        "correct": [0, 1, 2]
    },
    {
        "question": "Czy można zdefiniować pojęcie filtracji medianowej obrazów kolorowych?",
        "options": [
            "tak, trzeba tylko odpowiednio zdefiniować medianę i miarę odległości między pikselami (w sensie koloru)",
            "tak, ale tylko dla obrazów w przestrzeni RGB",
            "tak, ale tylko dla obrazów w przestrzeni HSV",
            "nie, mediana jest operacją tylko dla obrazów w skali szarości"
        ],
        "correct": [0]
    },
    {
        "question": "Jak będzie wyglądała amplituda F-obrazu po ograniczeniu się do I ćwiartki?",
        "options": [
            "amplituda będzie trudna w interpretacji (złożone kształty)",
            "jeden wyraźny punkt odpowiedzialny za funkcję sinus",
            "dwa wyraźne punkty: stała składowa oraz funkcja sinus",
            "trzy wyraźne punkty: stała składowa oraz dwa komponenty złożone z funkcji sinus",
            "cztery wyraźne punkty: stała składowa oraz trzy odpowiedzialne za różne funkcje sinus"
        ],
        "correct": [2]
    },
    {
        "question": "Filtracja medianowa wybiera wartość z otoczenia bez wprowadzania nowych wartości:",
        "options": ["prawda", "fałsz"],
        "correct": [0]
    },

    {
        "question": "Wyznaczono dwuwymiarową transformację Fouriera obrazu. Gdzie będą wysokie częstotliwości w F-obrazie?",
        "options": ["jest to zależne od obrazu", "tylko na krawędziach F-obrazu", "w centrum F-obrazu", "poza centrum F-obrazu"],
        "correct": [3]
    },
    {
        "question": "Splot obrazu z maską filtru w dziedzinie przestrzeni reprezentowany jest w dziedzinie częstotliwości jako:",
        "options": ["iloczyn F-obrazu i F-obrazu filtru", "sumę F-obrazu i F-obrazu filtru", "splot F-obrazu i F-obrazu filtru", "żadne z powyższych"],
        "correct": [0]
    },
    {
        "question": "Czy bazując tylko na amplitudzie F-obrazu można dokonać pełnej rekonstrukcji obrazu rzeczywistego?",
        "options": ["tak", "nie", "tak, ale pod warunkiem, że faza jest liniowa", "tak, ale pod warunkiem, że faza opisana jest funkcją analityczną"],
        "correct": [1]
    },
    {
        "question": "Dany jest obraz z szumem impulsowym. Najlepsze wyniki filtracji uzyskuje się wykorzystując:",
        "options": ["filtr górnoprzepustowy", "filtr dolnoprzepustowy", "filtr medianowy", "filtr maksymalny"],
        "correct": [2]
    },
    {
    "question": "Dany jest obraz wejściowy. Zaproponuj maskę 3x3, która pozwoli na wykrycie krawędzi poziomych. Następnie dokonaj filtracji splotowej z wybraną maską. Na wyniku zaznacza poszukiwaną krawędź. Uwaga: piksele brzegowe pozostaw bez zmian. Pomiń normalizację.\nObraz wejściowy:\n1 1 2 1 1\n1 1 2 1 1\n2 2 4 2 2\n4 4 6 4 4\n4 4 6 4 4",
    "options": [
        "[-1 0 1; -1 0 1; -1 0 1]",
        "[1 0 -1; 1 0 -1; 1 0 -1]",
        "[0 1 0; 1 -4 1; 0 1 0]",
        "[1 0 -1; 2 0 -2; 1 0 -1]"
    ],
    "correct": [1]
}


]


random.shuffle(questions)


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

        self.end_button = tk.Button(root, text="Zakończ quiz", command=self.end_quiz)
        self.end_button.pack(pady=10)

        self.show_question()
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
        correct_answers = [self.current_options[i] for i in self.correct_indices]
        self.correct_label.config(text="Poprawne odpowiedzi: " + ", ".join(correct_answers))

        self.update_buttons(after_check=True)

    def update_buttons(self, after_check=False):
        if self.current_q == 0:
            self.back_button.config(state=tk.DISABLED)
        else:
            self.back_button.config(state=tk.NORMAL)

        if after_check:
            self.check_button.config(state=tk.DISABLED)
            self.next_button.config(state=tk.NORMAL)
        else:
            self.check_button.config(state=tk.NORMAL)
            self.next_button.config(state=tk.DISABLED)

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
        self.next_button.config(state=tk.DISABLED)
        self.end_button.config(state=tk.NORMAL)

        self.update_timer()



# Uruchomienie
root = tk.Tk()
app = QuizApp(root)
root.mainloop()
