import time
from playwright.sync_api import sync_playwright, expect

def test_chatgpt_search():
   
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        
        #using the built-in stealth mode for the page so that it doesnt lag
        page.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {
                get: () => false,
            });
        """) 
        """stealth_sync(page)"""
                
        print("Navigating to ChatGPT...")
        # goes to ChatGPT
        page.goto("https://chatgpt.com/", timeout=60000)
        
        # Wait for page to load
        time.sleep(5)
        
        print("Looking for the search/input box...")
                
        try:
            prompt_box = page.locator("#prompt-textarea").first
            prompt_box.wait_for(state="visible", timeout=10000)
            
            print("Found the input box, typing the question...")
            
            prompt_box.fill("what is the future of sdet role??")
            
            # Waiting time
            time.sleep(1)

            print("Pressing Enter to submit...")
            # Enter to submit the prompt
            prompt_box.press("Enter")
            
            print("Waiting for response...")

            # Waiting for response to appear
            page.wait_for_selector("button[data-testid='send-button']", state="visible", timeout=98000 )

                # screenshot for proof
            print("Taking screenshot...")
            page.screenshot(path="chatgpt_response.png", full_page=True)
            print("Screenshot saved as chatgpt_response.png")
            
        except Exception as e:
                print(f"An error occurred: {e}")
                page.screenshot(path=" not PeRFECT_screenshot.png")
                print("not Perfect screenshot saved")
        
        browser.close()
        print("Test completed!")

if __name__ == "__main__":
    test_chatgpt_search() 