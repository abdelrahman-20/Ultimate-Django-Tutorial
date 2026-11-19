# Ultimate Django Course

## Part-1

### Initial-Steps

- Install `pipenv` + Create a project directory
- Start new project using `django-admin startproject pro_name .`
- Run the new project `python manage.py startserver`

---

### Django App Structure

### URL Module

- It's for routes "resources"

### Views Module

- It's a request handler `Req -- Res`

### Model Module

- For database models

---

### Create Database Models `01:01:20`

- Relationships
  - 1-to-1
  - 1-to-many
  - many-to-many
- Generic-Relationships `01:26:40`
  1. Content-Type
  2. Object-ID
  3. Content-Object

---

### Setting-Up Database `01:33:36`

- Make-Migrations
  - Generating migrations files
- Applying Migrations
  - Reflecting databases models and changes to the actual database
- Customizing DB Schema
  - Using `Meta` Class, We can customize the Data-Model
- Use Your Own Database System
  - Edit the `DATABASES` object configurations in the Project's Settings

---

### Django `ORM` `02:12:17`

- What does it do
  - Maps objects to relational records
- Why `ORM`
  - Maps Python code to `SQL` code
  - Don't have to write repetitive `SQL` code
  - reduce complexity
  - make the code more understandable
  - faster and much efficient
