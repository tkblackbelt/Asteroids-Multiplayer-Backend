from typing import Dict
from server.packets.packet import Packet


class GameLeftPacket(Packet):

    def __init__(self, player_id: str, game_id: str):
        self.player_id = player_id
        self.game_id = game_id

    def encode(self) -> Dict:
        packet = super().encode()
        packet["player_id"] = self.player_id
        packet["game_id"] = self.game_id
        return packet


    @staticmethod
    def decode(data: Dict) -> Packet:
        return GameLeftPacket(
            player_id=data["player_id"],
            game_id=data["game_id"]
        )

    @staticmethod
    def get_type() -> str:
        return "leave_game"
