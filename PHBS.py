import requests
import time
import os
import sys
import json
import hashlib
import random

# ================== PROTEKSI AUTHOR ==================
AUTHOR = "@FALHORUS"
# PENTING: Jika token tidak valid, bot akan memberikan notifikasi.
TOKEN = 
token_id = hashlib.md5(TOKEN.encode()).hexdigest()[:6]
FILE_DATA = f"data_cd_{token_id}.json"

LOG_AKTIVITAS = []


# ================== DATABASE FULL ==================
tugas_spam = [
   # 1. Alien & City
    {
        "nama": "BUY/SELL ALIEN",
        "channel_id": "944664069972049960", 
        "pesan": (
            "Sell Alien & City Items At PHBS\n\n"
            "Sell Takeaway Joint\n"
            "Sell Takeaway Joint Roof\n"
            "Sell Space Conveyor Block\n"
            "Sell Storm Drain Cover\n"
            "Sell Street Sidewalk\n"
            "Sell Street Clock\n"
            "Sell Subway Wall\n"
            "Sell Subway Stairs\n"
            "Sell Pizza Sign\n"
            "Sell City Bench\n"
            "Sell Subway Sign\n"
            "Sell Space Station Sign\n"
            "Sell Greetings Earthlings Sign\n"
            "Sell Geometric Bench\n"
            "Sell Techno Grass\n\n"
            "Buy All Aliens Item Dm "
        )
    },
    # 2. Anniversary Items
    {
        "nama": "BUY/SELL ANNIVERSARY",
        "channel_id": "796633769917546536", 
        "pesan": (
            "**CHEAP ANNIVERSARY SHOP AT PHBS**\n\n"
            "Sell Party Block\n"
            "Sell Retro Tape Block\n"
            "Sell Rave Hall Wall\n"
            "Sell Rave Hall Floor\n"
            "Sell Rave Haze Light\n"
            "Sell Fireflies In A Jar\n"
            "Sell Party Punch Bowl\n"
            "Sell Balloon Decorations\n"
            "Sell Buddy Balloons\n"
            "Sell Rave Stage\n"
            "Sell Party Couch\n"
            "Sell Retro Record Block\n"
            "Sell Retro Pattern Background\n"
            "Sell Retro Pattern Block\n"
            "Sell Black Display Shelf\n"
            "Sell Black Party Table\n"
            "Sell Retro Computer\n"
            "Sell Shiny Mannequin\n"
            "Sell Digital Pet Block\n"
            "Sell Party Pager Block\n"
            "Sell Party Bunting\n"
            "Sell Polka-Dot Ball\n"
            "Sell Fidget Spinner Pinwheel\n"
            "Sell Glitter Pillow Trampoline\n"
            "Sell Ballroom Party Chair\n"
            "Sell Neon Party House Roof\n"
            "Sell Neon Party House\n"
            "Sell Party Mocktail Table\n"
            "Sell Party Screamer\n\n"
            "BUY ALL ANNIVERSARY ITEM DM "
        )
    },
    # 3. Supplier Search
    {
        "nama": "FIND SUPPLIER",
        "channel_id": "1106191543452307537",
        "pesan": (
            "**CHEAP VEND SHOP AT ( PHBS )** Looking for supplier:\n\n"
        "**BUY ALL:** (CRYSTAL/RUBY/EMERALD/TOPAZ/SAPPHIRE/OPAL/SHIFTY Block), "
        "JAMMER (P/Z/S/FH/GC/AG/Minimod/PineGuard), CHEMICALS (R/B/Y/G/P), SL/BL/HL, SSP/RSP BLOCK/SEED, "
        "DIMENSION BLOCK, ALL EVENT BLOCKS, BBM ITEMS, COUCH/BED, CHECKPOINT, "
        "PLATFORM, SHEET MUSIC, FOOD, PAINT, DECOR ITEM, AWNING, ADVENTURE BLOCK, "
        "STEAM BLOCK, NUMBER BLOCK, ALL WALLPAPER, ALL BLOCK, WEATHER, Vending Machine "
        "SURG TOOLS, GALA TOOLS, FARMABLE BLOCK (Chand,Lgrid Etc), DISPLAY BLOCK/BOX/SHELF, "
        "CLASH BLOCK, MANNEQUIN, SCIENCE ITEMS, SIGN, DOOR, All TREE.\n\n"
        "DM ME, PUT VEND OR DROPPED"
        )
    },
    # 4. BBM Shop List
    {
        "nama": "BUY/SELL BBM",
        "channel_id": "1106191572573364264",
        "pesan": (
            "**CHEAP BBM SHOP AT PHBS**\n\n"
        "Balloon Throwing Stand, Bouncy Balloon,Dunking Bucket,Kiddie Pool,Inflatable Ring,Target, "
        "Waterslide,Waterslide Strut,Party Block,Party Bunting,Adobe Block,Churro Block, "
        "Corn Field Ladder,Nacho Block,Olmec Head,Pinata Block,Wrestling Ring,Castle Stone, "
        "Castle Stone Background,Castle Turret,Manor House Sandstone,Manor House Sandstone Background, "
        "Nobleman's House,Stables,Art Wall,Audio Gear,Audio Rack,Clouds Background,Clouds Wallpaper, "
        "Dark Aqua Wallpaper,Dark Blue Wallpaper,Dark Brown Wallpaper,Dark Green Wallpaper, "
        "Dark Grey Wallpaper,Dark Orange Wallpaper,Dark Purple Wallpaper,Dark Yellow Wallpaper, "
        "Dark Walnut Block,Dark Walnut Ladders,Dark Walnut Wall, Dinosaur Wallpaper, E-Z Cook Oven, "
        "Innie Block, Jade Block,Outie Block,Picket Fence, Skull Wallpaper,Sheet Music Bass Note, "
        "Sheet Music Drums,Sheet Music Piano Note,Sheet Music Sax Note,Sheet Music Flute Note.\n"
        "Buy BBM and clearing stock, DM me "
        )
    },
    # 5. Huge Vend Shop
    { 
        "nama": "PROMOTE WORLD", 
        "channel_id": "1106191597298798662", 
        "pesan": (
        "**FREE PUBLIC WRENCH AT PHBS**\n"
        "Free Lock-Bot Remote\n"
        "Free Telephone\n"
        "Free Sewing Machine\n"
        "Free Anvil\n"
        "Free Clothing Compactor\n"
        "Free Food Grinder\n"
        "Free DNA Extarctor\n"
        "Free DNA Processors\n"
        "Free Autoclave\n"
        "Free Transmutabooth\n"
        "Free Star Tool Nanoforge\n"
        "Free Forge\n"
        "Free Spotlight\n\n"
        
        "**CHEAP AUTO SURG AT CUREBOYS**\n"
        "Auto Surg Gem Cuts\n"
        "Auto Surg Torn\n"
        "Auto Surg Chicken Feet\n"
        "Auto Surg Ecto-Bones\n"
        "Auto Surg Lupus\n"
        "Auto Surg Fatty Liver\n"
        "Auto Surg Chaos Infection\n"
        "Auto Surg Moldy Guts\n"
        "Auto Surg Brainworms\n"
        "Auto Surg Grumbleteeth\n"
        "Auto Surg Broken Heart\n\n"
        "**VISIT PHBS & CUREBOYS NOW!**"
        )
    },
    # 6. SSP Blocks
    { 
        "nama": "BUY/SELL SSP", 
        "channel_id": "1106191612339564554", 
        "pesan": ( "SELL SSP BLOCKS AT PHBS\n"
                  "BUY ALL SSP BLOCK 200/1 NEED SUPPLIER DM "
        
        )
    },
    # 7. RSP Blocks
    { 
        "nama": "BUY/SELL RSP", 
        "channel_id": "1106191627204169828", 
        "pesan": ( "SELL RSP BLOCKS AT PHBS"
                  "BUY ALL RSP BLOCK NEED SUPPLIER DM "
        )
    },
    # 8. Rare Items
    { 
        "nama": "BUY/SELL RARE ITEM", 
        "channel_id": "900836866373333052", 
        "pesan": "SELL CHEAP RARE ITEM AT PHBS" 
    },
    # 9. Marvelous Missions
    {
        "nama": "BUY/SELL MARVELOUS",
        "channel_id": "900833650654994442",
        "pesan": (
            "**SELL MARVELOUS MISSIONS ITEMS AT PHBS**\n\n"
        "Sell Greg The Octopus\n"
        "Sell Slithering Serpent Hair\n"
        "Sell Druids Robe\n"
        "Sell Bunny Ear Magnifying Glass\n"
        "Sell Bagpipes\n"
        "Sell Riding RV Chick Tricycle\n"
        "Sell Red Bicycle\n"
        "Sell Magic Armor Plate\n"
        "Sell Crab Claw & Shield\n"
        "Sell Purple Shore Crab Headband\n"
        "Sell Hermit Crab Leash\n"
        "Sell Seafoam Scarf\n"
        "Sell Presidential Beard\n"
        "Sell Eldritch Crossbow\n"
        "Sell Freezing Skull Mask\n"
        "Sell Fire Punk Hair\n"
        "Sell Skull Of Burning Horrors\n"
        "Sell Goldfish Bowler Hat\n"
        "Sell Poseidons Trident\n"
        "Sell Aquamarine Stone\n"
        "Sell American Eagle Wings\n"
        "Sell Partydactyl Wings\n"
        "Sell Crystal Aura\n"
        "Sell Matrix Aura\n"
        "Sell Ying-Yang Pendant\n"
        "Sell Pineapple Chakram\n"
        "Sell Northern Lights Aura\n"
        "Sell Nightwings\n"
        "Sell Devil Wings\n"
        "Sell Bloom Aura\n"
        "Sell Golden Aura\n"
        "Sell Sun Block\n"
        "Sell Raven Wings\n"
        "Sell Pooka Hood\n\n"
        "**DM ME IF BUYING!**"
        )
    },
    # 10. Obtainable / Rollback Plaques
    {
        "nama": "BUY/SELL OBTAINABLE ",
        "channel_id": "900860787298553877",
        "pesan": (
           "Rollback Plaque I\n"
        "Rollback Plaque II\n"
        "Rollback Plaque III\n"
        "Rollback Plaque IV\n"
        "Rollback Plaque V\n"
        "Rollback Plaque VI\n"
        "Rollback Plaque VII\n"
        "Rollback Plaque VIII\n"
        "Rollback Plaque IX"
        "Also buy all rollback plaque Dm"
        )
    },
# 11. Legendary Items
{
    "nama": "BUY/SELL LEGENDARY",
    "channel_id": "900847822570651658",
    "pesan": (
        "**Sell Legendary Items AT PHBS**\n\n"
        "Sell Honor Fire\n"
        "Sell Steel Heavens\n"
        "Sell Blade Candour\n"
        "Sell Sky Owl Mech\n"
        "Sell Sand\n"
        "Sell Display Box\n"
        "Sell Tombstone\n"
        "Sell Birth Certificate\n"
        "Sell Lava\n"
        "Sell Dragon Gate\n"
        "Sell Rocket Thruster\n"
        "Sell Chemical G\n"
        "Sell High Tech Block\n"
        "Sell Clouds\n"
        "Sell Iron Bars\n"
        "Sell Mind-Ghost-In-A-Jar\n"
        "Sell Obsidian\n"
        "Sell Clouds Wallpaper\n"
        "Sell Dwarven Background\n"
        )
    },
    # 12. Growtoken Items
    {
        "nama": "BUY/SELL GROWTOKEN ",
        "channel_id": "1282079076890443786",
        "pesan": (
            "**SELL Items at PHBS**\n"
        "Buy Snow Leopard Shawl 50 DL\n"
        "Buy Weather Nothingness 15 DL\n"
        "Buy Mini-Mod 10 DL\n"
        "Buy Saeedru's Ghutra 10 DL\n"
        "Buy Grip Tape 30 DL\n"
        "Buy Doodad 20 DL\n"
        "Buy Mighty Snow Rod 10 DL\n"
        "Buy Night Vision Goggles 70 DL\n"
        "Buy Cat Eye 35 DL\n"
        "Buy Muddy Pants 75 DL\n"
        "Buy Derpy Star Block 10 DL\n"
        "Buy Cuddly Piranha 60 DL\n"
        "Buy Puddy Leash 80 DL\n"
        "Buy Challenge Timer 25 WL\n"
        "Buy Crystal Cape 45 DL\n\n"
        "Dm me if sell "
        )
    },
    # 13. Clash Items
    {
        "nama": "BUY/SELL CLASH",
        "channel_id": "762435449909542942",
        "pesan": ( "**SELL CLASH ITEMS AT PHBS**\n"
"Castle Background, Sewage, Stone, Turret, Moat, Door, Gate. "
"Galleon Hull, Mast, Crow Nest, Crossbeam, Ratlines. "
"Manor Sandstone/Background, Red Wallpaper, Door, Stair. "
"Royal Canopy Bed,Carpet, Gilt Bathtub, Throne. "
"Stable Background,Roof, Stables. Nobleman: House, Roof. "
"Garden Bench, Planter, Trellis. Sunset: Background, Cloud. "
"Baroque Fountain,Fence, Gate. Winter: Foliage, Hedge. "
"Greenhouse, Gilt Ceiling, Oak Tree, Cheval De Frise, Peasant Fence, "
"Drafting Table, Birdhouse, Hibiscus, Lavender, Wall Clock, Statue Pillar, "
"Vintage Armchair, Topiary Hedge, Weapons Rack, Suit Of Armor, "
"Holo Mannequin, Wall Sconce, Gibbet, Iron Torch, Sandstone Fireplace, "
"Banquet Table, Dining Chair, Book Shelf, Weather Vane, Rotten Woodland, "
"Guard Tower, Sundial, Dimension Block, Gravity Well, Storm Cloud, "
"Trickster, Cracked Stone,Doppleganger, Mud Puddle, Mirage, Death Trap, "
"Storage Box 1-3, Tapestry,Bear Mount, Reading Lamp, "
"Regal Stairs,Clash Tickets.\n\n"
"BUY ALL CLASH ITEMS DM"
        )
    },
     # 13. Guild Item
    {
        "nama": "BUY/SELL GUILD",
        "channel_id": "900847998320406599",
        "pesan": ( "SELL GUILD ITEMS AT PHBS\n\n"
        "Sell Guild Name Changer\n"
        "Sell Guild Chest\n"
        "Sell Guild Banner - Normal Horizontal\n"
        "Sell Guild Banner Normal Vertical\n"
        "Sell Guild Banner Ornate Horizontal\n"
        "Sell Guild Banner Ornate Vertical\n"
        "Sell Guild Entrance Normal\n"
        "Sell Guild Entrance Ornate\n"
        "Sell Guild Flag Pole Spear\n"
        "Sell Guild Flag Pole Wings\n"
        "Sell Guild Flag Arrow\n"
        "Sell Guild Flag Peak\n"
        "Sell Guild Flag Shield\n"
        "Sell Guild Flag Tatters\n"
        "Sell Guild Flag Wave\n"
        "Sell Guild Potion Black Mixer\n"
        "Sell Guild Potion White Mixer\n\n"
        "Buy All Guild Reward DM "
        )
    },
    # 14. Lunar Items
    {
        "nama": "BUY/SELL LUNAR",
    "channel_id": "806455542591651840",
    "pesan": (
        "Sell Lucky Fortune Cookie, Sell Fortune Cookie, Sell Lunar Chest, Sell Lunar Spice Spray, "
"Sell Lucky Token, Sell Paper Dividing Wall, Sell Chinese Arch, Sell Coin Door, "
"Sell Festival Lanterns, Sell Lucky Golden Ingot, Sell Chinese Prayer Wheel, "
"Sell Chinese Firework, Sell Chinese Crackers, Sell Chinese Temple Background, "
"Sell Incense Urn, Sell Chinese Temple Pillar, Sell Chinese Temple Awning, "
"Sell Year of the Snake/Dragon/Rabbit/Tiger/Ox/Rat/Pig Statue, Sell Red Coin Wallpaper, "
"Sell Dynasty Vase, Sell Terracotta Growtopian, Sell Great Wall Turret, "
"Sell Great Wall Growtopia, Sell Bamboo Boba, Sell Guardian Lion Statue, "
"Sell Dragon Decorations, Sell Maneki-neko, Sell Jade Pillar, Sell Vase of Souls, "
"Sell Dragon Teapot, Sell Lunar Food Cart, Sell Ta Couch, Sell Hanging Fan, "
"Sell Leaping Carp, Sell Hidden Dragon, Sell Antique Tea Caddy, Sell Que Stone Pillar, "
"Sell Red Lucky Knot, Sell Red Chinese Dragon Set\n\n"
"Buy All Lunar Items DM "
        )
    },
    # 15. Valentine Items
   {
    "nama": "BUY/SELL VALENTINE",
    "channel_id": "806455698014732318",
    "pesan": ( 
        "SELL VALENTINE ITEMS AT PHBS\n\n"
"Sell Gbc, Sell Sgbc, Sell Ready Well, Sell Well Of Love, Sell Love Pure Essence, "
"Sell Candy Heart, Sell Angel Wings, Sell Sparkling Mallet, Sell Rose Rifle, "
"Sell Bear That Cares, Sell Cotton Candy Swirl, Sell Cotton Candy Swirl Background, "
"Sell Dancing Candle, Sell Heart Awning, Sell Heartcastle Stone, "
"Sell Heartcastle Stone Background, Sell Heartstone Block, Sell Love Curtain, "
"Sell Love Portal, Sell Loveseat, Sell Pink Marble Arch, Sell Rink Of Love, "
"Sell Teddy Bear Block, Sell Valensign, Sell Fluttering Bunting, "
"Sell Potpourri Dispenser.\n\n"
"Buy Gbc, Buy Sgbc, Buy Ready Well, Buy Well Of Love, Buy Love Pure Essence 1 Wl, "
"Buy Candy Heart 350 Wl, Buy Heartcastle Stone/Background 50/1 Wl.\n\n"
"**DM ME IF SELL VALENTINE ITEMS**"
    )
},
    # 16. Garuda Item
    {
    "nama": "BUY/SELL GARUDA ITEM", 
    "channel_id": "1012658140694716436", 
    "pesan": (
         "**SELL GARUDA ITEMS AT PHBS**\n\n"
"Sell Garuda Chest\n"
"Sell Golden Garuda Chest\n"
"Sell Rumah Adat Asmat\n"
"Sell Floating Restaurant\n"
"Sell Pocong Statue\n"
"Sell Monkey Statue\n"
"Sell Bamboo Arc\n"
"Sell Bamboo Bridge\n"
"Sell Rice Terrace Block\n"
"Sell Lembuswana Statue\n"
"Sell Garuda Statue\n"
"Sell Garuda Feathers Background\n"
"Sell Garuda Feathers Block\n"
"Sell Sacred Temple\n"
"Sell Buddha Stand Holding\n\n"
"**Buy All Garuda & Golden Garuda Chest DM**"
        )
    },
    # 17. St. Patrick
    {
        "nama": "BUY/SELL ST PATRICK",
        "channel_id": "806456471302176788",
        "pesan": (
            "**Sell St. Patrick Items AT PHBS**\n\n"
       "Sell Green Block, Sell Golden Block, Sell Green Wallpaper, Sell Lucky Clover, "
    "Sell Pot O' Gold, Sell Green Beer, Sell Blarney Stone, Sell Celtic Block, "
    "Sell Lucky Horseshoe, Sell Emerald Shard, Sell Shamrock Sign, Sell Potato, "
    "Sell Potato Couch, Sell Bamboo, Sell Lucky Portal, Sell Ladybug Leaf, "
    "Sell Lucky Clover Background, Sell Sheet Music: Flute Note, Sell Giant's Causeway Block, "
    "Sell Giant Pot O' Gold, Sell Sheet Music: Sharp Flute, Sell Harp, Sell Sheet Music: Flat Flute, "
    "Sell Celtic Cross, Sell Minilith Stone, Sell Faerie Lanterns, Sell Heather Bush, "
    "Sell Lucky Chair, Sell Moss-Covered Stone, Sell Money Tree, Sell Four-Leaf Clover Checkpoint, "
    "Sell Giant Falling Shamrock, Sell Clover Fan, Sell Ye Olde Tavern, Sell Shamrock Seat, "
    "Sell Lucky Shamrock Seat, Sell Celtic Wheel, Sell Celtic Background, "
    "Sell Chain Quilt Background, Sell Harp Monument, Buy All St. Patrick Items DM me"
        )
    },
    # 18. Prince of Persia & Rayman
    {
        "nama": "BUY/SELL UBIWEEK",
        "channel_id": "997609617410490418",
        "pesan": (
          "**Sell UBIWEEK Items AT PHBS**\n\n"
    "Buy Prince of Persia: Cave Background 100/1\n"
    "Buy Prince of Persia: Cave Spikes 40/1\n"
    "Buy Prince of Persia: Cave Column 40/1\n"
    "Buy Prince of Persia: Cave Torch 30/1\n"
    "Buy Prince of Persia: Palace Background 40/1\n"
    "Buy Prince of Persia: Palace Spikes 40/1\n"
    "Buy Prince of Persia: Palace Wall 40/1\n"
    "Buy Prince of Persia: Palace Arch 40/1\n"
    "Buy Prince of Persia: Palace Turret 40/1\n"
    "Buy Prince of Persia: Palace Dome 10/1\n"
    "Buy Hourglass of Time 20/1\n"
    "Buy Rayman Forest Dirt 10 Wl\n"
    "Buy Rayman Forest Lianas 5/1\n"
    "Buy Rayman Forest Spikes 40/1\n"
    "Buy Rayman Forest Platform 3/1 Wl\n"
    "Buy Rayman Band Land Platform 5 Wl\n"
    "Buy Rayman Band Land Bridge 40/1\n"
    "Buy Rayman Band Land Drum 40/1\n"
    "Buy Rayman Band Land Flute 40/1\n"
    "Buy Rayman Band Land Pinwheel 40/1\n"
    "Buy Immortals Spring Mountain 4 Wl\n"
    "Buy Immortals Spring Column 3 Wl\n"
    "Buy Immortals Spring Topiary 2/1\n"
    "Buy Immortals Spring Torch 25/1\n"
    "Buy Athena Statue 3 Wl\n"
    "Buy All Ubiweek Items DM"
        )
    },
    # 19. Grow4Good
    {
        "nama": "BUY/SELL GROW4GOOD",
        "channel_id": "967097602153791528",
        "pesan": (
             "**Sell GROW4GOOD Items AT PHBS**\n\n"
        "Sell Startopia Supply Crate Sell Superhero Supply Crate Sell Surgery Supply Crate "
        "Sell Fishing Supply Crate Sell Cooking Supply Crate Sell Grow4Good Gift Hamper "
        "Sell Grow4Good Special Gift Hamper Sell Gift Hamper Sell Heli-cap-tor Sell Dirt Aura "
        "Sell Fish Tank Head Sell Mechanical Assistance Sell Mecha Med Scarf Sell Helping Hand "
        "Sell Sgt. Stubs Sell Backwards Ballcap Sell Pom-Poms Sell Waving Inflatable Arm Guy "
        "Sell Laser Light Sell Stage Fog Sell Party Projector Sell Balloon Arch Sell Donut Donation Box "
        "Sell Healing Station Sell Hand Chair Sell Floating Hand Sell Gummy Bear Block Red "
        "Sell Gummy Bear Block Yellow Sell Gummy Bear Block Green Sell Bouncy Castle Block "
        "Sell Unicorn Wallpaper Sell Candy Jar Sell Candy Brick\n\n"
        "Buy All Grow4Good Items DM "
        )
    },
    # 20. Easter Items
    {
        "nama":"BUY/SELL EASTER",
        "channel_id": "806456521335767070",
        "pesan": (
            "**Sell EASTER ITEMS AT PHBS**\n\n"
        "Sell Happy Flower Grass Sell Hidden Eggs Sell Lollipop Garden Sell Flower Pinwheel "
        "Sell Basket Chair Sell Easter Checkpoint Sell Bouncy Bunny Sell Sunnyside Yolkfall "
        "Sell Easter Island Head Sell Easter Deggcorations Sell Fancy Birdbath "
        "Sell Pastel Pink Block Sell Pastel Aqua Block Sell Pastel Green Block Sell Pastel Yellow Block "
        "Sell Pastel Orange Block Sell Pastel Blue Block Sell Pastel Purple Block "
        "Sell Pastel Pink Flower Block Sell Pastel Aqua Flower Block Sell Pastel Green Flower Block "
        "Sell Pastel Yellow Flower Block Sell Pastel Orange Flower Block Sell Pastel Blue Flower Block "
        "Sell Pastel Purple Flower Block Sell Pastel Brick Block Sell Pastel Mondrian Block "
        "Sell Pastel Bunny Block Sell Pastel Checkered Wallpaper Sell Easter Egg Arch "
        "Sell Bunny Boba Block Sell Marshmallow Sell Kulich Sell Egg Wreath Sell Egg Wallpaper\n\n"
        "Buy All Easter Items DM "
        )
    },
    # 21. Wildlife Items
    {
        "nama": "BUY/SELL WILDLIFE",
        "channel_id": "1083726271554519120",
        "pesan": (
         "Sell Wildlife Items at PHBS\n"
    "Sell Eco\n"
    "Sell Golden Eco\n"
    "Sell Coral Reef Block\n"
    "Sell Earth Block\n"
    "Sell Rainforest Roots\n"
    "Sell Swamp Stump\n"
    "Sell Turtle Block\n"
    "Sell Wild Grass\n"
    "Sell Zebra Block\n"
    "Sell Banana Barrel\n"
    "Sell Blue Bouncy Mushroom\n"
    "Sell Red Bouncy Mushroom\n"
    "Sell Sideways Vines\n\n"
    "Buy All Wildlife Items DM"
        )
    },
    # 22. Cinco De Mayo
    {
        "nama": "BUY/SELL CINCO DE MAYO",
        "channel_id": "806456631172136981",
        "pesan": (
            "**Sell CINCO DE MAYO ITEMS AT PHBS**\n\n"
    "Sell Adobe Block\n"
    "Sell Calavera Skull\n"
    "Sell Burrito Chair\n"
    "Sell Cactus Pot\n"
    "Sell Churro Block\n"
    "Sell Diamond Fiesta Candles\n"
    "Sell Festive Banner\n"
    "Sell Fiesta Wallpaper\n"
    "Sell Taco House\n"
    "Sell Lava Pinata\n"
    "Sell Marigold Flowers\n"
    "Sell Mystery Pinata\n"
    "Sell Nacho Block\n"
    "Sell Papel Picado\n"
    "Sell Pueblock\n"
    "Sell Puerto Growtopia House\n"
    "Sell Sombrero Bed\n"
    "Sell Taco Window\n"
    "Sell Wrestling Ring\n\n"
    "Buy All Cinco Items DM"
        )
    },
    # 23. Pineapple Items
    {
        "nama": "BUY/SELL PINEAPPLE",
        "channel_id": "806456721169973258",
        "pesan": (
          "**SELL PINEAPPLE ITEMS AT PHBS**\n\n"
"Sell Pineapple Block\n"
"Sell Sugarloaf Pineapple\n"
"Sell Frozen Pineapple\n"
"Sell Roasted Pineapple\n"
"Sell Pineapple Daiquiri\n"
"Sell Pineapple Ring\n"
"Sell Adventure Pineapple\n"
"Sell Pineapple Slice\n"
"Sell Pineapple Sign\n"
"Sell Pineapple Bamboo Frame\n"
"Sell Pineapple Tiki Door\n"
"Sell Koa Lantern\n"
"Sell Checkpoint Totem\n"
"Sell Pinedelier\n"
"Sell Looming Pineapple\n"
"Sell Prickly Pineapple\n"
"Sell Rotten Pineapple\n"
"Sell Dangerous Pineapple\n"
"Sell Sourloaf Pineapple\n"
"Sell Pineapple Pennant\n"
"Sell Pineapple Wallpaper\n"
"Sell Pineapple Door\n"
"Sell Pineapple Stone\n"
"Sell Pineapple Lamp\n"
"Sell Pineapple Table\n"
"Sell The Pine Throne\n"
"Sell Pineapple Stained Glass\n"
"Sell Super Pineapple Door\n"
"Sell Super House\n"
"Sell Super Window\n"
"Sell Pineapple Fountain\n"
"Sell Pineapple Disco Ball\n"
"Sell Fresh Pineapple\n"
"Sell Kiwi Block\n"
"Sell Fresh Kiwi\n"
"Sell Papaya Block\n"
"Sell Fresh Papaya\n"
"Sell Watermelon Block\n"
"Sell Fresh Watermelon\n"
"Sell Dragon Fruit\n"
"Sell Fresh Dragon Fruit\n"
"Sell Loop Of Fruits\n\n"
"**Buy All Pineapple Items DM**"
        )
    },
    # 24. Pearl Items
    {
        "nama": "BUY/SELL PEARL",
        "channel_id": "989905357063213106",
        "pesan": (
            "**Sell PEARL ITEM AT PHBS**\n\n"
            "Sell Barista Hair\n"
            "Sell Barista Pants\n"
            "Sell Barista Shades\n"
            "Sell Barista Shirt\n"
            "Sell Barista Shoes\n"
            "Sell Bouncer Pants\n"
            "Sell Bouncer Shades & Beard\n"
            "Sell Bouncer Shirt\n"
            "Sell Bouncer Shoes\n"
            "Sell Cucumber Eyes\n"
            "Sell Pearl Arch\n"
            "Sell Pearl Butterfly Wings\n"
            "Sell Pearl Castle Stone\n"
            "Sell Pearl Castle Stone Background\n"
            "Sell Pearl Castle Turret\n"
            "Sell Pearl Floral Lei\n"
            "Sell Pearl Lamp\n"
            "Sell Pearl Pants\n"
            "Sell Pearl Pointdexters\n"
            "Sell Pearl Polo\n"
            "Sell Pearl Pumps\n"
            "Sell Pearl Tiki Crown\n"
            "Sell Pearl Wallpaper\n"
            "Sell Pet Pearl\n"
            "Sell Mother Of Pearl\n"
            "Sell Towel Turban\n\n"
            "**Buy Bronze/Golden Pearl Chest DM**"
        )
    },
    # 25. SummerFest
    {
        "nama": "BUY/SELL SUMMERFEST",
        "channel_id": "806456760592105483",
        "pesan": (
            "**Sell SummerFest Item AT PHBS**\n\n"
            "Sell Super Summer Surprise\n"
            "Sell Summer Surprise\n"
            "Sell Beach Blast\n"
            "Sell Seaweed\n"
            "Sell Hula Bobblehead\n"
            "Sell Coral\n"
            "Sell Ocean Rock\n"
            "Sell Palm Tree\n"
            "Sell Barbecue Grill\n"
            "Sell Summer Breeze\n"
            "Sell Root Beer\n"
            "Sell Silk Bolt\n"
            "Sell Crab Wall Mount\n"
            "Sell Bubble Machine\n"
            "Sell Crushed Ice\n"
            "Sell Inflatable Dolphin\n"
            "Sell Message In A Bottle\n"
            "Sell Phoenix Fragment\n"
            "Sell Tropical Bar\n"
            "Sell Banana Caution Cone\n"
            "Sell Sandtopian\n\n"
            "**BUY ALL CHEAP SUMMERFEST ITEM DM**"
        )
    },
    # 26. Thanksgiving
    {
        "nama": "BUY/SELL THANKSGIVING",
        "channel_id": "779116201350529054",
        "pesan": (
            "**Sell THANKSGIVING & DINER ITEMS AT PHBS**\n\n"
            "Sell Roasted Turkey Sell Stuffins Support Package Sell Organic Turkey "
            "Sell Dead Thanksgiving Turkey Sell Diner Bell Sell Hay Chair Sell Eagle Statue "
            "Sell Sweet Potato Sell Thanksgiving Trifle Block Sell Vintage Jukebox "
            "Sell Grow-Cola Block Sell Welcome To Growtopia Sign Sell Campaign Poster "
            "Sell Turkey Dinner Flag Sell Enlightenment Bell Sell Grow Studios Globe "
            "Sell Stuffins Poster Sell Pie Crust Wallpaper Sell Diner Couch Sell Diner Background "
            "Sell Presidential Chair Sell Presidential Throne Sell Sweet Potato Mash "
            "Sell Organic Turkey Feather Sell Turkey Feather Sell Thanksgiving Frame "
            "Sell Colonization Wagon Canopy Sell Thanksgiving Bell Sell Wagon Wheel "
            "Sell Colonization Wagon Base\n\n"
            "**Special Offer:** 240K Sweet Potato Rate 4/1 (Take All Only)\n"
            "DM "
        )
    },
    # 27. Halloween
    {
        "nama": "BUY/SELL HALLOWEEN",
        "channel_id": "806456962882600960",
        "pesan": (
            "**Sell Halloween Items AT PHBS**\n\n"
            "Sell Boney Block\n"
            "Sell Buzzsaw\n"
            "Sell Calavera Skull\n"
            "Sell Corrupted Castle\n"
            "Sell Creepy Caged Doll\n"
            "Sell Creepy Wallpaper\n"
            "Sell Deadly Spider\n"
            "Sell Death Metal Block\n"
            "Sell Dino Ribcage\n"
            "Sell Evil Eye\n"
            "Sell Gibbet\n"
            "Sell Halloween Lantern\n"
            "Sell Hanging Bats\n"
            "Sell Haunted Darkness\n"
            "Sell Haunted Door\n"
            "Sell Haunted House\n"
            "Sell Haunted Portrait\n"
            "Sell Iron Maiden\n"
            "Sell Jack O Lantern\n"
            "Sell Obake Lantern\n"
            "Sell Pocong Statue\n"
            "Sell Rickety Window\n"
            "Sell Scarecrow\n"
            "Sell Skeleton\n"
            "Sell Eldritch Flame\n"
            "Sell Death Scarf\n\n"
            "**Buy All Halloween Items DM**"
        )
    },
    # 28. Assassin's Creed
    {
        "nama": "BUY/SELL ASSASINS",
        "channel_id": "1157271390962069545",
        "pesan": (
           "**Sell ASSASSIN'S CREED ITEMS AT PHBS**\n\n"
            "Sell Assassin's Creed: Hay Checkpoint\n"
            "Sell Assassin's Creed: Wanted Poster\n"
            "Sell Assassin's Creed: Renaissance Arch\n"
            "Sell Assassin's Creed: Renaissance Balustrade\n"
            "Sell Assassin's Creed: Renaissance House\n"
            "Sell Assassin's Creed: Renaissance Road\n"
            "Sell Assassin's Creed: Renaissance Roof\n"
            "Sell Assassin's Creed: Renaissance Scaffolding\n"
            "Sell Assassin's Creed: Renaissance Topiary\n\n"
            "**Buy All Assassin's Items DM**"
        )
    },
    # 29. Harvest Festival
    {
        "nama": "BUY/SELL HARVEST FESTIVAL",
        "channel_id": "806456916586790912",
        "pesan": (
          "**Sell HARVEST FESTIVAL ITEMS AT PHBS**\n\n"
    "Sell Chinese Lantern, Scarecrow, Moon Block, Autumn Viney Block, Autumn Viney Wallpaper, "
    "Autumn Leaf Block, Musical Gong, Sheep, Leaves, Dragon Scales, Hay, Pinecone, Acorn, "
    "Maple Leaf, Zen Garden, Bonsai, Tea Set, Centerpiece, Cherry Blossom Tree, Jade Spikes, "
    "Weeping Willow Branch, Weeping Willow Foliage, Weeping Willow Streamers, Weeping Willow, "
    "Chopping Wood Block, Lotus Lamp, Jade Brick Background, Mystic Record Player, "
    "Rice Crop Block, Rice Crop Wallpaper, Sunflower Ladder, Sunflower Pinwheel, "
    "Whoopie Pie Block, Firewood Cradle, Dewi Sri Statue, Harvest String Lights, "
    "Moon Palace, Moon Palace Door, Moon Palace Roof, Buddy To He, Jade Rabbit, "
    "Balance Shrub, Courage Shrub, Purity Shrub, Stone Block, Pebbles Block, "
    "Pebbles Background, Decorative Shrine, Floating Lotus Flower.\n\n"
    "Buy All Harvest Items DM "
        )
    },
    # 30. Wonder Week
    {
        "nama": "BUY/SELL WONDERWEEK",
        "channel_id": "1031260762083184650",
        "pesan": (
            "**Sell Wonder Week Items AT PHBS**\n\n"
            "Sell Neon Circuit Block, Sell Ghoulish Block, Sell GFW Bucket Block, "
            "Sell Party Plume Topiary, Sell Aqua Trident Statue, Sell Piano Platform, "
            "Sell Bling Background, Sell Lucid Sculpture Block, Sell Sakura Sushi Block, "
            "Sell Neon Party Machine Background, Sell Robot Lord Machine Wallpaper, "
            "Sell Sacred Scarf Block, Sell Lightning Umbrella Checkpoint, "
            "Sell Wyvern Statue Block, Sell Lightning Bottle Block, Sell Shattered Arch Block, "
            "Sell EQ Platform, Sell Super Background, Sell Starfire Background, "
            "Sell Kanji Canvas Block, Sell Minokawa Statue Block, Sell Tornado Block, "
            "Sell Soaring Beast's Nest,\n\n"
            "**Buy All Wonder Week Items DM**"
        )
    },
    # 31. Black Friday
    {
        "nama": "BUY/SELL BLACKFRIDAY",
        "channel_id": "806490613695512616",
        "pesan": (
            "**Sell BLACK FRIDAY ITEMS AT PHBS**\n\n"
    "Sell Black Friday Box Xtreme, Cashback Coupon, Shirt Rack, Sale Television, "
    "Onyx Block, Black Ultraviolet Sword Block, Matrix Dirt, Slouch Beanie, "
    "Bleached Hair, Black Friday Box Head, Black Swimming Cap, Streak Hair, "
    "Punk Mask, Black Mascara, Black Lavish Shades, Shady Shades, Bean Visor, "
    "Growtopian Bean, Punk Jacket, Varsity Jacket, Black Suit Jacket, "
    "Tie Dye Hoodie, Black Neon Hoodie, Vortex Shirt, Black Neon Pants, "
    "Vortex Skirt, Black Neon Hightops, Derpy Black Box Pet, Blackfire Crown, "
    "Black Crystal Ball Head, Black Ultraviolet Charm, BUVC, Matrix Trenchcoat, "
    "Black Blingin Board, Black Egg Cape, Pet Stealth Mech Robot, Matrix Aura, "
    "Noir American Eagle Wings, Black Big Fluffin Giga Ears, Shadow Cubes Aura, "
    "Black Radical Rollers, Remote Control TV, Black Burning Eyes, Neon Led Mask, "
    "Matrix Visor, Black Balrogs Tail, Metal Band Shirt, Edgy Anime Hair.\n\n"
    "Buy All Black Friday Items DM "
        )
    },
    # 32. Winterfest
    {
        "nama": "BUY/SELL WINTERFEST",
        "channel_id": "784189920742342688",
        "pesan": (
         "**Sell WINTERFEST ITEMS AT PHBS**\n\n"
    "Sell A Row of Winterfest Socks, Aurora Lantern, Big Bauble, "
    "Sell Bodacious Blue Dancefloor, Cherry Jelly Block, Creme Crown, Dark Snowy Cave Background, "
    "Sell Deluxe Grow Spray, Deluxe Winterfest Cracker, Festive Fence, Freeze Ray, Gingerbread Block, "
    "Sell Gingerbread Door, Gingerbread House, Gingerbread Roof, Groovy Green Dancefloor, "
    "Sell Hot Pink Dancefloor, Ice Throne of Winter, Icy Igloo, Jack-in-the-Box, Lime Jelly Block, "
    "Sell Log Cabin, Log Cabin Door, Log Cabin Roof, Long Tree Log, Long Yule Log, Mistletoe, "
    "Sell Raving Red Dancefloor, Santa's Chair, "
    "Sell Sheet Music: Winterfest, Sledding Penguin, Small Icicles, Snow Block, Sun Yellow Dancefloor, "
    "Sell Tall Tree Log, Tree Decorations, White Chocolate Block, "
    "Sell Winterfest Tree, Winterfest Wonderland Foliage, "
    "Sell Silverstar Bow, "
    "Sell Windup Musical Box, Winterfest Dancefloor, Winterfest Lantern\n\n"
    "Buy All Winterfest Items DM "
        )
    },
    # 33. Locke Items
    {
        "nama": "BUY/SELL LOCKE ITEM",
        "channel_id": "806494474200547338",
        "pesan": (
           "**Sell LOCKE & RARE ITEMS AT PHBS**\n\n"
            "Sell Neon Gum, Sell Locke's Mystery Box, Sell Guild Chest, Sell Transdimensional Vaporizer Ray, "
            "Sell Pet Trainer Whistle, Sell Sale Television, Sell Safe Vault, Sell Punch Antennae, "
            "Sell Build Antennae, Sell Grow Antennae, Sell Lock-Bot Remote, Sell Chi Harmonizer, "
            "Sell Extract-O-Snap, Sell Birth Certificate, Sell Wolf Whistle, Sell Lock Mover, "
            "Sell Edgy Anime Hair, Sell Edgy Anime Robe, Sell Stylish Sunglasses, Sell VIP Entrance, "
            "Sell Stretched Canvas, Sell Soul Stone, Sell Sword Pommel, Sell Remote Control Television, "
            "Sell Music Amplifier, Sell Burning Eyes, Sell Guild Name Changer, Sell Raccoon Leash, "
            "Sell Growmoji Chest, Sell Diamond Lock Mask, Sell Clothing Compactor, Sell Electric Bow, "
            "Sell MickeyMay Leash, Sell Golden Aura, Sell Blue Aura, Sell Pink Aura, Sell Neon Nerves, "
            "Sell Samille's Soul Abductor, Sell Harmonic Lock, Sell Solar Chariot, Sell Goldenrod Toy Lock-Bot,\n\n"
            "**Buy All Locke Items DM**"
        )
    },
    # 34. Mutation / Bio
    {
        "nama": "BUY/SELL MUTATION",
        "channel_id": "806493841015832586",
        "pesan": (
            "**Sell MUTATION ITEMS AT PHBS**\n\n"
            "Sell Bed Bugs, Sell Neon Green Mutation Layer, Sell Slithering Serpent Hair, "
            "Sell Googly-Woogly Fleshy Eye, Sell Googly-Woogly Verdant Eye, "
            "Sell Googly-Woogly Fleshy Eyed Wall, Sell Googly-Woogly Verdant Eyed Wall, "
            "Sell Googly-Woogly Fleshy Teeth, Sell Googly-Woogly Verdant Teeth, "
            "Sell Hairy Arm Horizontacles, Sell Hairy Leg Vertentacles, "
            "Sell Riding 'roach, Sell Riding Firefly, Sell The Beast with a Thousand Eyes Mask, "
            "Sell Cute Bulb Mask, Sell Worm Mutated Virus, Sell Wriggling Maggots, Sell Mutated Bones,\n\n"
            "**Buy All Mutation Items DM**"
        )
    },
    # 35. Space
    {
        "nama": "BUY/SELL COMET",
        "channel_id": "806494773711339530",
        "pesan": (
          "**Sell COMET ITEMS AT PHBS**\n\n"
            "Sell Space Command Seat\n"
            "Sell Ion Conduit\n"
            "Sell Transmatter Field\n"
            "Sell Hover Platform\n"
            "Sell Cosmic Rain\n"
            "Sell One-Way Block\n"
            "Sell Infected Block\n"
            "Sell Asteroid\n"
            "Sell Xenoid Block\n"
            "Sell Weather Machine - Comet\n"
            "Sell Alien Block\n"
            "Sell Comet Dust\n"
            "Sell Antimatter Dust\n\n"
            "**Buy All Comet Dust DM**"
        )
    },
    # 36. Carnival
    {
        "nama": "BUY/SELL CARNIVAL",
        "channel_id": "712744557519044719",
        "pesan": (
          "**Sell CARNIVAL ITEMS AT PHBS**\n\n"
            "Sell Blazing Electro Wings\n"
            "Sell Diamond Rocket Shoes\n"
            "Sell Edvoid's Fire-Nado\n"
            "Sell Ethereal Rainbow Dragon\n"
            "Sell Flame Scythe\n"
            "Sell Diamond Diaper\n"
            "Sell Diamond Wings\n"
            "Sell Calliope\n"
            "Sell Lion Taming Whip\n"
            "Sell Orbs Of Elixir\n"
            "Sell Tiny Tank\n"
            "Sell Funhouse Mirror\n"
            "Sell Ringmaster Hat\n"
            "Sell Ringmaster Suit\n"
            "Sell Carny Vest\n"
            "Sell Dragon Block\n"
            "Sell Lion Block\n"
            "Sell Elephant Block\n"
            "Sell Carnival Awning\n"
            "Sell Carnival Sign\n"
            "Sell Carnival Block\n"
            "Sell Carnival Platform\n"
            "Sell Carnival Wallpaper\n"
            "Sell Carnival Pinwheel\n"
            "Sell Carnival Spikeball\n"
            "Sell Carnival Pipe\n"
            "Sell Carnival Ladders\n"
            "Sell Yellow Pennant\n"
            "Sell Blue Pennant\n"
            "Sell Red Pennant\n"
            "Sell Green Pennant\n"
            "Sell Jester's Cap\n"
            "Sell Licorice Rod\n"
            "Sell Globe\n"
            "Sell Toucan's Bill\n"
            "Sell Capuchin Leash\n"
            "Sell Pet Pidgeon\n\n"
            "**Buy All Carnival Items DM**"
        )
    },
    # 37. Fossil / Dino
    {
        "nama": "BUY/SELL FOSSIL",
        "channel_id": "743173219971760180",
        "pesan": (
            "**Sell FOSSIL & PREHISTORIC ITEMS AT PHBS**\n\n"
            "Sell Polished Fossil\n"
            "Sell Fossil Brush\n"
            "Sell Fossil Prep Station\n"
            "Sell Dino Ribcage\n"
            "Sell T-Rex Skull\n"
            "Sell Amber Block\n"
            "Sell Fossilized Spirit Block\n"
            "Sell Ammonite Block\n"
            "Sell Fossil Rock\n"
            "Sell Rock Chisel\n"
            "Sell Rock Hammer\n"
            "Sell DNA Processor\n"
            "Sell Ancient Plant Seed (APS)\n"
            "Sell Extractium Shard\n"
            "Sell Stone Spear\n"
            "Sell Dino DNA Strand (A, C, G, T)\n"
            "Sell Raptor DNA Strand (Alpha, Omega)\n"
            "Sell DNA Plant (X, Y)\n\n"
            "**Prehistoric Decorations:**\n"
            "Sell Prehistoric Fern\n"
            "Sell Prehistoric Flowering Fern\n"
            "Sell Prehistoric Red Fern\n"
            "Sell Blue Devourer Plant\n"
            "Sell Purple Devourer Plant\n"
            "Sell Prehistoric Vines\n"
            "Sell Prehistoric Candy Vines\n"
            "Sell Seussian Tree\n\n"
            "**Buy All Fossil & DNA Items DM**"
        )
    },
    # # 38. Zombie / Apocalypse
    {
        "nama": "BUY/SELL ZOMBIE",
        "channel_id": "806498636065931265",
        "pesan": (
           "**SELL ZOMBIE ITEMS AT PHBS**\n\n"
"Sell Camouflage Facepaint\n"
"Sell Zombie Defense Force Helmet\n"
"Sell Zombie Defense Force Uniform\n"
"Sell Zombie Defense Force Pants\n"
"Sell Retinal Scan Data Repository\n"
"Sell Barbed Wire Barrier\n"
"Sell Barricaded Door\n"
"Sell Objective Marker\n"
"Sell Sandbag Wall\n"
"Sell Z.D.F. Fence\n"
"Sell Chainlink Fence\n\n"
"**Buy All ZDF Items DM**"
        )
    },
    # 39. Wolf / Dark Castle
    {
        "nama": "BUY/SELL WOLF",
        "channel_id": "806494307036037140",
        "pesan": (
            "**Sell WOLFWORLD ITEMS AT PHBS**\n\n"
            "Sell Vile Vial - Lupus\n"
            "Sell Wolf Totem\n"
            "Sell Massive Fang\n"
            "Sell Wolfy Block\n"
            "Sell Tousled Hair\n"
            "Sell Snow Goggles\n"
            "Sell Hot Dog Hat\n"
            "Sell Jujutsu Hair\n"
            "Sell Jujutsu Shirt\n"
            "Sell Jujutsu Pants\n"
            "Sell Jujutsu Scarf\n"
            "Sell Jujutsu Shoes\n"
            "Sell Weather Machine - Black Hole\n"
            "Sell Wolf Gate\n"
            "Sell Dark Castle Stone\n"
            "Sell Dark Castle Stone Background\n"
            "Sell Dark Castle Door\n"
            "Sell Dark Castle Turret\n"
            "Sell Dire Wolf Mask\n"
            "Sell Howling Wolf Emblem\n"
            "Sell Wolf Tamer's Glove\n"
            "Sell Riding War Wolf\n"
            "Sell Wolf Whistle\n"
            "Sell Gemmin' Juice\n"
            "Sell Wolf Skull Shoulders\n"
            "Sell Raven Wings\n"
            "Sell No-Face Howler\n"
            "Sell Anvil Mountain\n"
            "Sell Dire Wolf\n\n"
            "**Buy All Wolf Items DM**"
        )
    },
    # 40. Geiger / Nuclear
    {
        "nama": "BUY/SELL GEIGER",
        "channel_id": "806507394791768094",
        "pesan": (
          "**SELL GEIGER ITEMS AT PHBS**\n\n"
"Sell Digital Sign\n"
"Sell Star Fuel\n"
"Sell Nuclear Fuel\n"
"Sell Radioactive Chemical\n"
"Sell Geiger Charger\n"
"Sell D Battery\n"
"Sell Glowstick\n"
"Sell Orange Stuff\n"
"Sell Purple Stuff\n"
"Sell Blue Stuff\n"
"Sell Green Stuff\n"
"Sell Red Stuff\n"
"Sell White Stuff\n"
"Sell Black Stuff\n\n"
"**Buy All Chemicals & Geiger Items DM**"
        )
    },
    # 41. Ghost Hunter
    {
        "nama": "BUY/SELL GHOST HUNTER",
        "channel_id": "762435265025277993",
        "pesan": (
            "**Sell GHOST HUNTING ITEMS AT PHBS**\n\n"
            "Sell Ghost Jar\n"
            "Sell Ghost-In-A-Jar (GIJ)\n"
            "Sell Mind-Ghost-In-A-Jar\n"
            "Sell Ghost Dragon Charm (GDC)\n"
            "Sell Ghost Charm\n"
            "Sell Boss Goo\n"
            "Sell Spirit Storage Unit (SSU)\n"
            "Sell Containment Field\n"
            "Sell Power Node\n"
            "Sell Ghost-Be-Gone (GBG)\n"
            "Sell Dark Spirit Board\n"
            "Sell Spirit Board\n"
            "Sell Spectral Goggles\n"
            "Sell Synthetic Oculum\n"
            "Sell Neutron Pack\n"
            "Sell Neutron Gun\n"
            "Sell Rubber Boots\n"
            "Sell Foil Hat\n"
            "Sell Mysterious Portal\n"
            "Sell Ecto Bones\n"
            "Sell Otherworldly Block\n"
            "Sell Crystallized Ghost\n"
            "Sell Bone Spike\n"
            "Sell Warning Block\n"
            "Sell Fuse Box\n"
            "Sell Dumpster\n\n"
            "**Buy All Ghost Items DM**"
        )
    },
    # 42. Pagoda 
    {
        "nama": "BUY/SELL PAGODA",
        "channel_id": "847208477553066025",
        "pesan": (
            "**Sell PAGODA & TOURNAMENT ITEMS AT PHBS**\n\n"
            "Sell Stone Pagoda\n"
            "Sell Stone Pagoda Base\n"
            "Sell Stone Pagoda Roof Element\n"
            "Sell Decorative Roof Dragon\n"
            "Sell Wooden Pagoda Roof\n"
            "Sell Wooden Pagoda Wall\n"
            "Sell Wooden Pagoda Window\n"
            "Sell Wooden Pagoda Door\n"
            "Sell Pagoda Tower Block\n"
            "Sell Grand Jade Platform\n"
            "Sell Paper Wall\n"
            "Sell Master Peng Stonework\n"
            "Sell Jade Portcullis\n"
            "Sell Jade Dragon Statue\n"
            "Sell Tournament Ticket\n"
            "Sell Pow Stones\n"
            "Sell Wasabi Peas\n"
            "Sell Popcorn\n"
            "Sell Ramune\n"
            "Sell Can Of Beans\n\n"
            "**Buy All Pagoda Items DM**"
        )
    },
    # 43. Consumables
    {
        "nama": "BUY/SELL CONSUMABLES",
        "channel_id": "847201895873118218",
        "pesan": (
            "**Sell CONSUMABLES & FOOD AT PHBS**\n"
            "AI Brain, Birth Certificate, Anniversary Skyrocket, Antidote, Antimatter Dust, "
            "Autumn Bomb, Balloon Fragment, Balloon Repellent, Ban Wand, Beach Blast, "
            "Biotronic Brain Enhancer, Black Friday Black Box, Cashback Coupon, Bountiful Seed Pack, "
            "Cave Blast, Celestial Dust, Change of Address, Apple Pie, Apple Strudel, "
            "Arroz Con Pollo, BBQ Bacon Burger, Berry Crepes, Beer-Battered Fish And Chips, "
            "Blueberry Muffin, Blueberry Pie, Burrito, Chocolate Bunny, Chocolate Easter Bilby, "
            "Coconut Tart, Composer's Cookie, Chips And Guacamole, Ancestor Mooncake, "
            "Balance Mooncake, Courage Mooncake, Barf Gross Bean, Booger Gross Bean, "
            "Candy Cane Bait, Candy Corn, Candy Heart, Black Contact Lens, Blue Contact Lens, "
            "Black Eye Drops, Blue Eye Drops, Black Hair Dye, Blue Hair Dye, "
            "Contact Lens Cleaning Solution, Block Glue, "
            "Buy All Items DM "
        )
    },
    # 44. World Sales
    {
        "nama": "BUY/SELL WORLD",
        "channel_id": "734717853965615124",
        "pesan": (
          "**SELL WORLD & NAME LIST**\n"
            "• CHEFF + PHBS (Perma Link): 10 BGL (Good For Food Shop + 4 Letter Promote)\n"
            "• PHBS (Perma Link): Taking Offers\n"
            "• KAKUL (Vend Shop): 20 BGL (Auto People Daily #SHOP)\n"
            "• DZEH (Clear World): 3 BGL\n"
            "• PHIRS: 5 BGL (Auto People Daily Promote On Discord All Channels)\n"
            "• 8QBH: 270 DL (Cloud + Display Block Full World)\n\n"
            "**SELL TYPO NAMES:**\n"
            "BUYJAJUTSU, SELLJAJUTSU, SELLCORNMEALSS, SELLBACKGROUNDD, BUYTOASTEDVILLAGEWALLP, "
            "SELLWEATHERMACHINERAIN, SELLWINTERHOLIDAY, SELLPOPPYBLOCKSEED+S, BUYCOMBERW, "
            "BUYNOTEF, BUYDREAMFORESTDIRTB+SELL, BUYADBLOCKG, SELLBAITB, SELLBAITG, "
            "SELLDIGIE, BUYALIENBLOCKSS, SELLTERRACOTTABLOCK+S, BUYMOSSYY, SELLFRUITWARIORS, BUYFENCEW\n\n"
            "**5 LETTER NAMES (Taking Offers):**\n"
            "HCIUG, UAGAX, VLCDI, PHIRF, VWTYP, FRUGG, ZHGAU, AQIVR, FMGEE, HACSE, "
            "WNPYK, FALHR, FALHS, FALHP, WKXOT, BNKTR, HGGOE, TJYXN, YYJGW, HMQAB, "
            "ZFDHY, IZAQR, IFDBB, ZEZGJ, IQLJZ\n\n"
            "Buy all 4-5 letter DM "
        )
    },
   # 45. Crime Card
    {
        "nama": "BUY/SELL CRIME",
        "channel_id": "742546954503848006",
        "pesan": (
            "**SELL SUPERPOWER CARDS AT PHBS**\n\n"
            "Sell Heat Vision\n"
            "Sell Incinerate\n"
            "Sell Flame On!\n"
            "Sell Liquify\n"
            "Sell Overheat\n"
            "Sell Ice Shards\n"
            "Sell Frost Breath\n"
            "Sell Ice Barrier\n"
            "Sell Puddle\n"
            "Sell Frozen Mirror\n"
            "Sell Super Strength\n"
            "Sell Super Speed\n"
            "Sell Enrage\n"
            "Sell Crush\n"
            "Sell Regeneration\n"
            "Sell Shocking Fist\n"
            "Sell Thunderstorm\n"
            "Sell Overcharge\n"
            "Sell Megawatt Pulse\n"
            "Sell Resuscitate\n"
            "Sell Comet Strike\n"
            "Sell Star Burst\n"
            "Sell Lunar Barrier\n"
            "Sell Nebula Gas\n"
            "Sell Death Ray\n"
            "Sell Ban Hammer\n"
            "Sell G-Virus\n"
            "Sell Duct Tape\n"
            "Sell Alien Egg\n"
            "Sell Lucky Shot\n"
            "Sell Egg Shield\n"
            "Sell Atomic Backbreaker\n"
            "Sell Pineapple Spear\n"
            "Sell Life Harvest\n"
            "Sell Crime Wave\n"
            "Sell Henchman\n\n"
            "**Buy All Superpower Cards DM**"
        )
    },
    # 46. Essence & Elements
    {
        "nama": "BUY/SELL ESSENCE",
        "channel_id": "782720570143277116",
        "pesan": (
            "**SELL ESSENCE & ELEMENTS AT PHBS**\n\n"
            "Sell Earth Essence\n"
            "Sell Fire Essence\n"
            "Sell Water Essence\n"
            "Sell Wind Essence\n"
            "Sell Aurora\n"
            "Sell Anemone\n"
            "Sell Waterfall\n"
            "Sell Lava Lamp\n"
            "Sell Fissure\n"
            "Sell Obsidian\n"
            "Sell Hourglass\n\n"
            "**Buy All Essence Items DM**"
        )
    },
    # 47. Chemicals & Fuel
    {
        "nama": "BUY/SELL CHEMICAL",
        "channel_id": "762448042011000842",
        "pesan": (
            "**SELL CHEMICAL & FUEL AT PHBS**\n\n"
            "Sell Fuel Pack\n"
            "Sell Forcefield\n"
            "Sell Slime\n"
            "Sell Shockinator\n"
            "Sell Blue Chemical\n"
            "Sell Pink Chemical\n"
            "Sell Red Chemical\n"
            "Sell Green Chemical\n"
            "Sell White Chemical\n"
            "Sell Yellow Chemical\n"
            "Sell Block Glue\n\n"
            "**Buy All Chemicals DM**"
        )
    },
    # 48. Growmoji
    {
        "nama": "BUY/SELL GROWMOJI",
        "channel_id": "782911415676960778",
        "pesan": (
            "**SELL GROWMOJI ITEMS AT PHBS**\n"
            "Sell Growmoji Oops Sell Growmoji Sleep Sell Growmoji Punch Sell Growmoji Broken Heart "
            "Sell Growmoji Cry Sell Growmoji Party Sell Growmoji World Lock Sell Growmoji Grow "
            "Sell Growmoji Gems Sell Growmoji Growtoken Sell Growmoji Plead Sell Growmoji Vend "
            "Sell Growmoji Bunny Sell Growmoji Cactus Sell Growmoji Peace Sign Sell Growmoji Terrified Face "
            "Sell Growmoji Trollface Sell Growmoji Halo Sell Growmoji Nuke Sell Growmoji Super Pineapple "
            "Sell Growmoji Football Sell Growmoji Fireworks Sell Growmoji Songpyeon Sell Growmoji Ghost "
            "Sell Growmoji Evil Devil Sell Growmoji Pizza Sell Growmoji Alien Sell Growmoji Clapping Hands "
            "Sell Growmoji Turkey Sell Growmoji Gift Sell Growmoji Cake Sell Growmoji Heart with Arrow "
            "Sell Growmoji Shamrock Sell Growmoji Grin Sell Growmoji Ill Sell Growmoji Eyes "
            "Sell Growmoji Weary Sell Growmoji Moyai\n\n"
            "Buy All Growmojis DM "
        )
    },
    # 49. Paint & Dye
    {
        "nama": "BUY/SELL PAINT",
        "channel_id": "774455258407370752",
        "pesan": (
            "**SELLING CHEAP PAINT AT PHBS**\n\n"
            "Sell Varnish\n"
            "Sell Aqua Paint\n"
            "Sell Blue Paint\n"
            "Sell Charcoal Paint\n"
            "Sell Green Paint\n"
            "Sell Purple Paint\n"
            "Sell Red Paint\n"
            "Sell Yellow Paint\n"
            "Sell Paint Brush\n"
            "Sell Portrait\n"
            "Sell Posh Portrait\n"
            "Sell Painting Easel\n"
            "Sell Black Hair Dye\n"
            "Sell Red Hair Dye\n"
            "Sell Blue Hair Dye\n"
            "Sell Green Hair Dye\n"
            "Sell Black Contact Lens\n"
            "Sell Red Contact Lens\n"
            "Sell Green Contact Lens\n"
            "Sell Blue Contact Lens\n"
            "Sell Eye Cleaning Solution\n"
            "Sell Blue Eye Drops\n"
            "Sell Red Eye Drops\n"
            "Sell Black Eye Drops\n"
            "Sell Green Eye Drops\n\n"
            "**Buy All Paint & Dye DM**"
        )
    },
    # 50. Blast
    {
        "nama": "BUY/SELL BLAST",
        "channel_id": "782718823488290826",
        "pesan": (
            "**SELL WORLD BLASTS AT PHBS**\n\n"
            "Sell Beach Blast\n"
            "Sell Bountiful Blast\n"
            "Sell Cave Blast\n"
            "Sell Desert Blast\n"
            "Sell Jungle Blast\n"
            "Sell Mars Blast\n"
            "Sell Monochrome Blast\n"
            "Sell Thermonuclear Blast\n"
            "Sell Treasure Blast\n"
            "Sell Undersea Blast\n"
            "Sell SurgWorld Blast\n"
            "Sell Harvest Moon Blast\n"
            "Sell CandyLand Blast\n"
            "Sell Greezak Starship Blast\n"
            "Sell HyperTech Starship Blast\n"
            "Sell Imperial Starship Blast\n"
            "Sell Stellarix Starship Blast\n\n"
            "**Buy All Blasts DM**"
        )
    },
    # 51. Crystals
    {
        "nama": "BUY/SELL CRYSTAL",
        "channel_id": "742547014197313576",
        "pesan": (
            "**SELL CRYSTAL AT PHBS**\n\n"
            "Sell Blue Crystal\n"
            "Sell Red Crystal\n"
            "Sell White Crystal\n"
            "Sell Black Crystal\n"
            "Sell Kaleidoscopic Block\n"
            "Sell Shifty Block\n"
            "Sell Amethyst Block\n"
            "Sell Sapphire Block\n"
            "Sell Opal Block\n"
            "Sell Onyx Block\n"
            "Sell Topaz Block\n"
            "Sell Crystal Gate\n"
            "Sell Stained Glass\n"
            "Sell Crystal Block\n\n"
            "**Buy All Crystals DM**"
        )
    },
    # 52. Weather & Machines
    {
    "nama": "BUY/SELL WEATHER",
    "channel_id": "782722952256159754",
    "pesan": (
        "**SELL WEATHER MACHINE & VENDING MACHINE AT PHBS**\n\n"
"Sell Vending Machine\n"
"Sell Digivend Machine\n"
"Sell Vending Hub Checkout Counter\n"
"Sell Bubble Machine\n"
"Sell Smoke Machine\n"
"Sell Snowy Machine\n"
"Sell Rainy City\n"
"Sell Snowy\n"
"Sell Snowy Night\n"
"Sell Dark Mountain\n"
"Sell Crack In Reality\n"
"Sell Background\n"
"Sell Infinity\n"
"Sell Arid\n"
"Sell Autumn\n"
"Sell Jungle\n"
"Sell Mt Growmore\n"
"Sell Night\n"
"Sell Stargazing\n"
"Sell Spooky\n"
"Sell Stuff\n"
"Sell Plaza\n"
"Sell St Paddy Day\n"
"Sell Warp Speed\n"
"Sell Valentines\n"
"Sell Celebrity Hills\n"
"Sell Sunny\n"
"Sell Frozen Cliffs\n"
"Sell Holiday Haven\n"
"Sell Nians Mountain\n"
"Sell Spring\n"
"Sell Protostar Landing\n"
"Sell Pineapple\n"
"Sell Rainin Gems\n"
"Sell South Pole\n"
"Sell Nothingness\n\n"
"**BUY ALL WEATHER & VEND DM**"
        )
    },
    # 53. Jammers & Tools
    {
        "nama": "BUY/SELL JAMMER",
        "channel_id": "806523338797219860",
        "pesan": (
            "**SELL JAMMERS & SECURITY AT PHBS**\n\n"
            "Sell Signal Jammer\n"
            "Sell Punch Jammer\n"
            "Sell Zombie Jammer\n"
            "Sell Firehouse\n"
            "Sell Ghost Charm\n"
            "Sell Antigravity Generator\n"
            "Sell Mini-Mod\n"
            "Sell Pigeon\n"
            "Sell Security Camera\n"
            "Sell Starship Security Camera\n"
            "Sell Door Mover\n"
            "Sell Change Of Address\n"
            "Sell Birth Certificate\n"
            "Sell Lock Mover\n"
            "Sell Safe Vault\n"
            "Sell Music Amplifier\n"
            "Sell Game Generator\n"
            "Sell Transmutabooth\n"
            "Sell Phone Booth\n"
            "Sell Spotlight\n"
            "Sell Guardian Pineapple\n\n"
            "**Buy All Jammers & Tools DM**"
        )
    },
    # 54. Mines Block
    {
        "nama": "BUY/SELL MINES",
        "channel_id": "889189591083520060",
        "pesan": (
            "**SELL MINING Item AT PHBS**\n"
            "Sell Magic Armor Plate Design Sell Smoke Machine Sell Eldritch Eyes Sell Mageblade "
            "Sell Balrog Tails Sell Balrog Wings Sell Armored Riding Troll Sell Lightning Gauntlets "
            "Sell Golden Apple Sell Engineer Helmet Sell Engineer Goggles Sell Strange Eyes "
            "Sell Pet Moyaimorph Sell Crystal Block Sell Ruby Block Sell Emerald Block "
            "Sell Topaz Block Sell Sapphire Block Sell Onyx Block Sell Shifty Block "
            "Sell Golden Treasure Hoard Sell Aqua Cave Crystal Sell Golden Cave Crystal "
            "Sell Mining Explosives Sell Cobblestone Block Sell Mossy Cobblestone Block "
            "Sell Magic Stones Sell Deep Iron Ore Sell Hand Torch Sell Dwarven Wall "
            "Sell Cave Dirt Sell Crystal Block Seed Sell Emerald Seed Sell Ruby Block Seed\n\n"
            "Buy All Mining Items DM "
        )
    },
    # 55. Locks
    {
        "nama": "BUY/SELL LOCK",
        "channel_id": "878779329864167504",
        "pesan": (
          "**SELL LOCKS AT PHBS**\n\n"
            "Sell Small Lock\n"
            "Sell Big Lock\n"
            "Sell Huge Lock\n"
            "Sell Builder's Lock\n"
            "Sell Radical City Lock\n"
            "Sell Blood Dragon Lock\n"
            "Sell Assassin's Lock\n"
            "Sell Rayman's Lock\n"
            "Sell Legendary Lock\n"
            "Sell Steampunk Lock\n"
            "Sell Robotic Lock\n"
            "Sell Persian Lock\n"
            "Sell Bunny Lock\n"
            "Sell Fenyx Lock\n\n"
            "**Buy All Locks DM**"
        )
    },
    # 56. Music Sheet
    {
        "nama": "BUY/SELL MUSIC",
        "channel_id": "782718975091933214",
        "pesan": ( "SELL SHEET MUSIC AT PHBS\n\n"
    "Sheet Music Blank Sheet Music Drums Sheet Music Piano Note Sheet Music Flat Piano Sheet Music Sharp Piano "
    "Sheet Music Bass Note Sheet Music Flat Bass Sheet Music Sharp Bass Sheet Music Flute Note Sheet Music Flat Flute "
    "Sheet Music Sharp Flute Sheet Music Lyre Note Sheet Music Flat Lyre Sheet Music Sharp Lyre Spanish Guitar Note "
    "Sheet Music Flat Spanish Guitar Sheet Music Sharp Spanish Guitar Mexican Trumpet Flat Mexican Trumpet "
    "Sheet Music Sharp Mexican Trumpet Violin Note Flat Violin Sharp Violin Sheet Music Sax Note "
    "Sheet Music Flat Sax Sharp Sax Electric Guitar Flat Electric Guitar Sharp Electric Guitar "
    "Sheet Music Spooky Winterfest Repeat End Repeat Begin Audio Gear Audio Rack Mega Rock Speaker "
    "Boombox Military Radio Music Box Mystic Recorder Player Olde Timey Radio Victrola Disco Ball Note Block Head Bangin Steel Wolf "
    "Hula Bubblehead Dancing Reindeer Dancing Snow Globe Dancing Candle Wind up Musical Box Love Birds."
        )
    },
    # 57. Unicorn & Retro
    {
        "nama": "BUY/SELL UNICORN",
        "channel_id": "879846165196181616",
        "pesan": (
            "**SELL UNICORN & RAINBOW ITEMS AT PHBS**\n\n"
            "Sell Clouds\n"
            "Sell Dreamstone Block\n"
            "Sell Rainbow Block\n"
            "Sell Rainbow Wig\n"
            "Sell Enchanted Spatula\n"
            "Sell Happy Unicorn Block\n"
            "Sell Angry Unicorn Block\n"
            "Sell Unicorn Jumper\n"
            "Sell Horse Mask\n"
            "Sell Scroll Bulletin\n"
            "Sell Very Bad Unicorn\n"
            "Sell Unicorn Horn\n"
            "Sell Teddy Bear\n"
            "Sell Gift Of The Unicorn\n"
            "Sell Retro Leg Warmers\n"
            "Sell Rainbow Scarf\n"
            "Sell Twintail Hair\n"
            "Sell Growmoji Cool Shades Mask\n"
            "Sell Cartoon Glove Hat Red\n"
            "Sell Cartoon Glove Hat Blue\n"
            "Sell That 90's Hair\n"
            "Sell Freaky Fried Egg Eyes\n"
            "Sell Peas In A Pod Hat\n"
            "Sell Pet Pink Crocodile\n"
            "Sell Death Top Stompers\n\n"
            "**Buy All Rainbow Items DM**"
        )
    },
    # 58. Steam Items
    {
        "nama": "BUY/SELL STEAM",
        "channel_id": "806499108801478676",
        "pesan": (
            "**SELL STEAMPUNK & STEAM ITEMS AT PHBS**\n\n"
            "Sell Steam Bellows\n"
            "Sell Steam Collector\n"
            "Sell Steam Crank\n"
            "Sell Steam Crossover\n"
            "Sell Steam Door\n"
            "Sell Steam Engine\n"
            "Sell Steam Funnel\n"
            "Sell Steam Funnel - Down\n"
            "Sell Steam Funnel - Up\n"
            "Sell Steam Gear\n"
            "Sell Steam Lamp\n"
            "Sell Steam Launcher\n"
            "Sell Steam Lifter Piston\n"
            "Sell Steam Organ\n"
            "Sell Steam Pipe\n"
            "Sell Steam Piston\n"
            "Sell Steam Revolver\n"
            "Sell Steam Riser Bellows\n"
            "Sell Steam Scrambler\n"
            "Sell Steam Spikes\n"
            "Sell Steam Stomper\n"
            "Sell Steam Tubes\n"
            "Sell Steam Vent\n"
            "Sell Steam Valve\n"
            "Sell Steampunk Sprocket\n\n"
            "**Buy All Steampunk Items DM**"
        )
    },
    # 59. Providers
    {
        "nama": "BUY/SELL PROVIDERS",
        "channel_id": "880294786236579860",
        "pesan": (
            "**SELL PROVIDER ITEMS AT PHBS**\n\n"
            "Sell ATM Machine\n"
            "Sell Awkward Friendly Unicorn\n"
            "Sell Balloon Filling Station\n"
            "Sell Buffalo\n"
            "Sell Building Blocks Machine\n"
            "Sell Chicken\n"
            "Sell Coffee Maker\n"
            "Sell Cow\n"
            "Sell Diamond Builders Bonanza\n"
            "Sell Science Station\n"
            "Sell Sheep\n"
            "Sell Silkworm\n"
            "Sell Star Tool Droid\n"
            "Sell Surgical Tool Bag\n"
            "Sell Tackle Box\n"
            "Sell Tea Set\n"
            "Sell Well\n"
            "Sell Well Of Love\n"
            "Sell Wonder Provider\n"
            "Sell Winterfest Calendar 2017\n"
            "Sell Winterfest Calendar 2018\n"
            "Sell Winterfest Calendar 2019\n"
            "Sell Winterfest Calendar 2020\n"
            "Sell Winterfest Calendar 2021\n"
            "Sell Winterfest Calendar 2022\n"
            "Sell Winterfest Calendar 2023\n"
            "Sell Winterfest Calendar 2024\n"
            "Sell Winterfest Calendar 2025\n\n"
            "**Buy All Providers DM**"
        )
    },
    # 60. Adventure
    {
        "nama": "BUY/SELL ADVENTURE",
        "channel_id": "900812336116416563",
        "pesan": (
            "**SELL ADVENTURE ITEMS AT PHBS**\n\n"
            "Sell Adventure's End\n"
            "Sell The Adventure Begins\n"
            "Sell Checkpoint\n"
            "Sell Flower Checkpoint\n"
            "Sell Adventure Checkpoint\n"
            "Sell Adventure Barrier\n"
            "Sell Locked Adventure\n"
            "Sell Adventure Item - Golden Idol\n"
            "Sell Adventure Item - Key\n"
            "Sell Adventure Item - Banana\n"
            "Sell Adventure Item - Pineapple\n"
            "Sell Adventure Item - Torch\n"
            "Sell Adventure Item - Rope\n"
            "Sell Adventure Item - Crystal Goblet\n"
            "Sell Hanging Snake\n"
            "Sell Adventure Gorilla\n"
            "Sell Lazy Cobra\n"
            "Sell Adventure Braizer\n"
            "Sell Adventure Rope Piton\n\n"
            "**Buy All Adventure Items DM**"
        )
    },
    # 61. Rune & Ice
    {
        "nama": "BUY/SELL RUNE & ICE",
        "channel_id": "806499467711742002",
        "pesan": (
            "**SELL ICE & RUNE ITEMS AT PHBS**\n\n"
            "Sell Frozen Stone Cliffs\n"
            "Sell Rune Stone\n"
            "Sell Rune Carved Stone Pillar\n"
            "Sell Glacier Background\n"
            "Sell Altar\n"
            "Sell Icicles\n"
            "Sell Ice\n"
            "Sell Hidden Treasure\n"
            "Sell Water Bucket\n\n"
            "**Buy All Ice Items DM**"
        )
    },
    # 62. Mage Items
    {
        "nama": "BUY/SELL MAGE",
        "channel_id": "1324916884205998242",
        "pesan": (
            "**SELL DUNGEON & MAGIC ITEMS AT PHBS**\n\n"
            "Sell Enchanted Iron Bars\n"
            "Sell Magic Prism Background\n"
            "Sell Mage's Curtains\n"
            "Sell Magic Cobblestone Column\n"
            "Sell Moon Greatsword Block\n"
            "Sell Mage's Chest\n"
            "Sell Altered Throne\n"
            "Sell Blade Of Revolt\n"
            "Sell Seat Of Power Banner\n"
            "Sell Mage's Bookcase\n"
            "Sell Grace Of Light\n"
            "Sell Pet Mimic Chest\n"
            "Sell Crystal Ball Head\n"
            "Sell Mage's Pedestal\n\n"
            "**Buy All Dungeon Items DM**"
        )
    },
    # 63. Hair / Anime Hair
    {
        "nama": "BUY/SELL HAIR",
        "channel_id": "889183252735225886",
        "pesan": (
         "**SELL VARIOUS HAIR AT PHBS**\n\n"
            "Sell Crazy Purple, Purple Mohawk, Spikey Hair, Janeway Hair, Hot Head, Preppy Blonde, "
            "Sell Red Hair, Messy Brown, Strawberry Hair, Old Rocker, Streak Hair, Long Blonde Bangs, "
            "Sell Platinum Blonde, Flat Top, Slick Black, Long Brown, Ornamental Hair Fan, Liberty Hair, "
            "Sell Mochi Twintails, Neat Bun, Curly Hair, Buzz Cut, Undercut, Pineapple Hair, Jankom Hair, "
            "Sell Braided Hair, Farmgirl Hair, Pigtails, Ginger Bun, Grey Hair, Messy Auburn, Ponytails, "
            "Sell Hot Pink Highlight, Black Braids, Long Black Bangs, Frankenhair, Afro, Creepy Hair, "
            "Sell Malevolent Hair, Spikey Anime, Anime Male/Female, Gem Hair, Roughed Up Anime, "
            "Sell Tousled Hair, Birthday Band, Daring Dandy, Short Surfer, Statesman, Presidential Wig, "
            "Sell Mysterious Detective, Emo Hair, Rainbow Hair, Weekend Raver, Gwyn, Fruit Warrior\n\n"
            "Buy All Hair Items DM "
        )
    },
    # 64. Roles Drops Farmer & Fishing
    {
        "nama": "BUY/SELL DROPS BLOCK",
        "channel_id": "782718661336760380",
        "pesan": (
            "**SELL VARIOUS DROPS AT PHBS**\n\n"
            "Sell Beat Root Block\n"
            "Sell Fallen Pillar\n"
            "Sell Carrot Block\n"
            "Sell Broccoli Mini Tree\n"
            "Sell Strawberry Block\n\n"
            "**Buy All Items DM**"
        )
    },
    # 65. Hat / Anime Hat
    {
        "nama": "BUY/SELL HAT",
        "channel_id": "900863315381739651",
        "pesan": (
            "**SELL HAT AT PHBS**\n\n"
            "Flower Headbands, Dried Leaf Crown, Old Timey Hat, Cowboy Hat, Pirate Hat, Ringmaster Hat, Foxy Hat, Vampire Hunter Hat, Red Brimmed Hat, Coconut Crown, Cupcake Hat, Knight Helmet, Flamingo Hat, Viking Hat, Froghat, Baseball Cap, Backward Ballcap, Spelunker Headlamp, Dinosaur Mask, Reanimated Howly Hat, Pooka Hood, Howly Hat, Doompunk Top Hat, Grey Cat as a Hat, Pink, Blue Cat Hat, Orange Cat Hat, Chip and Dip, Silk Turban, Outback Hat, Raspberry Beret, Starfire Crown, Stained Glass Crown, Txmom Crown, Heartking Crown, Heartqueen Crown, Guild Challange Crown, Heart of Diamond Crown, Heartthrob Helm, Pineapple Coronet, Flare Fedora, Fedora, Black Beret, Slouch Beanie, Straw Fedora, Floppy Straw Sun Hat, Pith Helmet, Blue Hardhat, Red Dragon Legs, Body, Tail, Head, Red Volcanic Hat, Blue Volcanic Hat, Santa Hat, Rooster Hat, Growch Hat, Straw Hat, Oceanic Crown\n\n"
            "Buy All Items DM "
        )
    },
    # 66. Face Items
    {
        "nama": "BUY/SELL FACE",
        "channel_id": "944657054377836645",
        "pesan": (
            "**SELL FACE AT PHBS**\n\n"
            "Spring Flinger Squirrel, Frog Mask, Wicked Wizard Scar, Super Utility Helmet Red, Yellow, Chef Cap, Pilgrim Hat, Bunny Beanie, Chichen Itza Hat, Mountain Cap, Winter Bush Hood, Lars Lamora Miner Helmet, Greezak Horde Warrior Helmet, Axolotl, Flaming Skull Mask, Demented Cowl, Cultist Hood, Edvoid Mistake, Neon Voodoo Mask, Pure White, Ghost Costume, Diving Bell, Space Helmet, Zeta, Barky Mask, Growmoji Wow Mask, Octopus Head, Cardboard Box, TV Head, Grow Punk Helmet, Astronaut Helmet, Scarecrow Mask, Crystal Mask, Ghost Wolf Monocle, Rave Safe Mask, Techno Visor, Snow Goggles, Futuristic Sunglasses, Pacifier, Eyepatch, Vampire Fangs, Blue Headbands, Growbeats Headphones, Shades, Strange Eyes, Space Opera Mask, Sad Mask, Swordsman Mask, Seafoam Beard, Ghost Costume, Demented Cowl, Freezing, Oxen Battle Helm, Bean Visor, Crown of Enlightenment, Marching Band Hat, Pocong Mask, Pocong Clothes, Snowfrost Top Hat, Hazmat Helmet,\n\n"
            "Buy All Items DM "
        )
    },
    # 67. High Value Items / Necklaces & Charms
    {
        "nama": "BUY/SELL HIGH VALUE ITEMS",
        "channel_id": "762434767912173588",
        "pesan": (
            "**BUY VARIOUS ITEMS AT PHBS**\n\n"
            "Buy Tiger Pauldrons 8 dl, Sam Fisher 75 dl, Cauldron Of Dagda 1820 wl, Astral Crest 37 dl, Amber Necklace 48 dl, Celestial Dragon Charm 55 dl, Speed Medalion 7 bgl, Shamrock Shield 3600 wl, Royal Primal Spirit 40 dl, Feathered Scarf 67 dl, Zraei Dragoscarf 290 dl, Pharaoh Pendant 29 dl, World Owner Blingin Chain 37 dl, Royal World Owner Blingin Chain 75 dl, Primal Spirit 35 dl, Diamond Dust 630 wl, Crystal Shard Necklace 610 wl, Bear Spirit 33 dl, Purple Scarf 20.5 dl, Astral Aura Dragon 352 dl, Royal Scarf Of Chains 240 dl, Mantle Of Chang'e 670 wl, Spiked Collar 2 dl, Shark Tooth Necklace 1130 wl, Ghost Dragon Charm 21 dl, Celebration Charm 11 dl, Northern Lights Aura 2.1 dl, Royal Astral Crest 64 dl, Black Ultraviolet Charm 39 dl, Scarf Of Prometheus 16 dl, Soulbinder 77 dl, Astral Aura Lion 305 dl, Astral Aura Rabbit 270 dl, Black Bowtie 2340 wl, Equinox Scarf 62 dl, Sargon Bandolier 61 dl, Cresent Charm 4110 wl, Chili Con Charme 45 dl, Scarf Of Chains 65 dl, Royal Cresent Charm 70 dl\n\n"
            "DM  to Sell"
        )
    },
    # 68. Silk Vests & Shirts
    {
        "nama": "BUY/SELL VEST",
        "channel_id": "944660041636659271",
        "pesan": (
            "**SELL ALL CHEAP AT PHBS**\n\n"
            "Silk Vest (Black, Blue, Green, Grey, Purple, Red), Winter Turtleneck, Neon Nerves, Hideous Holiday, Country Tweed Jacked & Yellow Tie, Comet Shirt, Country Tweed Waistcoat & Tie, Rok Overalls\n\n"
            "Buy All Items DM "
        )
    },
    # 69. Seasonal Outfits
    {
        "nama": "BUY/SELL CLOTHES",
        "channel_id": "762434767912173588",
        "pesan": (
            "**SELL CLOTHES AT PHBS**\n\n"
            "Party Vest, Ultra Flame Tee, Tetra T-Shirt, Retro Jacket, Glitter Gown, Groom's Coat, Bridal Dress, Bunny Onesie, Fiesta Dress, Luchador Jersey, Mexican Dress, Shark Suit, Country Tweed Sets, Aviator Jacket, Air Force Flight Suit, Spring Flinger Suits, Winter Freezer Robes, Ghost Costume, Cultist Robe, Vamp Vest, Burger Suit, Barbershop Quartet Shirt\n\n"
            "Buy All Items DM "
        )
    },
    # 70. Pants & Leggings
    {
        "nama": "BUY/SELL PANTS",
        "channel_id": "949006096746578000",
        "pesan": (
            "**SELL PANTS AT PHBS**\n\n"
            "Pop Demon’s Shorts, Doompunk Leggings, Werewolf Jeans, The Chosen One Pants, That 70’s Pants, Exo Suit Pants, Barbershop Quartet Pants, Marching Band Pants, Scarlet Rider’s Pants, Mighty Legend Pants, Jodhpurs, Garuda Legs, Celestial Trousers, Vortex Skirt, Ninja Tights, Gwyn’s Pants, Jankom Pog’s Pants, Janeway’s Pants, Zero’s Legs, Tars Lamora Miner Pants, Mariachi Pants, Girl’s School Uniform Skirt, Boy’s School Uniform Pants, Firefighter Pants, Fruit Warrior Pants, Fenyx’s Skirt, Starfleet Uniform Pants, Jujutsu Pants, Hazmat Pants, Buckskin Pants, Showgirl Leggings, Toasted Villager Pants, Stars And Stripes Pants, Pop Idol’s Pants, Sami Pants, Edward’s Trousers, Ezio’s Trousers, Luchador Tights, Denim Shorts, Sargon’s Trousers, Crimson Thief Pants, Disco Dude’s Pants, Fancy Pants, Cheerful Skirt, Fishnet Stocking, Zombie Defense, Formal Rose Pants, Oxen Battle, Country Tweed Trousers\n\n"
            "Buy All Items DM "
        )
    },
    # 71. Shoes & Boots
    {
        "nama": "BUY/SELL SHOES",
        "channel_id": "900862136086061078",
        "pesan": (
            "**SELL SHOES AT PHBS**\n\n"
            "Asbestos Boots, Patent Leather Shoes, Monster Feet, Checkered Espadrille, Zombie-Stompin' Boots, Clown Shoes, Peg Leg, Climbing Boots, Black Espadrille, Ninja Slippers, Air Robinsons, Blue Star Shoes, Ruby Slippers, Fairy Slippers, Firefighter Boots, Moon Boots, High Heels (Green, Blue, Pink, Purple, Red, Yellow), Stinky Socks, Boots, Brown Shoes\n\n"
            "Selling item Cq/Dq For Cheap DM "
        )
    },
    # 72. Wings & Auras
    {
        "nama": "BUY/SELL WINGS",
        "channel_id": "762446834454495282",
        "pesan": (
            "**SELL WINGS & BACK ITEMS AT PHBS**\n\n"
            "Sell Ripper Wings, Astronaut Pack, Fairy Wings, Crimson Eagle, Jetpack, Cape of Shadows, "
            "Sell Cauldron Cannon, Dragon Warrior Cape, Fiesta Cape, Leaf Wings, Shawl of Shadows, "
            "Sell Teeny Angel/Devil Wings, Turkey Onesie Tail, Cloak of Fire and Ice, Raven Wings, "
            "Sell Mosquito King's Wings, Rainbow Crystal Cloak, Puppet Master, Snowflake Wings, "
            "Sell Matrix Aura, Cloak of S'mores, Star and Stripes Cape, Firecracker Wings, "
            "Sell Black Shadow Shawl, Pineapple Juice, Blazing Electro Wings, Confetti Jump Pack, "
            "Sell Backpack, Ezio's Cape, Shoulder Cape, Blanket Cape, Heavy Artillery, Harvest Shawl, "
            "Sell Majestic Pineapple Cape, Vampire Cape, Rose Cape, Diamond Wings, Helping Hand, "
            "Sell Waist Tied Sweater (Yellow/Red/Green/Blue), Tiger Spirit, Cosmic Cape, "
            "Sell Stone Gargoyle Wings, Orbs of Elixir, Robotic Tentacles\n\n"
            "Buy All Wings & Back Items DM "
        )
    },
    # 73. Hand Items
    {
        "nama": "BUY/SELL HAND",
        "channel_id": "889195913275408455",
        "pesan": (
       "**SELL HAND ITEMS AT PHBS**\n\n"
           "**SELL HIGH DEMAND HAND ITEMS AT PHBS**\n\n"
            "Sell DMK \n"
            "Sell Black Balrog Wings\n"
            "Sell Heartbreaker Hammer\n"
            "Sell Growsaber (Red/Blue/Black/Green)\n"
            "Sell Skull Launcher\n"
            "Sell Butcher Knife\n"
            "Sell Sushi Knife\n"
            "Sell Summer Kite\n"
            "Sell Rainbow Kite\n"
            "Sell Yeonnalligi\n"
            "Sell Datemaster's Rose\n"
            "Sell Balrog Tail\n"
            "Sell Fire Hose\n"
            "Sell Magic Magnet\n"
            "Sell Bubble Gun\n"
            "Sell Beach Ball\n"
            "Sell Heartsword\n"
            "Sell Heartstaff\n"
            "Sell Heartbow\n"
            "Sell Heatbow\n"
            "Sell Black Frost Bow\n"
            "Sell Winter Frost Bow\n"
            "Sell Silverstar Bow\n"
            "Sell Candy Cane Bow\n"
            "Sell Rainbow Bow\n"
            "Sell Primal Bow\n"
            "Sell Zeus' Lightning Bolt\n"
            "Sell Hand Scythe\n"
            "Sell Candy Cane\n"
            "Sell Diamond Flashaxe\n\n"
            "**BUY ALL HAND ITEMS DM**"
        )
    },
    # 74. Pet & Riding 
    {
        "nama": "BUY/SELL RIDING",
        "channel_id": "847208536760909874",
        "pesan": (
"**SELL PET & RIDING AT PHBS**\n\n"
"Pet Twin Cherries, Snow Leopard, Unicorn Garland, Sonar Bracelet, Riding Llama, Capuchin Leash, Missile Toad Pet, Frog, Pet Turtle, Demon Megalodon, Diamond Dog,Riding Raptor, Pet Burrito, LoveBird Pendant, Electro Magnifying Glass, Mid Pacific Owl, Dyrad, Polar Bear Leash, Playful Fire Sprite, Pegasus, Pet Pidgeon, Familliar Leash, Ice Calf Leash, Cute Mutant Wonky, Cupid Leash, Mini Mammoth Leash, Penguin Leash, Giraffe Pet, MickeyMay Leash\n\n"
"Can less? Just DM! Also Buy Cheap Pet Tons Budget 1-10000\n"
"Not on vend? Sold! DM "
        )
    },
    # 75. Various Pets & Leashes
    {
        "nama": "BUY/SELL PETS",
        "channel_id": "731475906723315752",
        "pesan": (
            "**SELL VARIOUS PETS AT PHBS**\n\n"
            "Mickeymay Leash, Pet Leprechaun, Wolf Tamers Glove, Pet Burrito, Sonar Bracelet, Mid-Pacific Owl, Butterfly Leash, Lovebird Pendant, Pineapple Kite, Haunted Pants, Electro Magnifying Glass, Ladybug Leaf, Deaths Scarf, Summer kite, Winter Flu Vaccine, Pet Frog, Ice Calf Leash, Maidmare, Leashed Silkworm- Black, Skeletal Dragon Claw, Dryad, Mini Growtopian, Thinking Cap, Yeonnalligi, Ghost Wolf Monocle, Battle Mutant Fish, Playful Fire Sprite, Playful Wind Sprite, Playful Wood Sprite, Moose Cap, Mini Mammoth leash, CRISPR Technology, Battle Cage, Pet Trainer Whistle, Haunted Synthoid, Fiesta Dragon, Strawberry Slime, Pet Slime, Flowersaurus rex, Cinder Sprites, Dragon Hand, Radioactive Synthoid, Cloud Rabbit, Ice Calf Leash, Rhino Horn, Ice Dragon Hand, Unicorn Garland, Rainbow Kite, Gingerbread Man, Phlogiston, Passionate Painter Paintbrush Pet\n\n"
            "Also buying super cheap stock please dm me!!\n"
            "Not on vend? Sold! DM "
        )
    },
    # 76. Cheap Riding
    {
        "nama": "BUY/SELL RIDING",
        "channel_id": "944668428919259177",
        "pesan": (
            "**CHEAP RIDING AT PHBS**\n\n"
"Famine's Steed, Zombie Horse, Chaos Dragon, Smoog The Great Dragon, Kelpie, Riding Rhino, "
"Floating Throne, TK69's Mystical Etherboard, Floating Leaf, Wind Surfer, Growboard, "
"StarBoard, Fruit Brigade, Edvoid's Fire-nado, Tornado Aura, Sleigh of Winter, "
"Candy Cane Cruiser, Ride'O'Gold, Harvester of Sorrows, Harvester, Dear John Tractor, "
"Sturdy Crackfire Fighter, Wheelchair Speedster, Apocalypse Steed, Growley Motorcycle, "
"Ghost Rider Bike, Ameri-car, Fire Truck, Ambulance, Riding Raven, Ice Horse, "
"Irish Sport Horsie, Tiny Horsie, Avenie Golden Horse, Skeletal Horsie, Sledding Penguin, "
"Mountain Dire Wolf, Red Bicycle, Minecart, Skateboard, Solar Chariot, Ridin' Truck, "
"Fireworks Cart, Ionic Pulse Cannon, Bek and Cal, Serpentail, Super Speeder, "
"Scavenger Wheels, Hype Train, Ghost Mobile\n\n"
"Not on vend? Sold! DM "
        )
    },
    # 77. Baits
    {
        "nama": "BUY/SELL BAITS",
        "channel_id": "709362882055241808",
        "pesan": (
          "**SELL FISHING BAITS AT PHBS**\n\n"
            "Sell Wiggly Worm\n"
            "Sell Salmon Eggs\n"
            "Sell Shiny Flashy Thing\n"
            "Sell Fishing Fly\n"
            "Sell Uranium Glowing Lure\n"
            "Sell Mega-Pellet Bait\n"
            "Sell Shrimp Lure\n"
            "Sell Otherworldly Bait\n"
            "Sell Minor Otherworldly Bait\n"
            "Sell Lesser Otherworldly Bait\n"
            "Sell Whizmo Gizmo\n"
            "Sell Candy Cane Bait\n"
            "Sell Catch-Of-The-Day Bait\n\n"
            "**Need Supplier Bait Dm**"
        )
    },
    # 78. Fishing & Sea
    {
        "nama": "BUY/SELL FISHING ITEMS",
        "channel_id": "709363155309953105",
        "pesan": (
            "**SELL FISHING & ROLE ITEMS AT PHBS**\n"
    "Electric Eel,Fishbowl,Fishing Stool,Fish Landing Platform,Great White Shark,Jellyfish,Sea Lantern,Seaweed,"
    "Battle Trout,Fishnet Stocking,Shield Fragment,Lobster Trap,Fish Wall Mount,Large Radioactive Bit,"
    "Large Frozen Chunk,Cooler Box,Davy Jones Chest,Fancy Fish Wall Mount,Ice Crust Block,Puffer Fish Block,"
    "Queen Conch Shell,Sea Urchin,Aqua Cave Crystal,Copper Block,Radiation Block,Radiation Sign,Tentacle Beard,"
    "Water Bucket,Uranium Block,Nuclear Detonator,Hand Drill,Training Port,Fish Tank Port,Fish Tank,Fish Medicine,"
    "Fish Reviver,Fish Flakes,Cutting Board,Vile Vial Brainworms,Fish Chunk,Shark Tooth,Aquamarine Stone,"
    "Sea Sponge,Oil Slick,Naval Mine,Quantum Starfish,Primordial Ooze,Mint,Undersea Blast,Fishing Supply Crate,"
    "\n**BUY ALL FISHING & ROLE ITEMS DM **"
        )
    },
    # 79. Fishing Rods 
    {
        "nama": "BUY/SELL FISHING RODS",
        "channel_id": "709363256220712981",
        "pesan": (
            "**SELL FISHING RODS AT PHBS**\n\n"
            "Sell E-Z Rod\n"
            "Sell Fishing Rod\n"
            "Sell Reliable Anomarod\n"
            "Sell Pristine Anomarod\n"
            "Sell Exquisite Anomarod\n"
            "Sell Cursed Rod\n"
            "Sell Licorice Fishing Rod\n"
            "Sell Golden Rod\n"
            "Sell Magical Rainbow Fishing Rod\n"
            "Sell Elegant Anomarod\n"
            "Sell Thanksgiving Dinner Fishing Rod\n\n"
            "**Not on vend? Sold!**"
        )
    },

# 80. Perfect Seafood & Traps
    {
        "nama": "BUY/SELL LOBSTER TRAPS",
        "channel_id": "709363456125435934",
        "pesan": (
            "**SELL LOBSTER TRAPS AT PHBS**\n\n"
            "Sell Lobster Trap 10 wl each\n"
            "Buy Perfect Alaskan King Crab (PAKC) 250 dl\n"
            "Buy Placed Lobster Trap 5 wl each\n\n"
            "Not on vend? Sold! DM "
        )
    },
# 81. All Blocks (SSP/RSP)
    {
        "nama": "BUY/SELL BLOCKS",
        "channel_id": "1104057271215984741",
        "pesan": (
        "**SELL BLOCKS AT PHBS**\n"
"Sell: Shifty Block, Crystal Block, Emerald Block, Ruby Block, Topaz Block, "
"Sapphire Block, Dimension Block, Snowflake Block, Roulette Wheel, FirePlace, "
"Transmatter Field, Donation Box, Donut Donation Box, Holiday Gift Box, "
"Glowy Block, Cutaway Building, Basic Blue Block, Xenoid Block, Clouds, Pillar, "
"Fallen Pillar, Candy Cane Block, Rainbow Block, Toasted Village Wall, Hedge, "
"Dragon Gate, Treasure Chest, Golden Block, Manor House Sandstone, Jungle Pillar, "
"HeartCastle Stone, Dwarven Wall, Art Deco, Steel Block, Granite Block, "
"Granite Column, Digital Dirt, Techno Grass, Matrix Dirt, Theater Curtain, "
"Marble Block, Lovewillow, Foliage, Asteroid, Castle Block, Jade Block, "
"Conveyor Block, Display Shelf, Display block/box, Heartcastle Column, "
"Marquee Block, Alien Block, Rune Carved Stone, Ancient Block, Icy Igloo, "
"Dreamstone Block, Cloudstone Block, Sandbag Wall, Greezak Hive Floor, "
"SELL ALL DIRT BLOCK\n\n"
"Buy All Blocks DM "
        )
    },
    #82. Wallpapers
    {
        "nama": "BUY/SELL WALLPAPER",
        "channel_id": "782718523629633567",
        "pesan": (
         "**SELL BACKGROUNDS & WALLPAPERS AT PHBS**\n"
"Sell: Superstar Background, Stained Glass, Dark Cave Background, Clouds Wallpaper, "
"Toasted Village Background, Dinosaur Wallpaper, Space Connector, Neon Lights, "
"Red/Blue Royal Wallpaper, Starship Light Wall, The Darkness, Movie Screen, "
"Hospital Wall, Magic Bacon Wallpaper, High Tech Wall, Dark Walnut Wall, "
"Heartcastle Stone Background, Greezak Hive Wall, Clouds Background, Amber Glass, "
"Stained Glass Pineapple, Tenement Building, Art Wall, Lattice Background, "
"Grimstone Wall, Skull Wallpaper, Red Coin Wallpaper, Pastel Wallpaper (All Colors), "
"Dark Wallpaper (All Colors), Solid Color Wallpaper (All), Window Curtains, "
"Glass Pane, Air Duct, Bubble Wrap, Chinese Temple Background, Celestial Frame, "
"Gilded Frame, Mahogany Frame, Chalkboard, Cliffside, Pebbles Background, "
"Sunset Clouds Background, Jade Brick Background, Western Building, "
"Stripey Wallpaper, Checker Wallpaper, Field Grass\n\n"
"Buy All Wallpaper DM "
        )
    },
    # 83. Doors & Portals
    {
        "nama": "BUY/SELL DOORS",
        "channel_id": "846671811223355402",
        "pesan": (
         "**SELL DOORS & ENTRANCES AT PHBS**\n"
"Sell Door,Sell Screen Door,Sell Hospital Door,Sell Saloon Doors,Sell Dungeon Door,Sell Heartcastle Gate,"
"Sell Bountiful Jungle Temple Door,Sell Rickety Door,Sell Cave Entrance,Sell Twisted Mansion Door,"
"Sell Castle Door,Corrupted Castle Door,Sell Starship Door,Sell Halfling House Door,Sell Log Cabin Door,"
"Sell Gingerbread Door,Sell Cottage Doorway,Sell Moon Palace Door,Sell Toasted Village Door,Sell Air Vent,"
"Sell Dark Castle Door,Sell Pueblock Door,Sell Mystery Door,Sell Taco Door,Sell Password Door,Sell Portcullis,"
"Sell Haunted Door,Sell Gateway To Adventure,Sell Hellgate,Sell Orange Portal,Sell Time-Space Rupture,"
"Sell Love Portal,Sell Mystery Portal,Sell Blue Portal,Sell Objective Marker,Sell Path Marker,Sell VIP Entrance,"
"Sell Guild Entrance-Ornate,Sell Guild Entrance-Normal,Sell Forcefield,Sell Dark Magic Barrier,Sell House Entrance,"
"Sell Red House Entrance,Growtorial Entrance,Ancient Stone Gate,Sell Coin Door,Sell Jail Door, Baroque Iron Gate."
        )
    },
    # 84. Signs & Chairs
    {
        "nama": "BUY/SELL SIGNS",
        "channel_id": "846661246303469598",
        "pesan": (
        "**SELL SIGNS & MANNEQUINS AT PHBS**\n"
"Sell Tavern Sign,Sell Western Banner,Sell Shop Sign,Sell Open Sign,Sell Valensign,Sell Holographic Sign,"
"Sell Digital Sign,Danger Sign,Sell Mannequin,Sell Shiny Mannequin,Troll Mannequin,Omg Mannequin,"
"Sell Lol Mannequin,Sell Sad Mannequin,Sell Guestbook,Sell Bulletin Board,Sell Mailbox,Sell Blue Mailbox,"
"Sell Message In A Bottle,Message In A Diamond Bottle,Sell Space Conveyor Block,Sell One-Way Block,"
"Sell Big Old Up Arrow,Big Old Down Arrow,Big Old Sideways Arrow,Diagonal Up Arrow,Sell Pizza Sign,"
"Sell Diagonal Down Arrow,Welcome To Growtopia Sign,Sell Pineapple Sign,Ruined Sign,Sell Pointy Sign,"
"Sell For Sale Sign,Sell Tombstone,Gem Sign,Sell World Lock Neon Sign,Street Sign,Sell Crappy Sign,"
"Sell Arrow Placard,Sell Scroll Bulletin,Exclamation Sign,Sell Space Station Sign,Sell Subway Sign,"
"Sell Shamrock Sign,Sell Gates Motel Sign,Sell Greetings Earthlings Sign,Sell Buddy's Sign,Sell Snowtopian,"
"Sell Sandtopian,Carnival Sign,Neon Sign,Directional Sign."
        )
    },
    # 85. Platforms & Ladders
    {
        "nama": "BUY/SELL PLATFORMS",
        "channel_id": "846673193426354176",
        "pesan": (
           "**SELL PLATFORMS & LADDERS AT PHBS**\n"
"Sell Cave Platform,Fish Landing Platform,Wooden Platform,Sell Bone Platform,Sell Creepstone Platform,"
"Sell Horizontacles,Bountiful Bamboo Platform,Sell Snowy Rocks Platform,Candy Cane Platform,Hover Platform,"
"Sell Fire Escape,Starship Floor Grill,Sell Steel Girder,Sell Seagull,Galleons Mast-Crossbeam,Sideways Vines,"
"Sell Inflatable Ring,Sell Colonization Wagon Base,Cracked Stone Slab,Sell Dark Walnut Ladders,Sell Ladder,"
"Sell Starship Deck Ladders,Bountiful Bamboo Ladder,Rickety Ladders,Stage Support,Diving Board Support,"
"Sell Climbing Vine,Sell Tiled Staircase,Sell Staircase,Regal Bannister,Diamond Regal Bannister,"
"Sell Slippery Flag Pole,Sell U.S.S. Protostar Platform,Sell Floating Hand,Love Ladder,Subway Stairs,"
"Sell Regal Stairs,Diamond Regal Stairs,Corn Field Ladder,Sunflower Ladder,Sell Swamp Stump,"
"Sell Sacred Scarf Block,Rock Platform,Display Shelf,Spooky Display Shelf,Piano Platform,"
"Sell Rave Stage,Sell Galleons Ratlines,Sell Carnival Ladders."
        )
    },
    # 86. Farmable
    {
        "nama": "BUY/SELL FARMABLE",
        "channel_id": "846678373635457024",
        "pesan": (
           "**SELL FARMABLES AT PHBS**\n\n"
            "Sell Chandelier, Sell Laser Grid, Sell Pepper, Sell Fish Tank, "
            "Sell Golden Block, Sell Steel Block, Sell Purple Block, Sell Black Block, "
            "Sell White Block, Sell High Tech Block, Sell Pinball Bumper, Sell Venus Guytrap, "
            "Sell Magic Bell, Sell Sorcerer Stone, Sell Pastel Bricks, Sell Pastel Flower Block, "
            "Sell Xenoid Block, Sell Alien Block, Sell Marble Block, Sell Granite Block, "
            "Sell Sugar Cane, Sell Lovewillow, Sell Fertile Soil Block, Sell Space Dirt, "
            "Sell Martian Soil, Sell Mossy Cobblestone, Sell Ice, Sell Lava, "
            "Sell Monochromatic Lava, Sell Lava Cube, Sell Ocean Rock, "
            "Sell Blackrock Wall, Sell Magic Infused Stone, Sell Space Junk Dirt, "
            "Sell Cave Dirt, Sell Frozen Stone Cliffs, Sell Deep Sand\n\n"
            "Buy All Dropped Farmable Minim 2-5K DM "
        )
    },
    # 87. Food
    {
        "nama": "BUY/SELL FOOD",
        "channel_id": "737344235199660123",
        "pesan": "**SELL FOOD AT PHBS**\n\n"
            "Sell Skill Spice, Sell Gemonade, Sell Trawlerman's Friend, Sell Arroz Con Pollo, "
            "Sell Hot Chocolate, Sell Flashback Flan, Sell Eggs Benedict, Sell Berry Crepes, "
            "Sell Apple Strudel, Sell Beer-Battered Fish And Chips, Sell Homemade Fish Taco, "
            "Sell Gingerbread Cookie, Sell Composer's Cookie, Sell Coconut Tart, "
            "Sell Growlectable, Sell Sweet Potato Tots, Sell Tea, Sell Pineapple Turnover, "
            "Sell Magnifico Carne Guacamole, Sell Chip And Guacamole, Sell Cheeseburger\n\n"
            "Buy All Food DM "
    },
    # 88. Food Ingredients
    {
        "nama": "BUY/SELL FOOD INGRED",
        "channel_id": "737344491526029384",
        "pesan": (
           "**SELL COOKING INGREDIENTS AT PHBS**\n\n"
            "Sell Coconut Milk, Sell Baking Chocolate, Sell Gingerbread Dough, Sell Sugar, "
            "Sell Flour, Sell Rice, Sell Onion, Sell Cherry, Sell Tomato, Sell Egg, "
            "Sell Milk, Sell Blueberry, Sell Apple, Sell Lemon, Sell Salt, Sell Pepper, "
            "Sell Water Bucket, Sell Honey, Sell Dough, Sell Bacon, Sell Chicken Meat, "
            "Sell Beef, Sell Ground Beef, Sell Fish Chunk, Sell Pineapple Slice, "
            "Sell Orange Juice, Sell Lettuce, Sell Potato, Sell Avocado, Sell Corn Meal, "
            "Sell Beat-Root Puree, Sell Habanero Pepper, Sell Swiss Cheese Block, "
            "Sell Chocolate Sprinkles Block, Sell Large Frozen Chunk, Sell Large Radioactive Bit, "
            "Sell Pumpkin Candy, Sell Cobweb, Sell Caramel, Sell Sprig Of Mint, "
            "Sell Primordial Soup, Sell Cosmic 5-Spice Star, Sell Chrono-Luminescent Liquid, "
            "Sell Crushed Ice, Sell Disgusting Mess, Sell Gruel, Sell Seaweed\n\n"
            "Buy All Cooking Ingredients DM "
        )
    },
    # 89. Kitchen Tools
    {
        "nama": "BUY/SELL KITCHEN",
        "channel_id": "737429783201447937",
        "pesan": (
            "**SELL COOKING TOOLS AT PHBS**\n\n"
            "Sell Replicator, Sell Food Grinder, Sell Commercial Oven, Sell Laboratory, "
            "Sell E-Z Cook Oven, Sell Home Oven, Sell Microwave, Sell Refrigerator, "
            "Sell Barbecue Grill, Sell Stove, Sell Taco Truck Oven, Sell Master Chef Oven, "
            "Sell Cutting Board, Sell Sushi Knife, Sell Butcher Knife, Sell Exquisite Rolling Pin, "
            "Sell Race Start Flag, Sell Race End Flag, Sell Dumplings Hat, Sell Ghost Dumplings Hat, "
            "Sell Gourmet Dragon Claw, Sell Blender Bop, Sell Dinner Bell, Sell Enlightenment Bell, "
            "Sell Cooking Supply Crate, Sell Cooling Supply Crate, Sell Spatula, Sell Apron, "
            "Sell Tea Set, Sell Well, Sell Buffalo, Sell Cow, Sell Chicken\n\n"
            "Buy All Kitchen Tools DM "
        )
    },
    # 90. Surgical Tools
    {
        "nama": "BUY/SELL SURGICAL",
        "channel_id": "733049257648586792",
        "pesan": (
            "**SELL SURGERY TOOLS AT PHBS**\n\n"
            "Sell Surgical Stitches\n"
            "Sell Surgical Antibiotics\n"
            "Sell Surgical Scalpel\n"
            "Sell Surgical Sponge\n"
            "Sell Surgical Anesthetic\n"
            "Sell Surgical Antiseptic\n"
            "Sell Surgical Clamp\n"
            "Sell Surgical Defibrillator\n"
            "Sell Surgical Lab Kit\n"
            "Sell Surgical Pins\n"
            "Sell Surgical Splint\n"
            "Sell Surgical Transfusion\n"
            "Sell Surgical Ultrasound\n"
            "Sell Surgical Love Mallet\n"
            "Buy All Cheap Surg Tools 5/1 DM "
        )
    },
    # 91. Vile Vials
    {
        "nama": "BUY/SELL VIALS",
        "channel_id": "733050486143320164",
        "pesan": (
          "**SELL VILE VIALS & MALADY AT PHBS**\n\n"
            "Sell Vile Vial - Brainworms\n"
            "Sell Vile Vial - Ecto Bones\n"
            "Sell Vile Vial - Lupus\n"
            "Sell Vile Vial - Moldy Guts\n"
            "Sell Vile Vial - Fatty Liver\n"
            "Sell Vile Vial - Chaos Infection\n"
        )
    },
    # 92. Hospital & Medical
    {
        "nama": "BUY/SELL MEDICAL",
        "channel_id": "733050809314705458",
        "pesan": (
        "**SELL SURGERY ITEMS & DROPS AT PHBS**\n\n"
            "Sell Surg-E, Sell Train-E, Sell Legal Brief, Sell Wolf Whistle, "
            "Sell Healing Tome, Sell Hospital Wall, Sell Hospital Window, "
            "Sell Hospital Door, Sell Hospital Curtain, Sell Hospital Bed, "
            "Sell Hospital Sign, Sell Operating Table, Sell Heart Monitor, "
            "Sell Autoclave, Sell Auto Surgeon Station, Sell Toffee Block, "
            "Sell Bio-Waste, Sell Electrical Power Cube, Sell Operating Theater Lamp, "
            "Sell Doctor's Blingin Set, Sell Plague Doctor Set, Sell Medical Scarf, "
            "Sell UV Vaccine, Sell Half-Faced Scarf, Sell G-Virus, Sell Tiled Staircase\n\n"
            "Buy All Medical Items DM "
        )
    },
    # 93. Gala Tools
    {
        "nama": "BUY/SELL GALA",
        "channel_id": "733052554820452423",
        "pesan": (
        "**SELL STAR TOOLS AT PHBS**\n\n"
            "Sell AI Brain\n"
            "Sell Cyborg Diplomat\n"
            "Sell Galacticbolt\n"
            "Sell Gigablaster\n"
            "Sell Growton Torpedo\n"
            "Sell Hyper Shields\n"
            "Sell Quadriscanner\n"
            "Sell Space Meds\n"
            "Sell Star Supplies\n"
            "Sell Stellar Documents\n"
            "Sell Starfuel\n"
            "Sell Tactical Drone\n"
            "Sell Teleporter Charge\n\n"
            "Buy All Cheap Gala Tools 5/1 DM "
        )
    },
    # 94. Star Trek / Protostar
    {
        "nama": "BUY/SELL STARTEK",
        "channel_id": "991332606434103316",
        "pesan": (
            "**SELL PROTOSTAR & STAR TREK ITEMS AT PHBS**\n\n"
            "Sell Battery Block, Sell U.S.S. Protostar Bulkhead, Sell U.S.S Protostar Platform, "
            "Sell U.S.S. Protostar Wall, Sell U.S.S. Protostar Wall Console, Sell U.S.S. Protostar Wall Panel, "
            "Sell U.S.S. Protostar Wall Vent, Sell U.S.S Protostar Window, Sell Protostar Captain Seat, "
            "Sell Protostar Officer Seat, Sell Tars Lamora Drill, Sell Vehicle Replicator, "
            "Sell Janeway Coffee, Sell Murf Hood, Sell Murf Onesie, Sell Nutri-goop, "
            "Sell Blood Truffle Biscuits, Sell Starfleet Uniform Shirt, Sell Starfleet Uniform Pants, "
            "Sell Janeway Hair, Sell Janeway Shirt, Sell Gwyn Hair, Sell Gwyn Shirt, "
            "Sell Rok Hair, Sell Rok Shirt, Sell Tars Lamora Miner Set, Sell The Diviner Set, "
            "Sell Zero Containment Hood, Sell Zero Medusa Mask, Sell Dal Goggles, "
            "Sell Jankom Pog Multi Mitt, Sell Drednok Helmet, Sell Drednok Robe, "
            "Sell Mine Laser Drill, Sell Dal Phaser, Sell Weather Machine Protostar, "
            "Sell Startopia Supply Crate\n\n"
            "Buy Starfleet Cadet Supply Box DM "
        )
    },
    # 95. Starship Items 
    {
        "nama": "BUY/SELL STARSHIP",
        "channel_id": "733054141106094130",
        "pesan": (
           "**SELL STARSHIP ITEMS AT PHBS**\n\n"
            "Sell Starship Floor Tile, Sell Starship Wall, Sell Starship Ladder, Sell Starship Door\n"
            "Sell Starship Mess Hall Stool, Sell Starship Mess Hall Table, Sell Starship Airlock\n"
            "Sell Starship Light Wall, Sell Starship Porthole, Sell Starship Floor Grill\n"
            "Sell Moonlamp, Sell Starship Packing Crate, Sell Encapsulated Galaxy, Sell Starship Turbo Fan\n"
            "Sell Hypertech Multi-Jet Energy Pulser, Sell Hypertech Antigravity Field\n"
            "Sell Replicator, Sell Xenoid Acid Pool, Sell Greezak Hive Wall, Sell Greezak Hive Floor\n"
            "Sell The Varlaak, Sell Starship Transporter, Sell Starship Sickbay Bed, Sell Looming Triffid\n"
            "Sell Starship Security Camera, Sell Crystalized Star Fragment Block\n"
            "Sell Space Command Seat, Sell Tars Lamora Drill, Sell Starship Console Panel, Sell Star Tool Droid\n\n"
            "Buy All Starship Items DM"
        )
    },
    # 96. Starship Blast
    {
        "nama": "BUY/SELL STARSHIP BLAST",
        "channel_id": "733053014163587145",
        "pesan": (
            "**SELL STARSHIP BLASTS AT PHBS**\n\n"
            "Sell Imperial Starship Blast\n"
            "Sell Stellarix Starship Blast\n"
            "Sell Greezak Starship Blast\n"
            "Sell HyperTech Starship Blast\n\n"
            "Buy All Starship Blasts DM "
        )
    }
]

