CREATE TABLE `page` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date_created` datetime DEFAULT NULL,
  `date_modified` datetime DEFAULT NULL,
  `link` varchar(32) DEFAULT NULL,
  `title` varchar(64) DEFAULT NULL,
  `content` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

LOCK TABLES `page` WRITE;
/*!40000 ALTER TABLE `page` DISABLE KEYS */;

INSERT INTO `page` (`id`, `date_created`, `date_modified`, `link`, `title`, `content`)
VALUES
	(1,'2018-02-23 15:37:18','2018-02-23 15:37:18','sta-je-lozinka-me','Šta je lozinka.me?','<div class=\"eight columns offset-by-two\">\n	<h2>Šta je lozinka.me?</h2>\n	<p>\n        <span class=\"text-primary\"><b>lozinka.me</b></span>\n            je online platforma, nastala kao hobi projekat, koja vam omogućava da brzo, anonimno i sigurno\n            provjerite jačinu lozinke.\n    </p>\n    <p>\n        Sav sadržaj ovog sajta (skripte, baza podataka, kod na osnovu kojeg sajt funkcioniše, slike i ostali fajlovi)\n        je javno dostupan - <a><b>open source</b></a>.</p>\n    <p>	 \n	Ovo garantuje sigurnost i anonimnost servisa.\n        Svako ko želi, može pregledati kod na osnovu kojeg ovaj sajt fukcioniše i može predložiti izmjene.\n    </p>\n    <p>Provjera jačine lozike vam omogućava da:\n    <ul>\n        <li>Vidite karakteristike lozinke</li>\n        <li>Provjerite koliko je vremena računaru potrebno da otkrije lozinku</li>\n        <li>Utvrdite da li se lozinka nalazi u listama najčešće korištenih lozinki</li>\n        <li>Dobijete konačan rezultat jačine lozinke baziran na svim karakteristikama lozinke (0-4)</li>\n    </ul>\n    </p>\n</div>'),
	(2,'2018-02-23 15:37:18','2018-02-23 15:37:18','open-source','Open source','<div class=\"eight columns offset-by-two\">\n	<h2>Open source</h2>\n	<p>\n        Otvoreni softver (eng. Open source software) se odnosi na softver čiji je izvorni kod dostupan unutar\n        „open source” licence svim korisnicima koji ga mogu mijenjati, prepravljati i poboljšavati njegov sadržaj.\n        To znači da uz „open source” programe dolazi i čitav izvorni kod u nekom programskom jeziku, što nije slučaj sa plaćenim softverom.\n    </p>\n    <p>\n        Sav sadržaj ovog sajta (skripte, baza podataka, kod na osnovu kojeg sajt funkcioniše, slike i ostali fajlovi)\n        je javno dostupan - <b>open source</b>.</p>\n    <p>\n</div>'),
	(3,'2018-02-23 15:37:18','2018-02-23 15:37:18','sigurnost','Sigurnost','<div class=\"eight columns offset-by-two\">\n	<h2>Sigurnost</h2>\n	<p>\n        Svaka vrsta razmjene informacija između korisnika i sajta je enkriptovana pomoću <b class=\"text-primary\">HTTPS</b>.\n    </p>\n    <p>\n        HTTPS (engl. Hypertext Transfer Protocol Secure) je kombinacija Hypertext Transfer Protocol-a sa SSL/TSL\n        protokolom da bi se obezbijedila enkripcija i sigurna identifikacija servera. \n    </p>\n    <p>\n        HTTPS konekcija se često koristi za novčane transakcije preko Interneta i za prenos osjetljivih informacija.</p>\n    <p>\n        Glavna ideja HTTPS protokola je da se kreira bezbjedni kanal preko nezaštićene mreže.\n    </p>\n</div>'),
	(4,'2018-02-23 15:37:18','2018-02-23 15:37:18','privatnost','Privatnost','<div class=\"eight columns offset-by-two\">\n	<h2>Privatnost</h2>\n	<p>\n        Ovaj sajt ne prikuplja nikakve podatke koji bi mogli da dovedu do identifikacije korisnika.\n    </p>\n    <p>\n        Na osnovu izvornog koda ovog sajta, koji je javno dostupan, možete se uvjeriti da ovaj sajt ne prikuplja nikakve\n        podatke.\n    </p>\n    <p>\n        Cilj ovog servisa nije identifikacija i prikupljanje podataka, već povećanje sigurnosti.\n    </p>\n</div>\n');

/*!40000 ALTER TABLE `page` ENABLE KEYS */;
UNLOCK TABLES;