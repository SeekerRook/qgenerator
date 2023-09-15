# ΟΔΗΓΙΕΣ

## ΓΙΑ ΝΑ ΤΑ ΕΞΑΓΩ 
1. Βρισκω το path του αρχειου (.txt) που θελω. Εστω raw.txt
2. τρεχω `python qparser.py raw.txt data.json` οπου `data.json` το ονομα που θελω να σωθουν οι ερωτησεις
3. Για κάθε αρχείο json (πχ `data_part1.json`) που θα παραχθει τρέχω `python qgenerator.py data_part1.json data1.xlsx` οπου `data1.xlsx` το ονομα του αρχειου excel που θελω να σωσει τις ερωτησεις 

## ΓΙΑ ΝΑ ΤΑ ΑΝΕΒΑΣΩ 
1. παιρνω τις ερωτησεις απο το excel (χωρις τιτλους) και τις επικολλαω χωρις μορφοποιηση (`Ctrl+Shift+V`) στo sample.xlsx. καλο ειναι να κραταω backup αυτου του αρχειου για να μη το χαλασω
2. αποθηκευω τις αλαγες και το ανεβαζω στο [quizz.com](https://quizizz.com/)