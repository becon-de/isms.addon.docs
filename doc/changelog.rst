#########
Changelog
#########

***********
Version 1.3.3
***********

Deutsch
=======
::

	[Bug]  	        ISMS-Addon lässt sich auf einer frischen i-doit 1.14 Installation nicht installieren


English
=======
::

	[Bug]  	        Installation of ISMS addon does not work in fresh installed i-doit 1-.14


***********
Version 1.3.2
***********

Deutsch
=======
::

	[Neue Funktion] Die Report-Views können jetzt nach Standorten gefiltert werden
	[Neue Funktion] Das Recht "Ansehen" auf "Kategorie in Objekten unterhalb eines 	Standortes" für die Kategorie "ISMS" wird bei den ISMS-Report-Views berücksichtigt
	[Neue Funktion] Die Berücksichtigung der Standortrechte kann in den 	Mandanteneinstellungen konfiguriert werden
	[Bug]  	        In der Report-View "ISMS Geltungsbereich" wird der Standort nicht 	angezeigt
	[Bug]			Filter auf Anwendungsbereich funktioniert nicht in den Report Views 	"ISMS Risiko nach Level" und "ISMS Restrisiko nach Level"


English
=======
::

	[New feature]   Report views can now be filtered by location
	[New feature]   The right "View" of "Category in Objects underneath a location" for 	category "ISMS" is taken into account in the ISMS report views
	[New feature]   New tenant settings: Filter report views with location based rights
	[Bug]           The location isn't shown in the report view "ISMS Scope"
	[Bug]			Filter for scope does not work in report views " ISMS Risk by Level" and "ISMS Residual Risk by Level"

***********
Version 1.3.1
***********

Deutsch
=======
::

	[Neue Funktion] Report-View "ISMS Risikomatrix" erweitert um zweite Risikomatrix 	nach Risikobehandlung
	[Verbesserung]  Optische Verbesserungen in der Report-View "ISMS Risikomatrix"
	[Bug]           Reports werden bei der Neuinstallation in i-doit 1.13.1 (und höher) 	in die falsche Datenbank geschrieben
	[Bug]           Fehlende und fehlerhafte Übersetzungen in Report-View "ISMS Risikomatrix"


English
=======
::

	[New feature]   Extended report view "ISMS Risk Matrix" erweitert with second risk 	matrix after risk treatment
	[Improvement]   Visual improvements in report view "ISMS Risk Matrix"
	[Bug]           Reports are stored in the wrong database during a new installation 	in i-doit 1.13.1 (or higher)
	[Bug]           Missing or faulty translations in report view "ISMS Risk Matrix"


***********
Version 1.3.0
***********

Deutsch
=======
::

	[Neue Funktion] Erstellen eines neuen Objekttypes "Maßnahme Anhang A"
	[Neue Funktion] Erweiterung des Objekttyps Bewertungskriterium zur textuellen 	Beschreibung des Schadensausmaßes
	[Neue Funktion] Neue Report-View "SOA-Vollständigkeitsprüfung"
	[Verbesserung]  Neue Icons und Bilder für ISMS-Objekttypen
	[Verbesserung]  BSI-Elementargefährdungen nach Bedrohung und Schwachstelle 	aufgeteilt und als CSV-Import zur Verfügung gestellt
	[Verbesserung]  Risikoeinschätzung erweitert um das Attribut "Datum der 	Risikobewertung"
	[Verbesserung]  Report-View "Erklärung der Anwendbarkeit (SOA)" erweitert
	[Verbesserung]  Report-View "Risikomatrix" nutzt neue textuelle Ausprägung des 	Schadensausmaßes
	[Verbesserung]  Anforderungen aus dem BSI-Grundschutzkompedium werden als CSV-Import 	zur Verfügung gestellt
	[Verbesserung]  Bedrohungen, Schwachstellen und Maßnahmen aus der 	"Orientierungshilfe zu Inhalten und Anforderungen an 	branchenspezifischeSicherheitsstandards (B3S) gemäß §8a(2) BSIG" (KRITIS) werden als 	CSV-Import zur Verfügung gestellt
	[Änderung]      Objekttyp "Gefährdung" umbenannt in "Bedrohung"
	[Änderung]      Entfernen des nicht benötigten dritten Schwellenwert im Abschnitt 	"ISMS" der Mandanteneinstellungen
	[Änderung]      Risikobehandlungsoptionen an Werte der ISO 31000 angepasst
	[Änderung]      Umbennenen des Objekttyps "Maßnahme" in "Maßnahme (SOA)"
	[Bug]           Fehlender Objekttitel in Report-View "ISMS Risikoeinschätzung 	objektbasiert"
	[Bug]           unbewertete Schadenszenarien führen zu falscher Darstellung in 	Report-Views "ISMS Risikoeinschätzung" und "... objektbasiert"
	[Bug]           Falsche Reihenfolge der Schandenszenario-Bewertungen in den 	Report-Views "ISMS Risikoeinschätzung" und "... objektbasiert"
	[Bug]           Rechtefehler bei Listeneditierung von Kategorie "Empfehlungen nach 	ISO 27002"
	[Bug]           SQL-Fehler bei Listeneditierung des Attributes "Anwendbarkeit"
	[Bug]           Kategorie "Empfehlungen nach ISO 27002" lässt sich nicht der 	Listenansicht hinzufügen
	[Bug]           Fehler im variablen Report
	[Bug]           Das Attribute "ISMS Relevanz" wird in der Listeneditierung nicht 	speichern
	[Bug]           Fehlende englische Übersetzung der Report view "ISMS 	Risikobehandlungsplan (RTP)"


English
=======
::

	[New feature]   Created new object-type "Control Annex A"
	[New feature]   Added new attribute to object-type "Criteria" to describe 	consequences
	[New feature]   New Report-view "SOA completeness check"
	[Improvement]   New icons and images for ISMS object types
	[Improvement]   Splitted BSI elementary threads to threads and vulnerabilitys and 	published them as csv-import
	[Improvement]   Added new attribute to risk assessment: "Date of risk-evaluation"
	[Improvement]   Report-view "Statement of Applicability (SOA)" extended
	[Improvement]   Report-view "Risk Matrix" uses new attribute for consequences
	[Improvement]   Requirements from "BSI-Grundschutzkompendium" are published as 	csv-import
	[Improvement]   Threads, vulnarabilities and controls from "Guidelines on content 	and requirements for industry-specific security standards (B3S) according to §8a(2) 	BSIG" (KRITIS) are published as csv-import
	[Change]        Object-type "Threat" renamed in german language
	[Change]        Removed the unused treshold value in the ISMS section of the 	Tenantsettings
	[Change]        Options for risk treatment adjusted to values of ISO 310000
	[Change]        Renamed "Control" to "SOA-Control" 
	[Bug]           Missing object title in Report-view "ISMS risk assessment object 	based"
	[Bug]           Unrated incident scenarios lead to false representation in 	Report-Views "ISMS risk assessment" and "... object based"
	[Bug]           False order of incendent scenario ratings in Report-Views "ISMS risk 	assessment" and "... object based"
	[Bug]           Authentication error in multi-edit for category "Advised by ISO27002"
	[Bug]           SQL-Error thrown at multi-edit for attribute "Applicability"
	[Bug]           Category "Advised by ISO27002" cannot be added to list-view
	[Bug]           Error in variable Report
	[Bug]           Attribute "ISMS relevant" cannot be saved in multi-edit
	[Bug]           Missing english translation of report view "ISMS treatment plan (	RTP)"	