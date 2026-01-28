import json
import random

def generate_question_bank():
    print("Generating question bank...")
    
    modules = {
        "Module 1: My Body": {
            "items": [
                {"name": "Eye", "emoji": "👁️", "q": "Which part helps us see?"},
                {"name": "Nose", "emoji": "👃", "q": "Which part helps us smell?"},
                {"name": "Ear", "emoji": "👂", "q": "What do we use to listen to music?"},
                {"name": "Mouth", "emoji": "👄", "q": "Which part helps us speak?"},
                {"name": "Tongue", "emoji": "👅", "q": "Which part helps us taste food?"},
                {"name": "Leg", "emoji": "🦵", "q": "What part of the body helps us in walking?"},
                {"name": "Foot", "emoji": "🦶", "q": "Which part helps us stand?"},
                {"name": "Hand", "emoji": "✋", "q": "What part of the body helps us lift things?"},
                {"name": "Arm", "emoji": "💪", "q": "Which helps us show our strength?"},
                {"name": "Brain", "emoji": "🧠", "q": "Which part helps us think?"},
                {"name": "Heart", "emoji": "🫀", "q": "Which part pumps blood?"},
                {"name": "Teeth", "emoji": "🦷", "q": "What do we use to chew food?"},
                {"name": "Bone", "emoji": "🦴", "q": "Select the Bone"},
                {"name": "Lips", "emoji": "💋", "q": "Select the Lips"}
            ],
            "type": "identification"
        },
        "Module 2: Sense Organs": {
            "items": [
                {"name": "Sight/Seeing", "emoji": "👀", "q": "Which sense organ helps us see?"},
                {"name": "Hearing", "emoji": "👂", "q": "Which sense organ used for listening?"},
                {"name": "Smell", "emoji": "👃", "q": "Which sense organ helps us smell flowers?"},
                {"name": "Taste", "emoji": "👅", "q": "Which sense organ helps us taste food?"},
                {"name": "Touch", "emoji": "✋", "q": "Which helps us feel hot or cold?"}
            ],
            "type": "identification"
        },
        "Module 3: Community Helpers": {
            "items": [
                {"name": "Police Officer", "emoji": "👮", "q": "Who catches thieves?"},
                {"name": "Doctor", "emoji": "👩‍⚕️", "q": "Who treats sick people?"}, 
                {"name": "Firefighter", "emoji": "🧑‍🚒", "q": "Who puts out fires?"},
                {"name": "Chef/Cook", "emoji": "👨‍🍳", "q": "Who cooks food for us?"}, 
                {"name": "Farmer", "emoji": "🧑‍🌾", "q": "Who grows crops?"},
                {"name": "Teacher", "emoji": "👩‍🏫", "q": "Who teaches us in school?"},
                {"name": "Postman", "emoji": "📮", "q": "Who brings letters and parcels?"},
                {"name": "Artist", "emoji": "🎨", "q": "Who paints pictures?"},
                {"name": "Astronaut", "emoji": "🧑‍🚀", "q": "Who goes to space?"},
                {"name": "Construction Worker", "emoji": "👷", "q": "Who builds houses?"},
                {"name": "Detective", "emoji": "🕵️", "q": "Who solves mysteries?"},
                {"name": "Mechanic", "emoji": "👨‍🔧", "q": "Who repairs cars?"},
                {"name": "Scientist", "emoji": "🧑‍🔬", "q": "Who does experiments?"},
                {"name": "Judge", "emoji": "🧑‍⚖️", "q": "Who decides cases in court?"},
                {"name": "Pilot", "emoji": "👨‍✈️", "q": "Who flies the airplane?"}
            ],
            "type": "identification"
        },
        "Module 4: Animal Kingdom": {
            "items": [
                {"name": "Lion", "emoji": "🦁", "q": "Which animal is the king of the jungle?"},
                {"name": "Tiger", "emoji": "🐯", "q": "Select the Tiger"},
                {"name": "Elephant", "emoji": "🐘", "q": "Which animal has a long trunk?"},
                {"name": "Dog", "emoji": "🐶", "q": "Which animal guards our house?"},
                {"name": "Cat", "emoji": "🐱", "q": "Which animal says 'Meow'?"},
                {"name": "Mouse", "emoji": "🐭", "q": "Which animal loves cheese?"},
                {"name": "Rabbit", "emoji": "🐰", "q": "Which animal loves carrots?"},
                {"name": "Fox", "emoji": "🦊", "q": "Select the Fox"},
                {"name": "Bear", "emoji": "🐻", "q": "Select the Bear"},
                {"name": "Panda", "emoji": "🐼", "q": "Select the Panda"},
                {"name": "Cow", "emoji": "🐮", "q": "Which animal gives us milk?"},
                {"name": "Pig", "emoji": "🐷", "q": "Select the Pig"},
                {"name": "Frog", "emoji": "🐸", "q": "Which animal hops and lives in ponds?"},
                {"name": "Monkey", "emoji": "🐵", "q": "Which animal loves bananas?"},
                {"name": "Chicken", "emoji": "🐔", "q": "Which animal gives us eggs?"},
                {"name": "Penguin", "emoji": "🐧", "q": "Which bird cannot fly but swims?"},
                {"name": "Bird", "emoji": "🐦", "q": "Which animal can fly?"},
                {"name": "Duck", "emoji": "🦆", "q": "Which animal says 'Quack'?"},
                {"name": "Owl", "emoji": "🦉", "q": "Which bird is awake at night?"},
                {"name": "Bat", "emoji": "🦇", "q": "Select the Bat"},
                {"name": "Wolf", "emoji": "🐺", "q": "Select the Wolf"},
                {"name": "Horse", "emoji": "🐴", "q": "Select the Horse"},
                {"name": "Unicorn", "emoji": "🦄", "q": "Select the Unicorn"},
                {"name": "Bee", "emoji": "🐝", "q": "Which insect makes honey?"},
                {"name": "Butterfly", "emoji": "🦋", "q": "Select the Butterfly"},
                {"name": "Ladybug", "emoji": "🐞", "q": "Select the Ladybug"},
                {"name": "Snake", "emoji": "🐍", "q": "Select the Snake"},
                {"name": "Turtle", "emoji": "🐢", "q": "Which animal moves very slowly?"},
                {"name": "Whale", "emoji": "🐳", "q": "Which is the largest animal in the sea?"},
                {"name": "Dolphin", "emoji": "🐬", "q": "Select the Dolphin"},
                {"name": "Fish", "emoji": "🐟", "q": "Which animal lives in water?"},
                {"name": "Octopus", "emoji": "🐙", "q": "Select the Octopus"},
                {"name": "Crab", "emoji": "🦀", "q": "Select the Crab"},
                {"name": "Shark", "emoji": "🦈", "q": "Select the Shark"},
                {"name": "Snail", "emoji": "🐌", "q": "Select the Snail"},
                {"name": "Ant", "emoji": "🐜", "q": "Select the Ant"}
            ],
            "type": "identification"
        },
        "Module 5: Plant Life": {
            "items": [
                {"name": "Tree", "emoji": "🌳", "q": "Select the Tree"},
                {"name": "Pine Tree", "emoji": "🌲", "q": "Select the Pine Tree"},
                {"name": "Cactus", "emoji": "🌵", "q": "Which plant grows in the desert?"},
                {"name": "Flower", "emoji": "🌺", "q": "Select the Flower"},
                {"name": "Rose", "emoji": "🌹", "q": "Which flower protects itself with thorns?"},
                {"name": "Sunflower", "emoji": "🌻", "q": "Which flower looks towards the sun?"},
                {"name": "Tulip", "emoji": "🌷", "q": "Select the Tulip"},
                {"name": "Leaf", "emoji": "🍃", "q": "Select the Leaf"},
                {"name": "Seedling", "emoji": "🌱", "q": "Select the Seedling"},
                {"name": "Herb", "emoji": "🌿", "q": "Select the Herb"},
                {"name": "Mushroom", "emoji": "🍄", "q": "Select the Mushroom"},
                {"name": "Palm Tree", "emoji": "🌴", "q": "Select the Palm Tree"},
                {"name": "Apple", "emoji": "🍎", "q": "Which fruit keeps the doctor away?"},
                {"name": "Grapes", "emoji": "🍇", "q": "Select the Grapes"},
                {"name": "Watermelon", "emoji": "🍉", "q": "Select the Watermelon"},
                {"name": "Strawberry", "emoji": "🍓", "q": "Select the Strawberry"},
                {"name": "Carrot", "emoji": "🥕", "q": "Which vegetable is orange and good for eyes?"},
                {"name": "Corn", "emoji": "🌽", "q": "Select the Corn"}
            ],
            "type": "identification"
        },
        "Module 6: Transport": {
            "items": [
                {"name": "Car", "emoji": "🚗", "q": "Which vehicle has 4 wheels?"},
                {"name": "Taxi", "emoji": "🚕", "q": "Select the Taxi"},
                {"name": "Bus", "emoji": "🚌", "q": "Which vehicle carries many people to school?"},
                {"name": "Police Car", "emoji": "🚓", "q": "Which car chases bad guys?"},
                {"name": "Ambulance", "emoji": "🚑", "q": "Which vehicle takes sick people to hospital?"},
                {"name": "Fire Truck", "emoji": "🚒", "q": "Which vehicle carries water to fight fire?"},
                {"name": "Bicycle", "emoji": "🚲", "q": "Which vehicle has 2 wheels and no engine?"},
                {"name": "Motorcycle", "emoji": "🏍️", "q": "Select the Motorcycle"},
                {"name": "Scooter", "emoji": "🛴", "q": "Select the Scooter"},
                {"name": "Train", "emoji": "🚂", "q": "Which vehicle runs on tracks?"},
                {"name": "Bullet Train", "emoji": "🚄", "q": "Select the Bullet Train"},
                {"name": "Airplane", "emoji": "✈️", "q": "Which vehicle flies in the sky?"},
                {"name": "Helicopter", "emoji": "🚁", "q": "Select the Helicopter"},
                {"name": "Rocket", "emoji": "🚀", "q": "Which vehicle goes to space?"},
                {"name": "Ship", "emoji": "🚢", "q": "Which vehicle sails on the ocean?"},
                {"name": "Boat", "emoji": "⛵", "q": "Select the Boat"},
                {"name": "Canoe", "emoji": "🛶", "q": "Select the Canoe"},
                {"name": "Tractor", "emoji": "🚜", "q": "Which vehicle works on a farm?"},
                {"name": "Truck", "emoji": "🚚", "q": "Which vehicle carries heavy loads?"}
            ],
            "type": "identification"
        },
        "Module 7: Weather & Seasons": {
            "items": [
                {"name": "Sun/Sunny", "emoji": "☀️", "q": "What do we see in the sky during the day?"},
                {"name": "Cloud/Cloudy", "emoji": "☁️", "q": "Select the Cloud"},
                {"name": "Rain/Rainy", "emoji": "🌧️", "q": "What falls from the cloud?"},
                {"name": "Full Moon", "emoji": "🌕", "q": "What do we see at night?"},
                {"name": "Crescent Moon", "emoji": "🌙", "q": "Select the Crescent Moon"},
                {"name": "Star", "emoji": "⭐", "q": "What twinkles at night?"},
                {"name": "Thunderstorm", "emoji": "⛈️", "q": "Select the Thunderstorm"},
                {"name": "Snow/Snowy", "emoji": "❄️", "q": "What falls in winter?"},
                {"name": "Wind/Windy", "emoji": "🌬️", "q": "Select the Wind"},
                {"name": "Rainbow", "emoji": "🌈", "q": "What has 7 colors?"},
                {"name": "Umbrella", "emoji": "☂️", "q": "What do we use when it rains?"},
                {"name": "Snowman", "emoji": "☃️", "q": "What do we build with snow?"},
                {"name": "Summer (Sunglasses)", "emoji": "🕶️", "q": "What do we wear when it's sunny?"},
                {"name": "Winter (Scarf)", "emoji": "🧣", "q": "What do we wear when it's cold?"},
                {"name": "Fire", "emoji": "🔥", "q": "Which gives us heat?"},
                {"name": "Droplet", "emoji": "💧", "q": "Select the Droplet"}
            ],
            "type": "identification"
        },
        "Module 8: Good Manners & Safety": {
            "items": [
                {"name": "Good / Correct", "emoji": "✅", "q": "Which symbol means Correct?"},
                {"name": "Bad / Wrong", "emoji": "❌", "q": "Which symbol means Wrong?"},
                {"name": "Trash in Bin", "emoji": "🚮", "q": "Where should we throw trash?"},
                {"name": "No Littering", "emoji": "🚯", "q": "Which sign says No Littering?"},
                {"name": "Traffic Light", "emoji": "🚦", "q": "What controls traffic on the road?"},
                {"name": "Wash Hands", "emoji": "🧼", "q": "What should we do before eating?"},
                {"name": "Handshake", "emoji": "🤝", "q": "How do we greet friends?"},
                {"name": "Toilets", "emoji": "🚻", "q": "Select the Restroom sign"},
                {"name": "Wheelchair Access", "emoji": "♿", "q": "Select the Wheelchair symbol"},
                {"name": "Quiet", "emoji": "🤫", "q": "Which sign means 'Be Quiet'?"},
                {"name": "Recycle", "emoji": "♻️", "q": "Select the Recycle sign"},
                {"name": "Stop Sign", "emoji": "🛑", "q": "Which sign tells cars to stop?"},
                {"name": "Crossing", "emoji": "🚸", "q": "Where should we cross the road?"},
                {"name": "Warning", "emoji": "⚠️", "q": "Select the Warning sign"}
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
        "Module 10: My Home & Objects": {
            "items": [
                {"name": "Chair", "emoji": "🪑", "q": "Select the Chair"},
                {"name": "Bedroom", "emoji": "🛏️", "q": "Where do we sleep at night?"},
                {"name": "Door", "emoji": "🚪", "q": "What do we open to enter a room?"},
                {"name": "Key", "emoji": "🔑", "q": "What do we use to lock the door?"},
                {"name": "Hammer", "emoji": "🔨", "q": "What do we use to hit a nail?"},
                {"name": "Spoon", "emoji": "🥄", "q": "What do we use to eat soup?"},
                {"name": "Balloon", "emoji": "🎈", "q": "Select the Balloon"},
                {"name": "Book", "emoji": "📖", "q": "What do we read?"},
                {"name": "Pencil", "emoji": "✏️", "q": "What do we use to write?"},
                {"name": "Shirt", "emoji": "👕", "q": "Select the Shirt"},
                {"name": "Shoe", "emoji": "👞", "q": "What do we wear on our feet?"},
                {"name": "Glasses", "emoji": "👓", "q": "What helps us see better?"},
                {"name": "Watch", "emoji": "⌚", "q": "What shows us time?"},
                {"name": "Camera", "emoji": "📷", "q": "What do we use to take photos?"},
                {"name": "Computer", "emoji": "💻", "q": "Select the Computer"},
                {"name": "Phone", "emoji": "📱", "q": "What do we use to call someone?"},
                {"name": "Envelope", "emoji": "✉️", "q": "What holds a letter?"},
                {"name": "Package", "emoji": "📦", "q": "Select the Package"},
                {"name": "Scissors", "emoji": "✂️", "q": "What do we use to cut paper?"},
                {"name": "Magnet", "emoji": "🧲", "q": "Select the Magnet"},
                {"name": "Microscope", "emoji": "🔬", "q": "Select the Microscope"},
                {"name": "Telescope", "emoji": "🔭", "q": "What do we use to see stars?"},
                {"name": "Light Bulb", "emoji": "💡", "q": "What gives us light?"},
                {"name": "Candle", "emoji": "🕯️", "q": "Select the Candle"},
                {"name": "TV", "emoji": "📺", "q": "What do we watch cartons on?"},
                {"name": "Cupboard", "emoji": "🚪", "q": "Where do we keep our clothes?"},
                {"name": "Stairs", "emoji": "🪜", "q": "What do we use to go upstairs?"}
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
                # Typical "Identify the X" question OR specific "q"
                correct_item = random.choice(data["items"])
                
                # Pick a wrong item that is NOT the same emoji
                wrong_item = random.choice(data["items"])
                while wrong_item["emoji"] == correct_item["emoji"]:
                    wrong_item = random.choice(data["items"])
                    
                # 50/50 chance of order
                is_option_a_correct = random.choice([True, False])
                
                # Use custom question if available, else default
                question_text = correct_item.get("q", f"Select the {correct_item['name']}")

                q_obj = {
                    "id": i + 1,
                    "question": question_text,
                    "options": [
                        {"id": "a", "content": correct_item["emoji"] if is_option_a_correct else wrong_item["emoji"]},
                        {"id": "b", "content": wrong_item["emoji"] if is_option_a_correct else correct_item["emoji"]}
                    ],
                    "correctAnswer": "a" if is_option_a_correct else "b",
                    "correctContent": correct_item["emoji"],
                    "correctLabel": correct_item['name'] 
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
