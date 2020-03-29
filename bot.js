const Discord = require("discord.js");
const fs = require("file-system");
require("dotenv").config();
const bot = new Discord.Client()
Token = (process.env.TOKEN);

try {
    bot.commands = new Discord.Collection();
    bot.settings = require("JS-System/loader.json");
    fs.readdir("js-command/", (err, files) => {
        if(err) console.log(err);
      
        let jsfile = files.filter(f => f.split(".").pop() === "js")
        if(jsfile.length <= 0) return console.log(`${bot.settings.name} No Commands!`);
      
        jsfile.forEach((f, i) =>{
          let props = require(`js-command/${f}`);
          console.log(`[${bot.settings.name}] > Command Has Loaded > ${f}`);
          bot.commands.set(props.help.name, props);
        });
    });
} catch (e) {
    console.log(e);
}

bot.on("message", message => {
    if(message.author.bot) return;
    if(message.channel.type === "dm") return;
	  if (message.content.indexOf(bot.settings.prefix) !== 0) return;
  
    let messageArray = message.content.split(" ");
    const args = message.content.slice(bot.settings.prefix.length).trim().split(/ +/g);
    const command = args.shift().toLowerCase();

    const cmd = bot.commands.get(command);
    if(!cmd) return;
    cmd.run(bot, message, args);
});

bot.login(Token)