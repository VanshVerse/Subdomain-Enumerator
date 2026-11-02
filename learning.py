
# DAY 1

# import dns.resolver                                                       # DNS lookup ke functions import karta hai.

# domain = "example.com"                                                      # target jisse lookup krna hai.. variable mai store kiya 

# try:
#     answers = dns.resolver.resolve(domain, "A")                             #Domain ka A record, yaani IPv4 address, poochta hai.

#     print("Domain:", domain)
#     print("IPv4 addresses:")

#     for answer in answers:                                                   # loop all result print
#         print(answer)

# except dns.resolver.NXDOMAIN:
#     print("Domain does not exist.")

# except dns.resolver.NoAnswer:
#     print("No A record found.")

# except dns.resolver.DNSException as error:
#     print("DNS lookup failed:", error)












# DAY 2

# # Offline Subdomain Enumeration Practice

# domain = "mycompany.test"

# # Simulated DNS records for learning
# known_subdomains = [
#     "www.mycompany.test",
#     "mail.mycompany.test",
#     "blog.mycompany.test",
#     "api.mycompany.test",
#     "support.mycompany.test"
# ]

# # Read wordlist file
# file = open("wordlist.txt", "r")

# print("Starting Subdomain Enumeration...")
# print("Target:", domain)
# print("-----------------------------")

# for word in file:
#     word = word.strip()

#     subdomain = word + "." + domain

#     if subdomain in known_subdomains:
#         print("[FOUND]", subdomain)
#     else:
#         print("[NOT FOUND]", subdomain)

# file.close()

# print("-----------------------------")
# print("Enumeration Completed!")




# DAY 3 
# import dns.resolver

# domain = "example.com"

# wordlist = [
#     "www",
#     "mail",
#     "admin",
#     "blog",
#     "dev"
# ]

# print("Starting DNS Enumeration...")
# print("Target:", domain)
# print("-----------------------------")

# for word in wordlist:

#     subdomain = word + "." + domain

#     try:
#         answers = dns.resolver.resolve(subdomain, "A")

#         print("[FOUND]", subdomain)

#         for answer in answers:
#             print("IP Address:", answer)

#     except dns.resolver.NXDOMAIN: #NXDOMAIN--> 	DNS name exist nahi karta     
#         print("[NOT FOUND]", subdomain)

#     except dns.resolver.NoAnswer: # NoAnswer-->Name ke liye A record nahi mila
#         print("[NO A RECORD]", subdomain)

#     except dns.exception.DNSException as error:   # DNSException--> Other DNS-related error
#         print("[ERROR]", subdomain, error)

# print("-----------------------------")
# print("Enumeration Completed!")






# DAY 4

# import dns.resolver

# domain = "example.com"

# wordlist = [
#     "www",
#     "mail",
#     "admin",
#     "blog",
#     "dev"
# ]

# record_types = ["A", "AAAA", "CNAME"]

# resolver = dns.resolver.Resolver()
# resolver.timeout = 2
# resolver.lifetime = 4

# print("Starting DNS Enumeration...")
# print("Target:", domain)
# print("-----------------------------")

# for word in wordlist:

#     subdomain = word + "." + domain

#     print("\nChecking:", subdomain)

#     for record in record_types:

#         try:
#             answers = resolver.resolve(subdomain, record)

#             print(record, "Record:")

#             for answer in answers:
#                 print(answer)

#         except dns.resolver.NXDOMAIN:
#             print("Domain does not exist.")

#         except dns.resolver.NoAnswer:
#             print("No", record, "record found.")

#         except dns.resolver.LifetimeTimeout:
#             print("DNS request timed out.")

#         except dns.exception.DNSException as error:
#             print("DNS Error:", error)

# print("\nEnumeration Completed!")







# DAY 5

# import dns.resolver

# domain = "example.com"

