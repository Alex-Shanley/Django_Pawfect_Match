# 🐾 Pawfect

**Pawfect** When I first read the brief and saw that it had a database focus, I wanted to challenge myself to think differently. Rather than taking a typical approach, I decided to step outside my comfort zone and explore a more creative direction. I began ideating ways to bring all my skills together into one cohesive project, which led me to the concept of building an admin-style portal.

I chose to develop Pawfect Match, a playful and engaging platform centred around pet adoption. As an animal lover, I wanted to create something that not only showcased my technical abilities, such as integrating SQL templates, flash submission forms, and pet management features like "Add Pet" and "Edit Pet" pages, but also carried a meaningful purpose.

The idea of pets without homes is something that deeply resonates with me, so I intentionally designed the platform to be cheerful and uplifting. By creating a vibrant and user-friendly experience, I aimed to bring positivity and joy to a serious topic, making Pawfect Match both functional and emotionally engaging.

## 🚀 superuser - username / admin
## Password / Pawfectmatch

🔗 **Live Site**: [https://pawfect-match-b7p8.onrender.com/]

## 🚀 Key Features

- 📋 **Pet Listings** – Browse all available pets with detailed profiles.
- ➕ **Add & Edit Pets** – Admin-style routes for adding and managing pet entries.
- 📨 **Contact Form** – Users can submit questions or adoption inquiries with feedback via flash messages.
- ❓ **FAQ & Questions Sections** – Informative content on the adoption process and common pet-related queries.
- 🐶 **Random Dog Facts** – Integrated with a public API to show new dog facts on each visit.
- 📊 **Adoption Stats** – Data-driven insights on adoption trends.
- 🧭 **Multi-Page Layout** – Includes Home, Pets, About, Contact, FAQ, and more.
- ⚡ **Dynamic UX** – Flash messaging for user feedback and clean navigation across pages.


## 🖥️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, Django
- **Database**: PostgreSQL
- **Deployment**: Render
- **API Integration**: Dog facts from [Dog API](https://dogapi.dog/api/v2/facts?)



## 📁 Project Structure

pawfect/

│
├── static/
│ ├── css/
│ └── images/
| └── Js/
│
│
├── templates/
│   ├── about.html
│   ├── add.html
│   ├── base.html             
│   ├── contact.html
│   ├── dog-fact.html         
│   ├── edit.html             
│   ├── faq.html
│   ├── featured-pets.html
│   ├── form.html             
│   ├── hero.html             
│   ├── how_we_work.html      
│   ├── index.html            
│   ├── pets.html             
│   ├── questions.html        
│   └── stats.html    
│
├── app.py
├── requirements.txt
└── README.md

## ✨ Requirements

alembic==1.16.4
blinker==1.9.0
click==8.2.1
Flask==3.1.1
Flask-Migrate==4.1.0
Flask-SQLAlchemy==3.1.1
greenlet==3.2.3
gunicorn==23.0.0
itsdangerous==2.2.0
Jinja2==3.1.6
Mako==1.3.10
MarkupSafe==3.0.2
packaging==25.0
psycopg2-binary==2.9.10
python-dotenv==1.1.1
requests==2.31.0
SQLAlchemy==2.0.41
typing_extensions==4.14.1
Werkzeug==3.1.3

## Deploy Pawfect on Render.com

Push your Pawfect code to GitHub (with requirements.txt and Procfile).

- ## Create a PostgreSQL database on Render and get the connection URL.

- ## Create a new Web Service on Render:

- ## Connect your GitHub repo.

- ## Set build command: pip install -r requirements.txt

- ## Set start command: gunicorn app:app

- ## Add environment variables:

- ## DATABASE_URL = your Render PostgreSQL URL

- ## SECRET_KEY = your Flask secret key

- ## Deploy and wait for Render to build the app.

Access Pawfect
Once deployed, open the Render URL provided, e.g.,

🔗 **Live Site**: [https://pawfect-match-b7p8.onrender.com/]