const { SlashCommandBuilder } = require('discord.js');

module.exports = {
	data: new SlashCommandBuilder()
		.setName('banmember')
		.setDescription('Bans a student id from database'),
	async execute(interaction) {
		await interaction.reply('Pong!');
	},
};
