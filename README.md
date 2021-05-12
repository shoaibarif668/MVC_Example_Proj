# pythonMVC

**Simplified MVC implementation in python.**

The three components of the MVC pattern are decoupled and they are responsible for different things:

the Model manages the data and defines rules and behaviors. It represents the business logic of the application. The data can be stored in the Model itself or in a database (only the Model has access to the database).

the View presents the data to the user. A View can be any kind of output representation: a HTML page, a chart, a table, or even a simple text output. A View should never call its own methods; only a Controller should do it.

the Controller accepts user’s inputs and delegates data representation to a View and data handling to a Model.
