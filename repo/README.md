# REPO


[![Spellcheck Pass](https://img.shields.io/badge/Spellcheck%20Pass-brightgreen?style=for-the-badge&logo=spellcheck&logoColor=black)](#)
[![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)](https://www.microsoft.com/windows)
[![Linux](https://img.shields.io/badge/Linux-20232A?style=for-the-badge&logo=linux&logoColor=white)](https://www.linux.org/)
[![Markdown](https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white)](https://daringfireball.net/projects/markdown/) 
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/) 
[![PEP8 Test Pass](https://img.shields.io/badge/PEP8%20Test%20Pass-g?style=for-the-badge&logo=)](#)
[![Test Pass](https://img.shields.io/badge/Test%20Pass-brightgreen?style=for-the-badge&)](#)

## Descrizione

`REPO` è UN pacchetto Python che utilizza il modulo `comune.py` come libreria all'interno del programma principale `repo.py`.
Implementa delle funzioni per copiare file `.py` da una directory di origine ad una di destinazione.

## Requisiti

- `Python` installato sul proprio computer.
- Aver installato le librerie contenute nel file `requirements.txt`.

## Esecuzione

Per eseguire il progetto, segui questi passaggi:

1. Assicurati che tutti i **requisiti** siano soddisfatti.
2. Apri il **prompt dei comandi** di Windows o di Linux.
3. Naviga nella cartella contenente il file `repo.py`.

4. - Esegui il comando `python.exe repo.py c:\work c:\programmmi_python` sul prompt dei comandi di Windows per copiare i file `.py` dalla directory `c:\work` nella directory `c:\programmmi_python`.

   - Esegui il comando `$ python3 repo.py c:/work c:/programmmi_python` sul prompt dei comandi di Windows per copiare i file `.py` dalla directory `c:/work` nella directory `c:/programmmi_python`.

### Esempio di input:
...\browseos\src>`python.exe repo.py C:\\Users\\ivang C:\\Users\\ivang\\OneDrive\\Documenti`
### Esempio di output:

   ```
Esecuzione COPY *.py da C:\Users\ivang to C:\Users\ivang\OneDrive\Documenti
ic| f"COPY {file_origine} TO {file_destinazione}": ('COPY '
                                                    'C:\\Users\\ivang\\comune.py '
                                                    'TO '
                                                    'C:\\Users\\ivang\\OneDrive\\Documenti\\comune_1.py')
ic| f"COPY {file_origine} TO {file_destinazione}": ('COPY '
                                                    'C:\\Users\\ivang\\repo.py '
                                                    'TO '
                                                    'C:\\Users\\ivang\\OneDrive\\Documenti\\repo_2.py')
   ```

## Tags

- #python
- #package
- #commit
- #cross

## Author

Questo progetto è stato creato da:
- Ivan Granata