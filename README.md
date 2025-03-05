# 🚀 Project Steps

## Step 1: Set Up the Project in VS Code  

### 📌 Create a New Project Folder  
1. Open **Visual Studio Code**.  
2. Create a new folder named **PyCashRegister**.  
3. Open the terminal in VS Code (**Ctrl + `** or **View > Terminal**).  

### 📌 Initialize a Virtual Environment   
Run the following command to create a virtual environment:  
```sh
python3 -m venv venv
```
### 📌 Activate the virtual environment
Mac/Linux:
```sh
source venv/bin/activate 
# Windows: venv\Scripts\activate
```

### 📌 Create the Initial File Structure 
```sh
mkdir tests
touch checkout.py requirements.txt README.md tests/test_checkout.py
```
## Step 2: Created checkout.py
- Introduced the `checkout.py` file which contains the product logic for managing products in the system.
- This file defines the Product class for representing individual products and the Checkout class for handling cart operations and applying pricing rules.

## Step 3: Created test_checkout.py
- Introduced the `test_checkout.py` file which contains unit tests to validate the functionality of the `checkout.py` file.

## Step 4: Created app.py
In this step, we introduced the `app.py` file, which serves as the main entry point for the application. The `app.py` file initializes and configures the Flask web application, setting up routes for handling product scanning, checkout logic, and returning the total price. It also includes necessary configurations such as enabling CORS (Cross-Origin Resource Sharing) to allow communication between the frontend and backend, ensuring smooth interaction with the React app.
