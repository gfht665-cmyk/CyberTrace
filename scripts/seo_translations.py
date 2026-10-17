# -*- coding: utf-8 -*-
"""
CyberTrace Multi-Lingual Technical CTI Generator
Produces professional technical translations in Russian (ru) and Hindi (hi)
for all 50 cataloged malware families.
"""

# Category-level technical phrasing
RU_CATEGORY_PHRASES = {
    "RAT": "Троян удаленного доступа (RAT)",
    "InfoStealer": "Вредоносная программа для кражи конфиденциальных данных (Инфостилер)",
    "Ransomware": "Программа-вымогатель (Шифровальщик)",
    "Loader": "Загрузчик вредоносного ПО (Дроппер/Стейджер)",
    "C2 Framework": "Фреймворк командно-контрольного управления (C2)",
    "Botnet": "Сетевой ботнет и инструмент распределенных атак (DDoS)",
    "Banking Trojan": "Банковский троян и финансовый сниффер",
    "Spyware": "Шпионское программное обеспечение и кейлоггер"
}

HI_CATEGORY_PHRASES = {
    "RAT": "रिमोट एक्सेस ट्रोजन (RAT)",
    "InfoStealer": "डेटा और क्रेडेंशियल चोरी करने वाला मैलवेयर (इन्फोस्टीलर)",
    "Ransomware": "डेटा एन्क्रिप्ट करने वाला रैंसमवेयर",
    "Loader": "मैलवेयर लोडर और ड्रॉपर पेलोड",
    "C2 Framework": "कमांड और कंट्रोल (C2) फ्रेमवर्क",
    "Botnet": "बॉटनेट नेटवर्क और डीडीओएस अटैक इंजन",
    "Banking Trojan": "बैंकिंग ट्रोजन और वित्तीय क्रेडेंशियल स्निफर",
    "Spyware": "स्पाइवेयर और कीलॉगर निगरानी टूल"
}

def generate_multilingual_data(threat):
    name = threat['name']
    cat = threat['category']
    lang = threat['lang']
    arch = threat['arch']
    c2 = threat['c2']
    
    ru_cat = RU_CATEGORY_PHRASES.get(cat, "Вредоносное программное обеспечение")
    hi_cat = HI_CATEGORY_PHRASES.get(cat, "मैलवेयर और साइबर खतरा")
    
    # Russian summary
    summary_ru = (
        f"Детальный технический анализ {name} — это {ru_cat}, разработанный на стеке {lang}. "
        f"В отчете подробно исследуются этапы скрытого внедрения в память (Process Injection), "
        f"методы обхода EDR-систем, структура сетевых пакетов командного сервера ({c2}) и механизмы кражи данных."
    )
    c2_ru = f"Шифрованный протокол обмена данными с использованием {c2}, защита от сетевого перехвата и анализ маяков (Beacons)."
    
    keywords_ru = f"{name}, анализ {name}, {name} сигнатуры, разбор C2 {name}, правила YARA {name}, индикаторы компрометации IoC, киберразведка, декомпиляция"

    # Hindi summary
    summary_hi = (
        f"{name} एक परिष्कृत {hi_cat} है जिसे {lang} का उपयोग करके विकसित किया गया है। "
        f"इस तकनीकी CTI विश्लेषण में मेमोरी इंजेक्शन तकनीक, EDR सुरक्षा बाईपास, "
        f"कमांड और कंट्रोल सर्वर ({c2}) संचार प्रोटोकॉल और डेटा चोरी तंत्र का पूर्ण विवरण दिया गया है।"
    )
    c2_hi = f"{c2} आधारित एन्क्रिप्टेड C2 इंफ्रास्ट्रक्चर और ऑटोमेटेड पेलोड रिट्रीवल चैनल।"
    
    keywords_hi = f"{name}, {name} मैलवेयर, {name} रिवर्स इंजीनियरिंग, {name} सुरक्षा नियम, साइबर इंटेलिजेंस रिपोर्ट, YARA और Sigma नियम"

    return {
        "summary_ru": summary_ru,
        "c2_ru": c2_ru,
        "keywords_ru": keywords_ru,
        "summary_hi": summary_hi,
        "c2_hi": c2_hi,
        "keywords_hi": keywords_hi
    }
