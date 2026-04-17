import asyncio
import platform

import inquirer
from colorama import Fore
from inquirer.themes import Default
from rich.console import Console

from check_python import check_python_version
from data.constants import PROJECT_NAME
from functions.activity import activity
from utils.create_files import create_files
from utils.db_api.models import Wallet
from utils.db_api.wallet_api import db
from utils.db_import_export_sync import Export, Import, Sync
from utils.git_version import check_for_updates
from utils.output import show_channel_info

console = Console()


PROJECT_ACTIONS = [
    "1. Run All Tasks In Random Order",
    "2. Daily Check-in & Faucet",
    "3. Complete Quests",
    "4. Twitter Tasks",
    "5. Join and Bind Discord",
    "6. Zenith Swap & Liquidity",
    "7. Faroswap Swap & Liquidity",
    "8. Brokex CFD Trading",
    "9. ELFi RWA Lending",
    "10. R2 Stablecoin Minting",
    "11. PNS Domain Minting",
    "12. NFT Minting",
    "13. Use Referral Code",
    "14. View Referral Stats",
    "15. Update Points",
    "Back",
]


async def choose_action():
    cat_question = [
        inquirer.List(
            "category",
            message=Fore.LIGHTBLACK_EX + "Choose action",
            choices=["DB Actions", PROJECT_NAME, "Exit"],
        )
    ]

    answers = inquirer.prompt(cat_question, theme=Default())
    category = answers.get("category")

    if category == "Exit":
        console.print(f"[bold red]Exiting {PROJECT_NAME}...[/bold red]")
        raise SystemExit(0)

    if category == "DB Actions":
        actions = ["Import wallets to Database", "Sync wallets with tokens and proxies", "Export Database to CSV", "Back"]

    if category == PROJECT_NAME:
        actions = PROJECT_ACTIONS

    act_question = [
        inquirer.List(
            "action",
            message=Fore.LIGHTBLACK_EX + f"Choose action in '{category}'",
            choices=actions,
        )
    ]

    act_answer = inquirer.prompt(act_question, theme=Default())
    action = act_answer["action"]

    if action == "Import wallets to Database":
        console.print(f"[bold blue]Starting Import Wallets to DB[/bold blue]")
        await Import.wallets()
    elif action == "Sync wallets with tokens and proxies":
        console.print(f"[bold blue]Starting sync data in DB[/bold blue]")
        await Sync.sync_wallets_with_tokens_and_proxies()
    elif action == "Export Database to CSV":
        console.print(f"[bold blue]Starting Export Database to CSV[/bold blue]")
        await Export.data_to_csv()

    elif "1" in action:
        await activity(action=1)
    elif "2" in action:
        await activity(action=2)
    elif "3" in action:
        await activity(action=3)
    elif "4" in action:
        await activity(action=4)
    elif "5" in action:
        await activity(action=5)
    elif "6" in action:
        await activity(action=6)
    elif "7" in action:
        await activity(action=7)
    elif "8" in action:
        await activity(action=8)
    elif "9" in action:
        await activity(action=9)
    elif "10" in action:
        await activity(action=10)
    elif "11" in action:
        await activity(action=11)
    elif "12" in action:
        await activity(action=12)
    elif "13" in action:
        await activity(action=13)
    elif "14" in action:
        await activity(action=14)
    elif "15" in action:
        await activity(action=15)
    elif action == "Back":
        await choose_action()
    else:
        console.print(f"[bold red]Invalid action[/bold red]")

    await choose_action()


async def main():
    check_python_version()
    create_files()
    await check_for_updates(repo_name=PROJECT_NAME, repo_private=False)
    db.ensure_model_columns(Wallet)
    await choose_action()


if __name__ == "__main__":
    show_channel_info(PROJECT_NAME)

    if platform.system() == "Windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(main())