# ================= FUNGSI SISTEM =================

def cek_validasi_token():
    """Fungsi untuk mengecek apakah token valid di awal running."""
    url = "https://discord.com/api/v9/users/@me"
    headers = {"authorization": TOKEN}
    try:
        res = requests.get(url, headers=headers, timeout=10)
        if res.status_code == 200:
            user_data = res.json()
            return True, user_data.get('username', 'Unknown')
        else:
            return False, None
    except:
        return False, None

def muat_data_semua():
    try:
        if os.path.exists(FILE_DATA):
            with open(FILE_DATA, "r") as f:
                content = f.read()
                if not content.strip(): return {}
                return json.loads(content)
    except Exception: pass
    return {}

def simpan_status(channel_id, durasi_cd):
    data = muat_data_semua()
    data[str(channel_id)] = {"last_run": time.time(), "cd_duration": durasi_cd}
    with open(FILE_DATA, "w") as f: 
        json.dump(data, f, indent=4)

def ambil_info(data_db, channel_id):
    item = data_db.get(str(channel_id))
    if not item: return 0
    sisa = item["cd_duration"] - (time.time() - item["last_run"])
    return int(sisa) if sisa > 0 else 0

def tambah_log(pesan):
    jam = time.strftime("%H:%M:%S")
    LOG_AKTIVITAS.append(f"[{jam}] {pesan}")
    if len(LOG_AKTIVITAS) > 5:
        LOG_AKTIVITAS.pop(0)

