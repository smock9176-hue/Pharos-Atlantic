# Pharos-Atlantic
Pharos Atlantic tesnet
# Pharos Network Atlantic Bot 🚀

Автоматизированный бот для взаимодействия с сетью **Pharos Atlantic** - высокопроизводительной EVM-совместимой Layer 1 блокчейном для Real World Assets (RWA).

## 📋 Требования к версии Python

**Минимальная версия:** Python **3.10**  
**Рекомендуемая версия:** Python **3.11** или **3.12**  
**Максимальная версия:** Python **3.12**

### Почему именно эти версии?

- **Python 3.10+** поддерживает все современные async/await функции
- **Python 3.11-3.12** имеют лучшую производительность и оптимизацию
- **Python 3.9 и ниже** не поддерживают некоторые зависимости (особенно cryptography 44.0.2)

## ✨ Функциональность

### Основные возможности:
- ✅ **Daily Check-in** - Ежедневное получение очков
- ✅ **Faucet** - Получение бесплатных токенов PHRS
- ✅ **Zenith Swap** - Обмен токенов на DEX
- ✅ **Faroswap** - Альтернативный DEX с ликвидностью
- ✅ **Brokex CFD** - Торговля синтетическими активами
- ✅ **ELFi Lending** - Кредитование Real World Assets (RWA)
- ✅ **R2 Stablecoin** - Минтинг стейблкоинов
- ✅ **PNS** - Регистрация доменов Pharos Name Service
- ✅ **NFT Minting** - Минтинг NFT и Soulbound токенов
- ✅ **Quest System** - Выполнение ежедневных и специальных квестов
- ✅ **Referral System** - Реферальная программа с бонусами
- ✅ **Social Tasks** - Twitter и Discord задачи

## 🛠️ Установка

### Шаг 1: Клонировать репозиторий
```bash
git clone https://github.com/Phoenix0x-web3/pharos_network
cd pharos_network
```

### Шаг 2: Проверить версию Python
```bash
python --version
# Должна быть версия 3.10, 3.11 или 3.12
```

### Шаг 3: Установить зависимости
```bash
python install.py
```

### Шаг 4: Активировать виртуальное окружение

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### Шаг 5: Запустить бот
```bash
python main.py
```

## 📁 Структура проекта

```
pharos_network/
├── data/
│   ├── constants.py              # Константы проекта
│   ├── config.py                 # Конфигурация файлов
│   ├── models.py                 # Модели контрактов (старая сеть)
│   ├── pharos_atlantic_contracts.py  # Контракты Atlantic
│   ├── rpc.py                    # RPC endpoints
│   ├── settings.py               # Настройки из YAML
│   └── abis/                     # ABI файлы контрактов
├── files/
│   ├── private_keys.txt          # Приватные ключи (одна ключ на строку)
│   ├── proxy.txt                 # Прокси адреса (опционально)
│   ├── twitter_tokens.txt        # Twitter токены (опционально)
│   ├── discord_tokens.txt        # Discord токены (опционально)
│   ├── discord_proxy.txt         # Discord прокси (опционально)
│   ├── settings.yaml             # Основная конфигурация
│   └── wallets.db                # База данных кошельков
├── functions/
│   ├── activity.py               # Основная логика активности
│   ├── controller.py             # Контроллер всех модулей
│   └── select_random_action.py   # Выбор случайного действия
├── modules/
│   ├── elfi_lending.py           # RWA Lending (ELFi)
│   ├── daily_checkin.py          # Daily Check-in
│   ├── quests.py                 # Система квестов
│   ├── referral_system.py        # Реферальная система
│   ├── brokex_atlantic.py        # CFD Trading
│   ├── zenith.py                 # Zenith Swap
│   ├── faroswap.py               # Faroswap DEX
│   ├── r2.py                     # R2 Stablecoin
│   ├── pns.py                    # Pharos Name Service
│   └── ... (другие модули)
├── utils/
│   ├── db_api/                   # API базы данных
│   ├── discord/                  # Discord интеграция
│   ├── twitter/                  # Twitter интеграция
│   └── ... (утилиты)
├── libs/
│   └── eth_async/                # Web3 библиотека
├── main.py                       # Точка входа
├── requirements.txt              # Зависимости Python
└── README.md                     # Этот файл
```

## ⚙️ Конфигурация

### 1. Файл `files/private_keys.txt`
Добавьте приватные ключи ваших кошельков, по одному на строку:
```
0x1234567890abcdef...
0xabcdef1234567890...
0x9876543210fedcba...
```

