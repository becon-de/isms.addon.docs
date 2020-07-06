###########
Einrichtung
###########

Bevor man mit dem ISMS-Add-on Risikoeinschätzungen vornehmen kann, müssen 4 grundlegende Dinge vorbereitet werden:

* Bewertungskriterien festlegen
* Schadenszenarien beschreiben
* Risikoformel definieren
* eigene Maßnahmen definieren
* Daten importieren

 Der erste Schritt ist die Einrichtung von Bewertungskriterien:

.. image:: img/einrichtung_1.PNG

Das Level der Bewertungskritierien wird später für die Berechnung der Risikohöhe genutzt und gilt gleichermaßen für die Eintrittswahrscheinlichkeit und das Schadensausmaß des jeweiligen Bewertungskriteriums. Die Bezeichnung der Bewertungskriterien bildet später die Achsenbeschriftung für die Eintrittswahrscheinlichkeit in der Riskiomatrix, das Schadensausmaß die Achsenbeschriftung für das Schadensausmaß.
Die Level müssen Ganzzahlen sein, Kommazahlen sind derzeit nicht möglich.

Der zweite Schritt ist die Einrichtung der Schadenszenarien:

.. image:: img/einrichtung_2.PNG

Die Schadenszenarien im Screenshot enstammen dem IT-Grundschutz Kompendium und werden für das ISMS-Add-on als CSV-Datei mit ausgeliefert. Natürlich müssen Sie diese Schadenszenarien nicht importieren, sondern können auch eigene erstellen. Die Kennzeichnung der Schadenszenarien ist nur für die Reihenfolge der Darstellung relevant. In den Schadenszenarien sollte eine Ausprägung für jedes vorhandene Bewertungskriterium (in unserem Beispiel: Selten, Mittel, Häufig, Sehr häufig) erstellt werden. Die Ausprägungen werden später an den Schiebereglern für die Risikoeinschätzung erscheinen. Es bietet sich also an, diese möglichst kurz zu fassen und die ausformulierten Beschreibungen aus dem IT-Grundschutz durch Werte zu ersetzen, die für Ihr Unternehmen relevant sind. (Als Beispiel sehen Sie im Screenshot die Finanziellen Auswirkungen)

Im dritten Schritt sollten Sie die Risikoformel definieren.

Diese Einstellung können Sie in den Mandanteneinstellungen unter Verwaltung->Systemeinstellungen->Mandanteneinstellungen im Reiter ISMS finden.

Im vierten Schritt sollten Sie eigene Maßnahmen erstellen. Natürlich können Sie hier auch mit dem bereitgestellten Import der 1657 Anforderungen aus dem Grundschutz-Kompendium arbeiten.

Alle Dateien, die zum Import angeboten werden finden Sie in den ISMS-Bundle oder Testversionen indem Sie zunächst die ZIP-Datei entpacken und anschließend zu folgendem Pfad navigieren:
**/src/classes/modules/iso27001/Catalogs**

Im fünften und letzten Schritt sollten Sie den mitgelieferten Import für die Anhang A Maßnahmen (wahlweise deutsch oder englisch) importieren.
Navigieren Sie dazu zum CSV-Import (Extras->CMDB-Import->CSV Import) und laden Sie die entsprechende Datei hoch.

.. image:: img/einrichtung_3.PNG

Die hochgeladene Datei können Sie nun zum Import verwenden. Wählen Sie oben rechts das Import Profil "ISMS universal (new)" aus und starten Sie den Import mit dem Button "Importieren" ganz unten rechts.

.. image:: img/einrichtung_4.PNG

Da ein Risiko immer aus Bedrohung und Schwachstelle besteht, empfiehlt es sich, auch von diesen Objekttypen bereits Objekte zu erstellen. Alternativ bieten wir hier die Elementargefährdungen aus dem IT-Grundschutz, augesplittet nach Bedrohung und Schwachstelle zum Import an. Um diese zu importieren verfahren sie analog zu den Anhang A Maßnahmen.

Die technische Einrichtung des ISMS-Add-ons ist jetzt abgeschlossen.


.. |pfeil| unicode:: U+23F5