from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy data for initial recipes
recipes = [
    {"id": 1, "name": "Pasta Carbonara", "ingredients": ["Spaghetti", "Eggs", "Bacon", "Parmesan Cheese"], "instructions": "Cook spaghetti. Fry bacon. Mix eggs and cheese. Combine all."},
    {"id": 2, "name": "Chicken Stir Fry", "ingredients": ["Chicken Breast", "Bell Peppers", "Broccoli", "Soy Sauce"], "instructions": "Cut chicken and veggies. Stir-fry in pan with soy sauce."},
    {"id": 3, "name": "Chocolate Cake", "ingredients": ["Flour", "Sugar", "Cocoa Powder", "Eggs", "Butter"], "instructions": "Mix dry ingredients. Add eggs and melted butter. Bake in oven."}
]

# Route to display all recipes
@app.route('/')
def index():
    return render_template('index.html', recipes=recipes)


# Route to add a new recipe
@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        name = request.form['name']
        ingredients = request.form['ingredients'].split(',')
        instructions = request.form['instructions']
        new_recipe = {"id": len(recipes) + 1, "name": name, "ingredients": ingredients, "instructions": instructions}
        recipes.append(new_recipe)
        return redirect(url_for('index'))
    return render_template('add_recipe.html')

# Route to view a single recipe
@app.route('/recipe/<int:id>')
def view_recipe(id):
    recipe = next((r for r in recipes if r["id"] == id), None)
    if recipe:
        return render_template('recipe.html', recipe=recipe)
    return 'Recipe not found', 404

# Route to delete a recipe
@app.route('/delete_recipe/<int:id>')
def delete_recipe(id):
    global recipes
    recipes = [r for r in recipes if r["id"] != id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)