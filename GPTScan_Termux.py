import requests
import json
import os
import platform
import psutil
import socket
import datetime
import time
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

# Tool Information
VERSION = "1.2.0"
OWNER = "ADE PRATAMA"
GITHUB = "https://github.com/HolyBytes"
DONATION = "https://saweria.co/HolyBytes"

# ASCII Art
ASCII_ART = f"""
{Fore.CYAN}╔════════════════════════════════════════════════════════╗
{Fore.CYAN}║ {Fore.YELLOW}  ██████╗{Fore.GREEN} ██████╗{Fore.RED} ████████╗{Fore.MAGENTA}███████╗{Fore.BLUE}███████╗{Fore.CYAN} █████╗ {Fore.YELLOW}███╗   ██╗{Fore.CYAN} ║
{Fore.CYAN}║ {Fore.YELLOW} ██╔════╝{Fore.GREEN}██╔═══██╗{Fore.RED}╚══██╔══╝{Fore.MAGENTA}██╔════╝{Fore.BLUE}██╔════╝{Fore.CYAN}██╔══██╗{Fore.YELLOW}████╗  ██║{Fore.CYAN} ║
{Fore.CYAN}║ {Fore.YELLOW} ██║  ███╗{Fore.GREEN}██║   ██║{Fore.RED}   ██║   {Fore.MAGENTA}███████╗{Fore.BLUE}█████╗  {Fore.CYAN}███████║{Fore.YELLOW}██╔██╗ ██║{Fore.CYAN} ║
{Fore.CYAN}║ {Fore.YELLOW} ██║   ██║{Fore.GREEN}██║   ██║{Fore.RED}   ██║   {Fore.MAGENTA}╚════██║{Fore.BLUE}██╔══╝  {Fore.CYAN}██╔══██║{Fore.YELLOW}██║╚██╗██║{Fore.CYAN} ║
{Fore.CYAN}║ {Fore.YELLOW} ╚██████╔╝{Fore.GREEN}╚██████╔╝{Fore.RED}   ██║   {Fore.MAGENTA}███████║{Fore.BLUE}███████╗{Fore.CYAN}██║  ██║{Fore.YELLOW}██║ ╚████║{Fore.CYAN} ║
{Fore.CYAN}║ {Fore.YELLOW}  ╚═════╝ {Fore.GREEN} ╚═════╝ {Fore.RED}   ╚═╝   {Fore.MAGENTA}╚══════╝{Fore.BLUE}╚══════╝{Fore.CYAN}╚═╝  ╚═╝{Fore.YELLOW}╚═╝  ╚═══╝{Fore.CYAN} ║
{Fore.CYAN}║             {Fore.WHITE}╔════════════════════════════╗             {Fore.CYAN}║
{Fore.CYAN}║             {Fore.WHITE}║      {Fore.LIGHTMAGENTA_EX}TERMUX EDITION{Fore.WHITE}        ║             {Fore.CYAN}║
{Fore.CYAN}║             {Fore.WHITE}╚════════════════════════════╝             {Fore.CYAN}║
{Fore.CYAN}╚════════════════════════════════════════════════════════╝
"""

# Copyright notice
COPYRIGHT = f"{Fore.WHITE}© 2025 {OWNER} | {GITHUB} | {DONATION} | v{VERSION}"

# Konfigurasi API Key
API_KEYS = {
    "SHODAN": "EwsQRyFtHuwJ3TBDAxcj1oBniw3pBotz",
    "VIRUSTOTAL": "2b1ead776607420c7462b57b8ae0bbbcbe429b955da1f28976f6a5e6ac05302a",
    "OPENWEATHER": "8e2f5c8a82b8692c7ed0139a7b15db45",
    "OPENROUTER": "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"
}

def get_system_info():
    """Gather system information"""
    try:
        # OS info
        os_name = platform.system()
        os_version = platform.version()
        os_architecture = platform.machine()
        
        # RAM info
        total_ram = round(psutil.virtual_memory().total / (1024**3), 2)  # GB
        used_ram = round(psutil.virtual_memory().used / (1024**3), 2)    # GB
        free_ram = round(psutil.virtual_memory().available / (1024**3), 2)  # GB
        ram_percent = psutil.virtual_memory().percent
        
        # Network info
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        
        # CPU info
        cpu_count = psutil.cpu_count(logical=True)
        cpu_usage = psutil.cpu_percent(interval=1)
        
        # Current time
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        return {
            "os_name": os_name,
            "os_version": os_version,
            "os_architecture": os_architecture,
            "total_ram": total_ram,
            "used_ram": used_ram,
            "free_ram": free_ram,
            "ram_percent": ram_percent,
            "hostname": hostname,
            "ip_address": ip_address,
            "cpu_count": cpu_count,
            "cpu_usage": cpu_usage,
            "current_time": current_time
        }
    except Exception as e:
        return {"error": str(e)}

