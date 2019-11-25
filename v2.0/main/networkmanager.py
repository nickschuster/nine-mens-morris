import socket
import threading
import pygame
from player import Player

THIS_PLAYER = None

# Connects to server. Connects to opponent. Decides who goes first.
#
# Returns true or false depending on if the connection could be established.
def setUpConnection():
	return False

def getPlayerOne():
	return OnlinePlayer()

def getPlayerTwo():
	return OnlinePlayer()

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
