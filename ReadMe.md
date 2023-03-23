# Python webscraper, czy znajdzie mi prackę?
### Program będzie przeszukiwał kilka serwisów z ogłoszeniami o pracę, skupiając się na portalach przeznaczonych dla osób szukających zatrudnienia w branży IT, ale także najpopularniejsze portale gromadzące ogłoszenia z wielu branż (olx, pracuj.pl, potencjalnie linked.in).

### Następnie program odfiltruje oferty pasujące do tagów jakie poda użytkownik np. lokalizacja, technologia, doświadczenie.

### Ostatecznie, po zakończeniu poszukiwań, program wyśle na wskazany adres email znalezione oferty pracy.

### Dzięki takiemu rozwiązaniu nie trzeba się zapisywać na usługi mailingowe oferowane przez te strony, dzięki czemu zachowujemy nieco więcej prywatności a nasza skrzynka nie będzie otrzymywać ofert pracy zmieszanych z potencjalnym spamem.

### Strony jakie będziemy przeszukiwać:
- justjoin.it
- bulldogjob.pl
- nofluffjobs.com


### Atrybuty:
- Podane wartości powinny zostać umieszczone w odpowiednich miejscach miedzy znakami " "
    - justjoinit:
        - city: remote, warszwa, krakow, wroclaw, poznan trojmiasto, slask, bydgoszcz, bielsko-biala, bialystok, czestochowa, kielce, lublin, lodz, olsztyn, opole, rzeszow, szczecin, torun, zielona_gora, new-york, sydney, berlin, san-francisco, london

        - technology: html, php, ruby, python, java, net, scala, c, mobile, testing, devops, ux/ui, pm, game, analytics, security, data, go, support, erp, architecture, other

        - role: junior, mid, senior

    - bulldog:
        - city: Kraków, Remote, Abroad, Warszawa, Wrocław, Śląsk, Trójmiasto, Łódź, Lublin, Białystok, Kielce, Szczecin, Toruń, Częstochowa, Piła, Rzeszów, Bydgoszcz

        - technology: Java, JavaScript, Python, C%23, C++, PHP, Swift, Kotlin, Ruby

        - role: junior, medium, senior
        
    - nofluffjobs:
        - city: warszawa, krakow, wroclaw, gdansk, poznan, trojmiasto, katowice, slask, lodz, bialystok, gdynia, lublin, rzeszow, bydgoszcz, gliwice, czestochowa, szczecin, sopot
        
        - technology: .NET, SQL, Java, Python, React, AWS, TypeScript, HTML, Angular, Azure, PHP, C%2B%2B, Android, Kotlin, Vue.js, iOS, Golang, Spark, Scala, C, Hadoop, Ruby, Flutter, Elixir, C%23

        - role: trainee, junior, mid, senior, expert

### Uwagi:
#### Pierwsze uruchomienie programu wygeneruje pliki korespondujące ofertom znalezionym na poszczególnych portalach. Pliki te następnie są scalane w plik "offers.txt". Domyślnym zastosowaniem programu jest wywoływanie go np. raz w tygodniu, co sprawdzi czy pojawiły się nowe ofery.
#### Program po przeszukaniu, porówna zawartości plików z nowymi danymi i zapisze tylko nowe, w efekcie zapisując nowe oferty, których jeszcze nie widzieliśmy.
#### Z tego powodu jeśli uruchomimy program raz, a następnie zaraz po tym drugi raz, pliki nie będą zawierały żadnych ofert. Żeby ponownie zobaczyć wybrane ofery, należy uruchomić program ponownie.
#### Oferty z portalu nofluff mogą być w niektórych sytuacjach niezbyt dobrze dopasowane do oczekiwań postawionych przez użytkownika. Wynika to ze sposobu w jaki oferty są na tym portalu kategoryzowane. Każda technologia wprowadzona przez pracodawcę zalicza się do tagów. Więc w przypadku przeszukiwania ofert np. dla junior Javascript developera w Warszawie, zdarzało się spotkać oferty "Junior PHP Developer" dlatego że JavaScript został wpisany w stack technologiczny
#### Podejście w przeszukiwaniu justjoinit: Ta witryna prawdopodobnie używa dynamicznego ładowania treści, co oznacza, że treść strony jest generowana i ładowana w miarę interakcji użytkownika z nią. W takich przypadkach web scraper może nie być w stanie uzyskać pełnego kodu HTML strony, a w rezultacie żądana zawartość może nie zostać znaleziona. W takim przypadku szukanie diva z określoną klasą okazywało się bezcelowe, gdyż jego zawartość i tak nie zostawała wczytana. 
#### Zdecydowałem się użyć przeglądarki headless do przeszukiwania witryny, ponieważ umożliwi to interakcję z witryną tak, jakbyś był użytkownikiem, oraz uzyskanie dostępu do dynamicznie generowanej treści. Wybrałem jedną z popularnych headless przeglądarek - Selenium. 
#### Do wysyłania maili używamy API SendGrid które pozwala nam wysłać do 100 wiadomości dziennie co znacznie przekracza potrzeby projektu

### Przed uruchomnieniem:
W terminalu wpisz polecenie:
    pip install -r req.txt
    
#### Zajrzyj do pliku main.py. Domyślnymi wartościami wyszkiwanymi dla wszytkich stron jest pozycja juniora w technologii JavaSacript w Krakowie. Zmień poszczególne atrybuty aby spersonalizować poszukiwania. Ważne żeby zmienić adres email na który wysyłana będzie wiadomość (linia 52 pliku main.py)

### Instrukcja uruchomienia:
python3 main.py
