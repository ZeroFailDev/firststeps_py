# BrowseOs


[![Spellcheck Pass](https://img.shields.io/badge/Spellcheck%20Pass-brightgreen?style=for-the-badge&logo=spellcheck&logoColor=black)](#)
[![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)](https://www.microsoft.com/windows)
[![Linux](https://img.shields.io/badge/Linux-20232A?style=for-the-badge&logo=linux&logoColor=white)](https://www.linux.org/)
[![Markdown](https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white)](https://daringfireball.net/projects/markdown/) 
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/) 
[![PEP8 Test Pass](https://img.shields.io/badge/PEP8%20Test%20Pass-g?style=for-the-badge&logo=)](#)
[![Test Pass](https://img.shields.io/badge/Test%20Pass-brightgreen?style=for-the-badge&)](#)


## Descrizione

`BrowseOs` è un pacchetto Python che utilizza il modulo `comune.py` come libreria all'interno del programma principale `browseos.py`. 

Quando eseguito, il programma `browseos.py` esegue i seguenti controlli:
1. Mostra il sistema operativo in uso.
2. Verifica se la directory inserita esiste.
3. Controlla i permessi di lettura per la directory indicata.

Dopodiché `browseos.py` cerca la presenza di file `.py` all'interno della directory e sottodirectory e li elenca insieme al loro intero percorso.

Al termine, mostra anche il numero totale di file Python trovati nella directory specificata.

Se il programma non trova file `.py` visualizza tutti gli altri file con il loro intero percorso.

## Requisiti

Per eseguire questo progetto, è necessario avere i seguenti requisiti:

- *Aver installato python sul proprio computer*
- *Aver installato tutte le librerie contenute nel file `requirements.txt`*

## Esecuzione

Per eseguire il progetto, segui questi passaggi:

1. Assicurati che tutti i **requisiti** siano soddisfatti.
2. Apri il **prompt dei comandi** di Windows o di Linux.
3. **Naviga alla cartella** contenente il file `browseos.py`.
4. - Esegui il file scrivendo per esempio `python.exe browseos.py C:\users\12345` sul prompt dei comandi di Windows per visualizzare l'elenco dei file python all'interno della directory `C:\users\12345`.


   - Esegui il file scrivendo per esempio `$ python3 browseos.py` sul prompt dei comandi  di Linux per visualizzare l'elenco dei file python all'interno della directory nella quale ci si trova al momento.

### Esempio di input:
...\browseos\src>`python.exe browseos.py`
### Esempio di output:

   ```
   Operative system: Windows
Files found:
.\browseos.py
ic| '_________________________________________________________'
.\comune.py
ic| '_________________________________________________________'
In Dir '.' there are '2' file .py
   ```

## Tags

- #browseos
- #cross
- #librerie
- #python
- #array

## Author

Questo progetto è stato creato da:

- Ivan Granata
