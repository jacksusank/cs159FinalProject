from bs4 import BeautifulSoup
import requests

file_name = "harris_speeches.txt"

trump_urls={
    "https://rollcall.com/factbase/trump/transcript/donald-trump-speech-campaign-rally-reading-pennsylvania-november-4-2024/",
    "https://rollcall.com/factbase/trump/transcript/donald-trump-speech-campaign-rally-raleigh-north-carolina-november-4-2024/",
    "https://rollcall.com/factbase/trump/transcript/donald-trump-speech-campaign-rally-grand-rapids-michigan-november-4-2024/",
    "https://rollcall.com/factbase/trump/transcript/donald-trump-speech-campaign-rally-pittsburgh-november-4-2024/",
    "https://rollcall.com/factbase/trump/transcript/donald-trump-speech-campaign-rally-macon-georgia-november-3-2024/",
    "https://rollcall.com/factbase/trump/transcript/donald-trump-speech-campaign-rally-lititz-pennsylvania-november-3-2024/",
    "https://rollcall.com/factbase/trump/transcript/donald-trump-speech-campaign-rally-kinston-north-carolina-november-3-2024/",
    "https://rollcall.com/factbase/trump/transcript/donald-trump-speech-campaign-rally-salem-virginia-november-2-2024/",
    "https://rollcall.com/factbase/trump/transcript/donald-trump-speech-campaign-rally-gastonia-north-carolina-november-2-2024/",
    "https://rollcall.com/factbase/trump/transcript/donald-trump-speech-campaign-rally-greensboro-north-carolina-november-2-2024/",
    "https://rollcall.com/factbase/trump/transcript/donald-trump-speech-campaign-rally-warren-michigan-november-1-2024/",
    "https://rollcall.com/factbase/trump/transcript/donald-trump-speech-campaign-rally-milwaukee-wisconsin-november-1-2024/",
    "https://rollcall.com/factbase/trump/transcript/donald-trump-speech-campaign-rally-albuquerque-new-mexico-october-31-2024/",
    "https://rollcall.com/factbase/trump/transcript/donald-trump-speech-campaign-rally-henderson-nevada-october-31-2024/",
    "https://rollcall.com/factbase/trump/transcript/donald-trump-speech-campaign-rally-rocky-mount-north-carolina-october-30-2024/",
    "https://rollcall.com/factbase/trump/transcript/donald-trump-speech-campaign-rally-green-bay-wisconsin-october-30-2024/",
    "https://rollcall.com/factbase/trump/transcript/donald-trump-speech-campaign-rally-allentown-pennsylvania-october-29-2024/",
    "https://rollcall.com/factbase/trump/transcript/donald-trump-interview-sean-hannity-mar-a-lago-october-29-2024/",
    "https://rollcall.com/factbase/trump/transcript/donald-trump-speech-campaign-rally-new-york-madison-square-garden-october-27-2024/",
    "https://rollcall.com/factbase/trump/transcript/donald-trump-speech-campaign-rally-state-college-pennsylvania-october-26-2024/",
    "https://rollcall.com/factbase/trump/transcript/donald-trump-speech-campaign-rally-novi-michigan-october-26-2024/",
    "https://rollcall.com/factbase/trump/transcript/donald-trump-speech-campaign-rally-traverse-city-michigan-october-25-2024/",
    "https://rollcall.com/factbase/trump/transcript/donald-trump-speech-campaign-event-austin-texas-october-25-2024/",
    "https://rollcall.com/factbase/trump/transcript/donald-trump-speech-campaign-rally-tempe-arizona-october-24-2024/",
    "https://rollcall.com/factbase/trump/transcript/donald-trump-speech-campaign-rally-las-vegas-october-24-2024/",
    "https://rollcall.com/factbase/trump/transcript/donald-trump-speech-town-hall-style-campaign-event-zebulon-georgia-october-23-2024/",
    "https://rollcall.com/factbase/trump/transcript/donald-trump-speech-campaign-rally-duluth-georgia-october-23-2024/",
    "https://rollcall.com/factbase/trump/transcript/donald-trump-speech-campaign-rally-greensboro-north-carolina-october-22-2024/",
    "https://rollcall.com/factbase/trump/transcript/donald-trump-speech-campaign-rally-greenville-north-carolina-october-21-2024/",
    "https://rollcall.com/factbase/trump/transcript/donald-trump-speech-campaign-rally-concord-north-carolina-october-21-2024/",
    "https://rollcall.com/factbase/trump/transcript/donald-trump-speech-campaign-rally-lancaster-pennsylvania-october-20-2024/",
    "https://rollcall.com/factbase/trump/transcript/donald-trump-speech-campaign-rally-latrobe-pennsylvania-october-19-2024/",
    "https://rollcall.com/factbase/trump/transcript/donald-trump-speech-campaign-rally-detroit-october-18-2024/",
    "https://rollcall.com/factbase/trump/transcript/donald-trump-interview-patrick-bet-david-pbd-podcast-october-16-2024/",
    "https://rollcall.com/factbase/trump/transcript/donald-trump-speech-campaign-rally-atlanta-october-15-2024/",
    "https://rollcall.com/factbase/trump/transcript/donald-trump-speech-campaign-rally-prescott-valley-arizona-october-13-2024/",
    "https://rollcall.com/factbase/trump/transcript/donald-trump-speech-campaign-rally-coachella-california-october-12-2024/",
    "https://rollcall.com/factbase/trump/transcript/donald-trump-speech-campaign-rally-reno-nevada-october-11-2024/",
    "https://rollcall.com/factbase/trump/transcript/donald-trump-speech-campaign-rally-aurora-colorado-october-11-2024/"
}