### 2. Файл `files/settings.yaml`

#### Основные параметры:
```yaml
# Шифровать ли приватные ключи
private_key_encryption: true

# Количество потоков обработки
threads: 2

# Количество повторов при ошибке
retry: 3

# Перемешивать ли кошельки перед запуском
shuffle_wallets: true

# Скрывать адрес кошелька в логах
hide_wallet_address_log: true

# Уровень логирования: DEBUG, INFO, WARNING, ERROR
log_level: INFO
```

#### Параметры задержки:
```yaml
# Задержка перед стартом кошелька (в секундах)
random_pause_start_wallet:
  min: 10
  max: 60

# Задержка между действиями (в секундах)
random_pause_between_actions:
  min: 20
  max: 30

# Задержка после завершения всех действий (в секундах) 
random_pause_wallet_after_completion:
  min: 26000   # ~7 часов
  max: 30000   # ~8 часов
```

#### Параметры модулей:

**Swap / Liquidity:**
```yaml
swap_percent:
  min: 5
  max: 30

swaps_count:
  min: 15
  max: 30

liquidity_percent:
  min: 1
  max: 3

liquidity_count:
  min: 5
  max: 10
```

**Brokex CFD Trading:**
```yaml
brokex_percent:
  min: 1
  max: 2

brokex_count:
  min: 5
  max: 10
```

**Staking:**
```yaml
autostake_percent:
  min: 5
  max: 10

autostake_count:
  min: 1
  max: 4
```

### 3. Файл `files/proxy.txt` (опционально)
```
http://user:pass@ip:port
https://user:pass@ip:port
socks5://user:pass@ip:port
```

## 🚀 Использование

### Запуск программы:
```bash
python main.py
```

### Меню выбора действий:

1. **DB Actions** - Работа с базой данных
   - Import wallets to Database
   - Sync wallets with tokens and proxies
   - Export Database to CSV

2. **Pharos Network** - Действия на сети
   - Run All Tasks In Random Order
   - Twitter Tasks
   - Join and Bind Discord
   - Update Points
   - Mint All Badges
   - Daily Check-in
   - Claim Faucet
   - Complete Quests
   - Trade CFD (Brokex)
   - Provide Liquidity

## 🔐 Безопасность

### Шифрование приватных ключей:

При первом запуске с `private_key_encryption: true`:
1. Введите пароль для шифрования
2. Подтвердите пароль
3. Приватные ключи будут зашифрованы в БД
4. Файл `private_keys.txt` будет очищен
5. При каждом запуске вводите пароль для расшифровки

## 📊 Сеть Pharos Atlantic

**Сетевые параметры:**
- **Chain ID:** 8008
- **RPC Endpoint:** https://atlantic.dplabs-internal.com
- **Block Time:** ~1 сек
- **TPS:** до 30,000 транзакций/сек

**Основные контракты:**
- **PHRS Token:** 0x0000000000000000000000000000000000000000
- **USDC:** 0xe0be08c77f415f577a1b3a9ad7a1df1479564ec8
- **USDT:** 0xe7e84b8b4f39c507499c40b4ac199b050e2882d5
- **Zenith Router:** 0x9b84996d519c6a046da9fb6b9be41bad217cb783
- **Brokex Router:** 0xEcbAc797f28f412ddF0D38B50f5B4a6904d46e0A

## 🐛 Troubleshooting

### Ошибка: "ModuleNotFoundError: No module named 'web3'"
```bash
pip install -r requirements.txt
python install.py
```

### Ошибка: "UnsupportedPythonVersion"
```bash
# Проверьте версию Python
python --version

# Если < 3.10, обновите:
# Скачайте Python 3.11 или 3.12 с python.org
```

### Транзакции не проходят
- Проверьте баланс кошелька (нужны PHRS на комиссии)
- Убедитесь, что используете правильный RPC endpoint
- Увеличьте gas limit в настройках

## 📞 Поддержка

- **Telegram:** https://t.me/phoenix_w3
- **Discord:** [Pharos Network Discord](#)
- **GitHub Issues:** https://github.com/Phoenix0x-web3/pharos_network/issues

## 📝 Лицензия

MIT License - смотрите файл LICENSE

## ⚠️ Дисклеймер

Этот бот создан в образовательных целях. Использование торговых ботов может нарушить условия обслуживания платформы. Используйте на свой риск!

---

**Версия:** 2.0.0 (Pharos Atlantic Edition)  
**Последнее обновление:** 17 апреля 2026  
**Поддержка Python:** 3.10, 3.11, 3.12
