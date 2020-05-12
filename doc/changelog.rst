#########
Changelog
#########


***********
Version 3.1
***********

Deutsch
=======
::

	[Neue Funktion] Neuer Objekttyp "Kommunikationsverbindung"
	[Neue Funktion] Vererbung des Schutzbedarfs über die neue Beziehung "Kommunikationsverbindung"
	[Neue Funktion] Die grafische Darstellung der Schutzbedarfsfeststellung kann jetzt gefiltert werden
	[Neue Funktion] Die Begründung für die Schutzbedarfsfeststellung kann in der grafischen Darstellung eingetragen werden
	[Verbesserung]  Die Begründung für die Schutzbedarfsfeststellung ist jetzt auch im CSV-Export enthalten
	[Verbesserung]  Rollen, die durch das Grundschutzkompendium hinzugefügt werden, werden jetzt auch deinstalliert
	[Verbesserung]  Die aktualisierte Dokumentation zum VIVA2-Addons ist ab jetzt hier zu finden: https://viva2.readthedocs.io
	[Bug]           Übersetzungen für "SVG-Datei" und "PNG-Datei" sind in der 1.14.1 nicht mehr vorhanden und werden jetzt durch das Addon geliefert
	[Bug]           Übersetzung vom "Bitte warten" Overlay der Schutzbedarfsfeststellung wurde nur angezeigt, wenn das Raumplan-Addon installiert ist
	[Bug]           Die Schutzbedarfsfeststellung zeigte einen Fehler an, wenn die angezeigten Zielobjekte keine Verbindung haben.


English
=======
::

	[New feature]   New object type "communication link"
	[New feature]   The protection requirements will be inherited over the new relation "communication link"
	[New feature]   It is now possible to set a filter in the graphical representation of the assessment of protection requirements
	[New feature]   The reason for the assessment of the protection requirements can now be edited in the graphical representation
	[Improvement]   The reason for the assessment of the protection requirements in included now in the CSV export
	[Improvement]   Contact roles, which will be imported by the IT-Grundschutz Compendium, will now be removed during deinstallation of the addon
	[Improvement]   The updated documentation for the VIVA2 addon can now be found here: https://viva2.readthedocs.io (only in german yet)
	[Bug]           Translations for "CSV file" and "PNG file" were not available in 1.14.1 anymore
	[Bug]           Translation of the "Please wait" Overlay in the assessment of protection requirements was only shown, if floorplan addon was installed
	[Bug]           The assessment of the protection requirements has shown an error, if the shown target objects didn't have any links


***********
Version 3.0
***********

Deutsch
=======
::

	[Neue Funktion] Der Umsetzungsstatus der Anforderungen wird jetzt an den Zielobjekten/-gruppen gespeichert
	[Neue Funktion] Komplette Überarbeitung des "IT-Grundschutz-Check"
	[Neue Funktion] Neue Kategorie "Prozessbausteine" am Informationsverbund
	[Verbesserung]  Die IT-GS-Kategorien am Informationsverbund sind in einem Ordner zusammengefasst
	[Verbesserung]  Überarbeitung aller mitgelieferten Reports, Entfernen der Reports "Nicht vom Informationsverbund abgedeckt" und "Nicht von Informationsverbünden abgedeckt"
	[Verbesserung]  Umbenennung von Zielgruppen und Zielobjektgruppen
	[Verbesserung]  Umbenennung der Rolle "Verantwortliche Stelle" zu "Grundsätzlich zuständig"
	[Verbesserung]  Alle bei der Installations des VIVA2-Addon hinzugefügten Rollen erhalten den Prefix "IT-GS:"
	[Verbesserung]  Vorbereitung für nächste Version zum Editieren der Begründung bei der Schutzbedarfsfeststellung
	[Bug]           Reports mit Kategorien aus VIVA2 führen zu einem SQL-Fehler (behoben ab 1.14.1)
	[Bug]           Nach dem Import des Kompendiums wird der Suchindex für die neuen/geänderten Objekte nicht neu erstellt
	[Bug]           VIVA2-Deinstallation lässt die Objekttypgruppe im Menü 
	[Bug]           Fehler bei der Listeneditierung der Kategorie IT-Grundschutz-Check
	[Bug]           Der "Durchsuchen"-Button fehlt in ->Informationsverbund->Bereinigter Netzplan


