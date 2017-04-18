# DIS-P16
DIS project - Team P16

Team members: 
Ritish Reddy Bandi, 
Sai Suneel Reddy Challa

Developed as part of the profession-based learning cirriculum at:
44-564 Design of Data Intensive Systems, Northwest Missouri State University, Maryville, MO.

Client:
Denise Case, PhD, PE, Assistant Professor, Assistant Coordinator, Masters of Applied Computer Science Program, School of Computer Science and Information Systems, Colden Hall 2280, Northwest Missouri State University, 800 University Drive, Maryville, MO 64468, dcase@nwmissouri.edu 
https://www.linkedin.com/in/denisecase

Faculty:
Dr.Denise Case

Assistants:
Sai Sri Ravali Chinthareddy, Course Assistant

Developers, Designers, and Software Engineers:
Ritish Reddy Bandi 
Sai Suneel Reddy Challa

Prerequisites:
Following must be installed to run this application:
Python
Notepad++ (recommended)

Get started:
Clone this repo to your local machine. 
In Windows, 
Right-click on C:\44564.
git clone https://github.com/RitishBandi30/DIS-P16.git

Overview:
Short introduction to our project:
Our project is mapreduce program that finds the maximum number of gold medals won by each country and in which sport did USA get highest number of gold medals at the  2016 Olympics.
Link to Data Source: https://www.kaggle.com/rio2016/olympic-games
 
Process:
Initially, our input file is filtered and copied into a text file and is feed to the mapper program to retrieve required fields of dataset. Output of mapper program is sorted & shuffled before passing it to the reducer program. In reducer program, we apply maximum aggregate function to generate maximum gold medals won by each country and in which sport did USA get highest number of gold medals at 2016 Olympics.

Initialize (do these just once when setting up the project):
Clone a copy of repository to your c:\44564 folder.
Open a command window as Administrator in this project folder (e.g. C:\44564\P16).

Follow the below commands:
>python Mapper.py

![mapper](https://cloud.githubusercontent.com/assets/22079666/25057731/046dc342-2138-11e7-8229-cb6fdb5f606f.PNG)

The output of the mapper function gives us a mapper_output_sorted.txt file.
This mapper_output_sorted.txt file is fed to reducer function to give us reducer_output.txt file.
below is the command to execute reducer function

>python Reducer.py

![reducer](https://cloud.githubusercontent.com/assets/22079666/25157718/9fc8b1ac-2468-11e7-8a95-6eef2833522e.PNG)

The output of the reducer is plotted as below.

![image](https://cloud.githubusercontent.com/assets/22079666/25060031/7cdb342a-2158-11e7-8760-1193c6c8848a.png)

Commands to find medals in different games for USA:
>python Mapper_USA.py
![mapper_usa](https://cloud.githubusercontent.com/assets/22079666/25060069/1668e366-215a-11e7-8b12-908812b40ece.PNG)
The output is mapper_sorted_USA.txt file which is then fed to reducer
>python Reducer_USA.py
![red_usa](https://cloud.githubusercontent.com/assets/22079666/25060070/166c367e-215a-11e7-8cf7-a29c4628668b.PNG)
The output is plotted in pie chart as below using excel sheet. We did it by selecting the complete data and inserting a pie chart.
![image](https://cloud.githubusercontent.com/assets/22079666/25060067/0d0c7508-215a-11e7-9b4e-a71c467d8bfc.png)

We have used git for sharing our code and is accessible as it is public. The work was shared to all and everyone did there part and pushed their work into the git repository.
