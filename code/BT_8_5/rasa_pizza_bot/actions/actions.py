from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionConfirmRide(Action):
    def name(self) -> Text:
        return "action_confirm_ride"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        from_location = tracker.get_slot("from_location")
        to_location = tracker.get_slot("to_location")
        vehicle_type = tracker.get_slot("vehicle_type")

        distances = {
            ("VKU", "sân bay"): 8,
            ("Cầu Rồng", "bến xe"): 5,
            ("VKU", "bến xe"): 15,
            ("Cầu Sông Hàn", "sân bay"): 3,
        }

        price_per_km = {
            "xe máy": 8000,
            "ô tô": 12000,
            "4 chỗ": 14000,
            "7 chỗ": 18000,
        }

        distance = distances.get((from_location, to_location), 10)
        unit_price = price_per_km.get(vehicle_type, 10000)
        total_price = distance * unit_price

        message = (
            f"Đã đặt {vehicle_type} từ {from_location} đến {to_location}. "
            f"Khoảng cách dự kiến: {distance} km. "
            f"Giá dự kiến: {total_price:,}đ."
        )

        dispatcher.utter_message(text=message)

        return []