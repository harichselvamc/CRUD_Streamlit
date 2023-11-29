import streamlit as st
import sqlite3

# Function to create or connect to the SQLite database
def create_db():
    conn = sqlite3.connect('streamlit_database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS books 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, author TEXT, year INTEGER)''')
    conn.commit()
    conn.close()

# Create or connect to the database
create_db()

# Streamlit app
def main():
    st.title('Book Library')

    # Display all books in a table
    st.header('All Books')
    with st.expander('View Books'):
        conn = sqlite3.connect('streamlit_database.db')
        c = conn.cursor()
        c.execute('SELECT * FROM books')
        books = c.fetchall()
        conn.close()

        st.table(books)

    # Add a new book
    st.header('Add a New Book')
    title = st.text_input('Title')
    author = st.text_input('Author')
    year = st.number_input('Year', min_value=0, max_value=9999)

    if st.button('Add Book'):
        conn = sqlite3.connect('streamlit_database.db')
        c = conn.cursor()
        c.execute('INSERT INTO books (title, author, year) VALUES (?, ?, ?)', (title, author, year))
        conn.commit()
        conn.close()
        st.success('Book added successfully!')

    # Update or delete a book
    st.header('Update or Delete a Book')
    book_id = st.number_input('Enter Book ID:', min_value=1, max_value=9999, step=1)

    if st.button('Edit Book'):
        st.session_state.edit_book_id = book_id
        st.experimental_rerun()

    if hasattr(st.session_state, 'edit_book_id'):
        st.header('Edit Book')
        conn = sqlite3.connect('streamlit_database.db')
        c = conn.cursor()

        c.execute('SELECT * FROM books WHERE id=?', (st.session_state.edit_book_id,))
        book = c.fetchone()
        conn.close()

        new_title = st.text_input('New Title', value=book[1])
        new_author = st.text_input('New Author', value=book[2])
        new_year = st.number_input('New Year', value=book[3], min_value=0, max_value=9999)

        if st.button('Save Changes'):
            conn = sqlite3.connect('streamlit_database.db')
            c = conn.cursor()
            c.execute('UPDATE books SET title=?, author=?, year=? WHERE id=?',
                      (new_title, new_author, new_year, st.session_state.edit_book_id))
            conn.commit()
            conn.close()
            st.success('Book updated successfully!')
            del st.session_state.edit_book_id  # Remove edit_book_id after editing

    if st.button('Delete Book'):
        conn = sqlite3.connect('streamlit_database.db')
        c = conn.cursor()
        c.execute('DELETE FROM books WHERE id=?', (book_id,))
        conn.commit()
        conn.close()
        st.success('Book deleted successfully!')

if __name__ == '__main__':
    main()
