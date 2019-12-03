import socket
import threading
import pygame
from player import Player

# Globals
PLAYER_TYPE = None
HOST = None

# Constants
SERVER = '192.168.0.8'
PORT = 12345

# Connects to server. Connects to opponent. Decides who goes first. 
# Affects the two globals PLAYER_TYPE, HOST and 
#
# Returns true or false depending on if the connection could be established.
def setUpConnection():
	global PLAYER_TYPE
	global HOST
	global CONNECTION
	try:
		# Determine what
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect((SERVER, PORT))
		# Player type
		PLAYER_TYPE = sock.recv(1).decode('utf-8')
		print("here")
		print(PLAYER_TYPE)
		if PLAYER_TYPE == "C":
			# Host IP address
			HOST = sock.recv(4)
			# Close the server connection
			sock.close()

			# Connect to the host
			CONNECTION = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			CONNECTION.connect((HOST, PORT))
		elif PLAYER_TYPE == "H":
			# Close the server connection
			sock.close()

			# Wait for a client connection
			HOST = socket.gethostbyname(socket.gethostname())
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			sock.bind((HOST, PORT))
			sock.listen(1)
			print("Connection: ", sock.getsockname())
			CONNECTION, sockname = sock.accept()
			print("Client: ", sockname)
		return True
	except Exception as e:
		print(e)
		return False

def getPlayerOne():
	if PLAYER_TYPE == "H":
		return Player()
	else:
		return OnlinePlayer(CONNECTION)

def getPlayerTwo():
	if PLAYER_TYPE == "H":
		return OnlinePlayer(CONNECTION)
	else:
		return Player()

class OnlinePlayer(Player):
	# Constructor
	def __init__(self, connection):
		self.isOnline = True
		self.connection = connection

	# Gets the opponents move from the network.
	#
	# Returns an X/Y coord of that move (click position).
	def getAction(self, pos):

		return 10

	# Sends the local player's move to the opponent.
	#
	# Returns nothing.
	def sendMove(event, pos):

		return None
