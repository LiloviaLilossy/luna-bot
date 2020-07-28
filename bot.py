from discord.ext import commands
import logging

class Luna(commands.Bot):
    def __init__(self):
        self.logger = logging.getLogger("Luna~lu")
        self.logger.setLevel(logging.INFO)
        log_format = '%(asctime)s %(name)s %(levelname)s: %(message)s~lu'
        logging.basicConfig(filename="logs/Luna.log", format=log_format,
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.logger.info("Init started, defining all necessary variables")
        self.owner_id = 321566831670198272
        self.command_prefix = "lu~"
        self.logger.info(f"Done! Prefix is {self.command_prefix}, owner id is {self.owner_id}")
        self.logger.info("Calling the main class")
        super().__init__(command_prefix=self.command_prefix, owner_id=self.owner_id)
        self.logger.info("Done! Loading the extensions")
        # insert cog for loop
        self.load_extension("jishaku")
        self.logger.info("Jishaku is ready")
    
    async def on_ready(self):
        print("Logged in as "+self.user.name)
        self.logger.info("Logged in as "+self.user.name)
    
    async def on_error(self, event, *args, **kwargs):
        self.logger.error("There is error!", exc_info=1)

luna = Luna()
luna.run()