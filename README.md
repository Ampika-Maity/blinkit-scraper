# 🛒 Blinkit Product Scraper

This project is a Python-based web scraper that extracts product data from the Fresh Vegetables category on [Blinkit](https://blinkit.com).

It scrolls through the entire product list, scrapes key pricing details, and saves them to a CSV file on your desktop.

---

## 📌 Features

- Auto-scrolls to load all products
- Extracts the following details:
  - ✅ Product Name
  - 💰 Selling Price
  - 💸 Original Price
  - 🏷️ Discount (calculated if available)
- Saves data in blinkit_products.csv (UTF-8 encoded)

---

## 🛠️ Tech Stack

- Python 3
- Selenium
- ChromeDriver

---

## 📁 Project Files

| File Name              | Description                                 |
|------------------------|---------------------------------------------|
| blinkit_scraper.py     | Main script to scrape product data          |
| blinkit_products.csv   | Output file containing scraped product info |
| README.md              | Project documentation (you’re reading it)   |

---

## 🚀 How to Run the Scraper

### 1. Install Required Libraries

`bash
pip install selenium

## 📷 Screenshots

### 🔹 GitHub Repo View

![Repository Screenshot](https://github.com/Ampika-Maity/blinkit-scraper/blob/main/SS%20of%20blinkit%20scraper.png)
