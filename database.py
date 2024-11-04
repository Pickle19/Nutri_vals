import pandas as pd
import os

#columns = ["Name", "Ár", "Kalória", "Fehérje", "Szénhidrát", "Zsírok"]
#food_data = pd.DataFrame(columns=columns)

food_data = pd.read_csv('food.csv', index_col = 0)

def add_food(df, name: str, price: float, calories: int, protein : float, carbs : float, fats : float):
    if not os.path.exists('food.csv'):
        df.to_csv('food.csv')

    df.loc[len(df) + 1, :] = (name, price, calories, protein, carbs, fats)
    df.to_csv('food.csv')
    return df

def remove_food(df, name: str):
    df = df[df['Name'] != name]
    df.to_csv('food.csv')
    return df

#food_data = add_food(food_data,'Csirke mell',28,195,29.5,0,7.7)
#food_data = remove_food(food_data, 'kaja3')
print(food_data)

