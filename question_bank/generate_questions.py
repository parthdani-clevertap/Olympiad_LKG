import json
import random

def generate_question_bank():
    print("Generating question bank...")
    
    modules = {
        "Module 1: My Body": {
            "items": [
                {"name": "Eye", "emoji": "👁️"}, {"name": "Nose", "emoji": "👃"}, {"name": "Ear", "emoji": "👂"},
                {"name": "Mouth", "emoji": "👄"}, {"name": "Tongue", "emoji": "👅"}, {"name": "Leg", "emoji": "🦵"},
                {"name": "Foot", "emoji": "🦶"}, {"name": "Hand", "emoji": "✋"}, {"name": "Arm", "emoji": "💪"},
                {"name": "Brain", "emoji": "🧠"}, {"name": "Heart", "emoji": "🫀"}, {"name": "Teeth", "emoji": "🦷"},
                {"name": "Bone", "emoji": "🦴"}, {"name": "Lips", "emoji": "💋"}
            ],
            "type": "identification"
        },
        "Module 2: Sense Organs": {
            "items": [
                {"name": "Sight/Seeing", "emoji": "👀", "q": "Which helps us see?"},
                {"name": "Hearing", "emoji": "👂", "q": "Which helps us hear?"},
                {"name": "Smell", "emoji": "👃", "q": "Which helps us smell?"},
                {"name": "Taste", "emoji": "👅", "q": "Which helps us taste?"},
                {"name": "Touch", "emoji": "✋", "q": "Which helps us feel/touch?"}
            ],
            "type": "function"
        },
        "Module 3: Community Helpers": {
            "items": [
                {"name": "Police Officer", "emoji": "👮"}, {"name": "Doctor", "emoji": "👩‍⚕️"}, 
                {"name": "Firefighter", "emoji": "🧑‍🚒"}, {"name": "Chef/Cook", "emoji": "👨‍🍳"}, 
                {"name": "Farmer", "emoji": "🧑‍🌾"}, {"name": "Teacher", "emoji": "👩‍🏫"}, 
                {"name": "Artist", "emoji": "🎨"}, {"name": "Astronaut", "emoji": "🧑‍🚀"},
                {"name": "Construction Worker", "emoji": "👷"}, {"name": "Detective", "emoji": "🕵️"},
                {"name": "Mechanic", "emoji": "👨‍🔧"}, {"name": "Scientist", "emoji": "🧑‍🔬"},
                {"name": "Judge", "emoji": "🧑‍⚖️"}, {"name": "Pilot", "emoji": "👨‍✈️"}
            ],
            "type": "identification"
        },
        "Module 4: Animal Kingdom": {
            "items": [
                {"name": "Lion", "emoji": "🦁"}, {"name": "Tiger", "emoji": "🐯"}, {"name": "Elephant", "emoji": "🐘"},
                {"name": "Dog", "emoji": "🐶"}, {"name": "Cat", "emoji": "🐱"}, {"name": "Mouse", "emoji": "🐭"},
                {"name": "Rabbit", "emoji": "🐰"}, {"name": "Fox", "emoji": "🦊"}, {"name": "Bear", "emoji": "🐻"},
                {"name": "Panda", "emoji": "🐼"}, {"name": "Cow", "emoji": "🐮"}, {"name": "Pig", "emoji": "🐷"},
                {"name": "Frog", "emoji": "🐸"}, {"name": "Monkey", "emoji": "🐵"}, {"name": "Chicken", "emoji": "🐔"},
                {"name": "Penguin", "emoji": "🐧"}, {"name": "Bird", "emoji": "🐦"}, {"name": "Duck", "emoji": "🦆"},
                {"name": "Owl", "emoji": "🦉"}, {"name": "Bat", "emoji": "🦇"}, {"name": "Wolf", "emoji": "🐺"},
                {"name": "Horse", "emoji": "🐴"}, {"name": "Unicorn", "emoji": "🦄"}, {"name": "Bee", "emoji": "🐝"},
                {"name": "Butterfly", "emoji": "🦋"}, {"name": "Ladybug", "emoji": "🐞"}, {"name": "Snake", "emoji": "🐍"},
                {"name": "Turtle", "emoji": "🐢"}, {"name": "Whale", "emoji": "🐳"}, {"name": "Dolphin", "emoji": "🐬"},
                {"name": "Fish", "emoji": "🐟"}, {"name": "Octopus", "emoji": "🐙"}, {"name": "Crab", "emoji": "🦀"},
                {"name": "Shark", "emoji": "🦈"}, {"name": "Snail", "emoji": "🐌"}, {"name": "Ant", "emoji": "🐜"}
            ],
            "type": "identification"
        },
        "Module 5: Plant Life": {
            "items": [
                {"name": "Tree", "emoji": "🌳"}, {"name": "Pine Tree", "emoji": "🌲"}, {"name": "Cactus", "emoji": "🌵"},
                {"name": "Flower", "emoji": "🌺"}, {"name": "Rose", "emoji": "🌹"}, {"name": "Sunflower", "emoji": "🌻"},
                {"name": "Tulip", "emoji": "🌷"}, {"name": "Leaf", "emoji": "🍃"}, {"name": "Seedling", "emoji": "🌱"},
                {"name": "Herb", "emoji": "🌿"}, {"name": "Mushroom", "emoji": "🍄"}, {"name": "Palm Tree", "emoji": "🌴"},
                {"name": "Apple", "emoji": "🍎"}, {"name": "Grapes", "emoji": "🍇"}, {"name": "Watermelon", "emoji": "🍉"},
                {"name": "Strawberry", "emoji": "🍓"}, {"name": "Carrot", "emoji": "🥕"}, {"name": "Corn", "emoji": "🌽"}
            ],
            "type": "identification"
        },
        "Module 6: Transport": {
            "items": [
                {"name": "Car", "emoji": "🚗"}, {"name": "Taxi", "emoji": "🚕"}, {"name": "Bus", "emoji": "🚌"},
                {"name": "Police Car", "emoji": "🚓"}, {"name": "Ambulance", "emoji": "🚑"}, {"name": "Fire Truck", "emoji": "🚒"},
                {"name": "Bicycle", "emoji": "🚲"}, {"name": "Motorcycle", "emoji": "🏍️"}, {"name": "Scooter", "emoji": "🛴"},
                {"name": "Train", "emoji": "🚂"}, {"name": "Bullet Train", "emoji": "🚄"}, {"name": "Airplane", "emoji": "✈️"},
                {"name": "Helicopter", "emoji": "🚁"}, {"name": "Rocket", "emoji": "🚀"}, {"name": "Ship", "emoji": "🚢"},
                {"name": "Boat", "emoji": "⛵"}, {"name": "Canoe", "emoji": "🛶"}, {"name": "Tractor", "emoji": "🚜"},
                {"name": "Truck", "emoji": "🚚"}
            ],
            "type": "identification"
        },
        "Module 7: Weather & Seasons": {
            "items": [
                {"name": "Sun/Sunny", "emoji": "☀️"}, {"name": "Cloud/Cloudy", "emoji": "☁️"}, {"name": "Rain/Rainy", "emoji": "🌧️"},
                {"name": "Full Moon", "emoji": "🌕"}, {"name": "Crescent Moon", "emoji": "🌙"}, {"name": "Star", "emoji": "⭐"},
                {"name": "Thunderstorm", "emoji": "⛈️"}, {"name": "Snow/Snowy", "emoji": "❄️"}, {"name": "Wind/Windy", "emoji": "🌬️"},
                {"name": "Rainbow", "emoji": "🌈"}, {"name": "Umbrella", "emoji": "☂️"}, {"name": "Snowman", "emoji": "☃️"},
                {"name": "Summer (Sunglasses)", "emoji": "🕶️"}, {"name": "Winter (Scarf)", "emoji": "🧣"}, {"name": "Fire", "emoji": "🔥"},
                {"name": "Droplet", "emoji": "💧"}
            ],
            "type": "identification"
        },
        "Module 8: Good Manners & Safety": {
            "items": [
                {"name": "Good / Correct", "emoji": "✅"}, {"name": "Bad / Wrong", "emoji": "❌"},
                {"name": "Trash in Bin", "emoji": "🚮"}, {"name": "No Littering", "emoji": "🚯"},
                {"name": "Traffic Light", "emoji": "🚦"}, {"name": "Wash Hands", "emoji": "🧼"},
                {"name": "Handshake", "emoji": "🤝"}, {"name": "Toilets", "emoji": "🚻"},
                {"name": "Wheelchair Access", "emoji": "♿"}, {"name": "Quiet", "emoji": "🤫"},
                {"name": "Recycle", "emoji": "♻️"}, {"name": "Stop Sign", "emoji": "🛑"},
                {"name": "Crossing", "emoji": "🚸"}, {"name": "Warning", "emoji": "⚠️"}
            ],
            "type": "identification"
        },
        "Module 9: Living & Non-Living": {
            "subcategories": {
                "Living": ["👶", "👧", "👨", "👩", "🐶", "🐱", "🦁", "🐟", "🐝", "🌲", "🌹", "🐌"],
                "Non-Living": ["🪑", "🧸", "📺", "🚗", "📱", "⌚", "🖊️", "🎸", "🥣", "🥪", "🏠", "💎"]
            },
            "type": "classification"
        },
        "Module 10: Objects & Materials": {
            "items": [
                {"name": "Chair", "emoji": "🪑"}, {"name": "Bed", "emoji": "🛏️"}, {"name": "Door", "emoji": "🚪"},
                {"name": "Key", "emoji": "🔑"}, {"name": "Hammer", "emoji": "🔨"}, {"name": "Spoon", "emoji": "🥄"},
                {"name": "Balloon", "emoji": "🎈"}, {"name": "Book", "emoji": "📖"}, {"name": "Pencil", "emoji": "✏️"},
                {"name": "Shirt", "emoji": "👕"}, {"name": "Shoe", "emoji": "👞"}, {"name": "Glasses", "emoji": "👓"},
                {"name": "Watch", "emoji": "⌚"}, {"name": "Camera", "emoji": "📷"}, {"name": "Computer", "emoji": "💻"},
                {"name": "Phone", "emoji": "📱"}, {"name": "Envelope", "emoji": "✉️"}, {"name": "Package", "emoji": "📦"},
                {"name": "Scissors", "emoji": "✂️"}, {"name": "Magnet", "emoji": "🧲"}, {"name": "Microscope", "emoji": "🔬"},
                {"name": "Telescope", "emoji": "🔭"}, {"name": "Light Bulb", "emoji": "💡"}, {"name": "Candle", "emoji": "🕯️"}
            ],
            "type": "identification"
        }
    }

    final_data = {}

    for module_name, data in modules.items():
        questions = []
        
        # Generation Logic
        for i in range(100):
            if data["type"] == "identification":
                # Typical "Identify the X" question
                correct_item = random.choice(data["items"])
                
                # Pick a wrong item that is NOT the same emoji
                wrong_item = random.choice(data["items"])
                while wrong_item["emoji"] == correct_item["emoji"]:
                    wrong_item = random.choice(data["items"])
                    
                # 50/50 chance of order
                is_option_a_correct = random.choice([True, False])
                
                q_obj = {
                    "id": i + 1,
                    "question": f"Select the {correct_item['name']}",
                    "options": [
                        {"id": "a", "content": correct_item["emoji"] if is_option_a_correct else wrong_item["emoji"]},
                        {"id": "b", "content": wrong_item["emoji"] if is_option_a_correct else correct_item["emoji"]}
                    ],
                    "correctAnswer": "a" if is_option_a_correct else "b",
                    "correctContent": correct_item["emoji"],
                    "correctLabel": correct_item['name'] 
                }
                questions.append(q_obj)

            elif data["type"] == "function":
                # Specific questions defined in items
                item = random.choice(data["items"])
                
                # Find a wrong emoji from the same list
                wrong_item = random.choice(data["items"])
                while wrong_item["emoji"] == item["emoji"]:
                    wrong_item = random.choice(data["items"])
                
                is_option_a_correct = random.choice([True, False])
                
                q_obj = {
                    "id": i + 1,
                    "question": item["q"],
                    "options": [
                        {"id": "a", "content": item["emoji"] if is_option_a_correct else wrong_item["emoji"]},
                        {"id": "b", "content": wrong_item["emoji"] if is_option_a_correct else item["emoji"]}
                    ],
                    "correctAnswer": "a" if is_option_a_correct else "b",
                    "correctContent": item["emoji"],
                    "correctLabel": item['name']
                }
                questions.append(q_obj)

            elif data["type"] == "classification":
                # Living vs Non-Living
                target_category = random.choice(["Living", "Non-Living"])
                other_category = "Non-Living" if target_category == "Living" else "Living"
                
                correct_emoji = random.choice(data["subcategories"][target_category])
                wrong_emoji = random.choice(data["subcategories"][other_category])
                
                is_option_a_correct = random.choice([True, False])
                
                q_obj = {
                    "id": i + 1,
                    "question": f"Which one is {target_category}?",
                    "options": [
                        {"id": "a", "content": correct_emoji if is_option_a_correct else wrong_emoji},
                        {"id": "b", "content": wrong_emoji if is_option_a_correct else correct_emoji}
                    ],
                    "correctAnswer": "a" if is_option_a_correct else "b",
                    "correctContent": correct_emoji,
                    "correctLabel": target_category
                }
                questions.append(q_obj)

        final_data[module_name] = questions

    with open("questions.json", "w") as f:
        json.dump(final_data, f, indent=2)
    print("Successfully generated questions.json")

if __name__ == "__main__":
    generate_question_bank()
