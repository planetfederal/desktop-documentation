# Sample script for QGIS Init Script
# This script will initialize the authentication DB and 
# add and HTTP Basic authentication configuration. 
# The script will also set the master password to `password`
# 
# Note: this script can only run if the authentication DB was not 
# already created by the user, this means that it must be executed
# only once on a fresh QGIS installation before the user 
# started QGIS for the first time.


from qgis.PyQt.QtCore import QSettings
from qgis.core import QgsAuthManager, QgsAuthMethodConfig, QgsMessageLog

AUTHDB_MASTERPWD = 'password'

QgsMessageLog.logMessage("Init script: %s" % __file__, tag="Init script", level=QgsMessageLog.INFO)

# Do not run twice!
if not QSettings().value("InitScript/AuthCfgCreated", type=bool):
    QSettings().setValue("InitScript/AuthCfgCreated", True)
    # Check if authdb master password is set
    am = QgsAuthManager.instance()
    if not am.masterPasswordHashInDb():
        # Set it!
        am.setMasterPassword(AUTHDB_MASTERPWD, True)
        # Create config
        am.authenticationDbPath()
        am.masterPasswordIsSet()
        cfg = QgsAuthMethodConfig()
        cfg.setId('myauth1') # Optional, useful for plugins to retrieve an authcfg
        cfg.setName('Example Auth Config HTTP Basic')
        cfg.setMethod('Basic')
        cfg.setConfig('username', 'username')
        cfg.setConfig('password', 'password')
        am.storeAuthenticationConfig(cfg)
    else:
        QgsMessageLog.logMessage("Master password was already set: aborting", tag="Init script", level=QgsMessageLog.INFO)

else:
    QgsMessageLog.logMessage("AuthCfg was already created: aborting", tag="Init script", level=QgsMessageLog.INFO)
