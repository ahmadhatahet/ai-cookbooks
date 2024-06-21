# Utilizing the power of Agent to answer questions in Relational Database

Relational Databases are a huge topics when it comes to fetching information, finding the correct tables, identifying the key columns, and writing the query.<br />
This process has become more repetitive and time consuming for any Data Scientist.
<br /><br />
The following files demonstrate the ability to connect to a RDB (Relational Database) and answer a question using the reasoning and action method in an LLM model, more about it [here](https://arxiv.org/pdf/2210.03629).<br /><br />
The model try to think and form a query that answers his question.<br />
The output of the query is additional context the LLM, which utilize further to generate another thought of arrive to final solution where it stops.

<img width=600 src="https://storage.googleapis.com/gweb-research2023-media/original_images/cca912e7fbe652676302383247087e22-Screen20Shot202022-11-0820at208.53.4920AM.png">

<br /><br />
# Files
1. [MariaDB-Agent.ipynb](https://github.com/ahmadhatahet/llm-practical-applications/blob/master/ChatWithDatabase/MariaDB-Agent.ipynb),
this file utilizes [Maria DB](https://www.mariadbtutorial.com/) and the sample dataset "[nation](https://www.mariadbtutorial.com/getting-started/mariadb-sample-database/)" to answer question and outline the internal reasoning steps the LLM tokes to find the answer.

2. [SQL-Agent.ipynb](https://github.com/ahmadhatahet/llm-practical-applications/blob/master/ChatWithDatabase/SQL-Agent.ipynb), using the free version of [SQL Server](https://www.microsoft.com/en-us/sql-server/sql-server-downloads) and the sample database "[AdventureWorksDW2016](https://github.com/Microsoft/sql-server-samples/releases/download/adventureworks/AdventureWorksDW2016.bak)" to answer user query.
