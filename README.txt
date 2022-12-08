## Table of Contents

- Introduction
- Requirements
- How to Use
- Future Plans
- Closing Statements


## Introduction

Hello, Welcome to FlashED! This is my very first project after coding for approximately threee months so good practice
and standards are not really my strong suit :) Please be nice to me T^T

FlashED has been a program that I wish existed during my journey of learning different languages. I always hated upon
learning a new word to have to create a new flashcard by looking it up online and writing down all the fields for the 
flashcard. This program makes that process slightly easier as it makes use of txt file dictionaries that are readily
found online to make flashcards instantaneously with the click of a few buttons. 

See a new word you don't recognize? Look it up in FlashED and add it to a File consisting of a bunch of your flashcards.
Now this application does not allow you to study effectively with the flashcards it creates. Upon having a file of
flashcards, you can export them into a txt file that contains your terms in a way that you can import them into a flashcard
study program such as ANKI or Quizlet. The application generates txt files that are easily parseable by many flashcard
study programs to import them as actual electronic flashcards.

This was created using Tkinter and customTkinter. A big thank you to Tom Schimansky for creating such an awesome library
for modern UI. A big thank you to John Elder from Codemy for providing a TON of awesome tutorials on the FreeCodeCamp
YouTube Channel. Thank you to FreeCodeCamp for being a free library of pretty much everything related to code, thank you
for being the frontier force for providing people free education relating to software and computer engineering. A last but
not least, thank you to Calix Huang, my roommate for helping get through several issues I had programming and for guiding 
me during this learning process.


## Requirements

Opening this program requires the installation of Tkinter and customTkinter which hopefully, should have installed upon 
opening the program. If not, you can install Tkinter and customTkinter by writing the following in the Terminal:

pip3 install Tkinter
pip3 install customTkinter

or 

py -m pip install Tkinter
py -m pip install customtkinter


## How to Use

I have added two template dictionaries in the repository for you to try out, a Chinese to English dictionary and general
English Dictionary. These are txt file dictionaries that you can easily find online with a google search. 

In order to Import the Dictionary, press the Import button in the top left hand corner of the application. This will 
bring you to a Pop up Menu. Name the dictionary whatever you want and choose the Dictionary txt file.

This is where it gets tricky. You must open the txt file and look at how the text file separates each term. For example,
if you take a look at English.txt, you will notice that the term comes first, then the Part of Speech (POS), and then the 
definition. These will be your three fields. In the Import Window, name these three fields by writing the names in the 
text box. In the beginning there are only two fields available, simply press the + button to add a new field. Note that 
the zeroth field will always be the term field, as is the case with every dictionary ever. Thus, you can leave field 0 
empty.

Next is understanding how the program will separate these fields. Looking at the English Dictionary, you can separate the
term from the POS from the definition using " (" and ") ". Knowing this, the user must create a regex to account for this. 
Unfortunately, I do not know of any better way to do this as all txt file dictionaries are different and there is no one
true way of doing this for people who do not know regex. This is something that I wiil definitely try to fix soon. 

For the current scenario, the English.txt regex is " \(|\) " and the Chinese.txt regex is " \[|\] ". I highly recommend 
that for the English.txt file that the fields are: "Term", "POS", and "Definition", just those three. And for the 
Chinese.txt, I recommend that the fields are: "Term", "Pinyin", and "Definition"

Everything after Importing is very intuitive. Click a dictionary and search for a word that you can then add to a file by
pressing left click. These cards can be edited, with new fields being added to them. You can delete and rename files, and 
delete words from dictionaries or files. 

Lastly, you can export the files by selecting the file you want to export, selecting which fields you want to be mapped to 
either the front or back. And then, making a separation string to separate these two fields. This can be anything, from a 
TAB to a Hyphen to "akjlifijawliliaf". But this the string that will allow you to Import these cards into other programs 
such as ANKI or Quizlet.


## Future Plans

For future plans, I want to get rid of the god forsaken regex box in the import window and hopefully replace it with 
something much more intuitive. There are also a lot of bugs in the Import Window for people to discover that need to be
fixed. 

Currently, it is impossible to add a brand new card to a file. The only way to add a card to a file is by copying cards
from dictionaries.

Lastly, I am working on a method to change the color scheme of the application from light to dark, and green, blue, and
dark-blue. Unfortunately there is no button in the application but you want to change the color scheme because the color
scheme is hardcoded, you can open the code and change the color scheme yourself. I have made it very obvious on which 
strings you have to change. 


## Closing Statements

Again, I would like to thank all those who helped me during this path of creating this application. Again, this is my first
project and the work for this application was done over the course of 3 and a half weeks. So obviously it is super young in
the grand scheme of things. I hope that language learners find this application useful. I certainly will be using it to 
study Chinese. Thank you for reading and Enjoy :)








