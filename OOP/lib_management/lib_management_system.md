## lib mangement system,

helps keep check of the books and the checkouts, member subscriptions and profiles
main db from entering new books and recordign borrowed books, the the due dates

## System requirementsL

> ask for the scope of the system the interviewer has in mind

1. members should be able to search books by their title, author, subject cate and publication date
2. books have their own id, and other details includng rack number which will help to physically locate the book
3. there could be more than one copy of a book, lib member should be able to checkout and reserve any copy
4. the system should be able to retrieve informatin like who took a particular book or what are the books checkout-out by specific memeber
5. there sould be a maximum limit-5 on how many books a member can checkout
6. there should be max 1- days on how many days a member can keep a book
7. a system can collect fines for books returned after the due date
8. member should reserve books that are not curretly available
9. the system should be able send notification whenever the reserved books become available, when the books are not returned on time as well.
10. book and member card will have a unique barcode. the system will be able to read barcode from books and members' lib card

## use cases:

three main actors in the system:

- libraian: add/ modify books, book items and users, also search, issue, reserve and return book items

- member: search the catalog, checkout, reserve, renew and return a book.

- system: sending notification for overdue books, cancel books

Use cases:

- add/remove/edit books
- search cate: search books by cate
- register new account/ cancel membership
- check-out book
- reserve a book
- renew a book
- return a book

## class diagram

- lib: central party
- Book: The basic building block of the system. Every book will have ISBN, Title, Subject, Publishers, etc.
- BookItem: Any book can have multiple copies, each copy will be considered a book item in our system. Each book item will have a unique barcode.
- Account: We will have two types of accounts in the system, one will be a general member, and the other will be a librarian.
- LibraryCard: Each library user will be issued a library card, which will be used to identify users while issuing or returning books.
- BookReservation: Responsible for managing reservations against book items.
- BookLending: Manage the checking-out of book items.
- Catalog: Catalogs contain list of books sorted on certain criteria. Our system will support searching through four catalogs: Title, Author, Subject, and Publish-date.
- Fine: This class will be responsible for calculating and collecting fines from library members.
- Author: This class will encapsulate a book author.
- Rack: Books will be placed on racks. Each rack will be identified by a rack number and will have a location identifier to describe the physical location of the rack in the library.
- Notification: This class will take care of sending notifications to library members.

