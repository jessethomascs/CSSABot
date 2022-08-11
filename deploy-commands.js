require('dotenv').config();
const fs = require('node:fs');
const token = process.env.DISCORD_TOKEN;
const path = require('node:path');
const guildId = process.env.GUILD_ID;
const clientId = process.env.CLIENT_ID;

const { REST } = require('@discordjs/rest');
const { Routes } = require('discord.js');


const commands = [];
const commandsPath = path.join(__dirname, 'commands');
const databasePath = path.join(__dirname, 'database');
const commandFiles = fs.readdirSync(commandsPath).filter(file => file.endsWith('.js'));
const databaseFiles = fs.readdirSync(databasePath).filter(file => file.endsWith('.js'));

for (const file of commandFiles) {
	const filePath = path.join(commandsPath, file);
	const command = require(filePath);
	commands.push(command.data.toJSON());
}

for (const file of databaseFiles) {
	const filePath = path.join(databasePath, file);
	const command = require(filePath);
	commands.push(command.data.toJSON());
}


const rest = new REST({ version: '10' }).setToken(token);

rest.put(Routes.applicationGuildCommands(clientId, guildId), { body: commands })
	.then(() => console.log('Successfully registered application commands.'))
	.catch(console.error);
