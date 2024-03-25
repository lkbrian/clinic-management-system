# Clinic Management System

### Happy Hearts Pediatric Center

Welcome to the Happy Hearts Pediatric Center! This repository contains a Python project for managing the records and appointments of children and parents at the pediatric center.

#### Project Structure

The project structure is as follows:

```console
.
├── .gitignore
├── Pipfile
├── Pipfile.lock
├── README.md
└── project
    ├── happyhearts.db
    ├── interface.py
    ├── models
    │   ├── __init__.py
    │   ├── appointment.py
    │   ├── child.py
    │   └── parent.py
    ├── seed.py
    └── requirements.txt

```
- **.gitignore**: Specifies intentionally untracked files to ignore.
- **Pipfile**: Describes project dependencies for Pipenv.
- **Pipfile.lock**: Records the exact versions of dependencies.
- **README.md**: Provides information about the project.
- **project/**: Main project directory.
  - **happyhearts.db**: Database file for storing records.
  - **interface.py**: Python script containing the user interface.
  - **models/**: Directory containing Python modules for database models.
    - **\_\_init\_\_.py**: Initialization file for the models package.
    - **appointment.py**: Defines the Appointment model.
    - **child.py**: Defines the Child model.
    - **parent.py**: Defines the Parent model.
  - **seed.py**: Script for seeding initial data into the database.
- **requirements.txt**: Lists the Python packages required by the project.

#### Database Connection and Models Module

This module provides SQLAlchemy models for database interactions within the HappyHearts project. The models folder acts as a module containing the following classes:
Parent,Child  & Appointment .The use of class methods in each class provides reusable functionalities for database operations, enhancing modularity and ease of use across the application.To utilize these models, ensure you have SQLAlchemy installed. The provided code initializes a connection to an SQLite database and sets up a session for database operations. 

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()
engine = create_engine("sqlite:///project/happyhearts.db")
Session = sessionmaker(bind=engine)
session = Session()

from .child import Child
from .parent import Parent
from .appointment import Appointment
```

#### Usage

To run the project, follow these steps:

1. Ensure Python and Pipenv are installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the project directory.
4. Install dependencies using Pipenv:

   ```bash
   pipenv install
   ```

5. Activate the virtual environment:

   ```bash
   pipenv shell
   ```

6. Run the main interface script:

   ```bash
   python interface.py
   ```

7. Follow the prompts in the command-line interface to interact with the system.

#### Features

- **Registration**: Register parents, children, and appointments.
- **Updates**: Update parent information, child information, and appointment details.
- **Find Data**: Search for parents, children, and appointments by various criteria.
- **List Data**: View lists of parents, children, appointments, vaccinated, and unvaccinated.




Developed with ❤️ by lkbrian

