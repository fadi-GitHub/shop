```markdown
# Store Application cart functionality

A Django-based shopping cart functionality

## Prerequisites
- Python 3+
- Django 5+
- SQLite (default database)

## Installation

1. **Clone the repository**:
   git clone https://github.com/fadi-GitHub/shop.git
   cd Store

2. **Create and activate a virtual environment**:
   python3 -m venv venv
   source venv/bin/Scripts/activate

3. **Apply migrations**:
   python3 manage.py makemigrations
   python3 manage.py migrate
   python3 manage.py load_products (To load Dummy data in Product table)

4. **Create a superuser for admin access**:
   python3 manage.py createsuperuser
   give user_name and password what ever you like

5. **Run the Server**:
   You are all setup up now run the server
   python3 manage.py runserver 

6. **Initial data**:
   - Access the admin panel at `http://localhost:8000/admin/` and log in using the crediantial set previously.
   - Add products manually in table if not added previously using python3 manage.py load_products


## Features
- View and edit product inventory via Django admin.
- Shopping cart with default quantities (Potatoes: 2kg, Carrots: 1kg, Onions: 1kg).
- Not fixed for these three products more can be added.
- Purchase History page to see the past purchases and total
- Real-time price updates when modifying quantities.
- Responsive design using Tailwind CSS.
- Stock validation on order submission with descriptive error messages.
- Order confirmation message on successful submission.


```
![image alt](https://github.com/fadi-GitHub/shop/blob/df184a8f516a4cb527e36025b80d171791f50abb/images/Screenshot%202025-06-30%20at%2012.32.00%E2%80%AFam.png)
![image alt](https://github.com/fadi-GitHub/shop/blob/87a61785139240eb35cb61bed838aa11f4ad2982/images/Screenshot%202025-06-30%20at%2012.32.40%E2%80%AFam.png)
![image alt](https://github.com/fadi-GitHub/shop/blob/8bfad8fb9ad56bbd5d1db0e83300d5ed157d786b/images/Screenshot%202025-06-30%20at%2012.33.06%E2%80%AFam.png)
[![image alt](https://github.com/fadi-GitHub/shop/blob/8b1623ed618c40607988a8a4bcd01993abf5f2b9/images/Screenshot%202025-06-30%20at%2012.33.32%E2%80%AFam.png)
