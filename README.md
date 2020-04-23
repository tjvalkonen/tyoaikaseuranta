# Työaikaseuranta

Sovelluksen avulla pidetään kirjaa projekteihin käytetystä työajasta. Tarkoituksena on myös seurata toteutunutta työmäärää suhteessa alunperin arvioituun työmäärään. Jatkossa sovellus tuottaa parempia arvioita eri tyyppisten projektien suunnitteluun ja budjetointiin. Sovellusta on mahdollista käyttää useamman rekisteröityneen käyttäjän.

## Dokumentaatio

[Tietokantakaavio](https://github.com/tjvalkonen/tyoaikaseuranta/blob/master/dokumentointi/Tietokantakaavio01.png)

[Käyttötapaukset](https://github.com/tjvalkonen/tyoaikaseuranta/blob/master/dokumentointi/kayttotapaukset.md)

## Käyttöönotto

Kopioi repository koneellesi. (Jos kopioit .zip paketin, pura se haluamaasi kansioon koneellesi)

Tarvitset Pythonin käyttöön koneellesi. [www.python.org](https://www.python.org/)

Avaa komentorivi-näkymä ja mene kopioimasi repositoryn juurihakemistoon.

Luo uusi virtuaaliympäristö Python komennolla: python -m venv venv

Aktivoi luomasi virtuaaliympäristö: source venv/bin/activate

Asenna tarvittavat riippuvuudet: pip install -r requirements.txt

Käynnistä sovellus komennolla: python run.py

## Heroku

[tjv-tyoaikaseuranta](https://tjv-tyoaikaseuranta.herokuapp.com/)

Testitunnukset

username: hello

password: world

## Tietokanta

CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	role VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE project (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	done BOOLEAN NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	CHECK (done IN (0, 1)), 
	FOREIGN KEY(account_id) REFERENCES account (id)
);
CREATE TABLE task (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	tasktype VARCHAR(144) NOT NULL, 
	description VARCHAR(144) NOT NULL, 
	time INTEGER NOT NULL, 
	taskstatus VARCHAR(144) NOT NULL, 
	project_id INTEGER NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(project_id) REFERENCES project (id), 
	FOREIGN KEY(account_id) REFERENCES account (id)
);