def display_system_info():
    """Display system information in a visually appealing way"""
    info = get_system_info()
    if "error" in info:
        print(f"{Fore.RED}[❌] Error getting system info: {info['error']}")
        return
    
    print(f"\n{Fore.CYAN}╔══════════════════════════ SYSTEM INFO ══════════════════════════╗")
    print(f"{Fore.CYAN}║ {Fore.YELLOW}• OS: {Fore.WHITE}{info['os_name']} {info['os_version']} ({info['os_architecture']}){' ' * (43 - len(info['os_name'] + info['os_version'] + info['os_architecture']))} {Fore.CYAN}║")
    print(f"{Fore.CYAN}║ {Fore.YELLOW}• Hostname: {Fore.WHITE}{info['hostname']}{' ' * (51 - len(info['hostname']))} {Fore.CYAN}║")
    print(f"{Fore.CYAN}║ {Fore.YELLOW}• IP Address: {Fore.WHITE}{info['ip_address']}{' ' * (49 - len(info['ip_address']))} {Fore.CYAN}║")
    print(f"{Fore.CYAN}║ {Fore.YELLOW}• CPU Cores: {Fore.WHITE}{info['cpu_count']} (Usage: {info['cpu_usage']}%){' ' * (43 - len(str(info['cpu_count']) + str(info['cpu_usage'])))} {Fore.CYAN}║")
    
    # RAM usage bar
    ram_bar_length = 25
    ram_filled = int(ram_bar_length * info['ram_percent'] / 100)
    ram_bar = f"[{Fore.GREEN}{'█' * ram_filled}{Fore.RED}{'░' * (ram_bar_length - ram_filled)}{Fore.WHITE}]"
    
    print(f"{Fore.CYAN}║ {Fore.YELLOW}• RAM: {Fore.WHITE}{info['used_ram']}GB/{info['total_ram']}GB {ram_bar} {info['ram_percent']}%{' ' * (5 - len(str(info['ram_percent'])))} {Fore.CYAN}║")
    print(f"{Fore.CYAN}║ {Fore.YELLOW}• Time: {Fore.WHITE}{info['current_time']}{' ' * (51 - len(info['current_time']))} {Fore.CYAN}║")
    print(f"{Fore.CYAN}╚═════════════════════════════════════════════════════════════════╝")

def clear_screen():
    """Clear the terminal screen"""
    os.system('clear' if os.name == 'posix' else 'cls')

def loading_animation(duration=2):
    """Display a loading animation"""
    chars = "/-\\|"
    for _ in range(duration * 10):
        for char in chars:
            print(f"{Fore.CYAN}[{char}] Loading...", end='\r')
            time.sleep(0.025)
    print(" " * 30, end='\r')  # Clear the line

def menu_header():
    """Display the menu header"""
    clear_screen()
    print(ASCII_ART)
    display_system_info()
    print(f"\n{Fore.CYAN}╔══════════════════════════ MAIN MENU ═══════════════════════════╗")
    print(f"{Fore.CYAN}║                                                                 ║")
    print(f"{Fore.CYAN}║  {Fore.YELLOW}[1] {Fore.GREEN}Shodan Scanner {Fore.BLUE}- {Fore.WHITE}Search for IP/Device information        {Fore.CYAN}║")
    print(f"{Fore.CYAN}║  {Fore.YELLOW}[2] {Fore.GREEN}VirusTotal Scanner {Fore.BLUE}- {Fore.WHITE}Check URLs/Files for malware    {Fore.CYAN}║")
    print(f"{Fore.CYAN}║  {Fore.YELLOW}[3] {Fore.GREEN}OpenWeather Checker {Fore.BLUE}- {Fore.WHITE}Get current weather data     {Fore.CYAN}║")
    print(f"{Fore.CYAN}║  {Fore.YELLOW}[4] {Fore.GREEN}GPT-3.5 Turbo Chat {Fore.BLUE}- {Fore.WHITE}Chat with AI assistant        {Fore.CYAN}║")
    print(f"{Fore.CYAN}║  {Fore.YELLOW}[5] {Fore.RED}Exit                                                   {Fore.CYAN}║")
    print(f"{Fore.CYAN}║                                                                 ║")
    print(f"{Fore.CYAN}╚═════════════════════════════════════════════════════════════════╝")
    print(f"\n{COPYRIGHT}")