English
=======
::

	[New feature]   The implementation status of the requirements is now saved on the target objects/groups
	[New feature]   Complete revision of the "IT baseline protection check" category
	[New feature]   New category "process modules" at the object type "scope"
	[Improvement]   The addon categories in the object type "scope" are summarized in a folder
	[Improvement]   Revision of all supplied reports, removal of the reports "Not covered by scope" and "Not covered by scopes"
	[Improvement]   Renaming target groups into target object groups
	[Improvement]   Renaming the role "responsible person" to "basically responsible"
	[Improvement]   All roles added during the installation of the VIVA2 addon are given the prefix "IT-BP:"
	[Improvement]   Preparation for the next version to edit the reason in the asessment of protection requirements
	[Bug]           Reports containing categories from VIVA2 led to an SQL error (only working in 1.14.1)
	[Bug]           After importing the compendium, the search index for the new/changed objects wasn't recreated
	[Bug]           VIVA2 deinstallation leaves the object type group in the menu
	[Bug]           Error when using the list edit for the category IT baseline protection
	[Bug]           The "Browse" button is missing in Scope -> IT baseline protection (Scope)-> Adjusted network plan


*************
Version 2.0.3
*************

Deutsch
=======
::

[Neue Funktion] Schutzbedarfsfeststellung: Neue Exportmöglichkeit ím CSV Format
[Neue Funktion] Schutzbedarfsfeststellung: Neue Exportmöglichkeit ím JSON Format
[Verbesserung]  Schutzbedarfsfeststellung: Services und deren Beziehungen werden nun berücksichtigt
[Verbesserung]  Vorbereitung auf kommendes Major-Realease: Anforderungstyp wird beim Import des Kompendiums an der Anforderung gespeichert
[Bug]           Englische Übersetzungen fehlten teilweise
[Bug]           Beim Aktualisieren des Grundschutz-Kompendiums sollte es "Benutzerdefinierte Anforderungen" und nicht "Benutzer-definierte Anforderungen" heißen
[Bug]           Reports wurden bei der Installation nicht korrekt angelegt
[Bug]           Addon wird nicht ordnungsgemäß deinstalliert

English
=======
::

[New feature]   Asessment of protection requirements: New export option in CSV format
[New feature]   Asessment of protection requirements: New export option in JSON format
[Improvement]   Asessment of protection requirements: Services and their relationships are now taken into account
[Improvement]   Preperation for nect major release: Type of requirement is saved on requirement when importing the IT baseline protection kompendium
[Bug]           Some english translations were missing
[Bug]           Small fix in german translation
[Bug]           Reports were not created correctly during installation
[Bug]           Uninstallation of addon does not work correctly


*************
Version 2.0.2
*************

Deutsch
=======
::

[Verbesserung]  Neue Icons und Bilder für VIVA2-Objekttypen
[Bug]           Reports werden bei der Neuinstallation in i-doit 1.13.1 (und höher) in die falsche Datenbank geschrieben


English
=======
::

[Improvement]   New icons and images for VIVA2 object types
[Bug]           Reports are stored in the wrong database during a new installation in i-doit 1.13.1 (or higher)


*************
Version 2.0.1
*************

Deutsch
=======
::

[Bug]           YAML ungültig
[Bug]           Doppelte Anzeige von Informationsverbunde in der Migration
[Bug]           Gefährdungen im IT-Grundschutz werden nicht mehr angezeigt
[Bug]           Schutzbedarfsfeststellung lässt sich nicht direkt nach öffnen des Add-Ons aufrufen
[Bug]           Migration von VIVA auf VIVA2 bei leeren Inhalten teilweise fehlerhaft
[Bug]           In Kategorie Zugwiesene Anforderungen wird eine Fehlermeldung ausgegeben wenn man auf einen Eintrag klickt
[Aufgabe]       VIVA 2 PHP 7.2 Kompabilität


English
=======
::

[Bug]           Invalid YAML
[Bug]           Double display of information networks in the migration
[Bug]           Threats in basic IT protection are no longer displayed
[Bug]           Schutzbedarfsfeststellung doesn't open when selected right after opening the add-on
[Bug]           Migration from VIVA to VIVA2 sometimes faulty when using empty content
[Bug]           In category "Assigned requirements" an error message is displayed when clicking on an entry
[Task]          VIVA 2 PHP 7.2 Compability

