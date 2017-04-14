# DIS-P16
DIS project - Team P16

Team members: 
Ritish Reddy Bandi 
Sai Suneel Reddy Challa
Developed as part of the profession-based learning cirriculum at:
44-564 Design of Data Intensive Systems, Northwest Missouri State University, Maryville, MO.
Contributors
Client
Denise Case, PhD, PE, Assistant Professor, Assistant Coordinator, Masters of Applied Computer Science Program, School of Computer Science and Information Systems, Colden Hall 2280, Northwest Missouri State University, 800 University Drive, Maryville, MO 64468, dcase@nwmissouri.edu 
https://www.linkedin.com/in/denisecase
Faculty
Dr.Denise Case
Assistants
Sai Sri Ravali Chinthareddy, Course Assistant
Developers, Designers, and Software Engineers
Ritish Reddy Bandi 
Sai Suneel Reddy Challa
Prerequisites
Following must be installed to run this application:
Python
Notepad++ (recommended)
Get started
Clone this repo to your local machine. 
If Windows, 
Right-click on C:\44564.
git clone https://github.com/RitishBandi30/DIS-P16.git
Overview
Short introduction to our project:
Our project is mapreduce program that finds the maximum number of gold medals and total number of medals won by each country at the Olympics.
Process
Initially, our input file is filtered and copied into a text file and is feed to the mapper program to retrieve required fields of dataset. Output of mapper program is sorted & shuffled before passing it to the reducer program. In reducer program, we apply maximum aggregate function to generate maximum gold medals and total number of medals(gold, silver and bronze) won by each country at Olympics.
Initialize (do these just once when setting up the project)
Clone a copy of repository to your c:\44564 folder.
Open a command window as Administrator in this project folder (e.g. C:\44564\P16).
Follow the below commands:
>python Mapper.py
The output of the mapper function gives us a mapper_output_sorted.txt file.
This mapper_output_sorted.txt file is fed to reducer function to give us reducer_output.txt file.
below is the command to execute reducer function
>python Reducer.py