# # update day 6
# with open("wordlist.txt", "r") as file:
#     wordlist = file.readlines()
# # open() file open karta hai.
# # "r" ka matlab read mode.
# # readlines() file ki saari lines ko list mein store karta hai.
# # with ka use file ko automatically close karne ke liye hota hai.
# #ab... kuch aisa hoga ===> wordlist = ["www\n", "mail\n", "admin\n"]
# #ab.. loop mai .strip() ka use krenge \n remove krne ke liye

# # yha tk update 



# #manually code mai wordlist dena 

# # wordlist = [
# #     "www",
# #     "mail",
# #     "admin",
# #     "blog",
# #     "dev"
# # ]

# record_types = ["A", "AAAA", "CNAME"]

# resolver = dns.resolver.Resolver()
# resolver.timeout = 2
# resolver.lifetime = 4

# # Create result file
# file = open("results.txt", "w")

# file.write("DNS ENUMERATION REPORT\n")
# file.write("Target: " + domain + "\n")
# file.write("-----------------------------\n")

# print("Starting DNS Enumeration...")
# print("Target:", domain)

# for word in wordlist:
#     word = word.strip() # day 6 update iss yh line
#     subdomain = word + "." + domain

#     print("\nChecking:", subdomain)

#     file.write("\nChecking: " + subdomain + "\n")

#     for record in record_types:

#         try:
#             answers = resolver.resolve(subdomain, record)

#             print(record, "Record:")

#             file.write(record + " Record:\n")

#             for answer in answers:
#                 print(answer)
#                 file.write(str(answer) + "\n")

#         except dns.resolver.NXDOMAIN:
#             print("Domain does not exist.")
#             file.write("Domain does not exist.\n")

#         except dns.resolver.NoAnswer:
#             print("No", record, "record found.")
#             file.write("No " + record + " record found.\n")

#         except dns.resolver.LifetimeTimeout:
#             print("DNS request timed out.")
#             file.write("DNS request timed out.\n")

#         except dns.exception.DNSException as error:
#             print("DNS Error:", error)
#             file.write("DNS Error: " + str(error) + "\n")

# file.write("\nEnumeration Completed!\n")
# file.close()

# print("\nEnumeration Completed!")
# print("Results saved in results.txt")








# DAY 6
import dns.resolver

domain = "example.com"

# wordlist ki file use krne ke liye
with open("wordlist.txt", "r") as file:
    wordlist = file.readlines()

record_types = ["A", "AAAA", "CNAME"]

resolver = dns.resolver.Resolver()
resolver.timeout = 2
resolver.lifetime = 4

# Open result file
with open("results.txt", "w") as result_file:

    result_file.write("DNS ENUMERATION REPORT\n")
    result_file.write("Target: " + domain + "\n")
    result_file.write("-----------------------------\n")

    print("Starting DNS Enumeration...")
    print("Target:", domain)

    for word in wordlist:

        word = word.strip()

        if word == "":
            continue

        subdomain = word + "." + domain

        print("\nChecking:", subdomain)

        result_file.write("\nChecking: " + subdomain + "\n")

        for record in record_types:

            try:
                answers = resolver.resolve(subdomain, record)

                print(record, "Record:")
                result_file.write(record + " Record:\n")

                for answer in answers:
                    print(answer)
                    result_file.write(str(answer) + "\n")

            except dns.resolver.NXDOMAIN:
                print("Domain does not exist.")
                result_file.write("Domain does not exist.\n")

            except dns.resolver.NoAnswer:
                print("No", record, "record found.")
                result_file.write(
                    "No " + record + " record found.\n"
                )

            except dns.resolver.LifetimeTimeout:
                print("DNS request timed out.")
                result_file.write("DNS request timed out.\n")

            except dns.exception.DNSException as error:
                print("DNS Error:", error)
                result_file.write("DNS Error: " + str(error) + "\n")

    result_file.write("\nEnumeration Completed!!!!\n")

print("\nEnumeration Completed!")
print("Results saved in results.txt")