def section_header(title):
    """Create a section header"""
    print(f"\n{Fore.CYAN}╔{'═' * (len(title) + 10)}╗")
    print(f"{Fore.CYAN}║{Fore.YELLOW}    {title}    {Fore.CYAN}║")
    print(f"{Fore.CYAN}╚{'═' * (len(title) + 10)}╝")

def shodan_search():
    """Search Shodan for information"""
    clear_screen()
    section_header("SHODAN IP/DEVICE SCANNER")
    
    query = input(f"\n{Fore.YELLOW}[🔍] Enter IP/Host/Query: {Fore.WHITE}")
    print(f"\n{Fore.CYAN}[⏳] Searching Shodan for '{query}'...")
    loading_animation()
    
    try:
        url = f"https://api.shodan.io/shodan/host/{query}?key={API_KEYS['SHODAN']}"
        response = requests.get(url)
        data = response.json()
        
        if 'error' in data:
            print(f"\n{Fore.RED}[❌] Error: {data['error']}")
        else:
            print(f"\n{Fore.GREEN}[✓] Results found for {query}:")
            print(f"\n{Fore.CYAN}╔══════════════════ SHODAN RESULTS ══════════════════╗")
            
            # Display key information in a formatted way
            if 'ip_str' in data:
                print(f"{Fore.CYAN}║ {Fore.YELLOW}IP Address:  {Fore.WHITE}{data['ip_str']}{' ' * (41 - len(data['ip_str']))} {Fore.CYAN}║")
            
            if 'country_name' in data:
                print(f"{Fore.CYAN}║ {Fore.YELLOW}Location:    {Fore.WHITE}{data.get('country_name', 'Unknown')}{' ' * (41 - len(data.get('country_name', 'Unknown')))} {Fore.CYAN}║")
            
            if 'org' in data:
                org = data['org']
                if len(org) > 38:
                    org = org[:35] + "..."
                print(f"{Fore.CYAN}║ {Fore.YELLOW}Organization:{Fore.WHITE} {org}{' ' * (41 - len(org))} {Fore.CYAN}║")
            
            if 'isp' in data:
                isp = data['isp']
                if len(isp) > 38:
                    isp = isp[:35] + "..."
                print(f"{Fore.CYAN}║ {Fore.YELLOW}ISP:         {Fore.WHITE}{isp}{' ' * (41 - len(isp))} {Fore.CYAN}║")
            
            if 'ports' in data:
                ports = ', '.join(map(str, data['ports'][:10]))
                if len(data['ports']) > 10:
                    ports += "..."
                print(f"{Fore.CYAN}║ {Fore.YELLOW}Open Ports:  {Fore.WHITE}{ports}{' ' * (41 - len(ports))} {Fore.CYAN}║")
            
            if 'hostnames' in data and data['hostnames']:
                hostnames = ', '.join(data['hostnames'][:3])
                if len(data['hostnames']) > 3:
                    hostnames += "..."
                print(f"{Fore.CYAN}║ {Fore.YELLOW}Hostnames:   {Fore.WHITE}{hostnames}{' ' * (41 - len(hostnames))} {Fore.CYAN}║")
            
            print(f"{Fore.CYAN}╚════════════════════════════════════════════════════╝")
            
            # Ask if user wants full details
            if input(f"\n{Fore.YELLOW}[?] Show full JSON details? (y/n): {Fore.WHITE}").lower() == 'y':
                print(f"\n{Fore.CYAN}[📋] Full Shodan Data:")
                print(json.dumps(data, indent=4))
    
    except Exception as e:
        print(f"\n{Fore.RED}[❌] Error: {e}")

