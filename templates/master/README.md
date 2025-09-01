Project - Islington Marketplace
Project Description
This is an e-commerce platform built with Django for students at Islington College. The main goal is to create a functional marketplace where students can easily post their own products for sale and other students can browse and purchase them.

Key Features
User Accounts: Students can register for an account, log in, and post their own products for sale.

Product Browsing: The site allows buyers to browse, view, and filter products to find what they need.

Detailed Product Pages: Each product has its own page with images, a description, and the price.

Shopping Cart: A basic cart system lets users add and remove products before they proceed to a checkout summary.

Simple Admin Panel: An easy-to-use admin panel is in place to manage user accounts and all the product listings.

Clean and Responsive Design: The website has a clean and modern user interface built with Bootstrap, so it looks good on any device.

How to Get It Running
If you want to run this project yourself, here's a step-by-step guide.

1. What You'll Need
Make sure you have Python (version 3.8 or newer) and pip installed on your computer.

2. Get the Project Files
First, download and unzip the project files to a folder on your computer.

3. Set Up Your Environment
Using a virtual environment is a smart way to keep all your project files and dependencies organized.

# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS or Linux
python3 -m venv venv
source venv/bin/activate


4. Install the Right Packages
Next, you need to install the libraries this project relies on. You can find them in the requirements.txt file.

a. If you don't have requirements.txt yet, create it:

pip freeze > requirements.txt


b. Then, install everything:

pip install -r requirements.txt


5. Prepare the Database
Run these commands to get your database ready.

python manage.py makemigrations
python manage.py migrate


6. Log into the Admin
To get a user account for the admin panel, run this command and follow the instructions.

python manage.py createsuperuser


7. Run the Server
Start the development server with this command.

python manage.py runserver


8. Go Shopping!
Open your web browser and head to http://127.0.0.1:8000/ to see the website.

You can visit the admin panel at http://127.0.0.1:8000/admin/ and log in with the user details you created.