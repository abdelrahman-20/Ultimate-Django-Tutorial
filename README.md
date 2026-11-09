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

- **Make-Migrations**
  - Generating migrations files
- **Applying Migrations**
  - Reflecting databases models and changes to the actual database
- **Customizing DB Schema**
  - Using `Meta` Class, We can customize the Data-Model
- **Use Your Own Database System**
  - Edit the `DATABASES` object configurations in the Project's Settings

---

### Django `ORM` `02:12:17`

- **What does it do**
  - Maps objects to relational records
- **Why `ORM`**
  - Maps Python code to `SQL` code
  - Don't have to write repetitive `SQL` code
  - reduce complexity
  - make the code more understandable
  - faster and much efficient
- **Managers & Query-Sets**
  - Each Model has an object attribute
  - Acts as interface to the database
  - It returns a Query-Set (Doesn't Execute Immediately)
- **Retrieving Objects**
- **Querying Generic Relationships** `03:22:12`
- **Custom Managers** `03:28:32`
- **Creating Objects** `03:33:05`
- **Transactions** `03:42:41`

---

### Django Admin Interface `03:50:33`

- **Overriding The Base Query-Set** `04:09:11`
- **Provide Links to Other Pages** `04:12:02`
- **Adding Search to The List Page** `04:17:19`
- **Customizing Forms** `04:26:56`
- **Adding Data Validation** `04:32:40`
- **Editing Children Using In-lines** `04:36:28`
- **Using Generic Relations** `04:38:59`
- **Extending Plug-able Apps** `04:42:57`

---

## Part-2

### Building REST API `00:06:40`

- **REST Architecture**
  - Resources
    - `product, post, ...`
  - Representation
    - `XML, JSON`
  - HTTP method
    - `GET, POST, UPDATE, PATCH, DELETE`
- **Django `DRF`**
- **Creating `Serializers`** `00:24:02`
  - Convert model instance to python dictionary
- **Creating Custom `Serializer` Fields** `00:34:23`
- **`Serializing` Relationships** `00:38:54`
  - Primary-Key
    - Get a primary-key related field `PrimaryKeyRelatedField(QuerySet)`
  - String Representation
    - Get a string related field `StringRelatedField(QuerySet)` => Handle `N+1`
  - Nested Object
    - Use the `Model-Serializer` for the object
  - Hyperlink
    - `serializers.HyperLinkRelatedField(QuerySet, View_Name)`
    - The `View_Name` to get the related resource URL of the object
- **`Model-Serializers`** `00:47:44`
- **`Deserializing` Objects** `00:52:33`
- **Data Validation** `00:55:10`
- **Saving Objects** `01:00:47`
- **Deleting Objects** `01:08:45`
  - Handle foreign key relation constraints before deletion
- **Exercise: Building Collections API** `01:13:13`
  - Note: To add a new field in the query-set (using annotate), Add this field in the `Model-Serializer` with its type

---

### Advanced API Concepts `01:17:44`

- **Class-Based Views** `01:18:20`
  - Add reusable opportunities
- **`Mixins`** `01:22:33`
  - A class to encapsulate a pattern of code
- **Generic Views** `01:26:51`
- **Customizing Generic Views** `01:33:57`
- **View-Sets** `01:38:30`
  - Combine the logic for multiple related views in a single class
- **Routers** `01:43:30`
- **The Reviews API** `01:52:30`
  - To Build The API
    1. Create a `Model` + Migrations
    2. Create a `Serializer`
    3. create a `view`
    4. create a `route` (URL pattern, or router)
- **Nested Routers** `01:56:38`
  - Using Library: `drf-nested-routers`
- **Filtering** `02:06:32`
- **Generic Filtering** `02:11:20`
- **Searching** `02:17:44`
- **Sorting** `02:20:00`
- **Pagination** `02:21:45`

---

### Building Shopping-Cart API `02:27:05`

- **Designing The API** `02:27:27`
  - Carts
    - Create `POST /carts`
    - Get cart `GET /carts/pk`
    - Delete cart `DEL /carts/pk`
  - Cart-Items
    - Add items `POST /carts/pk/items` `{product_id, quantity}`
    - Update quantity `PATCH /carts/cart_pk/items/pk`
    - Remove items `DEL /carts/cart_pk/items/pk`
- **Revisiting Data Model** `02:30:38`
  - Create a `uuid` as cart-id
  - Add a unique-together constraints for Cart-Item model
- **Creating A Cart** `02:38:10`
  - Building `Serializer`, `View`, `Route`
- **Deleting A Cart** `02:53:42`
- **Getting Cart Items** `02:55:35` <<
- **Adding A Cart Item** `03:00:26`
- **Updating A Cart Item** `03:12:38`
- **Deleting A Cart Item** `03:14:50`

---

### Django Authentication System `03:15:50`

- **Django Authentication System** `03:16:30`
- **Extending The User Model** `03:21:50`
- **Creating User Profile** `03:32:25`
- **Groups And Permissions** `03:39:25`
- **Creating Custom Permissions** `03:42:20`

---

### Securing API `03:44:33`

- **Token Based Authentication** `03:45:10`
- **Adding Authentication Endpoints** `03:46:40`
- **Registering Users** `03:53:00`
- **Building The Profile API** `04:02:20`
- **Logging-In** `04:07:25`
- **Inspecting `JWT`** `04:12:22`
- **Refreshing Tokens** `04:15:52`
- **Getting Current User** `04:17:10`
- **Getting Current User's Profile** `04:21:55`
- **Applying Permissions** `04:28:55`
- **---** `04:00:00`
- **---** `04:00:00`
- **---** `04:00:00`

---

### Timing: `03:15:50`

---
