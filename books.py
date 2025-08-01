import chromadb
import uuid



client = chromadb.Client()

collection = client.create_collection(
    name = "book_collection",
    metadata = {"description" : "A collection for storing book data"}
)

# List of book dictionaries with comprehensive details for advanced search
books = [
    {
        "id": "book_1",
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "genre": "Classic",
        "year": 1925,
        "rating": 4.1,
        "pages": 180,
        "description": "A tragic tale of wealth, love, and the American Dream in the Jazz Age",
        "themes": "wealth, corruption, American Dream, social class",
        "setting": "New York, 1920s"
    },
    {
        "id": "book_2",
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": "Classic",
        "year": 1960,
        "rating": 4.3,
        "pages": 376,
        "description": "A powerful story of racial injustice and moral growth in the American South",
        "themes": "racism, justice, moral courage, childhood innocence",
        "setting": "Alabama, 1930s"
    },
    {
        "id": "book_3",
        "title": "1984",
        "author": "George Orwell",
        "genre": "Dystopian",
        "year": 1949,
        "rating": 4.4,
        "pages": 328,
        "description": "A chilling vision of totalitarian control and surveillance society",
        "themes": "totalitarianism, surveillance, freedom, truth",
        "setting": "Oceania, dystopian future"
    },
    {
        "id": "book_4",
        "title": "Harry Potter and the Philosopher's Stone",
        "author": "J.K. Rowling",
        "genre": "Fantasy",
        "year": 1997,
        "rating": 4.5,
        "pages": 223,
        "description": "A young wizard discovers his magical heritage and begins his education at Hogwarts",
        "themes": "friendship, courage, good vs evil, coming of age",
        "setting": "England, magical world"
    },
    {
        "id": "book_5",
        "title": "The Lord of the Rings",
        "author": "J.R.R. Tolkien",
        "genre": "Fantasy",
        "year": 1954,
        "rating": 4.5,
        "pages": 1216,
        "description": "An epic fantasy quest to destroy a powerful ring and save Middle-earth",
        "themes": "heroism, friendship, good vs evil, power corruption",
        "setting": "Middle-earth, fantasy realm"
    },
    {
        "id": "book_6",
        "title": "The Hitchhiker's Guide to the Galaxy",
        "author": "Douglas Adams",
        "genre": "Science Fiction",
        "year": 1979,
        "rating": 4.2,
        "pages": 224,
        "description": "A humorous space adventure following Arthur Dent across the galaxy",
        "themes": "absurdity, technology, existence, humor",
        "setting": "Space, various planets"
    },
    {
        "id": "book_7",
        "title": "Dune",
        "author": "Frank Herbert",
        "genre": "Science Fiction",
        "year": 1965,
        "rating": 4.3,
        "pages": 688,
        "description": "A complex tale of politics, religion, and ecology on a desert planet",
        "themes": "power, ecology, religion, politics",
        "setting": "Arrakis, distant future"
    },
    {
        "id": "book_8",
        "title": "The Hunger Games",
        "author": "Suzanne Collins",
        "genre": "Dystopian",
        "year": 2008,
        "rating": 4.2,
        "pages": 374,
        "description": "A teenage girl fights for survival in a brutal televised competition",
        "themes": "survival, oppression, sacrifice, rebellion",
        "setting": "Panem, dystopian future"
    },
]

book_docs = []

# write the book doc
for book in books:
    document = f"{book['title']} by {book['author']}. {book['description']} "
    document += f"Themes: {book['themes']}. Setting: {book['setting']}. "
    document += f"Genre: {book['genre']} published in {book['year']}."
    book_docs.append(document)


# add to collecion

collection.add(
    documents = book_docs,
    ids = [book['id'] for book in books],
    metadatas = [{
        "title": book['title'],
        "author": book['author'],
        "genre": book['genre'],
        "year": book['year'],
        "rating": book['rating'],
        "pages": book['pages'],
        "description": book['description'],
        "themes": book['themes'],
        "setting": book['settings']

    } for book in books]
)

#similarity search
result = collection.query(
    query_texts = "magical fantasy adventure",
    n_results = 3
)
print(result['documents'])

#metadata filtering
result = collection.get(
    where = {
        "genre" : {"$in" : ["Fantasy", "Science Fiction"]}
    }
)
print(result['documents'])

result = collection.get(
    where = {
        "rating" : {"$gte" : 4.0}
    }
)
print(result['documents'])

##combined search
result = collection.query(
    query_texts = "Highly rated dystopian books",
    n_results = 3,
    where = {
        '$and' : [
            {"genre" : {"$eq" : "Dystopian"}},
            {"rating" : {"$gte" : 4.5}}
        ]
    }
)
print(result['documents'])


'''
UPDATE :
c.update(
  ids = ["id1"],
  metadatas = [{}],
  document = [str1, str2]
)

DELETE

deletes docs with id : id1, id2
c.delete(
ids = [id1, id2]
)
'''

