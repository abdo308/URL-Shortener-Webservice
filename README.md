# URL Shortener Webservice

## 📌 Team Members
- **Abdalrhman Magdy** 
- **Mohamed Ezzat** 
- **Safiya Mahmoud** 
- **Mahmoud Hanafy**
- **Ahmed Tarek**

---

## 🚀 Project Overview
The **URL Shortener Webservice** is a lightweight web application designed to convert long, complex URLs into short and easy-to-share links. It provides users with a simple interface to generate shortened URLs, track usage, and manage their links.  

### ✨ Key Features:
- Shorten long URLs into compact links  
- Redirect to the original URL when the short link is accessed  
- Track the number of times each short link is used  
- REST API support for programmatic URL shortening  
- Optional user accounts for managing personal collections of links  

---

## 📖 Explanation
Long URLs are often difficult to share, remember, or include in text messages, emails, and social media posts. A **URL Shortener** solves this problem by generating a unique identifier (short code) that maps to the original URL.  

When a user enters a long URL:
1. The system generates a short, unique key (e.g., `abc123`).  
2. The key is stored in the database with its corresponding long URL.  
3. A shortened link is created (e.g., `https://short.ly/abc123`).  
4. When users visit the shortened link, the service looks up the key and redirects them to the original URL.  
