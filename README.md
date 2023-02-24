# About Dataset
Welcome to the Traditional Indian Texts dataset! This dataset is a collection of some of the most seminal works in Indian history, starting with the Charak Samhita, Chanakya Niti and Srimad Bhagavatam. We plan to add more texts to this collection soon, covering a wide range of topics and perspectives.  
## 1. Charak-Samhita
Welcome to the Charak Samhita dataset! Charak Samhita is an ancient Indian Ayurvedic text, considered to be one of the foundational texts of this traditional medical system. Charak Samhita  covers various aspects of Ayurvedic medicine such as anatomy, physiology, pathology, and treatment. The data has been sourced from Wisdomlib has been carefully curated to ensure accuracy and authenticity. By providing access to this valuable resource, we hope to facilitate the preservation and advancement of Ayurvedic knowledge..

### About Data collection methodology

The data has been web-scraped from the Wisdomlib using the Python library BeautifulSoup.

### Description of the data
```

Root ayurveda/
  -Sub charak-samhita/
    -Sub 1.Sutrasthana (Sutra Sthana) — General Principles
        -chapters
    -Sub 2.Nidanasthana (Nidana Sthana) — Section on Pathology
        -chapters
    -Sub 3.Vimanasthana (Vimana Sthana) — Section on Measure
        -chapters
    -Sub 4.Sharirasthana (Sharira Sthana) — Section on Human Embodiment
        -chapters
    -Sub 5.Indriyasthana (Indriya Sthana) — Section on Sensorial Prognosis
        -chapters
    -Sub 6.Cikitsasthana (Cikitsa Sthana) — Section on Therapeutics
        -chapters
    -Sub 7.Kalpasthana (Kalpa Sthana) — Section on Pharmaceutics
        -chapters
    -Sub 8.Siddhisthana (Siddhi Sthana) — Section on Successful Treatment
        -chapters
```

### Dataset formats

format of data is .json

```
[
    {
        "verse_id"="1";
        "text"="We shall now expound the chapter entitled";
    }
]
```
## 2. Chanakya-Niti
This dataset contains text from the ancient Indian treatise Chanakya Niti, a collection of political and ethical sayings attributed to the philosopher and advisor Chanakya. The text provides guidance on governance, diplomacy, leadership, and personal conduct and is considered one of the most important works on statecraft and leadership in ancient India.

### About Data collection methodology

The data has been web-scraped from chanakyadrishti.com using the Python library BeautifulSoup.

### Description of the data
```
Root chanakya/
  -Sub Chanakya-Niti/
    -chapter1.json
    -chapter2.json
    .
    .
    .
    -chapter17
```

### Dataset formats

format of data is .json

```
[
    {
        "verse_id"="1";
        "text"="Humbly bowing down before the almighty Lord Sri Vishnu, the Lord of the three worlds";
    }
]
```
## 3. Srimad Bhagavatam
The Srimad Bhagavatam, also known as the Bhagavata Purana, is considered to be one of the most important and revered texts in Hinduism. It is a sacred text that is believed to have been composed by the sage Veda Vyasa around 5000 years ago. The text is divided into 12 Cantos, consisting of 335 chapters.The first two Cantos provide an introduction to the text and describe the creation of the universe and the origins of the various deities. The next six Cantos focus on the life and teachings of Lord Krishna, including his childhood, his exploits as a warrior, and his philosophical teachings. The final four Cantos describe the process of spiritual realization and the path to liberation.

### About Data collection methodology

The data has been web-scraped from vedabase.io using the Python library BeautifulSoup.

### Description of the data
```
Root srimad-bhagavatam/
  -Sub With Purport/
    -Canto 1
      -chapter1.json
    .
    .
    .
    -Canto 12
```

### Dataset formats

format of data is .json

```
[
    {
        "verse": "1",
        "devanagari": "ॐ नमो भगवते वासुदेवायजन्माद्यस्य यतोऽन्वयादितरतश्चार्थेष्वभिज्ञ: स्वराट्तेने ब्रह्म हृदा य आदिकवये मुह्यन्ति यत्सूरय: ।तेजोवारिमृदां यथा विनिमयो यत्र त्रिसर्गोऽमृषाधाम्ना स्वेन सदा निरस्तकुहकं सत्यं परं धीमहि ॥ १ ॥",
        "english_devnagari": "oṁ namo bhagavate vāsudevāyajanmādy asya yato ’nvayād itarataś cārtheṣv abhijñaḥ svarāṭtene brahma hṛdā ya ādi-kavaye muhyanti yat sūrayaḥtejo-vāri-mṛdāṁ yathā vinimayo yatra tri-sargo ’mṛṣādhāmnā svena sadā nirasta-kuhakaṁ satyaṁ paraṁ dhīmahi",
        "verse_Syn": [
            "om",
            "namaḥ",
            "bhagavate",
            "vāsudevāya",
        ],
        "translation": "O my Lord, Śrī Kṛṣṇa, son of Vasudeva, O all-pervading Personality of Godhead, I offer my respectful obeisances unto You. I meditate upon Lord Śrī Kṛṣṇa because He is the Absolute Truth and the primeval cause of all causes of the creation, sustenance and destruction of the manifested universes.",
        "purport": " Obeisances unto the Personality of Godhead Vāsudeva directly indicate Lord Śrī Kṛṣṇa, who is the divine son of Vasudeva and Devakī. This fact will be more explicitly explained in the text of this work."
    },
]
```
