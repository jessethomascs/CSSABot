require('dotenv').config();
const mysql = require('mysql2');
const config = require('../config.json');
const dbconnect = mysql.createConnection(config.mysql);
const { SlashCommandBuilder } = require('discord.js');

module.exports = {
	data: new SlashCommandBuilder()
		.setName('removemember')
		.setDescription('Removes user from database')
		.addNumberOption(option =>
			option.setName('int')
				.setDescription('Member student ID')
				.setRequired(true)),
	async execute(interaction) {
		dbconnect.connect(err => {
			if (err) return console.log(err);
			// else
			console.log('Connection successful for DB_RemoveMember.js');
		});

		dbconnect.query('DELETE FROM ' + config.running_tables.Registered_Members + ' WHERE StudentID = ' + interaction.options.getNumber('int'), (err) => {
			if (err) console.log(err);
		});
		await interaction.reply({ content: 'Query executed.', ephemeral: true });
	},
};

