Codice gruppo: 8swi0vjwvl7

Traccia - Università

Scrivere un'applicazione client/server parallelo per gestire gli esami universitari

Linguaggio: ![Python Badge](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=for-the-badge)

## Segreteria
1. Inserisce gli esami sul server dell'università (salvare in un file o conservare in memoria il dato)
2. Inoltra la richiesta di prenotazione degli studenti al server universitario
3. Fornisce allo studente le date degli esami disponibili per l'esame scelto dallo studente

## Studente
1. Chiede alla segreteria se ci siano esami disponibili per un corso
2. Invia una richiesta di prenotazione di un esame alla segreteria 

## Server universitario
1. Riceve l'aggiunta di nuovi esami
2. Riceve la prenotazione di un esame
3. Il server universitario ad ogni richiesta di prenotazione invia alla segreteria il numero di prenotazione progressivo assegnato allo studente e la segreteria a sua volta lo inoltra allo studente

## Roadmap
### Backend
1. [x] Base client-server
2. [x] DB della piattaforma 
3. [x] Login differenziato Studente-Segreteria
4. [x] **Segreteria**
   1. [x] Inserimento esami
   2. [x] Inserimento richiesta di prenotazione esami
   3. [x] Fetch delle date disponibili per l'esame scelto
5. [ ] **Studente**
   1. [ ] Richiesta di date disponibili per un corso
   2. [ ] Invio richieste di prenotazione alla segreteria
6. **Server universitario**
   1. [x] Riceve l'aggiunta di nuovi esami
   2. [x] Riceve la prenotazione di un esame
   3. [x] Ad ogni richiesta di prenotazione invia alla segreteria il numero di prenotazione progressivo assegnato allo studente e la segreteria a sua volta lo inoltra allo studente

### GUI
1. [x] GUI Login
2. [ ] **Segreteria**
   1. [ ] Lista studenti ed esami con date
   2. [ ] Lista richieste di prenotazioni utente
   3. [ ] Lista richieste di date disponibili
3. [ ] **Studente**
   1. [ ] Lista esami dello studente
   2. [ ] Richiesta prenotazione
   3. [ ] Richiesta date d'esame

### Note di sviluppo
La prova d’esame richiede la progettazione e lo sviluppo della traccia proposta. 

Il progetto deve essere sviluppato secondo le seguenti linee:

utilizzare un linguaggio di programmazione a scelta (C, Java, Python, etc...)

utilizzare una piattaforma Unix-like;

utilizzare le socket;
inserire sufficienti commenti;

### Consegna progetto
Documentazione
Lo studente deve presentare la documentazione relativa al progetto. La documentazione deve contenere:

Descrizione del progetto;
Descrizione e schema dell'architettura;
Dettagli implementativi dei client/server;
Parti rilevanti del codice sviluppato;
Manuale utente con le istruzioni su compilazione ed esecuzione;
E' possibile redigere la documentazione usando latex o markdown

Per chi usa latex. Si consiglia di utilizzare la piattaforma Overleaf:

https://www.overleaf.com/
Per i markdown. 

https://mystmd.org/
Pagine descrittive usando Jekyll (https://jekyllrb.com/) o Hugo (https://gohugo.io/)
Consigliato usare le github pages (https://pages.github.com/)
Formato consegna
Ogni gruppo deve consegnare tutti i file e la documentazione tramite un servizio git remoto (github, gitlab, ...):

Creare un repository pubblico!
Ogni partecipante del gruppo deve essere aggiunto come collaboratore
Dare nomi significativi ai commit 
 

Consegna 
Il progetto va consegnato tramite email al docente emanuel.dinardo@uniparthenope.it

Obbligatorio inviare l'email dall'account studente
Inserire Nome, Cognome e Marticola di tutti i membri del gruppo
Inserire il link al repository github
Entro una settimana dall'esame
 

Modalità di esame
L'esame consisterà nella discussione del progetto con possibili domande sulla parte pratica e progettuale e domande di teoria.

I progetti di gruppo devono essere discussi OBBLIGATORIAMENTE da tutti i membri lo stesso giorno.
