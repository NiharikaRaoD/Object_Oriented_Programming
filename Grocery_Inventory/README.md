# Grocery Store Inventory Management System 🛒

A beginner-friendly Python project demonstrating **Object-Oriented Programming (OOP)** concepts such as classes, objects, attributes, methods, and relationships.  
This mini-application models a grocery store where you can manage products, inventory, customers, and orders.

---

## 📚 Project Overview

This project is designed to help beginners understand OOP principles in Python using a simple real-world example.

**Key Concepts:**
- Class and Object creation
- Use of `__init__` constructor and `self`
- Encapsulation and modular design
- Composition and association between objects

---

## 🧩 Class Design

| Class | Responsibility |
|--------|----------------|
| `Product` | Represents an item sold in the store (name, price, quantity, etc.) |
| `Inventory` | Manages all products, allows adding, removing, and searching |
| `Customer` | Represents a shopper with their own cart |
| `Order` | Represents a transaction made by a customer |
| `Store` | The main controller class that connects all other components |

---

## 🏗️ Folder Structure

```bash
grocery_store/
├── main.py              # Entry point for running the program
├── product.py           # Product class definition
├── inventory.py         # Inventory management class
├── customer.py          # Customer and cart handling
├── order.py             # Order management
├── store.py             # Store class integrating all modules
└── README.md            # Project documentation
