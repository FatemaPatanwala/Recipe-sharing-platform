# Recipe-sharing-platform

The Recipe Sharing Platform is a web application where users can share their recipes and review recipes from others. The application includes features for user authentication, recipe creation, editing, and deletion, as well as a review and rating system.

## **Features**

- User registration and authentication
- Add and edit recipes
- Upload images for recipes
- Review and rate recipes
- View all recipes and reviews


## **Screenshots**
1. **Home page**
![Screenshot 2024-08-10 154805](https://github.com/user-attachments/assets/d19e605a-b55b-4f86-b5fe-0833131ba120)

2. **Registration page**
![Screenshot 2024-08-10 154846](https://github.com/user-attachments/assets/b28374c0-981d-4400-bb06-55c1a6cfc420)

3. **Recipe page**
![Screenshot 2024-08-10 154917](https://github.com/user-attachments/assets/3b98bcdb-e3a9-4254-8cb6-9f1d4090d622)


## **Installation**

1. **Clone the repository**

```bash
  git clone https://github.com/FatemaPatanwala/Recipe-sharing-platform.git
  cd Recipe-sharing-platform
```
2. **Create a virtual environment**

```bash
 python -m venv .venv
```
3. **Activate the virtual environment**
```bash
 source .venv/Scripts/activate
```
4. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
5. **Set up the database**:
    ```bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```
6. **Run the application**:
    ```bash
    flask run
    ```