- Managers & Query-Sets
  - Each Model has an object attribute
  - Acts as interface to the database
  - It returns a Query-Set (Doesn't Execute Immediately)
- Retrieving Objects
- Querying Generic Relationships `03:22:12`
- Custom Managers `03:28:32`
- Creating Objects `03:33:05`
- Transactions `03:42:41`

---

### Django Admin Interface `03:50:33`

- Overriding The Base Query-Set `04:09:11`
- Provide Links to Other Pages `04:12:02`
- Adding Search to The List Page `04:17:19`
- Customizing Forms `04:26:56`
- Adding Data Validation `04:32:40`
- Editing Children Using In-lines `04:36:28`
- Using Generic Relations `04:38:59`
- Extending Plug-able Apps `04:42:57`

---

## Part-2

### Building REST API `00:06:40`

- REST Architecture
  - Resources
    - `product, post, ...`
  - Representation
    - `XML, JSON`
  - HTTP method
    - `GET, POST, UPDATE, PATCH, DELETE`
- Django `DRF`
- Creating `Serializers` `00:24:02`
  - Convert model instance to python dictionary
- Creating Custom `Serializer` Fields `00:34:23`
- `Serializing` Relationships `00:38:54`
  - Primary-Key
    - Get a primary-key related field `PrimaryKeyRelatedField(QuerySet)`
  - String Representation
    - Get a string related field `StringRelatedField(QuerySet)` => Handle `N+1`
  - Nested Object
    - Use the `Model-Serializer` for the object
  - Hyperlink
    - `serializers.HyperLinkRelatedField(QuerySet, View_Name)`
    - The `View_Name` to get the related resource URL of the object
- `Model-Serializers` `00:47:44`
- `Deserializing` Objects `00:52:33`
- Data Validation `00:55:10`
- Saving Objects `01:00:47`
- Deleting Objects `01:08:45`
  - Handle foreign key relation constraints before deletion
- Exercise: Building Collections API `01:13:13`
  - Note: To add a new field in the query-set (using annotate), Add this field in the `Model-Serializer` with its type

---

### Advanced API Concepts `01:17:44`

- Class-Based Views `01:18:20`
  - Add reusable opportunities
- `Mixins` `01:22:33`
  - A class to encapsulate a pattern of code
- Generic Views `01:26:51`
- Customizing Generic Views `01:33:57`
- View-Sets `01:38:30`
  - Combine the logic for multiple related views in a single class
- Routers `01:43:30`
- The Reviews API `01:52:30`
  - To Build The API
    1. Create a `Model` + Migrations
    2. Create a `Serializer`
    3. create a `view`
    4. create a `route` (URL pattern, or router)
- Nested Routers `01:56:38`
  - Using Library: `drf-nested-routers`
- Filtering `02:06:32`
- Generic Filtering `02:11:20`
- Searching `02:17:44`
- Sorting `02:20:00`
- Pagination `02:21:45`

---

### Building Shopping-Cart API `02:27:05`

- Designing The API `02:27:27`
  - Carts
    - Create `POST /carts`
    - Get cart `GET /carts/pk`
    - Delete cart `DEL /carts/pk`
  - Cart-Items
    - Add items `POST /carts/pk/items` `{product_id, quantity}`
    - Update quantity `PATCH /carts/cart_pk/items/pk`
    - Remove items `DEL /carts/cart_pk/items/pk`
- Revisiting Data Model `02:30:38`
  - Create a `uuid` as cart-id
  - Add a unique-together constraints for Cart-Item model
- Creating A Cart `02:38:10`
  - Building `Serializer`, `View`, `Route`
- Deleting A Cart `02:53:42`
- Getting Cart Items `02:55:35` <<
- Adding A Cart Item `03:00:26`
- Updating A Cart Item `03:12:38`
- Deleting A Cart Item `03:14:50`

---

### Django Authentication System `03:15:50`

- Django Authentication System `03:16:30`
- Extending The User Model `03:21:50`
- Creating User Profile `03:32:25`
- Groups And Permissions `03:39:25`
- Creating Custom Permissions `03:42:20`

---

### Securing API `03:45:10`

- Token Based Authentication `03:45:10`
- Adding Authentication Endpoints `03:47:15`
  - `djoser` Library => REST Implementation for Django Auth System
  - Auth System => Token-Based Auth , or , JSON Web Token Auth
- Registering Users `03:53:35`
  - Create a custom DJOSER serializer
  - Modify DJOSER Object in settings Module
- Building The Profile API `04:02:55`
  - Get the main user data (username, first_name, last_name, email) from main User model
  - Create a customer profile for Customers (Serializer, ViewSet, Route)
- Logging-In `04:08:00`
  - Create a JWT via `auth/jwt/create`
- Inspecting `JWT` `04:12:57`
  - Each JWT contains a signature generated using a secret stored on the server
- Refreshing Tokens `04:16:25`
- Getting Current User `04:17:10`
  - Send a GET request for `/users/me` with Authorization header "Bearer <..TOKEN..>"
- Getting Current User's Profile `04:22:30`
- Applying Permissions `04:28:55`
  - Add Default Permission Classes in Project's Settings --or
  - Add Permission Class For The ViewSet
- Applying Custom Permission `04:33:35`
- Applying Model Permissions `04:40:40`
- Applying Custom Model Permissions `04:45:20`

### Building The Orders API `04:49:55`

- --- `04:00:00`
- --- `04:00:00`

---

## Timing: `1:23:07`

---

## Original-TimeStamps

### 0:00 - Section 1 - Getting Started

---

### 6:58 - Section 2 - Building Restful APIs

7:36 - What are Restful APIs?
11:05 - Resource Representations
13:11 - HTTP Methods
15:15 - Installing Django REST Framework
16:13 - Creating API Views
24:21 - Creating Serializers
28:25 - Serializing Objects
34:39 - Creating Custom Serializer Fields
39:09 - Serializing Relationships
48:00 - Model Serializers
52:49 - Deserializing Objects
1:01:02 - Saving Objects
1:09:01 - Deleting Objects
1:13:27 - Exercise: Building the Collections API

---

### 1:18:19 - Section 3 - Advanced API Concepts

1:18:53 - Class-based Views
1:23:07 - Mixins
1:27:24 - Generic Views
1:34:30 - Customizing Generic Views <<
1:39:03 - ViewSets
1:44:03 - Routers
1:53:03 - Building the Reviews API
1:57:11 - Nested Routers
2:07:06 - Filtering
2:11:54 - Generic Filtering
2:18:17 - Searching
2:20:35 - Sorting
2:22:19 - Pagination

---

### 2:27:39 - Section 4 - Building a Shopping Cart

2:28:01 - Designing a Shopping Cart API
2:44:37 - Getting a Cart
2:54:16 - Deleting a Cart
2:56:07 - Getting Cart Items
3:00:59 - Adding a Cart Item
3:13:19 - Update a Cart Item
3:15:21 - Deleting a Cart Item

---

### 3:16:24 - Section 5 - Django Authentication System

3:17:03 - Django Authentication System
3:20:14 - Customizing the User Model
3:22:22 - Extending the User Model
3:32:57 - Creating User Profiles
3:39:57 - Groups and Permissions
3:42:54 - Creating Custom Permissions

---

### 3:45:06 - Section 6 - Securing APIs

3:45:44 - Token-based Authentication
3:47:14 - Adding the Authentication Endpoints
3:53:35 - Registering Users
4:02:55 - Building the Profile API
4:07:59 - Logging in
4:12:56 - Inspecting a JSON Web Token
4:16:27 - Refreshing Tokens
4:17:45 - Getting the Current User
4:22:30 - Getting Current User's Profile
4:29:30 - Applying Permissions
4:33:35 - Applying Custom Permissions
4:40:40 - Applying Model Permissions
4:45:20 - Applying Custom Model Permissions

---

### 4:49:54 - Section 7 - Building the Orders API

4:50:16 - Designing the Orders API
4:51:32 - Getting the Orders
4:57:16 - Applying Permissions
5:03:54 - Creating an Order
5:08:56 - Creating Order Items
5:15:45 - Returning the Created Order
5:19:37 - Data Validation
5:23:06 - Revisiting the Permissions
5:24:56 - Updating an Order
5:27:16 - Signals
5:35:24 - Creating Custom Signals