def virustotal_scan():
    """Scan URLs or file hashes with VirusTotal"""
    clear_screen()
    section_header("VIRUSTOTAL SCANNER")
    
    target = input(f"\n{Fore.YELLOW}[🛡️] Enter URL/File Hash (MD5/SHA256): {Fore.WHITE}")
    print(f"\n{Fore.CYAN}[⏳] Scanning with VirusTotal...")
    loading_animation()
    
    try:
        # Determine if it's likely a hash or a URL
        is_hash = len(target) in [32, 40, 64] and all(c in "0123456789abcdefABCDEF" for c in target)
        
        if is_hash:
            url = f"https://www.virustotal.com/api/v3/files/{target}"
        else:
            # For URLs, we need to get the ID first by submitting a scan
            url_id = requests.post(
                "https://www.virustotal.com/api/v3/urls",
                headers={"x-apikey": API_KEYS['VIRUSTOTAL']},
                data={"url": target}
            ).json()['data']['id']
            url = f"https://www.virustotal.com/api/v3/analyses/{url_id}"
        
        headers = {"x-apikey": API_KEYS['VIRUSTOTAL']}
        response = requests.get(url, headers=headers)
        data = response.json()
        
        if 'error' in data:
            print(f"\n{Fore.RED}[❌] Error: {data['error']['message']}")
        else:
            # Extract the stats if available
            stats = None
            if 'data' in data and 'attributes' in data['data'] and 'stats' in data['data']['attributes']:
                stats = data['data']['attributes']['stats']
            elif 'data' in data and 'attributes' in data['data'] and 'last_analysis_stats' in data['data']['attributes']:
                stats = data['data']['attributes']['last_analysis_stats']
            
            if stats:
                print(f"\n{Fore.GREEN}[✓] VirusTotal Results:")
                print(f"\n{Fore.CYAN}╔═════════════════ SCAN SUMMARY ═════════════════╗")
                print(f"{Fore.CYAN}║ {Fore.YELLOW}Target: {Fore.WHITE}{target[:30]}{'...' if len(target) > 30 else ''}{' ' * (25 - min(30, len(target)))} {Fore.CYAN}║")
                print(f"{Fore.CYAN}║ {Fore.YELLOW}Results:                                    {Fore.CYAN}║")
                print(f"{Fore.CYAN}║ {Fore.RED}  • Malicious:    {Fore.WHITE}{stats.get('malicious', 0)}{' ' * (29 - len(str(stats.get('malicious', 0))))} {Fore.CYAN}║")
                print(f"{Fore.CYAN}║ {Fore.YELLOW}  • Suspicious:   {Fore.WHITE}{stats.get('suspicious', 0)}{' ' * (29 - len(str(stats.get('suspicious', 0))))} {Fore.CYAN}║")
                print(f"{Fore.CYAN}║ {Fore.GREEN}  • Clean:        {Fore.WHITE}{stats.get('harmless', 0)}{' ' * (29 - len(str(stats.get('harmless', 0))))} {Fore.CYAN}║")
                print(f"{Fore.CYAN}║ {Fore.BLUE}  • Undetected:   {Fore.WHITE}{stats.get('undetected', 0)}{' ' * (29 - len(str(stats.get('undetected', 0))))} {Fore.CYAN}║")
                print(f"{Fore.CYAN}╚════════════════════════════════════════════════╝")
                
                # Calculate threat level
                threat_score = stats.get('malicious', 0) * 3 + stats.get('suspicious', 0)
                total_scans = sum(stats.values())
                
                if threat_score == 0:
                    threat_level = f"{Fore.GREEN}SAFE"
                elif stats.get('malicious', 0) > 3:
                    threat_level = f"{Fore.RED}HIGH RISK"
                elif stats.get('malicious', 0) > 0 or stats.get('suspicious', 0) > 3:
                    threat_level = f"{Fore.YELLOW}SUSPICIOUS"
                else:
                    threat_level = f"{Fore.BLUE}LOW RISK"
                
                print(f"\n{Fore.YELLOW}[⚠️] Threat assessment: {threat_level}")
                
                # Ask if user wants full details
                if input(f"\n{Fore.YELLOW}[?] Show full JSON details? (y/n): {Fore.WHITE}").lower() == 'y':
                    print(f"\n{Fore.CYAN}[📋] Full VirusTotal Data:")
                    print(json.dumps(data, indent=4))
            else:
                print(f"\n{Fore.YELLOW}[⚠️] No clear results found. Showing raw data:")
                print(json.dumps(data, indent=4))
    
    except Exception as e:
        print(f"\n{Fore.RED}[❌] Error: {e}")

