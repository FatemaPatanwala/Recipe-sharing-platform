from flask import render_template, flash, redirect, url_for, request
from Recipe_book import app, db
from werkzeug.utils import secure_filename
from Recipe_book.forms import RecipeForm, ReviewForm ,RegistrationForm,LoginForm
from Recipe_book.models import User,Recipe, Review
from flask_login import current_user, login_user, logout_user, login_required
from urllib.parse import urlparse
import os


@app.route('/')
@app.route('/index')
def index():
    recipes = Recipe.query.all()
    return render_template('index.html', title='Home', recipes=recipes)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlparse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/recipe/new', methods=['GET', 'POST'])
@login_required
def new_recipe():
    form = RecipeForm()
    if form.validate_on_submit():
        filename = None
        if form.picture.data:
            filename = secure_filename(form.picture.data.filename)
            form.picture.data.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        recipe = Recipe(
            name=form.name.data, ingredients=form.ingredients.data, steps=form.steps.data, picture=filename, user_id=current_user.id)
        db.session.add(recipe)
        db.session.commit()
        flash('Your recipe is now live!')
        return redirect(url_for('index'))
    return render_template('create_recipe.html', title='New Recipe', form=form)

@app.route('/recipe/<int:id>', methods=['GET', 'POST'])
def recipe(id):
    recipe = Recipe.query.get_or_404(id)
    form = ReviewForm()
    if form.validate_on_submit():
        review = Review(body=form.body.data, rating=form.rating.data, recipe_id=recipe.id)
        db.session.add(review)
        db.session.commit()
        flash('Your review has been added.')
        return redirect(url_for('recipe', id=recipe.id))
    reviews = Review.query.filter_by(recipe_id=recipe.id).all()
    return render_template('recipe.html', recipe=recipe, form=form,  reviews=reviews)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_recipe(id):
    recipe = Recipe.query.get_or_404(id)
    if recipe.author != current_user:
        flash('You are not authorized to update this recipe.')
        return redirect(url_for('index'))

    form = RecipeForm()
    if form.validate_on_submit():
        if form.picture.data:
            filename = secure_filename(form.picture.data.filename)
            form.picture.data.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            recipe.picture = filename
        recipe.name = form.name.data
        recipe.ingredients = form.ingredients.data
        recipe.steps = form.steps.data
        
        db.session.commit()
        flash('Recipe updated successfully!')
        return redirect(url_for('recipe', id=recipe.id))
    elif request.method == 'GET':
        form.name.data = recipe.name
        form.ingredients.data = recipe.ingredients
        form.steps.data = recipe.steps
        form.picture.data = recipe.picture

    return render_template('update_recipe.html', form=form, recipe=recipe)



@app.route('/reviews/<int:recipe_id>', methods=['GET', 'POST'])
def reviews(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    reviews = Review.query.filter_by(recipe_id=recipe.id).all()
    form = ReviewForm()
    if form.validate_on_submit():
        new_review = Review(body=form.body.data, rating=form.rating.data, recipe_id=recipe.id)
        db.session.add(new_review)
        db.session.commit()
        flash('Your review has been added.')
        return redirect(url_for('reviews', recipe_id=recipe.id))
    return render_template('review.html', recipe=recipe, reviews=reviews, form=form)



import os

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])
