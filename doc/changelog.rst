#########
Changelog
#########

*************
Version 1.4.1
*************

Deutsch
=======
::

[Neue Funktion] Neuer Objekttyp "Virtueller ISMS-Standort" verfügbar
[Neue Funktion] Risikoeinschätzungen können per CSV importiert werden
[Verbesserung]  Optische Verbesserungen der Schieberegler bei der Risikobewertung
[Änderung]      Zu Risikoeinschätzungen zugewiesene SOA-Maßnahmen werden in Reports jetzt mit Leerstellen getrennt, nicht mehr mit Komma
[Bug]           Bei der Listenansicht von Risikoeinschätzungen wurden überschrieben Risikoklassen teilweise falsch angezeigt
[Bug]           Bei älteren PHP-Version kam es zu einer Fehlermeldung nach Installation des Add-ons
[Bug]           Beim Sortieren nach ISMS-Relevanz kam es bei der Objektliste zu einem Datenbankfehler
[Bug]           Die englische Übersetzungen der Risikoformeln waren falsch
[Bug]           Es fehlten Übersetzungen im Dialog-Admin
[Bug]           Das horizontale Scrolling in breiten Reportviews funktionierte nicht mehr
[Bug]           Die Einträge einiger Tabellen im Dialog-Admin konnten nicht bearbeitet werden
[Bug]           Der Knopf "Bewertung vor Behandlung kopieren" hat den Wert für die Eintrittswahrscheinlichkeit nicht übernommen



English
=======
::

[New feature]   New object type "Virtual ISMS location" available
[New feature]   Risk assessments can be imported via CSV import
[Improvement]   Visual improvements of the risk evaluation sliders
[Change]        SOA controls assigned to risk assessments are in reports now seperated with spaces instead of comma
[Bug]           In the list view of risk assessments, overruled risk classes were sometimes displayes incorrectly
[Bug]           With older PHP version there was an error message after installing the ISMS add-on
[Bug]           When sorting according to ISMS relevance, a database error was shown in the object list
[Bug]           The english translations of the risk formulas were incorrect
[Bug]           In the dialog admin some translations were missing
[Bug]           Horizontal scrolling in wide report views didn't work
[Bug]           The entries of some tables in the dialog admin couldn't be edited
[Bug]           The button "Copy assessment before treatment" didn't copy the value of the likelihood 



***********
Version 1.4
***********

Deutsch
=======
::

[Neue Funktion] Asymmetrische Risikomatrix, Risikomatrix-Farbwerte können nun überschrieben werden
[Neue Funktion] Name, Farbe und Anzahl von Risikoklassen sind nun konfigurierbar
[Neue Funktion] Neues Menüpunkt "ISMS" unter "Extras"
[Neue Funktion] Neues Recht "ISMS" im Rechtesystem
[Verbesserung]  Erweiterung der verfügbaren Ausgabespalten bei der Listenasicht von Risikoeinschätzungen
[Verbesserung]  Druckansichten der Report-Views überarbeitet, Druckknopf hinzugefügt
[Verbesserung]  Anpassung des Wording in der Risikoeinschätzung
[Verbesserung]  Die aktualisierte Dokumentation zum ISMS-Add-ons ist ab jetzt hier zu finden: https://isms.readthedocs.io
[Änderung]      Konfiguration der Risiko-Klassen und -Formel unter "Extras" - nicht mehr in den Mandanteneinstellungen
[Änderung]      Mindestvoraussetzung i-doit Version 1.14.2 oder höher
[Änderung]      Anpassung aller Kategorien und Report-Views auf die neuen Risikoklassen
[Bug]           Es wurden falsche Werte für das Attribut "Eintrittswahrscheinlichkeit nach Behandlung" im Report-Manager ausgegeben
[Bug]           Bei der Kategorie Anwendbarkeit kam es im Reportmanager zu einer Fehlermeldung
[Bug]           Es gab einen Fehler beim Duplizieren von Anhang A Maßnahmen
[Bug]           Risikoeinschätzungen mit Kommazahlen wurden in der Risikomatrix teilweise nicht aufgeführt
[Bug]           Es gab falsche Verknüpfungen in Risikoeinschätzungen nach dem Duplizieren von Objekten
[Bug]           Report "ISMS Restrisiko nach Level" wertete das Level nicht aus
[Bug]           Schutzziele wurden neu angelegt, wenn Objekte oder Objektgruppen, die Risikoeinschätzungen hatten, dupliziert wurden.
[Bug]           Risikobehandlungsoptionen ließen sich nicht editieren
[Bug]           Falsches Wording in View "Risikobehandlungsplan"
[Bug]           Anwendbarkeit von SOA-Maßnahme wurde beim Hinzufügen zu einer Risikoeinschätzung nicht automatisch auf "Ja" gesetzt, wenn Kategorie Maßnahme nicht vorhanden war.
[Bug]           Archivierte und gelöschte Objekte sollten nicht in Report-Views angezeigt werden
[Bug]           Die View "ISMS Risikoeinschätzung objektbasiert" zeigte alle Schutzziele und nicht nur die zugeordneten.
[Bug]           Reindexierung des Sucheindexes nach CSV-Import warf eine Fehlermeldung
[Bug]           Nach Editieren der ISMS-Objekttypen gingen die relativen Pfade zu den Objekttyp-Icons verloren
[Bug]           Im Report-Manager gab die Spalte "Eintrittswahrscheinlichkait nach der Behandlung" das Gleiche aus wie "Eintrittswahrscheinlichkeit"
[Bug]           Die Report-View Risikobehandlungsplan funktionierte nicht, wenn die Kategorie "Bedrohung" leer ist
[Bug]           Es erschiene ein Datenbankfehler beim Löschen von unfertigen/archivierten/gelöschten Kategorieeinträgen


