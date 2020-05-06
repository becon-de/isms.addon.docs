#####################
Systemvoraussetzungen
#####################

Als Addon für die i-doit CMDB setzt das VIVA2-Addon natürlich ein funktionsfähiges i-doit voraus. Auf ein paar Bessonderheiten sollte geachtet werden:

* Für Upload und Import des Grundschutzkompendiums sollte die maximale Uploadgröße und die PHP-Execution-Time mindestens folgende Größe haben:
    * ``upload_max_filesize = 10MB``
    * ``post_max_size = 10MB``
    * ``max_execution_time = 300``
    * ``max_input_time = 300``
* Der variable Report ``IT-Grundschutz-Check`` benutzt eine Datenbankfunktion, die von MySQL 5.6 und 5.7 noch nicht unterstützt wird. Für eine volleständige Funktionalität sollte MariaDB >=10.1 oder MySQL >=8.0 eingesetzt werden (s. `Known issues <installation.html#known-issues>`_).