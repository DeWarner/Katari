"""
##    ##    ###    ########    ###    ########  ####
##   ##    ## ##      ##      ## ##   ##     ##  ##
##  ##    ##   ##     ##     ##   ##  ##     ##  ##
#####    ##     ##    ##    ##     ## ########   ##
##  ##   #########    ##    ######### ##   ##    ##
##   ##  ##     ##    ##    ##     ## ##    ##   ##
##    ## ##     ##    ##    ##     ## ##     ## ####

SIP (Session Initiated Protocol) Application Framework

"""

HOST = "127.0.0.1" #Specify interface to listen on 

PORT = 5060 # Specify port to listen on

ALLOWED_HOSTS = ["127.0.0.1"] # Katari whitelist

USER_AGENT = "Katari Server 0.0.6" # User Agent sent in response 

KATARI_LOGGING = {
                   "LOGFILE" :"Katari.log",
                   "LEVEL": "INFO", 
                   "OUTPUTMODE": "file"
                 }

# katari middleware 
KATARI_MIDDLEWARE = [
    
]

