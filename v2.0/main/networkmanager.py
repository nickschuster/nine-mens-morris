import socket
import threading
import pygame
from player import Player

PLAYER_TYPE = None
HOST = None
SERVER = '192.168.0.64'
PORT = 12345

# Connects to server. Connects to opponent. Decides who goes first. 
# Affects the two globals PLAYER_TYPE and HOST
#
# Returns true or false depending on if the connection could be established.
def setUpConnection():
	global PLAYER_TYPE
	global HOST
	# Determine what
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((HOST, PORT))
	# Player type
	PLAYER_TYPE = sock.recv(1).decode('utf-8')
	if(PLAYER_TYPE == "C"):
		# Host IP address
		HOST = sock.recv(4)
		# Close the server connection
		sock.close()

		# Connect to the host
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect((HOST, PORT))
	else:
		# Close the server connection
		sock.close()

		# Wait for a client connection
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
		sock.bind((HOST, PORT))
		sock.listen(1)
		print("Connection: ", sock.getsockname())
		sc, sockname = sock.accept()
		print("Client: ", sockname)
	return False

def getPlayerOne():
	if PLAYER_TYPE == "H":
		return Player()
	else:
		return OnlinePlayer()

def getPlayerTwo():
	if PLAYER_TYPE == "H":
		return OnlinePlayer()
	else:
		return Player()

class OnlinePlayer(Player):
	# Constructor
	def __init__(self, writer, reader):
		self.isOnline = True
		self.writer = writer
		self.reader = reader

	# Gets the opponents move from the network.
	#
	# Returns an X/Y coord of that move (click position).
	def getAction():
		return 10

	# Sends the local player's move to the opponent.
	#
	# Returns nothing.
	def sendMove():
		return None
