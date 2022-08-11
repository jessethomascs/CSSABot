require('dotenv').config();
const mysql = require('mysql2');
const config = require('../config.json');
const dbconnect = mysql.createConnection(config.mysql);
const { SlashCommandBuilder } = require('discord.js');

module.exports = {
	data: new SlashCommandBuilder()
		.setName('addmember')
		.setDescription('Adds a user to the database for pre-clearance')
		.addNumberOption(option =>
			option.setName('int')
				.setDescription('Member student ID')
				.setRequired(true)),
	async execute(interaction) {
		dbconnect.connect(err => {
			if (err) return console.log(err);
			// else
			console.log('Connection successful for DB_AddMember.js');
		});

		dbconnect.query('INSERT INTO ' + config.running_tables.Registered_Members + ' VALUES (' + interaction.options.getNumber('int') + ')', (err) => {
			if (err) console.log(err);
		});
		await interaction.reply({ content: 'Query executed.', ephemeral: true });
	},
};