kamala_urls={
    "https://rollcall.com/factbase/harris/transcript/kamala-harris-remarks-campaign-event-kalamazoo-michigan-october-26-2024/",
    "https://rollcall.com/factbase/harris/transcript/kamala-harris-remarks-campaign-event-atlanta-october-19-2024/",
    "https://rollcall.com/factbase/harris/transcript/kamala-harris-remarks-campaign-event-waterford-township-michigan-october-18-2024/",
    "https://rollcall.com/factbase/harris/transcript/kamala-harris-speech-economic-club-pittsburgh-september-25-2024/",
    "https://rollcall.com/factbase/harris/transcript/kamala-harris-speech-speaks-at-a-campaign-event-savannah-georgia-august-29-2024/",
    "https://rollcall.com/factbase/harris/transcript/kamala-harris-speech-democratic-nomination-acceptance-chicago-august-22-2024/",
    "https://rollcall.com/factbase/harris/transcript/kamala-harris-speech-campaign-rally-milwaukee-august-20-2024/",
    "https://rollcall.com/factbase/harris/transcript/kamala-harris-speech-campaign-rally-las-vegas-august-10-2024/",
    "https://rollcall.com/factbase/harris/transcript/kamala-harris-speech-campaign-rally-phoenix-august-9-2024/",
    "https://rollcall.com/factbase/harris/transcript/kamala-harris-speech-campaign-rally-romulus-michigan-august-8-2024/",
    "https://rollcall.com/factbase/harris/transcript/kamala-harris-speech-campaign-rally-eau-claire-wisconsin-august-7-2024/",
    "https://rollcall.com/factbase/harris/transcript/kamala-harris-speech-campaign-rally-tim-walz-philadelphia-august-6-2024/",
    "https://rollcall.com/factbase/harris/transcript/kamala-harris-speech-eulogy-sheila-jackson-lee-houston-august-1-2024/",
    "https://rollcall.com/factbase/harris/transcript/kamala-harris-speech-sigma-gamma-rho-biennial-houston-july-31-2024/",
    "https://rollcall.com/factbase/harris/transcript/kamala-harris-speech-campaign-event-atlanta-july-30-2024/",
    "https://rollcall.com/factbase/harris/transcript/kamala-harris-speech-american-federation-teachers-houston-july-25-2024/",
    "https://rollcall.com/factbase/harris/transcript/kamala-harris-speech-campaign-event-milwaukee-july-23-2024/"
}
    
with open(file_name, "w") as file:

    for url in kamala_urls:
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=60)  # Add a timeout to prevent hanging
        response.raise_for_status()  # Check for HTTP errors

        # Parse the HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        parent_element = soup.select_one("#main > div.w-full > div.mx-0.sm\\:mx-10.m-auto.bg-white.p-0.sm\\:p-4 > div.mt-4.w-full.flex.border.border-\\[\#D1D3EA\\].rounded-sm > div > div:nth-child(2)")
        
        #main > div.w-full > div.mx-0.sm\\:mx-10.m-auto.bg-white.p-0.sm\\:p-4 > div.mt-4.w-full.flex.border.border-\\[\#D1D3EA\\].rounded-sm > div > div:nth-child(2)
        #main > div.w-full > div.mx-0.sm\:mx-10.m-auto.bg-white.p-0.sm\:p-4 > div.mt-4.w-full.flex.border.border-\[\#D1D3EA\].rounded-sm > div > div:nth-child(2)

        # Check if the element was found
        if parent_element:
            # Get all the relevent children
            children = parent_element.find_all("div", class_="mb-4 border-b mx-6 my-4")

            # Loop through the children and print their tag names
            for child in children:
                if child.name == "div":
                    h2_element = child.find("h2", class_="text-md inline")
                    if h2_element and "Kamala Harris" in h2_element.get_text():
                        text_element = child.find("div", class_="flex-auto text-md text-gray-600 leading-loose")
                        if text_element:
                            file.write(text_element.get_text(strip=True))
                            file.write("\n")
                    else:
                        continue



