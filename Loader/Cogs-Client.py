for cogm3 in os.listdir('commands-m3'):
    if cog.endswith(".py"):
        try:
            cog = f"commands.{cog.replace('.py', '')}"
            client.load_extension(cog)
        except Exception as err:
            print("An Error Has Occured, Logs Has Been Generated")
            logging.basicConfig(filename="Logs/log.txt", filemode='w+', format='%(levelname)s > %(message)s')
            logging.error("An Error Occured.", exc_info=True)

for cogm4 in os.listdir('commands-m4'):
    if cogm2.endswith('.py'):
        with open(f'commands-m4/{cogm4}') as rk:
            exec(rk.read())