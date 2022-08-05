const { SlashCommandBuilder } = require('discord.js');

module.exports = {
	data: new SlashCommandBuilder()
		.setName('authenticate')
		.setDescription('Authenticates a user for streamlined joining'),
	async execute(interaction) {
		await interaction.reply('Pong!');
	},
};