def gambar_tampilan_utama():
    os.system('cls' if os.name == 'nt' else 'clear')
    db = muat_data_semua()
    
    print("┌──────────────────────────────────────────────────────────┐")
    print(f"│{'PROJECT BY ' + AUTHOR.upper():^58}│")
    print(f"│{'SCRIPT INI TIDAK DIPERJUALBELIKAN / DI BARTER':^58}│")
    print(f"│{'DILARANG KERAS MENYALAHGUNAKAN KONTEN INI!':^58}│")
    print("├──────────────────────────────────────────────────────────┤")
    print(f"│{'BUY/SELL BGL DM DC @FALHORUS':^58}│")
    print(f"│{'CHEAP VEND AT KAKUL':^58}│")
    print("└──────────────────────────────────────────────────────────┘")

    print("┌────────────────────────────┬─────────────────────────────┐")
    print(f"│ {'NAMA CHANNEL':26} │ {'COOLDOWN (JAM:MENIT)':27} │")
    print("├────────────────────────────┼─────────────────────────────┤")
    
    for t in tugas_spam:
        sisa = ambil_info(db, t['channel_id'])
        if sisa > 0:
            jam, menit = sisa // 3600, (sisa % 3600) // 60
            status_txt = f"COOLDOWN {jam:02d}H {menit:02d}M"
        else:
            status_txt = "READY TO SENT!"
        print(f"│ {t['nama'][:26].ljust(26)} │ {status_txt.ljust(27)} │")
    print("└────────────────────────────┴─────────────────────────────┘")

    print("\n[ LOG AKTIVITAS TERBARU ]")
    if not LOG_AKTIVITAS:
        print("  - Menunggu jadwal spam...")
    for log in LOG_AKTIVITAS:
        print(f"  {log}")
    print("-" * 60)