def openweather_check():
    """Check current weather for a location"""
    clear_screen()
    section_header("OPENWEATHER CHECKER")
    
    city = input(f"\n{Fore.YELLOW}[☀️] Enter City Name: {Fore.WHITE}")
    print(f"\n{Fore.CYAN}[⏳] Fetching weather data for {city}...")
    loading_animation()
    
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEYS['OPENWEATHER']}&units=metric"
        response = requests.get(url)
        data = response.json()
        
        if data.get('cod') != 200:
            print(f"\n{Fore.RED}[❌] Error: {data.get('message', 'Unknown error')}")
        else:
            weather_icon = {
                "Clear": "☀️",
                "Clouds": "☁️",
                "Rain": "🌧️",
                "Drizzle": "🌦️",
                "Thunderstorm": "⛈️",
                "Snow": "❄️",
                "Mist": "🌫️",
                "Fog": "🌫️",
                "Haze": "🌫️",
                "Smoke": "🌫️",
                "Dust": "🌫️",
                "Sand": "🌫️",
                "Ash": "🌫️",
                "Squall": "💨",
                "Tornado": "🌪️"
            }.get(data['weather'][0]['main'], "🌡️")
            
            # Format temperature with color based on value
            temp = data['main']['temp']
            if temp < 0:
                temp_color = Fore.BLUE
            elif temp < 15:
                temp_color = Fore.CYAN
            elif temp < 25:
                temp_color = Fore.GREEN
            elif temp < 35:
                temp_color = Fore.YELLOW
            else:
                temp_color = Fore.RED
            
            temp_formatted = f"{temp_color}{temp}°C"
            
            print(f"\n{Fore.GREEN}[✓] Current Weather:")
            print(f"\n{Fore.CYAN}╔═════════════════ WEATHER INFO ═════════════════╗")
            print(f"{Fore.CYAN}║ {Fore.YELLOW}Location: {Fore.WHITE}{data['name']}, {data['sys']['country']}{' ' * (36 - len(data['name'] + data['sys']['country']))} {Fore.CYAN}║")
            print(f"{Fore.CYAN}║ {Fore.YELLOW}Weather:  {Fore.WHITE}{weather_icon} {data['weather'][0]['description'].title()}{' ' * (36 - len(data['weather'][0]['description']) - 2)} {Fore.CYAN}║")
            print(f"{Fore.CYAN}║ {Fore.YELLOW}Temp:     {temp_formatted}{' ' * (36 - len(str(temp) + '°C'))} {Fore.CYAN}║")
            print(f"{Fore.CYAN}║ {Fore.YELLOW}Feels:    {Fore.WHITE}{data['main']['feels_like']}°C{' ' * (36 - len(str(data['main']['feels_like']) + '°C'))} {Fore.CYAN}║")
            print(f"{Fore.CYAN}║ {Fore.YELLOW}Humidity: {Fore.WHITE}{data['main']['humidity']}%{' ' * (36 - len(str(data['main']['humidity']) + '%'))} {Fore.CYAN}║")
            print(f"{Fore.CYAN}║ {Fore.YELLOW}Wind:     {Fore.WHITE}{data['wind']['speed']} m/s{' ' * (36 - len(str(data['wind']['speed']) + ' m/s'))} {Fore.CYAN}║")
            print(f"{Fore.CYAN}╚════════════════════════════════════════════════╝")
            
            # Additional weather information if requested
            if input(f"\n{Fore.YELLOW}[?] Show additional weather details? (y/n): {Fore.WHITE}").lower() == 'y':
                sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S')
                sunset = datetime.datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S')
                
                print(f"\n{Fore.CYAN}╔══════════════ ADDITIONAL DETAILS ══════════════╗")
                print(f"{Fore.CYAN}║ {Fore.YELLOW}Pressure:    {Fore.WHITE}{data['main']['pressure']} hPa{' ' * (31 - len(str(data['main']['pressure']) + ' hPa'))} {Fore.CYAN}║")
                print(f"{Fore.CYAN}║ {Fore.YELLOW}Visibility:  {Fore.WHITE}{data.get('visibility', 'N/A')} m{' ' * (31 - len(str(data.get('visibility', 'N/A')) + ' m'))} {Fore.CYAN}║")
                print(f"{Fore.CYAN}║ {Fore.YELLOW}Cloudiness:  {Fore.WHITE}{data['clouds']['all']}%{' ' * (31 - len(str(data['clouds']['all']) + '%'))} {Fore.CYAN}║")
                print(f"{Fore.CYAN}║ {Fore.YELLOW}Sunrise:     {Fore.WHITE}{sunrise}{' ' * (31 - len(sunrise))} {Fore.CYAN}║")
                print(f"{Fore.CYAN}║ {Fore.YELLOW}Sunset:      {Fore.WHITE}{sunset}{' ' * (31 - len(sunset))} {Fore.CYAN}║")
                print(f"{Fore.CYAN}╚════════════════════════════════════════════════╝")
    
    except Exception as e:
        print(f"\n{Fore.RED}[❌] Error: {e}")

