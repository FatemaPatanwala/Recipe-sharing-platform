# Recipe-sharing-platform

A web application built with Flask and SQLALCHEMY that allows users to share, review, and rate recipes. Features include user authentication, adding/editing recipes, uploading images, and viewing all recipes and reviews.


## **Features**

- User registration and authentication
- Add and edit recipes
- Upload images for recipes
- Review and rate recipes
- View all recipes and reviews


## **Screenshots**
1. **Main page**
![Screenshot 2024-08-10 154805](https://github.com/user-attachments/assets/9c4a4a50-7009-45bf-b43b-08a51ddcc917)

2. **Registration page**

![Screenshot 2024-08-10 154846](https://github.com/user-attachments/assets/ac751c52-4413-4acf-b2a4-7f7fb1783043)

3.**Recipe page**
![Screenshot 2024-08-10 154917](https://github.com/user-attachments/assets/8d98c845-0eb8-4870-af0c-2169d33ed374)


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
 .venv\Scripts\activate
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