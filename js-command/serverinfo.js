const Discord = require("discord.js")
const bot = new Discord.Client();

exports.run = (bot, message) => {
    message.delete(10);
    var embed = new Discord.RichEmbed()
    .setTitle("CLICK ME For This Server Icon!")
    .setURL(message.guild.iconURL)
    message.channel.sendEmbed(embed)
	.then(sentMessage => sentMessage.delete(10000))
} 

exports.help = {
    name: "si" 
}