def gpt35_chat():
    """Chat with GPT-3.5 Turbo through OpenRouter"""
    clear_screen()
    section_header("GPT-3.5 TURBO CHAT")
    
    # Display an intro message
    print(f"\n{Fore.YELLOW}[💬] Welcome to the GPT-3.5 Turbo assistant!")
    print(f"{Fore.YELLOW}[💡] You can ask questions, request creative content, or get technical help.")
    print(f"{Fore.YELLOW}[🔄] Type 'exit' to return to the main menu.")
    
    # Chat loop
    chat_history = []
    while True:
        prompt = input(f"\n{Fore.GREEN}[👤] You: {Fore.WHITE}")
        
        if prompt.lower() in ['exit', 'quit', 'back']:
            break
        
        print(f"\n{Fore.CYAN}[⏳] AI is thinking...")
        loading_animation(1)
        
        try:
            # Add user message to history
            chat_history.append({"role": "user", "content": prompt})
            
            # Keep only the last 10 messages to avoid token limits
            if len(chat_history) > 10:
                chat_history = chat_history[-10:]
            
            response = requests.post(
                url="https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {API_KEYS['OPENROUTER']}",
                    "Content-Type": "application/json",
                },
                data=json.dumps({
                    "model": "openai/gpt-3.5-turbo-0613",
                    "messages": chat_history
                })
            )
            data = response.json()
            
            if 'choices' in data and len(data['choices']) > 0:
                ai_response = data['choices'][0]['message']['content']
                
                # Add AI response to history
                chat_history.append({"role": "assistant", "content": ai_response})
                
                # Format and display the AI response
                print(f"\n{Fore.BLUE}[🤖] AI: {Fore.WHITE}{ai_response}")
            else:
                print(f"\n{Fore.RED}[❌] Error: No valid response received")
                if 'error' in data:
                    print(f"{Fore.RED}[❌] {data['error']['message']}")
        
        except Exception as e:
            print(f"\n{Fore.RED}[❌] Error: {e}")

def main():
    """Main function to run the tool"""
    # Initial setup
    clear_screen()
    print(f"{Fore.CYAN}[⏳] Initializing GPTScan Termux...")
    loading_animation()
    
    while True:
        menu_header()
        choice = input(f"\n{Fore.YELLOW}[?] Choose an option (1-5): {Fore.WHITE}")
        
        if choice == "1":
            shodan_search()
        elif choice == "2":
            virustotal_scan()
        elif choice == "3":
            openweather_check()
        elif choice == "4":
            gpt35_chat()
        elif choice == "5":
            clear_screen()
            print(ASCII_ART)
            print(f"\n{Fore.YELLOW}[👋] Thank you for using GPTScan Termux!")
            print(f"{Fore.YELLOW}[💻] {COPYRIGHT}")
            exit()
        else:
            print(f"\n{Fore.RED}[❌] Invalid option! Please try again.")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_screen()
        print(ASCII_ART)
        print(f"\n{Fore.YELLOW}[👋] Program terminated by user.")
        print(f"{Fore.YELLOW}[💻] {COPYRIGHT}")
        exit()
    except Exception as e:
        print(f"\n{Fore.RED}[❌] An unexpected error occurred: {e}")
        print(f"{Fore.YELLOW}[💻] {COPYRIGHT}")
        exit(1)
