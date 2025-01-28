import dns.resolver
import requests
import shodan

def get_subdomains_from_dns(domain):
    subdomains = []
    try:
        answers = dns.resolver.resolve(domain, 'A')  
        for answer in answers:
            subdomains.append(answer.to_text())
    except dns.resolver.NoAnswer:
        pass
    except Exception as e:
        print(f"DNS Sorgulama Hatası: {e}")
    return subdomains


def get_subdomains_from_ct(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    subdomains = []
    try:
        response = requests.get(url)
        response.raise_for_status()  
        entries = response.json()
        for entry in entries:
            subdomains.append(entry['name_value'])
    except requests.exceptions.RequestException as e:
        print(f"CT Logları Sorgulama Hatası: {e}")
    return subdomains

def get_subdomains_from_shodan(api_key, domain):
    subdomains = []
    try:
        api = shodan.Shodan(api_key)
        results = api.search(domain)
        for result in results['matches']:
            for hostname in result.get('hostnames', []):
                subdomains.append(hostname)
    except shodan.APIError as e:
        print(f"Shodan Hatası: {e}")
    return subdomains

def merge_subdomains(subdomains_list):
    return list(set(subdomains_list))  


def main(domain, api_key):
    print(f"Alt Alan Adı Tespiti Başlatılıyor: {domain}")

    print("[*] DNS Kayıtları İle Subdomain Keşfi Yapılıyor...")
    dns_subdomains = get_subdomains_from_dns(domain)
    print(f"DNS Subdomain'leri: {dns_subdomains}")

    print("[*] Sertifika Şeffaflık Logları İle Subdomain Keşfi Yapılıyor...")
    ct_subdomains = get_subdomains_from_ct(domain)
    print(f"CT Subdomain'leri: {ct_subdomains}")

    print("[*] Shodan API İle Subdomain Keşfi Yapılıyor...")
    shodan_subdomains = get_subdomains_from_shodan(api_key, domain)
    print(f"Shodan Subdomain'leri: {shodan_subdomains}")

    all_subdomains = dns_subdomains + ct_subdomains + shodan_subdomains
    unique_subdomains = merge_subdomains(all_subdomains)

    print("\n[*] Tespit Edilen Alt Alan Adları (Benzersiz):")
    for subdomain in unique_subdomains:
        print(subdomain)

if __name__ == "__main__":
    domain = input("Tespit edilecek domain'i girin (örneğin example.com): ").strip()
    api_key = input("Shodan API anahtarınızı girin: ").strip()

    main(domain, api_key)
