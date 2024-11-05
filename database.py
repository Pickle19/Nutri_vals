import pandas as pd
import os

#columns = ["Name", "Ár", "Kalória", "Fehérje", "Szénhidrát", "Zsírok"]
#food_data = pd.DataFrame(columns=columns)

food_data = pd.read_csv('food.csv', index_col = 0)

def add_food(name: str, price: float, calories: int, protein : float, carbs : float, fats : float, type_of_food: str, item_weight: int):
    if not os.path.exists('food.csv'):
        df = pd.DataFrame(columns = ['Name','Price','Calories','Protein','Carbs','Fats','Type','Item_weight','Price/100g'])
        df.to_csv('food.csv')

    food_data.loc[len(food_data) + 1, :] = (name, price, calories, protein, carbs, fats, type_of_food, item_weight, price*100/item_weight)
    food_data.to_csv('food.csv')
    return food_data

def remove_food(df, name: str):
    df = df[df['Name'] != name]
    df.to_csv('food.csv')
    return df


food_data = add_food('Fehérje puding',4,65, 10,6,0.3,'random', 200)
#food_data = remove_food(food_data, 'Fehér')
print(food_data)

#Columns: Name, Price, Calories, Protein, Carbs, Fats| Type, Item_weight, Weight_per_100
#Types: meat, vegetables, fruits, dairy, pastry, grain
#Item_weight: knowing this I can calculate what's the price / 100g

#Price / 100:
#6.5.......200
#x........ 100
# x = 6.5.100/200


