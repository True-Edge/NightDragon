for cog in os.listdir('commands'):
    if cog.endswith(".py"):
        try:
            cog = f"commands.{cog.replace('.py', '')}"
            bot.load_extension(cog)
        except Exception as err:
            print("An Error Has Occured, Logs Has Been Generated")
            logging.basicConfig(filename="Logs/log.txt", filemode='w+', format='%(levelname)s > %(message)s')
            logging.error("An Error Occured.", exc_info=True)

for cogm2 in os.listdir('commands-m1'):
    if cogm2.endswith('.py'):
        with open(f'commands-m1/{cogm2}') as rk:
            exec(rk.read())