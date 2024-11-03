import dice
        from time import sleep

        def roll(amount:int, sides:int):
            return dice.roll(f'{amount}d{sides}')

        for idx, result in enumerate(roll(5,6)):
            print(f'Resultado del lanzamiento {idx+1}: {result}')
            sleep(5)