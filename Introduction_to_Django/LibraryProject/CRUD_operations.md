### Create Operation

Command:
```python
new_book = Book.objects.create(title='1984', author='George Orwell', publication_year=1949)

### Expected output
<Book: 1984 by George Orwell (1949)>

### Retrieve Operation

Command:
```python
book = Book.objects.get(title='1984')

### Expected output
<Book: 1984 by George Orwell (1949)>

### Update Operation

Command:
```python
book.title = 'Nineteen Eighty-Four'
book.save()

### Expected output
<Book: Nineteen Eighty-Four by George Orwell (1949)>

### Delete Operation

Command:
```python
book.delete()

### Expected output
(1, {'bookshelf.Book': 1})
