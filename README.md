# Työaikaseuranta

Sovelluksen avulla pidetään kirjaa projekteihin käytetystä työajasta. Tarkoituksena on myös seurata toteutunutta työmäärää suhteessa alunperin arvioituun työmäärään. Jatkossa sovellus tuottaa parempia arvioita eri tyyppisten projektien suunnitteluun ja budjetointiin. Sovellusta on mahdollista käyttää useamman rekisteröityneen käyttäjän.

## Dokumentaatio

[Tietokantakaavio](https://github.com/tjvalkonen/tyoaikaseuranta/blob/master/dokumentointi/Tietokantakaavio02.png)

[Käyttötapaukset](https://github.com/tjvalkonen/tyoaikaseuranta/blob/master/dokumentointi/kayttotapaukset.md)

## Käyttöönotto

Kopioi repository koneellesi. (Jos kopioit .zip paketin, pura se haluamaasi kansioon koneellesi)

Tarvitset Pythonin käyttöön koneellesi. [www.python.org](https://www.python.org/)

Avaa komentorivi-näkymä ja mene kopioimasi repositoryn juurihakemistoon.

Luo uusi virtuaaliympäristö Python komennolla: python -m venv venv

Aktivoi luomasi virtuaaliympäristö: source venv/bin/activate

Asenna tarvittavat riippuvuudet: pip install -r requirements.txt

Käynnistä sovellus komennolla: python run.py

## Käyttöohje

Luo itsellesi tuonnus oikean yläkulman "Create new account" -linkin takaa.

Voit valita tunnukselle rooliksi User tai Admin. (Admin voi tehdä joitakin toimintoja mitä User ei)

Kun kirjaudut sovellukseen päänavigaatiossa on neljä osiota minne pääsee.

1. Project List (Projektien listaus)

2. Add a Project (Projektin lisäys)

3. Accounts (Käyttäjät)

4. Your Account (Sinun käyttäjätunnuksesi)

### 1. Project List (Projektien listaus)

Osiossa näytetään sovelluksessa olevat projektit ja niiden tietoja.

Projektin voi poistaa, jos siinä ei ole yhtään työtä merkittynä (töiden poisto puuttuu tällä hetkellä)

Projektin voi merkitä päättyneeksi (sillä ei ole merkitystä sovelluksessa tällä hetkellä)

Projektin nimeä klikkaamalla pääsee projektin töiden listukseen.

Work done in project -listauksessa on projekteihin tehty työ listattuna projekteittain.

#### Project's tasks (projektin töiden listaus)

Tässä on listattuna projektiin merkityt arviot töistä ja tehdyt työt.

Tasks status valitaan sen mukaan syötetäänkö arviota työmäärästä vai oikeaa toteutunutta työtä.

### 2. Add a Project (Projektin lisäys)

Tähän lomakkeeseen syötetään projektin nimi. (Lomakkeesa voi merkitä projektin jo tehdyksi, mutta tällä ei ole merkitystä)

### 3. Accounts (käyttäjät)

Tässä on lista kaikista käyttäjistä. Tarkoitus on että vain ylläpitäjä (Admin) pääsee hallinnoimaan kaikkia käyttäjiä. (kokonaisuus on keskeneräinen)

### 4. Your Account

Täällä näkee oman käyttäjätunnuksen tiedot ja voi muokata niitä sekä näkee mihin projekteihin on tehnyt työtä.

## Heroku

[tjv-tyoaikaseuranta](https://tjv-tyoaikaseuranta.herokuapp.com/)

Tällä hetkellä Heroku ei toimi. Yhteenvetokyselyt kun ovat tyhjiä, sovellus ei toimi. Omalla koneella toimii. 

Testitunnukset

username: hello

password: world

## Tietokanta
```
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
```
