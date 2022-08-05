const { SlashCommandBuilder } = require('discord.js');

module.exports = {
	data: new SlashCommandBuilder()
		.setName('clear')
		.setDescription('Clears last <n> messages'),
	async execute(interaction) {
		await interaction.reply('Pong!');
	},
};
