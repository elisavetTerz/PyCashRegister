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
- In this step, we introduced the `app.py` file, which serves as the main entry point for the application. 
- The `app.py` file initializes and configures the Flask web application, setting up routes for handling product scanning, checkout logic, and returning the total price.
- It also includes necessary configurations such as enabling CORS (Cross-Origin Resource Sharing) to allow communication between the frontend and backend, ensuring smooth interaction with the React app.

## Step 5: Created Frontend with React
- Create folder named fronted:
```sh
mkdir fronted
cd fronted
```
- Run the following command to create a new React app:
```sh
npx create-react-app
```
- Add `"proxy": "http://localhost:5000"` in package.json file.

## Step 6: Modify the App.js to Handle Cart Operations
- Add to Cart: Adds products to the cart and updates the total.
- Remove from Cart: Allows specific items to be removed from the cart.
- Clear Cart: Clears all items from the cart.
- Total Calculation: Dynamically calculates and updates the total price based on the cart contents.

## Step 7: Update the Backend Route for remove-from-cart
- remove() method on the Checkout class.

## Step 8: Updated app.py
- Connect Frontend to Backend:
The frontend communicates with the Flask backend via HTTP requests:
- GET /products: Retrieves the list of available products.
- POST /add-to-cart: Adds a product to the cart.
- POST /remove-from-cart: Removes a specific product from the cart. 
- POST /clear-cart: Clears all products in the cart.