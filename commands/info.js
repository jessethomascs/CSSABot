const { SlashCommandBuilder } = require('discord.js');

module.exports = {
	data: new SlashCommandBuilder()
		.setName('info')
		.setDescription('Sends the user an embedded list of commands'),
	async execute(interaction) {
		await interaction.reply(interaction);
	},
};
