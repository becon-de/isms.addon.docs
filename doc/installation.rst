############
Installation
############

Die Installation des VIVA2 Add-Ons entspricht dem Standardvorgehen für die Installation von i-doit Add-Ons:

* Einloggen in des i-doit Admin-Center
* Auf den Reiter "Add-ons" gehen
* Auf den Button "Install/update Add-on" klicken
* Das ZIP-Paket des Addons auswählen
* Auf den Knopf "Upload und install" klicken
* Fertig


************************************************
Wichtige Hinweise für das Update auf Version 3.0
************************************************

.. warning::
	Da sich innerhalb des VIVA2-Addons die Speicherstrukturen der Anforderungsumsetzungen geändert haben, ist eine Datenmigrationen der schon vorhandenen Daten notwendig. Wenn Sie das VIVA2-Addon in der Version 2.x schon im Einsatz und mit Daten befüllt haben, empfehlen wir daher, vor der Installation des VIVA2 3.0 ein Backup der i-doit-Datenbanken und des i-doit-Verzeichnisses zu machen.


.. note::
	Folgende Datenänderungen werden durch die Updateskripte durchgeführt:
	
	* Der Umsetzungsstand der Anforderungen in der Kategorie "IT-Grundschutz-Check" wird jetzt nicht mehr am Baustein gespeichert, sondern an den Zielobjekten/-gruppen bzw. am Informationsverbund. Bei der Updateinstallation wird der am Baustein gespeicherte Umsetzungsstand einer Anforderung an alle Zielobjekten/-gruppen kopiert, denen der Baustein zugeordnet ist.
	* Alle Kontaktzuweisungen an Bausteinen, die die Rolle "Ansprechpartner" haben, werden auf die Rolle "IT-GD: Grundsätzlich zuständig" umgestellt.
	* Die Reports "Nicht vom Informationsverbund abgedeckt" und "Nicht von Informationsverbünden abgedeckt" werden gelöscht, alle anderen Reports in der Report-Kategorie "IT-Grundschutz" werden aktualisiert. Wenn Sie an diesen Reports manuelle Änderungen durchgeführt und in Verwendung haben, sollten Sie diese Reports vor dem Update unter einem anderen Namen speichern.

	Seit der Version 2.0.3 wird der Anforderungstyp (Basisanforderung/Standardanforderung/Anforderung bei erhöhtem Schutzbedarf) beim Import des IT-Grundschutz-Kompendiums an der Anforderung gespeichert. Wenn seit der Installation der Version 2.0.3 das Kompendium nicht importiert wurde, sollte dies wiederholt werden (egal ob vor oder nach dem Update auf Version  3.0), um den vollen Funktionsumfang des VIVA2 3.0 nutzen zu können.

.. _known-issues:
************
Known issues
************

Bei Verwendung von MySQL 5.6 und 5.7 funktioniert der variable Report ``Report: IT-Grundschutz-Check`` nicht, der mit der gleichnamigen Kategorie am Informationsverbund hängt, da MySQL die Funktion ``REGEXP_SUBSTR`` erst ab Version 8.0 implementiert hat. Bei Verwendung von Maria DB gibt es keine Probleme.