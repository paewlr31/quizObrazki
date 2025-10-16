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
        "question": "Elementem światłoczułym oka jest:",
        "options": ["rogówka", "teczówka", "siatkówka", "źrenica"],
        "correct": [2]
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
        "question": "W przeciwienstwie do filtracji liniowej (dolnoprzepustowej), przy filtracji medianowej jako nowy piksel wybierana jest któraś wartość z otoczenia (tj. nie ma mozliwości pojaiwneia sie jasności/koloru który nie występuje w oryginalnym)",
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
    },
    #kolos1a 2016
    {
        "question": "Czy charakterystyka spektralna czujnika CCD i czułość spektralna ludzkiego oka są:",
        "options": [
            "takie same",
            "oko ludzkie obejmuje szerszy zakres niz CCD",
            "CCD obejmuje szerszy zakres niż oko ludzkie",
            "maksymalna czułość CCD jest przesunięta w stronę nadfioletu",
            "maksymalna czułość CCD jest przesunięta w stronę podczerwieni"
        ],
        "correct": [2,4]
    },{
        "question": "Plamka żółta w oku to",
        "options": [
            "miejsce o największym skupieniu czopków",
            "ujście nerwu wzrokowego"
        ],
        "correct": [0]
    },{
        "question": "Dla kombinacji liniowej dwóch obrazów monochromatycznych:",
        "options": [
            "należy bezwzględnie dokonać normalizacji obrazu wyjściowego",
            "nomrlaizacja obrazu wyjściowego nie jest potrzebna",
            "należy wykonać normalizację obrazu wyjściowego, jeżeli jest to niezbędne (zależy od współczynników kombinacji)",
            " zapobiec sytuacji, w której nastąpi ewentualne dzielenie przez zero za pomocą przekształcenia log(I(x,y)+1), np. drugi obraz ma punkt o wartości zero dla ustalonych współrzędnych (x,y)"
        ],
        "correct": [2,3]
    },{
        "question": " Często obraz kolorowy jest kodowany za pomocą 32 bitów. Wówczas 24 bity stosuje się na zakodowanie składowych punktu oraz dodatkowo 8 bitów w celu",
        "options": ["zapisania nasycenia barwy czerwonej", 
                    "zapisania nasycenia barwy zielonej",
                    "zapisania nasycenia barwy niebieskiej",
                    "zwiększenia wydajności operowania na obrazie"
                    ],
        "correct": [3]
    },{
        "question": " Z wymienionych poniżej, wskaż przestrzenie barw, w których wyróżnia się osobną składową jasności obrazu",
        "options": ["RGB", "YUV", "CMY", "HSV", "CMYK"],
        "correct": [1,3]
    },{
        "question": "Zaznacz prawidłowe zdanie(a) dotyczące interpolacji obrazów barwnych",
        "options": ["niezbędne jest wykonanie interpolacji najbliższego sąsiada dla każdego kanału oddzielnie", 
                    "interpolacje najbliższego sąsiada wystarczy wykonac dla pojedynczego kanału", 
                    "niezbędne jest wykonanie interpolacji liniowej dla każdego kanału oddzielnie", 
                    "interpolacje liniową wystarczy wykonac dla pojedynczego kanału"
                    ],
        "correct": [0,2]
    },{
        "question": "Który z filtrów górnoprzepustowych zachowuje informację o kierunku zmiany pochodnej (gradientu) na obrazie:",
        "options": ["filtr Prewitta", "filtr Sobela", "filtr adaptacyjny", "filtr Laplace'a (laplsjan)"],
                  
        "correct": [0,1]
    },{
        "question": "Czy przyjmując rozmiar okna globalnego równy rozmiarowi okna lokalnego, filtr NL-means (non-local means) sprowadza się do filtra bilateralnego?",
        "options": [
            "tak",
            "nie"
        ],
        "correct": [1]
    },{
        "question": "Filtr NL-means (non-local means) jest filtrem (zaznacz poprawne stwierdzenie lub stwierdzenia):",
        "options": [
            "liniowym",
            "nieliniowym",
            "rekurencyjnym"
           
        ],
        "correct": [1]
    },{
        "question": "Wskaż poprawne zdania o algorytmach binaryzacji poznanych na zajęciach:",
        "options": [
            "metoda Otsu wymaga podania dwoch progów T1 i T2",
            "w metodzie Sauvola próg binaryzacji wyznaczony jest na podstawie otoczenia analizowanego piksela",
            "w doborze progu binaryzacji największe znaczenie ma analiza histogramu",
            "do segmentacji obrazu o niejednorodnym oświetleniu najlepiej nadaje sie ktoras z metod globalnych"
           
        ],
        "correct": [1,2]
    },{
        "question": "Która (-e) z masek opisuja filtry kierunkowe?",
        "options": [
            "[0,-1,0] [-1,4,-1] [0,-1,0]",
            "[1,1,1] [1,-2,1] [-1,-1,-1]",
            "[1,1,1] [1,-2,-1] [1,-1,-1]",
            "[1,2,1] [2,4,2] [1,2,-1]"
           
        ],
        "correct": [1,2]
    },
    #kolos 1b 2016
    {
        "question": "W którym z wymienionych zakresów widmowym czułość sensorów obrazu typu CCD jest największa:",
        "options": [
            "ultrafioletu",
            "widzialnym",
            "bliskiej podczerwieni (800–1100 nm)",
            "fal radiowych UKF"
        ],
        "correct": [2]
    },{
        "question": "Opis: “niska czułość, widzenie przy dobrym oświetleniu, widzenie barwne” odpowiada",
        "options": [
            "pręcikom",
            "czopkom"
        ],
        "correct": [1]
    },{
        "question": "Ile różnych poziomów jasności może zawierać obraz, którego poziom jasności reprezentowany danym 16-bitowymi?",
        "options": [
            "16",
            "256",
            "1024",
            "8096",
            "65536"
        ],
        "correct": [4]
    },{
        "question": " Zaznacz prawidłowe odpowiedzi dotyczące modelu CMY/CMYK",
        "options": [
            "CMY to model subtraktywny",
            "Wartość składowej K otrzymujemy przez zależność: K=max(C,M,Y)",
            "Wartość składowej K otrzymujemy przez zależność: K=min(C,M,Y)",
            "CMY to model addytywny."
        ],
        "correct": [0,2]
    },{
        "question": " W jakich sytuacjach metoda najbliższego sąsiada daje lepsze efekty niż interpolacja dwuliniowa:",
        "options": ["nigdy", 
                    "w przypadku niektórych naturalnych obrazów, z bogatą paletą odcieni szarości", 
                    "zawsze", 
                    "w przypadku niektórych syntetycznych obrazów, z bardzo ograniczoną paletą odcieni szarości"
                    ],
        "correct": [3]
    },{
        "question": " Czy suma współczynników filtra (elementów maski) po normalizacji może przekraczać wartość 1?",
        "options": [
            "tak",
            "nie",
            "tak, ale tylko gdy filtr jest usredniajaco-medianowy"
           
        ],
        "correct": [1] 
    },{
        "question": "Które z poniższych zakłóceń może być lepiej usunięte przez medianę niż przez filtr uśredniający",
        "options": [
            " usunięcie szumu o rozkładzie normalnym (Gaussa)",
            "niewykorzystanie wszystkich poziomów jasności",
            "nierównomierne oświetlenie sceny",
            "usunięcie szumu salt and pepper"
           
        ],
        "correct": [3]
    },{
       "question": "Które z zakłóceń (ciemny kształt na jasnym tle) zostanie całkowicie wyeliminowane przez medianę o masce kwadratowej 5x5",
        "options": [
            "o rozmiarze 2x4",
            "o rozmiarze 5x6",
            "o rozmiarze 3x5",
            "o rozmiarze 11x2"
           
        ],
        "correct": [0]   
    },{
        "question": "Czy można ustawić filtr bilateralny w ten sposób, aby filtrował szum niejednorodny (zmienne natężenie szumu w obrazie)?",
        "options": ["tak", "nie"],
        "correct": [0]
    },{
        "question": "Zaznacz poprawne stwierdzenia dotyczące filtra NL-means (non-local means):",
        "options": [
            "wysoka złożoność obliczeniowa i duża dokładność filtracji",
            "niska złożoność obliczeniowa i duża dokładność filtracji",
            "filtr ustala wagi na podstawie podobieństw w jasności punktów w analizowanym oknie z punktem centralnym okna",
            "do poprawnego działania filtr NL-means wymaga obrazu referencyjnego (na przykład obraz przefiltrowany innym filtrem)" 
        ], 
        "correct": [0,2]
    },{
        "question": "Metoda lokalnej binaryzacji Sauvoli wykorzystuje jako parametry",
        "options": [
            "odchylenie standardowe w oknie",
            "średnią jasność w oknie",
            "wartość maksymalną w oknie",
            "wartość minimalną w oknie",
            "splot okna z filtrem Gabora"
           
        ],
        "correct": [0,1]
    },{
        "question": "Który z niekorzystnych efektów jest niwelowany dzięki zastosowaniu dwuetapowego przetwarzania w filtrze adaptacyjnym przedstawionym na wykładzie:",
        "options": [
            "sklejanie zakłóceń w większe grupy niemożliwe do usunięcia",
            "zmiana gabarytów małych obiektów",
            "rozjaśnienie obrazu",
            "rozmywanie punktów krawędziowych"
           
        ],
        "correct": [0]
    },{
        "question": "Która z poniższych masek nie jest maską laplasjanową?",
        "options": [
            "[0,-1,0] [-1,4,-1] [0,-1,0]",
            "[-1,-1,-1] [-1,7,-1] [0,-1,-1]",
           "[-1,-1,-1] [-1,8,-1] [-1,-1,-1]",
           
        ],
        "correct": [2]
    },
    #kolos 2018 a/b
    {
        "question": "W przypadku niejednorodnego oświetlenia obrazu dobrze sprawdzają się metody binaryzacji:",
        "options": [
            "lokalnej",
            "globalnej"
           
        ],
        "correct": [0]
    }


]


random.shuffle(questions)