package src;
import java.io.IOException;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;


public class WebScraper {
    public static void main(String[] args) {
        try {
            // The URL of the webpage you want to scrape
            String url = "https://rollcall.com/factbase/trump/search/?type=Speech&sort=desc&spage=1";

            // Fetch and parse the HTML content of the webpage
            Document doc = Jsoup.connect(url).get();

            // Find the element using the CSS selector (for example, the anchor tag with the specific CSS selector)
            // Elements elements = doc.select("#factbase-content > div.w-full > div > form > div.block.md\\:flex.gap-8.max-w-7xl.m-auto > div.w-full.md\\:w-3\\/4 > div:nth-child(2) > div:nth-child(1) > div.w-full.md\\:w-8\\/12.px-2.md\\:pl-0.pl-4.py-2.relative > div.flex.gap-4.items-center.py-2.flex-initial > div.flex-1.text-right > a");
            // Elements elements = doc.select("#factbase-content > div.w-full > div > form > div.block.md\\:flex.gap-8.max-w-7xl.m-auto > div.w-full.md\\:w-3\\/4 > div:nth-child(2) > div:nth-child(1) > div.w-full.md\\:w-8\\/12.px-2.md\\:pl-0.pl-4.py-2.relative > div.flex.gap-4.items-center.py-2.flex-initial > div.flex-1.text-right > a");
            Elements links = doc.select("a");
            for (Element link : links) {
                System.out.println("URL found: " + link.attr("href"));
            }

            // Check if any elements match the selector and get the first one (you can modify if needed)
            // if (!elements.isEmpty()) {
            //     Element element = elements.first(); // Get the first matching element
            //     String href = element.attr("href"); // Extract the URL (href attribute)
            //     System.out.println("URL found: " + href);
            // } else {
            //     System.out.println("Element not found using the selector.");
            // }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

