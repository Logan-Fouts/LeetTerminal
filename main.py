from rich.console import Console
from rich.table import Table
import scraper

console = Console()


def display_problems(home_links):
    # Determine the length of the longest title
    longest_title = max(len(link["title"]) for link in home_links)

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Index", style="dim", width=6)
    table.add_column("Title", style="bold", width=longest_title + 2)
    table.add_column("Index", style="dim", width=6)
    table.add_column("Title", style="bold", width=longest_title + 2)

    # Fill the table with problem titles in two columns
    for i in range(0, len(home_links), 2):
        left = home_links[i]
        right = (
            home_links[i + 1] if i + 1 < len(home_links) else {"title": "", "slug": ""}
        )
        table.add_row(
            str(i + 1),
            left["title"],
            str(i + 2) if i + 1 < len(home_links) else "",
            right["title"],
        )

    console.print(table)


def main():
    run = True

    while run:
        # Show all available problems
        home_links = scraper.get_problems(
            url="https://leetcode.com/studyplan/leetcode-75/"
        )
        console.print("[bold cyan]Problems[/bold cyan]")
        display_problems(home_links)

        # Let user select problem
        console.print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", style="bold green")
        selected_problem = home_links[
            int(console.input("[bold]Enter Number Of Desired Problem: [/bold]")) - 1
        ]
        selected_link = (
            f"https://leetcode.com/problems/{selected_problem['slug']}/description"
        )

        if selected_link == -1:
            run = False

        # Pull problem description
        console.print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", style="bold green")
        description = scraper.scrape_description(selected_link)
        console.print(description, style="bold yellow")

        console.print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", style="bold green")
        option = console.input(
            "Type [bold red]h[/bold red] to go home or [bold red]q[/bold red] to quit: "
        )
        if option == "h":
            continue
        if option == "q":
            run = False


if __name__ == "__main__":
    main()
