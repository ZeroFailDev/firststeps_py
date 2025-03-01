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

`browseos.py` elenca i file con un'estensione specificata (di default `.py`) all'interno di una cartella. Simile al comando `dir` della linea di comando, il programma usa le librerie `os`, `sys`, `platform`, `comune` e `icecream` per:

1. Verificare se il sistema operativo è supportato (Windows, Linux o macOS).
2. Verificare se la directory indicata esiste e può essere letta.
3. Elencare tutti i file con l'estensione specificata (o `.py` se non ne viene fornita una).
4. Mostrare il numero di file trovati con l'estensione desiderata.

Al termine, mostra anche il numero totale di file `.extension` trovati nella directory specificata.

Se il programma non trova file `.extension` visualizza tutti gli altri file con il loro intero percorso.

## Requisiti

Per eseguire questo progetto, è necessario avere i seguenti requisiti:

- *Aver installato python sul proprio computer*
- *Aver installato tutte le librerie contenute nel file `requirements.txt`*

## Esecuzione

Per eseguire il progetto, segui questi passaggi:

1. Assicurati che tutti i **requisiti** siano soddisfatti.
2. Apri il **prompt dei comandi** di Windows o di Linux.
3. **Naviga alla cartella** contenente il file `browseos.py`.
4. - Esegui il file scrivendo `python.exe browseos.py C:\users\12345` sul prompt dei comandi di Windows per visualizzare l'elenco dei file python all'interno della directory `C:\users\12345`.


   - Esegui il file scrivendo `$ python3 browseos.py` sul prompt dei comandi  di Linux per visualizzare l'elenco dei file python all'interno della directory nella quale ci si trova al momento.

### Esempio di input:
...\browseos\src>`python.exe browseos.py`
### Esempio di output:

   ```
   Operative system: Windows
Files found:
ic| '_________________________________________________________'
.\browseos.py
ic| '_________________________________________________________'
ic| '_________________________________________________________'
.\comune.py
ic| '_________________________________________________________'
ic| msg: "In Dir '.' there are '2' file .py"
ic| msg: 'The program execution time is 0.n'
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
