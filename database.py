
from typing import Any, List, Tuple

import sqlite3

from config import DATABASE_PATH


class DataBase:

	"""
		Class for connect to data base.

		Using in 'with' statement context. Example:

			with DataBase() as db:
				print(db.fetchone("SELECT name FROM materials WHERE id = 3")[0])
	"""

	def __enter__(self, *args):

		self.conn = sqlite3.connect(DATABASE_PATH, check_same_thread=False)
		self.cursor = self.conn.cursor()
		return self

	def __exit__(self, *args):

		self.cursor.close()
		self.conn.close()

	def fetchone(self, query, *args) -> Tuple[Any]:

		"""Returns single row from 'select' query."""

		self.cursor.execute(query, args)
		return self.cursor.fetchone()

	def fetchall(self, query, *args) -> List[Tuple[Any]]:

		"""Return all rows from 'select' query."""

		self.cursor.execute(query, args)
		return self.cursor.fetchall()

	def update(self, query, *args):

		self.cursor.execute(query, args)
		self.conn.commit()
		return True

