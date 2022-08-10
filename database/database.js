require('dotenv').config();
const mysql = require('mysql');

mysql.createConnection({
	user: process.env.DBUSER,
	// eslint-disable-next-line comma-dangle
	pass: process.env.DBPASS
});

mysql.createConnection();
