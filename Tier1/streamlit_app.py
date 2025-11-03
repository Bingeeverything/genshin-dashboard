import requests
import pandas as pd
import os

CHARACTER_NAMES = {
    10000002: "Kamisato Ayaka",
    10000003: "Jean",
    10000005: "Traveler",
    10000006: "Lisa",
    10000007: "Traveler",
    10000014: "Barbara",
    10000015: "Kaeya",
    10000016: "Diluc",
    10000020: "Razor",
    10000021: "Amber",
    10000022: "Venti",
    10000023: "Xiangling",
    10000024: "Beidou",
    10000025: "Xingqiu",
    10000026: "Xiao",
    10000027: "Ningguang",
    10000029: "Klee",
    10000030: "Zhongli",
    10000031: "Fischl",
    10000032: "Bennett",
    10000033: "Tartaglia",
    10000034: "Noelle",
    10000035: "Qiqi",
    10000036: "Chongyun",
    10000037: "Ganyu",
    10000038: "Albedo",
    10000039: "Diona",
    10000041: "Mona",
    10000042: "Keqing",
    10000043: "Sucrose",
    10000044: "Xinyan",
    10000045: "Rosaria",
    10000046: "Hu Tao",
    10000047: "Kaedehara Kazuha",
    10000048: "Yanfei",
    10000049: "Yoimiya",
    10000050: "Thoma",
    10000051: "Eula",
    10000052: "Raiden Shogun",
    10000053: "Sayu",
    10000054: "Sangonomiya Kokomi",
    10000055: "Gorou",
    10000056: "Sara",
    10000057: "Arataki Itto",
    10000058: "Yae Miko",
    10000059: "Shikanoin Heizou",
    10000060: "Yelan",
    10000062: "Aloy",
    10000063: "Shenhe",
    10000064: "Yun Jin",
    10000065: "Kuki Shinobu",
    10000066: "Ayato",
    10000067: "Collei",
    10000068: "Dori",
    10000069: "Tighnari",
    10000070: "Nilou",
    10000071: "Cyno",
    10000072: "Candace",
    10000073: "Nahida",
    10000074: "Layla",
    10000075: "Wanderer",
    10000076: "Faruzan",
    10000077: "Yaoyao",
    10000078: "Alhaitham",
    10000079: "Dehya",
    10000080: "Mika",
    10000081: "Kaveh",
    10000082: "Baizhu",
    10000083: "Kirara",
    10000084: "Lynette",
    10000085: "Lyney",
    10000086: "Freminet",
    10000087: "Neuvillette",
    10000088: "Wriothesley",
    10000089: "Charlotte",
    10000090: "Furina",
    10000091: "Chevreuse",
    10000092: "Navia",
    10000093: "Gaming",
    10000094: "Xianyun",
    10000095: "Chiori",
    10000096: "Arlecchino",
    10000097: "Sethos",
    10000098: "Sigewinne",
    10000099: "Clorinde",
    10000100: "Emilie",
    10000101: "Kachina",
    10000102: "Kinich",
    10000103: "Mualani",
    10000104: "Xilonen",
    10000105: "Chasca",
    10000106: "Mavuika",
    10000107: "Citlali",
    10000114: "Ororon"
}

def download_character_image(avatar_id, character_name):
    """Download character portrait from Enka Network CDN"""
    # Create images directory
    os.makedirs("data/images", exist_ok=True)
    
    # Use the character icon from Enka's assets
    # The naming convention removes the '1000' prefix
    short_id = str(avatar_id)[4:]  # Remove '1000' prefix, e.g., 10000052 -> 0052
    
    # Try different image sources
    image_urls = [
        f"https://enka.network/ui/UI_AvatarIcon_{character_name.replace(' ', '')}.png",
        f"https://genshin.honeyhunterworld.com/img/char/UI_AvatarIcon_{character_name.replace(' ', '')}_card.png",
        f"https://api.ambr.top/assets/UI/avatar/UI_AvatarIcon_{character_name.replace(' ', '')}.png",
    ]
    
    image_path = f"data/images/{character_name.replace(' ', '_')}.png"
    
    for image_url in image_urls:
        try:
            img_response = requests.get(image_url, timeout=5)
            if img_response.status_code == 200 and len(img_response.content) > 1000:  # Valid image
                with open(image_path, 'wb') as f:
                    f.write(img_response.content)
                print(f"  ✓ Downloaded image for {character_name}")
                return image_path
        except Exception:
            continue
    
    print(f"  ✗ Could not download image for {character_name} (ID: {avatar_id})")
    return None

def main():
    uid = 884514113
    
    # Fetch data directly from Enka Network API
    url = f"https://enka.network/api/uid/{uid}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Error fetching data: {response.status_code}")
        return
    
    data = response.json()
    
    # Player info
    player_info = data.get('playerInfo', {})
    print("=== Player Info ===")
    print(f"Nickname: {player_info.get('nickname', 'N/A')}")
    print(f"Level: {player_info.get('level', 'N/A')}")
    print(f"Signature: {player_info.get('signature', 'N/A')}")
    print(f"Achievement: {player_info.get('finishAchievementNum', 'N/A')}")
    
    # Character data
    rows = []
    avatar_list = data.get('avatarInfoList', [])
    
    print("\n=== Downloading Character Images ===")
    
    for avatar in avatar_list:
        # Get basic info
        avatar_id = avatar.get('avatarId', 0)
        character_name = CHARACTER_NAMES.get(avatar_id, f"Unknown ({avatar_id})")
        
        # Download character image
        image_path = download_character_image(avatar_id, character_name)
        
        # Get stats from fightPropMap
        fight_props = avatar.get('fightPropMap', {})
        
        # Get equipment (weapon is usually the last equipment)
        equip_list = avatar.get('equipList', [])
        weapon_name = "Unknown"
        if equip_list:
            # Weapon is identified by flat type (not reliquary)
            for equip in equip_list:
                if 'weapon' in equip or equip.get('flat', {}).get('itemType') == 'ITEM_WEAPON':
                    weapon_name = equip.get('flat', {}).get('nameTextMapHash', 'Unknown Weapon')
                    break
        
        rows.append({
            "avatar_id": avatar_id,
            "character": character_name,
            "image_path": image_path if image_path else "N/A",
            "level": avatar.get('propMap', {}).get('4001', {}).get('val', 0),
            "ascension": avatar.get('propMap', {}).get('1002', {}).get('val', 0),
            "weapon": weapon_name,
            "max_hp": fight_props.get('2000', 0),
            "atk": fight_props.get('2001', 0),
            "defense": fight_props.get('2002', 0),
            "crit_rate": round(fight_props.get('20', 0) * 100, 2),
            "crit_dmg": round(fight_props.get('22', 0) * 100, 2),
            "energy_recharge": round(fight_props.get('23', 0) * 100, 2)
        })
    
    df = pd.DataFrame(rows)
    print("\n=== Character Data ===")
    print(df.to_string())
    
    # Create data directory if it doesn't exist
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/enka_characters.csv", index=False)
    print("\nData saved to data/enka_characters.csv")

if __name__ == "__main__":
    main()