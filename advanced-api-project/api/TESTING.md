# Testing Strategy

We used Django REST Framework's `APITestCase` to test the Book API endpoints.

## What We Tested
- Listing all books
- Viewing book detail
- Creating, updating, deleting books
- Filtering by year
- Searching by title
- Ordering by fields
- Permissions for authenticated routes

## How to Run
```bash
python manage.py test api
