# Setting up groups and permissions in Django

# Permissions Setup
can_view - Allows users to view books.
can_create - Allows users to add books
can_edit - Allows users to edit books.
can_delete - Allows users to delete books.

# User groups
Admins - Full access to view, create, edit, and delete.
Editors - Can view, create, and edit books.
Viewers - Can only view books.

# How to Assign Users to Groups
1. Log in to Django Admin (`/admin`).
2. Navigate to **Groups**.
3. Select a group (**Admins, Editors, Viewers**).
4. Add users to the selected group.

## Testing Permissions
- Log in with a user from each group.
- Attempt to create, edit, or delete books.
- Verify access restrictions.