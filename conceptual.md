### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
PostgreSQL is a open-source, object-relational database management system (ORDBMS) with a strong reputation.
It provides a wide range of features including SQL support, transactions, data types, indexes, and more.
- What is the difference between SQL and PostgreSQL?
SQL is a language used to manage and manipulate relational databases, while PostgreSQL is a specific type of database management system that implements and uses SQL as its primary means of interacting with the data stored in its databases.
- In `psql`, how do you connect to a database?
First, postgres needs to be running. 
<!-- EXAMPLE using Ubuntu on Windows-->
<!-- Enter This in terminal and it checks status of postgresql-->sudo service postgresql status 
<!--Do this to start if needed-->sudo service postgresql start
<!--You need a database, create one if needed-->createdb [DBNAME]
<!--do this in order to connect to the database-->\c [DBNAME]
- What is the difference between `HAVING` and `WHERE`?
In SQL, HAVING and WHERE are both used to filter data from a query, but they are used in different contexts and for different purposes.

WHERE is used to filter data before it is grouped and aggregated. The WHERE clause is used to select rows from a table based on a specified condition. It filters the data based on the values in individual rows, and it can be used in both SELECT and UPDATE statements.
- What is the difference between an `INNER` and `OUTER` join?
An INNER join returns only the rows that have matching values in both tables. An INNER join returns only the rows for which there is a match in both tables. The result of an INNER join will only include rows where the join condition is true

An OUTER join returns all the rows from one table and the matching rows from the other table. If there is no match in one of the tables, the OUTER join will return NULL values for the columns of the non-matching table. There are three types of OUTER joins: LEFT, RIGHT, and FULL outer joins.
- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
A LEFT OUTER join returns all the rows from the left table and the matching rows from the right table, with NULL values for the non-matching columns of the right table, while a RIGHT OUTER join returns all the rows from the right table and the matching rows from the left table, with NULL values for the non-matching columns of the left table.
- What is an ORM? What do they do?
An Object-Relational Mapping (ORM) is a technique that allows developers to interact with a database using object-oriented programming languages, rather than writing raw SQL statements. It acts as an intermediary between the application code and the database, converting between the two representations of data. The application code works with objects, while the database stores relational data. The ORM takes care of the translation between the two, allowing the application code to remain focused on business logic, rather than on the details of working with the database.
- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
When you make an HTTP request using AJAX, the request is made from the user's browser to the server, while when you make an HTTP request from the server side using a library like requests, the request is made from the server to another server.
- What is CSRF? What is the purpose of the CSRF token?
CSRF stands for Cross-Site Request Forgery, and it is a type of attack in which an attacker tricks a user into making a request to a website, such as a form submission, that the user did not intend to make. The purpose of the CSRF token is to prevent CSRF attacks by making it difficult for an attacker to forge a request that appears to come from a user.
A CSRF token is a unique, random value that is generated by the server and included in a form or in a hidden field in a web page.
- What is the purpose of `form.hidden_tag()`?
form.hidden_tag() is used to generate a hidden input field in an HTML form. This hidden field is used to store a value that is included in the form submission, but is not visible to the user. 
It is often used to store a CSRF token.