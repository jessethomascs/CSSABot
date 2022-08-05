const { SlashCommandBuilder } = require('discord.js');

module.exports = {
	data: new SlashCommandBuilder()
		.setName('announce')
		.setDescription('Posts an embedded announcement from either message context or database'),
	async execute(interaction) {
		await interaction.reply('Pong!');
	},
};