English
=======
::

[New feature]   Asymmetrical risk matrix, risk matrix colors ​​can now be overwritten
[New feature]   Name, color and number of risk classes can now be configured
[New feature]   New menu item "ISMS" in "Extras"
[New feature]   New right "ISMS" in Authorization system
[Improvement]   Extension of available output columns in the list view of risk assessments
[Improvement]   Improved the print views of the report views, added print button
[Improvement]   Adaptation of the wording in the risk assessment
[Improvement]   The updated documentation for the ISMS addon can now be found here: https://isms.readthedocs.io (only in german yet)
[Change]        Configuration of the risk classes and formula in "Extras" - no longer in the Tenantsettings
[Change]        Required i-doit version is 1.14.2 or higher
[Change]        Adapt all categories and report views to the new risk classes
[Bug]           Wrong values ​​for attribute "Residual Risk Level" were displayed in the Report Manager
[Bug]           An error message appeared in the report manager for the Applicability category
[Bug]           There was an error duplicating Annex A Controls
[Bug]           Risk assessments with decimal numbers were sometimes not listed in the risk matrix
[Bug]           There were wrong links in risk assessments after duplicating objects
[Bug]           Report "ISMS residual risk by level" did not evaluate the level
[Bug]           Protection objectives were recreated when objects or object groups that had risk assessments were duplicated.
[Bug]           Risk Treatment options could not be edited
[Bug]           Incorrect wording in "Risk treatment plan" view
[Bug]           Applicability of SOA Controls was not automatically set to "Yes" when adding to a risk assessment if the Control category was nonexistent.
[Bug]           Archived and deleted objects should not be displayed in report views
[Bug]           The view "ISMS risk assessment object-based" showed all protection objectives and not just the assigned ones.
[Bug]           Reindexing the search index after CSV import threw an error message
[Bug]           After editing the ISMS object types, the relative paths to the object type icons were lost
[Bug]           In the report manager the column "Likelihood after treatment" the same value as "Likelihood"
[Bug]           The report view risk treatment plan did not work, if category "Threat" is empty
[Bug]           A database error was shown when deleting unfinished/archived/deleted category entries


***********
Version 1.3.3
***********

Deutsch
=======
::

	[Bug]  	        ISMS-Add-on lässt sich auf einer frischen i-doit 1.14 Installation nicht installieren


English
=======
::

	[Bug]  	        Installation of ISMS Add-on does not work in fresh installed i-doit 1-.14


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