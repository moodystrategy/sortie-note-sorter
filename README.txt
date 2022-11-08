Sortie (written in Python) is an automatic note sorter app, intended to categorize your study notes automatically.
Sortie works by reading all text files listed in files.txt for words that match your note.  
If one is found and not listed in ban.txt, the note will be written to that file.  
Ban.txt also curates itself, but you can also manually enter words to ban.
Using Sortie is simple!
All you need to run Sortie is to have Python installed.  After that, ensure that the folder that Sortie is contained in has the following files:
  ban.txt
  files.txt
  Any other files you want Sortie to write to
In files.txt, write the exact file names (including the extension) of any files you want to have Sortie write to.
ban.txt will curate a list of words that will not be considered for match searches. Any time a word is matched between multiple files, it will be added to the ban list.
When you first start using Sortie, you need to enter a few notes to start in each text file you want to use. This provides Sortie with a foothold to build off of.
If no word matches are found anywhere, Sortie can't sort your note. Seed your note files with as much as possible!
