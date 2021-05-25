
from typing import List

from database import DataBase


class Queries:


	@staticmethod
	def create_user(user_id: int, username: str):

		with DataBase() as db:

			db.update("INSERT OR IGNORE INTO users (id, username) VALUES (?, ?)", user_id, username)

	@staticmethod
	def create_address(address: str):

		with DataBase() as db:

			db.update("INSERT INTO addresses (address) VALUES (?)", address)

	@staticmethod
	def bind_material_with_address(material: str, address: str):

		with DataBase() as db:

			db.update(
				"INSERT INTO materials_addresses (material_id, address_id) VALUES ("
				"(SELECT id FROM materials WHERE name = ?), "
				"(SELECT id FROM addresses WHERE address = ?))",
				material, address
			)

	@staticmethod
	def get_materials() -> List[str]:

		with DataBase() as db:

			return [row[0] for row in db.fetchall("SELECT name FROM materials")]

	@staticmethod
	def get_material_advice(material: str) -> str:

		with DataBase() as db:

			return db.fetchone("SELECT advice FROM materials WHERE name = ?", material)[0]

	@staticmethod
	def get_addresses(material: str) -> List[str]:

		with DataBase() as db:

			return [row[0] for row in db.fetchall(
				"SELECT address FROM addresses WHERE id in ("
				"SELECT address_id FROM materials_addresses WHERE material_id = ("
				"SELECT id FROM materials WHERE name = ?))",
				material
			)]
