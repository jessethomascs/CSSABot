require('dotenv').config();
const mysql = require('mysql2');

const dbconnect = mysql.createConnection({
	host: 'localhost',
	user: process.env.DB_USER,
	password: process.env.DB_PASS,
	database: 'frederick_test',
	port: 3306
});


dbconnect.connect(function(err) {
	if (err) {
		console.log(err);
	} else {
		console.log('Database connection successful');
	}
});