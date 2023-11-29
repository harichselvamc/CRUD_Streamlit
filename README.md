# Streamlit CRUD App with SQLite - Book Library

This is a Streamlit web application for managing a book library with CRUD operations. The application allows you to view all books, add a new book, and update or delete existing books. The data is stored in an SQLite database (`streamlit_database.db`).

## Live Demo

You can access the live demo of this application [here](https://crudapp.streamlit.app/).
        https://crudapp.streamlit.app/



## Setup

1. Clone the repository:

  
        git clone https://github.com/harichselvamc/CRUD_Streamlit.git
    

2. Navigate to the project directory:

   
        cd CRUD_Streamlit
  

3. Install the required libraries:

    
        pip install -r requirements.txt
    

4. Run the Streamlit app:

   
        streamlit run app.py
    

5. Open your web browser and go to `http://localhost:8501` to access the Streamlit app.

## Functionality

### View All Books

- All books in the library are displayed in a table. Click the "View Books" expander to see the list of books.

### Add a New Book

- You can add a new book to the library by entering the title, author, and publication year. Click the "Add Book" button to add the book to the database.

### Update or Delete a Book

- Enter the Book ID to update or delete a specific book. Click the "Edit Book" button to edit the book's details, including title, author, and year. Click the "Save Changes" button to update the book.
  
- Alternatively, you can click the "Delete Book" button to remove the book from the library.

## Database

The data is stored in the SQLite database (`streamlit_database.db`). The database has a single table called `books` with the following columns:

- `id`: Integer (Primary Key, Auto-incremented)
- `title`: Text
- `author`: Text
- `year`: Integer