# ================= RUNNER UTAMA =================

if __name__ == "__main__":
    print("[-] Menghubungkan ke Discord...")
    valid, username = cek_validasi_token()
    
    if not valid:
        print("\n" + "!"*60)
        print(" ERROR: TOKEN TIDAK VALID ATAU EXPIRED!")
        print(" SILAKAN CEK KEMBALI TOKEN DISCORD ANDA.")
        print("!"*60 + "\n")
        input("Tekan Enter untuk keluar...")
        sys.exit()
    
    tambah_log(f"Login Berhasil sebagai: {username}")
    eksekusi_pertama = True

    while True:
        try:
            db_now = muat_data_semua()
            gambar_tampilan_utama()
            
            # Cek tugas yang siap
            siap = [t for t in tugas_spam if ambil_info(db_now, t['channel_id']) <= 0]
            
            if siap:
                cd_sama = random.randint(7200, 14400)
                jam_info = cd_sama // 3600
                menit_info = (cd_sama % 3600) // 60

                total_tugas = len(siap)
                for index, t in enumerate(siap):
                    
                    # --- CEK LIMIT KARAKTER (MAKS 1000) ---
                    char_count = len(t['pesan'])
                    if char_count > 1000:
                        tambah_log(f"FAIL: {t['nama']} | OVER 1000 CHAR ({char_count})")
                        # Tidak ada simpan_status di sini agar tetap READY
                        continue 
                    
                    tambah_log(f"PREPARING: {t['nama']}")
                    for i in range(5, 0, -1):
                        sys.stdout.write(f"\r\033[K>> MENGIRIM KE [{t['nama']}] DALAM {i} DETIK...")
                        sys.stdout.flush()
                        time.sleep(1)

                    url = f"https://discord.com/api/v9/channels/{t['channel_id']}/messages"
                    headers = {"authorization": TOKEN, "content-type": "application/json"}
                    payload = {"content": t['pesan']}
                    
                    try:
                        res = requests.post(url, headers=headers, json=payload, timeout=8)
                        if res.status_code in [200, 201]:
                            simpan_status(t['channel_id'], cd_sama)
                            tambah_log(f"SUCCESS: {t['nama']} | CD: {jam_info}j {menit_info}m")
                        elif res.status_code == 403:
                            tambah_log(f"SKIPPED: {t['nama']} | LEVEL TIDAK CUKUP")
                            simpan_status(t['channel_id'], 43200)
                        elif res.status_code == 429:
                            retry = res.json().get('retry_after', 10)
                            simpan_status(t['channel_id'], int(retry))
                            tambah_log(f"LIMIT: {t['nama']} | Re-try {int(retry)}s")
                        else:
                            tambah_log(f"FAILED: {t['nama']} ({res.status_code})")
                    except Exception:
                        tambah_log(f"ERROR: {t['nama']}")

                    if index < total_tugas - 1:
                        next_ch = siap[index + 1]['nama']
                        jeda_antar = random.uniform(10.0, 15.0)
                        for s_antar in range(int(jeda_antar), 0, -1):
                            sys.stdout.write(f"\r\033[K>> PINDAH KE [{next_ch}] DALAM {s_antar}s...")
                            sys.stdout.flush()
                            time.sleep(1)
                    gambar_tampilan_utama()

                eksekusi_pertama = False
                tambah_log("KLOTER SELESAI. MENUNGGU JADWAL...")

            else:
                list_sisa = [ambil_info(db_now, t['channel_id']) for t in tugas_spam]
                waktu_tunggu_terdekat = min(list_sisa) if list_sisa else 60
                waktu_tunggu_terdekat += 10 

                for s_sisa in range(int(waktu_tunggu_terdekat), 0, -1):
                    jam_v, s_sis = divmod(s_sisa, 3600)
                    menit_v, detik_v = divmod(s_sis, 60)
                    sys.stdout.write(f"\r\033[K>> NEXT SPAM DALAM: {jam_v:02d}:{menit_v:02d}:{detik_v:02d}")
                    sys.stdout.flush()
                    time.sleep(1)
            
            time.sleep(1)

        except KeyboardInterrupt:
            sys.exit()
        except Exception:
            time.sleep(5)