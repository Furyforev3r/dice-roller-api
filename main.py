from fastapi import FastAPI
import uvicorn
import random
import os


app = FastAPI()


@app.get("/{dice_input}")
async def main(dice_input: str):
    dice_split = []
    dices_mod = []
    dices = []
    dices_dict = {}
    if '+' in dice_input:
        dice_split = dice_input.split('+')
    else:
        dice_split = [dice_input]
    atualdiceverify = 0
    for dice_verificacao in dice_split:
        try:
            try:
                dices_mod[atualdiceverify][atualdiceverify].append(int(dice_verificacao))
            except IndexError:
                dices_mod.append({
                    atualdiceverify: [int(dice_verificacao)]
                    })
        except ValueError:
            if len(dices) > 1:
                atualdiceverify += 1
            dices.append(dice_verificacao)

    for dices_verificacao in range(0, len(dices)):
        try:
            dice_d_split = dices[dices_verificacao].split('d')
            dices_amount = int(dice_d_split[0])
            dices_sides = int(dice_d_split[1])
            if dices_amount > 100 or dices_amount < 1 or dices_sides <= 1:
                raise ValueError
            dices_array = []
            try:
                dice_mod = dices_mod[dices_verificacao][dices_verificacao]
            except IndexError:
                dice_mod = []
            mod_sum = sum(dice_mod)
            for i in range(dices_amount):
                dices_array.append(random.randint(1, dices_sides))
            greater = max(dices_array)
            less = min(dices_array)
            dice_sum = sum(dices_array)
            dices_dict[dices_verificacao] = {
                'Amount': dices_amount,
                'Sides': dices_sides,
                'Results': dices_array,
                'Mod': dice_mod,
                'ModSum': mod_sum,
                'TotalNoMod': dice_sum,
                'TotalMod': dice_sum+mod_sum,
                'Greater': greater,
                'Less': less,
                'Average': greater/less,
                'GreaterWMod': greater+mod_sum
                }
        except ValueError:
            dices_dict = {
                "Error": "Invalid input",
                "0": {
                    'Amount': 0,
                    'Sides': 0,
                    'Results': [],
                    'Mod': [],
                    'ModSum': 0,
                    'TotalNoMod': 0,
                    'TotalMod': 0,
                    'Greater': 0,
                    'Less': 0,
                    'Average': 0,
                    'GreaterWMod': 0
                }
            }
    return dices_dict

uvicorn.run(app, port = os.environ['PORT'], host = "0.0.0.0")
