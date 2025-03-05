import './App.css';
import { useEffect, useState } from "react";

function App() {
  const [products, setProducts] = useState([]);
  const [cart, setCart] = useState([]);
  const [total, setTotal] = useState(0); // Initialize total to 0

  useEffect(() => {
    fetch("http://localhost:5000/products")
      .then(response => response.json())
      .then(data => setProducts(data))
      .catch(error => console.error("Error fetching products:", error));
  }, []);

  const addToCart = (productCode) => {
    fetch("http://localhost:5000/add-to-cart", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ productCode }),
    })
      .then(response => response.json())
      .then(data => {
        if (data.error) {
          alert(data.error);
        } else {
          setCart(data.cart); // Update cart state with the new cart from backend
          setTotal(data.total); // Update the total based on the backend's calculation
        }
      })
      .catch(error => console.error("Error adding to cart:", error));
  };

  const removeFromCart = (productCode) => {
    console.log(`Removing product with code: ${productCode}`);
    fetch("http://localhost:5000/remove-from-cart", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ productCode }),
    })
      .then(response => response.json())
      .then(data => {
        if (data.error) {
          alert(data.error);
        } else {
          console.log('Updated cart:', data.cart);  // Debug log for updated cart
          setCart(data.cart); // Update cart state with the new cart after removal
          setTotal(data.total); // Update the total based on the backend's calculation
        }
      })
      .catch(error => console.error("Error removing from cart:", error));
  };

  const clearCart = () => {
    fetch("http://localhost:5000/clear-cart", { method: "POST" })
      .then(response => response.json())
      .then(data => {
        setCart(data.cart); // Clear cart items
        setTotal(data.total); // Reset total based on backend calculation
      })
      .catch(error => console.error("Error clearing cart:", error));
  };

  return (
    <div>
      <h1>Checkout System</h1>
      <h2>Products</h2>
      <ul>
        {products.map((product) => (
          <li key={product.code}>
            {product.name} - ${product.price.toFixed(2)}
            <button onClick={() => addToCart(product.code)}>Add to Cart</button>
          </li>
        ))}
      </ul>

      <h2>Cart</h2>
      <ul>
        {cart.map((item, index) => (
          <li key={index}>
            {/* Ensure each item has valid properties */}
            {item && item.name && item.price !== undefined ? (
              `${item.name} - $${item.price.toFixed(2)}`
            ) : (
              <span>Invalid item</span>
            )}
            <button onClick={() => removeFromCart(item.code)}>Remove</button>
          </li>
        ))}
      </ul>

      <button onClick={clearCart}>Clear Cart</button>

      <h2>Total: ${total !== undefined ? total.toFixed(2) : "0.00"}</h2>
    </div>
  );
}

export default App;