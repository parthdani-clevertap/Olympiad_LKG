import json
import random

def generate_question_bank():
    print("Generating question bank...")
    
    modules = {
        "Module 1: My Body": {
            "items": [
                {
                    "name": "Eye", 
                    "emoji": "👁️", 
                    "questions": [
                        "Which part helps us see?",
                        "What do we use to watch cartoons?",
                        "Identify the organ that helps you see colors.",
                        "If you close this, everything turns dark. What is it?"
                    ]
                },
                {
                    "name": "Nose", 
                    "emoji": "👃", 
                    "questions": [
                        "Which part helps us smell?",
                        "What do we use to breathe air?",
                        "Which part helps us smell a flower?",
                        "I am on your face and I help you smell. What am I?"
                    ]
                },
                {
                    "name": "Ear", 
                    "emoji": "👂", 
                    "questions": [
                        "What do we use to listen to music?",
                        "Which part helps us hear sounds?",
                        "Identify the organ that helps you hear a bell ringing.",
                        "I help you hear your favorite song. What am I?"
                    ]
                },
                {
                    "name": "Mouth", 
                    "emoji": "👄", 
                    "questions": [
                        "Which part helps us speak?",
                        "What do we use to eat food?",
                        "I help you smile and talk. What am I?",
                        "Open wide! What part is this?"
                    ]
                },
                {
                    "name": "Tongue", 
                    "emoji": "👅", 
                    "questions": [
                        "Which part helps us taste food?",
                        "What helps us lick an ice cream?",
                        "I am inside your mouth and help you taste. What am I?",
                        "Without me, you wouldn't know if a lemon is sour."
                    ]
                },
                {
                    "name": "Leg", 
                    "emoji": "🦵", 
                    "questions": [
                        "What part of the body helps us in walking?",
                        "Which part helps us jump and run?",
                        "Select the leg.",
                        "I help you kick a ball. What am I?"
                    ]
                },
                {
                    "name": "Foot", 
                    "emoji": "🦶", 
                    "questions": [
                        "Which part helps us stand?",
                        "What do we put a shoe on?",
                        "Select the foot.",
                        "I am at the bottom of your leg. What am I?"
                    ]
                },
                {
                    "name": "Hand", 
                    "emoji": "✋", 
                    "questions": [
                        "What part of the body helps us lift things?",
                        "What do we use to clap?",
                        "Which part has five fingers?",
                        "I help you hold a pencil. What am I?"
                    ]
                },
                {
                    "name": "Arm", 
                    "emoji": "💪", 
                    "questions": [
                        "Which helps us show our strength?",
                        "Select the arm.",
                        "I connect your hand to your shoulder."
                    ]
                },
                {
                    "name": "Brain", 
                    "emoji": "🧠", 
                    "questions": [
                        "Which part helps us think?",
                        "What helps us solve puzzles?",
                        "I am inside your head and I help you learn. What am I?",
                        "Who is the boss of the body?"
                    ]
                },
                {
                    "name": "Heart", 
                    "emoji": "🫀", 
                    "questions": [
                        "Which part pumps blood?",
                        "What beats faster when we run?",
                        "I go thud-thud inside your chest.",
                        "Select the heart."
                    ]
                },
                {
                    "name": "Teeth", 
                    "emoji": "🦷", 
                    "questions": [
                        "What do we use to chew food?",
                        "What should we brush twice a day?",
                        "I am white and I help you bite an apple.",
                        "Select the teeth."
                    ]
                },
                {
                    "name": "Bone", 
                    "emoji": "🦴", 
                    "questions": [
                        "Select the Bone",
                        "I am hard and white. I make up your skeleton.",
                        "Dogs love to chew on me."
                    ]
                },
                {
                    "name": "Lips", 
                    "emoji": "💋", 
                    "questions": [
                        "Select the Lips",
                        "We are two and we help you kiss.",
                        "What do you put lipstick on?"
                    ]
                }
            ],
            "type": "identification"
        },
        "Module 2: Sense Organs": {
            "items": [
                {
                    "name": "Sight/Seeing", 
                    "emoji": "👀", 
                    "questions": [
                        "Which sense organ helps us see?",
                        "Which sense do we use to watch a movie?",
                        "I help you see the colorful rainbow."
                    ]
                },
                {
                    "name": "Hearing", 
                    "emoji": "👂", 
                    "questions": [
                        "Which sense organ used for listening?",
                        "Which sense helps us hear music?",
                        "I help you hear a dog bark."
                    ]
                },
                {
                    "name": "Smell", 
                    "emoji": "👃", 
                    "questions": [
                        "Which sense organ helps us smell flowers?",
                        "Which sense tells you that cookies are baking?",
                        "I help you smell a stinky sock."
                    ]
                },
                {
                    "name": "Taste", 
                    "emoji": "👅", 
                    "questions": [
                        "Which sense organ helps us taste food?",
                        "Which sense tells you if candy is sweet?",
                        "I help you enjoy a yummy pizza."
                    ]
                },
                {
                    "name": "Touch", 
                    "emoji": "✋", 
                    "questions": [
                        "Which helps us feel hot or cold?",
                        "Which sense helps you feel a soft teddy bear?",
                        "I help you feel if a rock is rough."
                    ]
                }
            ],
            "type": "identification"
        },
        "Module 3: Community Helpers": {
            "items": [
                {"name": "Police Officer", "emoji": "👮", "questions": ["Who catches thieves?", "Who keeps our city safe?", "Who drives a car with a siren?"]},
                {"name": "Doctor", "emoji": "👩‍⚕️", "questions": ["Who treats sick people?", "Who works in a hospital?", "Who uses a stethoscope?"]}, 
                {"name": "Firefighter", "emoji": "🧑‍🚒", "questions": ["Who puts out fires?", "Who drives a big red truck?", "Who saves people from burning buildings?"]},
                {"name": "Chef/Cook", "emoji": "👨‍🍳", "questions": ["Who cooks food for us?", "Who makes yummy meals in a restaurant?", "Who wears a tall white hat?"]}, 
                {"name": "Farmer", "emoji": "🧑‍🌾", "questions": ["Who grows crops?", "Who provides us with vegetables and fruits?", "Who works in the fields?"]},
                {"name": "Teacher", "emoji": "👩‍🏫", "questions": ["Who teaches us in school?", "Who helps us learn new things?", "Who writes on the blackboard?"]},
                {"name": "Postman", "emoji": "📮", "questions": ["Who brings letters and parcels?", "Who delivers your mail?", "Who wears a uniform and carries a bag of letters?"]},
                {"name": "Artist", "emoji": "🎨", "questions": ["Who paints pictures?", "Who creates beautiful art?", "Who uses a brush and colors?"]},
                {"name": "Astronaut", "emoji": "🧑‍🚀", "questions": ["Who goes to space?", "Who travels in a rocket?", "Who walks on the moon?"]},
                {"name": "Construction Worker", "emoji": "👷", "questions": ["Who builds houses?", "Who wears a hard hat and builds buildings?", "Who uses bricks and cement?"]},
                {"name": "Detective", "emoji": "🕵️", "questions": ["Who solves mysteries?", "Who looks for clues with a magnifying glass?", "Who finds lost things?"]},
                {"name": "Mechanic", "emoji": "👨‍🔧", "questions": ["Who repairs cars?", "Who fixes broken vehicles?", "Who uses a wrench to fix engines?"]},
                {"name": "Scientist", "emoji": "🧑‍🔬", "questions": ["Who does experiments?", "Who works in a lab?", "Who discovers new things via science?"]},
                {"name": "Judge", "emoji": "🧑‍⚖️", "questions": ["Who decides cases in court?", "Who uses a gavel (hammer) in court?", "Who makes sure laws are followed?"]},
                {"name": "Pilot", "emoji": "👨‍✈️", "questions": ["Who flies the airplane?", "Who takes us to different countries by air?", "Who sits in the cockpit?"]}
            ],
            "type": "identification"
        },
        "Module 4: Animal Kingdom": {
            "items": [
                {"name": "Lion", "emoji": "🦁", "questions": ["Which animal is the king of the jungle?", "I have a big mane and I roar. Who am I?", "I am a big cat who rules the forest."]},
                {"name": "Tiger", "emoji": "🐯", "questions": ["Select the Tiger", "I have orange fur with black stripes. Who am I?", "I am the national animal of India."]},
                {"name": "Elephant", "emoji": "🐘", "questions": ["Which animal has a long trunk?", "I am the largest land animal and I have big ears.", "I have tusks and a trunk. Who am I?"]},
                {"name": "Dog", "emoji": "🐶", "questions": ["Which animal guards our house?", "I am man's best friend. Who am I?", "I bark and wag my tail."]},
                {"name": "Cat", "emoji": "🐱", "questions": ["Which animal says 'Meow'?", "I like to chase mice and drink milk.", "I have whiskers and I purr."]},
                {"name": "Mouse", "emoji": "🐭", "questions": ["Which animal loves cheese?", "I am small and I squeak.", "Tom the cat is always chasing me."]},
                {"name": "Rabbit", "emoji": "🐰", "questions": ["Which animal loves carrots?", "I have long ears and I hop.", "I live in a burrow and love veggies."]},
                {"name": "Fox", "emoji": "🦊", "questions": ["Select the Fox", "I am clever and cunning.", "I look like a dog but I live in the wild."]},
                {"name": "Bear", "emoji": "🐻", "questions": ["Select the Bear", "I love honey and I sleep all winter.", "I am big and furry."]},
                {"name": "Panda", "emoji": "🐼", "questions": ["Select the Panda", "I am black and white and love bamboo.", "I look like a bear but I am very cute."]},
                {"name": "Cow", "emoji": "🐮", "questions": ["Which animal gives us milk?", "I say 'Moo' and eat grass.", "Farmers keep me for milk."]},
                {"name": "Pig", "emoji": "🐷", "questions": ["Select the Pig", "I like to roll in the mud.", "I say 'Oink Oink'."]},
                {"name": "Frog", "emoji": "🐸", "questions": ["Which animal hops and lives in ponds?", "I am green and I say 'Croak'.", "I start as a tadpole."]},
                {"name": "Monkey", "emoji": "🐵", "questions": ["Which animal loves bananas?", "I swing from trees and have a long tail.", "I am very naughty and playful."]},
                {"name": "Chicken", "emoji": "🐔", "questions": ["Which animal gives us eggs?", "I say 'Cluck Cluck'.", "I live in a coop."]},
                {"name": "Penguin", "emoji": "🐧", "questions": ["Which bird cannot fly but swims?", "I live in the cold snow and waddle.", "I am a black and white bird."]},
                {"name": "Bird", "emoji": "🐦", "questions": ["Which animal can fly?", "I have wings and a beak.", "I lay eggs in a nest."]},
                {"name": "Duck", "emoji": "🦆", "questions": ["Which animal says 'Quack'?", "I swim in the pond and have webbed feet.", "I am a water bird."]},
                {"name": "Owl", "emoji": "🦉", "questions": ["Which bird is awake at night?", "I say 'Hoot Hoot'.", "I have big eyes and hunt at night."]},
                {"name": "Bat", "emoji": "🦇", "questions": ["Select the Bat", "I sleep upside down.", "I fly at night but I am not a bird."]},
                {"name": "Wolf", "emoji": "🐺", "questions": ["Select the Wolf", "I howl at the moon.", "I look like a wild dog."]},
                {"name": "Horse", "emoji": "🐴", "questions": ["Select the Horse", "I can run very fast and people ride me.", "I live in a stable and eat hay."]},
                {"name": "Unicorn", "emoji": "🦄", "questions": ["Select the Unicorn", "I am a magical horse with one horn.", "I can fly in fairytales."]},
                {"name": "Bee", "emoji": "🐝", "questions": ["Which insect makes honey?", "I buzz and visit flowers.", "I have black and yellow stripes."]},
                {"name": "Butterfly", "emoji": "🦋", "questions": ["Select the Butterfly", "I was a caterpillar before.", "I have colorful wings."]},
                {"name": "Ladybug", "emoji": "🐞", "questions": ["Select the Ladybug", "I am a small red beetle with black spots.", "I am a lucky insect."]},
                {"name": "Snake", "emoji": "🐍", "questions": ["Select the Snake", "I have no legs and I slither.", "I say 'Hiss'."]},
                {"name": "Turtle", "emoji": "🐢", "questions": ["Which animal moves very slowly?", "I carry my house on my back.", "I have a hard shell."]},
                {"name": "Whale", "emoji": "🐳", "questions": ["Which is the largest animal in the sea?", "I blow water from my head.", "I am the biggest mammal in the ocean."]},
                {"name": "Dolphin", "emoji": "🐬", "questions": ["Select the Dolphin", "I swim in the sea and jump high.", "I am very smart and friendly."]},
                {"name": "Fish", "emoji": "🐟", "questions": ["Which animal lives in water?", "I have gills to breathe underwater.", "I swim with my fins."]},
                {"name": "Octopus", "emoji": "🐙", "questions": ["Select the Octopus", "I have eight arms.", "I shoot ink to hide."]},
                {"name": "Crab", "emoji": "🦀", "questions": ["Select the Crab", "I walk sideways.", "I have two sharp claws."]},
                {"name": "Shark", "emoji": "🦈", "questions": ["Select the Shark", "I have sharp teeth and a fin on my back.", "I am a scary fish."]},
                {"name": "Snail", "emoji": "🐌", "questions": ["Select the Snail", "I move slowly and leave a slime trail.", "I carry a spiral shell."]},
                {"name": "Ant", "emoji": "🐜", "questions": ["Select the Ant", "I am tiny but very strong.", "I live in a colony."]}
            ],
            "type": "identification"
        },
        "Module 5: Plant Life": {
            "items": [
                {"name": "Tree", "emoji": "🌳", "questions": ["Select the Tree", "I am tall and have a trunk.", "birds build nests on me."]},
                {"name": "Pine Tree", "emoji": "🌲", "questions": ["Select the Pine Tree", "I am a Christmas tree.", "I stay green all year long."]},
                {"name": "Cactus", "emoji": "🌵", "questions": ["Which plant grows in the desert?", "I have thorns and need very little water.", "I am prickly."]},
                {"name": "Flower", "emoji": "🌺", "questions": ["Select the Flower", "I am colorful and smell nice.", "Bees love me."]},
                {"name": "Rose", "emoji": "🌹", "questions": ["Which flower protects itself with thorns?", "I am red and represent love.", "I smell beautiful but be careful of my thorns."]},
                {"name": "Sunflower", "emoji": "🌻", "questions": ["Which flower looks towards the sun?", "I am yellow and tall.", "I produce seeds you can eat."]},
                {"name": "Tulip", "emoji": "🌷", "questions": ["Select the Tulip", "I come in many colors and bloom in spring.", "I am a cup-shaped flower."]},
                {"name": "Leaf", "emoji": "🍃", "questions": ["Select the Leaf", "I grow on branches and make food for the tree.", "I turn brown and fall in autumn."]},
                {"name": "Seedling", "emoji": "🌱", "questions": ["Select the Seedling", "I am a baby plant.", "I just came out of a seed."]},
                {"name": "Herb", "emoji": "🌿", "questions": ["Select the Herb", "I am used to adding flavor to food.", "Mint and Basil are my friends."]},
                {"name": "Mushroom", "emoji": "🍄", "questions": ["Select the Mushroom", "I am not a plant but a fungus.", "I have a cap and a stem."]},
                {"name": "Palm Tree", "emoji": "🌴", "questions": ["Select the Palm Tree", "I grow on the beach.", "I have Coconuts."]},
                {"name": "Apple", "emoji": "🍎", "questions": ["Which fruit keeps the doctor away?", "I am red and crunchy.", "Snow White ate a poisoned one."]},
                {"name": "Grapes", "emoji": "🍇", "questions": ["Select the Grapes", "We grow in bunches on vines.", "We can be green or purple."]},
                {"name": "Watermelon", "emoji": "🍉", "questions": ["Select the Watermelon", "I am green outside and red inside.", "I am a big summer fruit."]},
                {"name": "Strawberry", "emoji": "🍓", "questions": ["Select the Strawberry", "I am red with tiny seeds on the outside.", "I am sweet and small."]},
                {"name": "Carrot", "emoji": "🥕", "questions": ["Which vegetable is orange and good for eyes?", "Rabbits love to eat me.", "I grow underground."]},
                {"name": "Corn", "emoji": "🌽", "questions": ["Select the Corn", "I have yellow kernels.", "You can pop me to make popcorn."]}
            ],
            "type": "identification"
        },
        "Module 6: Transport": {
            "items": [
                {"name": "Car", "emoji": "🚗", "questions": ["Which vehicle has 4 wheels?", "I run on the road and carry a family.", "I have a steering wheel."]},
                {"name": "Taxi", "emoji": "🚕", "questions": ["Select the Taxi", "I am a yellow car you pay to ride.", "I take you where you want to go for money."]},
                {"name": "Bus", "emoji": "🚌", "questions": ["Which vehicle carries many people to school?", "I am big and can carry many passengers.", "I stop at designated stops."]},
                {"name": "Police Car", "emoji": "🚓", "questions": ["Which car chases bad guys?", "I have a siren and red-blue lights.", "I help the police."]},
                {"name": "Ambulance", "emoji": "🚑", "questions": ["Which vehicle takes sick people to hospital?", "I have a loud siren and carry doctors.", "Call me for emergencies."]},
                {"name": "Fire Truck", "emoji": "🚒", "questions": ["Which vehicle carries water to fight fire?", "I am red and have a loud siren.", "I carry firefighters."]},
                {"name": "Bicycle", "emoji": "🚲", "questions": ["Which vehicle has 2 wheels and no engine?", "You have to pedal me to move.", "I am good for exercise."]},
                {"name": "Motorcycle", "emoji": "🏍️", "questions": ["Select the Motorcycle", "I have two wheels and an engine.", "You need a helmet to ride me."]},
                {"name": "Scooter", "emoji": "🛴", "questions": ["Select the Scooter", "You push me with your foot.", "I have two small wheels and a handle."]},
                {"name": "Train", "emoji": "🚂", "questions": ["Which vehicle runs on tracks?", "I say 'Choo Choo'.", "I have many carriages linked together."]},
                {"name": "Bullet Train", "emoji": "🚄", "questions": ["Select the Bullet Train", "I am very fast and look futuristic.", "I run on special tracks."]},
                {"name": "Airplane", "emoji": "✈️", "questions": ["Which vehicle flies in the sky?", "I have wings and jet engines.", "I take you to far away places quickly."]},
                {"name": "Helicopter", "emoji": "🚁", "questions": ["Select the Helicopter", "I have rotors on top to fly.", "I can take off vertically."]},
                {"name": "Rocket", "emoji": "🚀", "questions": ["Which vehicle goes to space?", "I blast off with fire.", "I take astronauts to the moon."]},
                {"name": "Ship", "emoji": "🚢", "questions": ["Which vehicle sails on the ocean?", "I am a very big boat.", "I carry cargo across the sea."]},
                {"name": "Boat", "emoji": "⛵", "questions": ["Select the Boat", "I float on water.", "You can row me or sail me."]},
                {"name": "Canoe", "emoji": "🛶", "questions": ["Select the Canoe", "I am a narrow boat.", "You paddle me."]},
                {"name": "Tractor", "emoji": "🚜", "questions": ["Which vehicle works on a farm?", "I have big back tires.", "I pull plows in the field."]},
                {"name": "Truck", "emoji": "🚚", "questions": ["Which vehicle carries heavy loads?", "I transport goods on the highway.", "I am big and strong."]}
            ],
            "type": "identification"
        },
        "Module 7: Weather & Seasons": {
            "items": [
                {"name": "Sun/Sunny", "emoji": "☀️", "questions": ["What do we see in the sky during the day?", "I give you light and heat.", "I am a big hot star."]},
                {"name": "Cloud/Cloudy", "emoji": "☁️", "questions": ["Select the Cloud", "I am white and fluffy in the sky.", "I can hide the sun."]},
                {"name": "Rain/Rainy", "emoji": "🌧️", "questions": ["What falls from the cloud?", "You need an umbrella when I am here.", "I make puddles."]},
                {"name": "Full Moon", "emoji": "🌕", "questions": ["What do we see at night?", "I am round and bright in the night sky.", "Wolves howl at me."]},
                {"name": "Crescent Moon", "emoji": "🌙", "questions": ["Select the Crescent Moon", "I look like a banana in the sky.", "I am not full."]},
                {"name": "Star", "emoji": "⭐", "questions": ["What twinkles at night?", "We are tiny dots of light in the night sky.", "Twinkle Twinkle little..."]},
                {"name": "Thunderstorm", "emoji": "⛈️", "questions": ["Select the Thunderstorm", "I am loud and scary.", "I have lightning and thunder."]},
                {"name": "Snow/Snowy", "emoji": "❄️", "questions": ["What falls in winter?", "I am cold and white.", "You can make a snowman with me."]},
                {"name": "Wind/Windy", "emoji": "🌬️", "questions": ["Select the Wind", "I blow leaves around.", "You cannot see me but you can feel me."]},
                {"name": "Rainbow", "emoji": "🌈", "questions": ["What has 7 colors?", "I appear after rain when the sun shines.", "I am a colorful arch in the sky."]},
                {"name": "Umbrella", "emoji": "☂️", "questions": ["What do we use when it rains?", "I keep you dry.", "Open me when it rains."]},
                {"name": "Snowman", "emoji": "☃️", "questions": ["What do we build with snow?", "I have a carrot nose.", "Frosty is my name."]},
                {"name": "Summer (Sunglasses)", "emoji": "🕶️", "questions": ["What do we wear when it's sunny?", "Protect your eyes from the sun.", "Cool shades for summer."]},
                {"name": "Winter (Scarf)", "emoji": "🧣", "questions": ["What do we wear when it's cold?", "Wrap me around your neck.", "I keep you warm in winter."]},
                {"name": "Fire", "emoji": "🔥", "questions": ["Which gives us heat?", "I am hot and dangerous.", "Don't touch me!"]},
                {"name": "Droplet", "emoji": "💧", "questions": ["Select the Droplet", "I am a small drop of water.", "I fall as rain."]}
            ],
            "type": "identification"
        },
        "Module 8: Good Manners & Safety": {
            "items": [
                {"name": "Good / Correct", "emoji": "✅", "questions": ["Which symbol means Correct?", "Select the check mark.", "This means Yes or Good."]},
                {"name": "Bad / Wrong", "emoji": "❌", "questions": ["Which symbol means Wrong?", "Select the cross mark.", "This means No or Stop."]},
                {"name": "Trash in Bin", "emoji": "🚮", "questions": ["Where should we throw trash?", "Keep our city clean.", "Put waste here."]},
                {"name": "No Littering", "emoji": "🚯", "questions": ["Which sign says No Littering?", "Do not throw trash on the ground.", "Keep nature clean."]},
                {"name": "Traffic Light", "emoji": "🚦", "questions": ["What controls traffic on the road?", "Red means Stop, Green means Go.", "I have three colors."]},
                {"name": "Wash Hands", "emoji": "🧼", "questions": ["What should we do before eating?", "Kill germs with soap.", "Keep your hands clean."]},
                {"name": "Handshake", "emoji": "🤝", "questions": ["How do we greet friends?", "Nice to meet you.", "Shake hands."]},
                {"name": "Toilets", "emoji": "🚻", "questions": ["Select the Restroom sign", "Where do you go to pee?", "Boy and Girl sign."]},
                {"name": "Wheelchair Access", "emoji": "♿", "questions": ["Select the Wheelchair symbol", "Reserved for disabled people.", "Accessibility sign."]},
                {"name": "Quiet", "emoji": "🤫", "questions": ["Which sign means 'Be Quiet'?", "Shhh!", "Silence please."]},
                {"name": "Recycle", "emoji": "♻️", "questions": ["Select the Recycle sign", "Reduce, Reuse, Recycle.", "Green arrows going in a circle."]},
                {"name": "Stop Sign", "emoji": "🛑", "questions": ["Which sign tells cars to stop?", "It is red and has 8 sides.", "STOP."]},
                {"name": "Crossing", "emoji": "🚸", "questions": ["Where should we cross the road?", "School crossing ahead.", "Watch out for children."]},
                {"name": "Warning", "emoji": "⚠️", "questions": ["Select the Warning sign", "Be careful!", "Danger ahead."]}
            ],
            "type": "identification"
        },
        "Module 9: Living & Non-Living": {
            "questions": ["Which one is [TARGET]?", "Identify the [TARGET] thing.", "Find the object that is [TARGET]."],
            "subcategories": {
                "Living": ["👶", "👧", "👨", "👩", "🐶", "🐱", "🦁", "🐟", "🐝", "🌲", "🌹", "🐌"],
                "Non-Living": ["🪑", "🧸", "📺", "🚗", "📱", "⌚", "🖊️", "🎸", "🥣", "🥪", "🏠", "💎"]
            },
            "type": "classification"
        },
        "Module 10: My Home & Objects": {
            "items": [
                {"name": "Chair", "emoji": "🪑", "questions": ["Select the Chair", "I have four legs and a back.", "You sit on me."]},
                {"name": "Bedroom", "emoji": "🛏️", "questions": ["Where do we sleep at night?", "This is a bed.", "I have a pillow and blanket."]},
                {"name": "Door", "emoji": "🚪", "questions": ["What do we open to enter a room?", "Knock knock!", "Close me for privacy."]},
                {"name": "Key", "emoji": "🔑", "questions": ["What do we use to lock the door?", "I unlock things.", "I am small and metal."]},
                {"name": "Hammer", "emoji": "🔨", "questions": ["What do we use to hit a nail?", "I bang things.", "Construction tool."]},
                {"name": "Spoon", "emoji": "🥄", "questions": ["What do we use to eat soup?", "I am not a fork.", "I scoop food."]},
                {"name": "Balloon", "emoji": "🎈", "questions": ["Select the Balloon", "I float and can pop!", "Happy Birthday decoration."]},
                {"name": "Book", "emoji": "📖", "questions": ["What do we read?", "I have pages and stories.", "Learn from me."]},
                {"name": "Pencil", "emoji": "✏️", "questions": ["What do we use to write?", "I have an eraser on top.", "Sharpen me to write."]},
                {"name": "Shirt", "emoji": "👕", "questions": ["Select the Shirt", "You wear me on your body.", "I have sleeves."]},
                {"name": "Shoe", "emoji": "👞", "questions": ["What do we wear on our feet?", "Tie your laces.", "Walk in me."]},
                {"name": "Glasses", "emoji": "👓", "questions": ["What helps us see better?", "You wear me on your eyes.", "Spectacles."]},
                {"name": "Watch", "emoji": "⌚", "questions": ["What shows us time?", "Wear me on your wrist.", "Tick tock."]},
                {"name": "Camera", "emoji": "📷", "questions": ["What do we use to take photos?", "Smile!", "Click click."]},
                {"name": "Computer", "emoji": "💻", "questions": ["Select the Computer", "I have a screen and keyboard.", "laptop."]},
                {"name": "Phone", "emoji": "📱", "questions": ["What do we use to call someone?", "Hello?", "Mobile phone."]},
                {"name": "Envelope", "emoji": "✉️", "questions": ["What holds a letter?", "Put a stamp on me.", "Mail me."]},
                {"name": "Package", "emoji": "📦", "questions": ["Select the Package", "A box in the mail.", "Delivery!"]},
                {"name": "Scissors", "emoji": "✂️", "questions": ["What do we use to cut paper?", "Snip snip.", "Be careful, I am sharp."]},
                {"name": "Magnet", "emoji": "🧲", "questions": ["Select the Magnet", "I stick to metal.", "I have a north and south pole."]},
                {"name": "Microscope", "emoji": "🔬", "questions": ["Select the Microscope", "See tiny things.", "Science tool."]},
                {"name": "Telescope", "emoji": "🔭", "questions": ["What do we use to see stars?", "Look at the moon.", "Astronomy tool."]},
                {"name": "Light Bulb", "emoji": "💡", "questions": ["What gives us light?", "Turn me on in the dark.", "Idea!"]},
                {"name": "Candle", "emoji": "🕯️", "questions": ["Select the Candle", "Light me with a match.", "Blow me out on birthday cake."]},
                {"name": "TV", "emoji": "📺", "questions": ["What do we watch cartons on?", "Television.", "Use the remote."]},
                {"name": "Cupboard", "emoji": "🚪", "questions": ["Where do we keep our clothes?", "Wardrobe.", "Open my doors."]},
                {"name": "Stairs", "emoji": "🪜", "questions": ["What do we use to go upstairs?", "Step up.", "Climb me."]}
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
                
                # Pick a random question from the list
                # Fallback to standard if "questions" missing (safety)
                question_list = correct_item.get("questions", [f"Select the {correct_item['name']}"])
                question_text = random.choice(question_list)

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
                
                # Pick varied question templates
                question_templates = data.get("questions", [f"Which is {target_category}?"])
                question_template = random.choice(question_templates)
                question_text = question_template.replace("[TARGET]", target_category)

                q_obj = {
                    "id": i + 1,
                    "question": question_text,
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
