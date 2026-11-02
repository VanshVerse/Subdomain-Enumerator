import dns.resolver

domain = "example.com"

# wordlist ki file use krne ke liye
with open("wordlist.txt", "r") as file:
    wordlist = file.readlines()

record_types = ["A", "AAAA", "CNAME"]

resolver = dns.resolver.Resolver()
resolver.timeout = 2
resolver.lifetime = 4
total_candidates = 0
found_subdomains = 0
no_record_subdomains = 0
error_subdomains = 0



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
        total_candidates = total_candidates + 1

        found = False
        had_error = False

        subdomain = word + "." + domain

        print("\nChecking:", subdomain)

        result_file.write("\nChecking: " + subdomain + "\n")

        for record in record_types:

            try:
                answers = resolver.resolve(subdomain, record)
                found = True

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
                had_error = True

            except dns.exception.DNSException as error:
                print("DNS Error:", error)
                result_file.write("DNS Error: " + str(error) + "\n")
                had_error = True

        if found:
         found_subdomains = found_subdomains + 1

        elif had_error:
         error_subdomains = error_subdomains + 1

        else:
         no_record_subdomains = no_record_subdomains + 1

    result_file.write("\nPROJECT SUMMARY\n")
    result_file.write("Total Candidates: " + str(total_candidates) + "\n")
    result_file.write("Records Found: " + str(found_subdomains) + "\n")
    result_file.write("No Records: " + str(no_record_subdomains) + "\n")
    result_file.write("DNS Errors: " + str(error_subdomains) + "\n")
    result_file.write("\nEnumeration Completed!!!!\n")


print("\nPROJECT SUMMARY")
print("Total Candidates:", total_candidates)
print("Records Found:", found_subdomains)
print("No Records:", no_record_subdomains)
print("DNS Errors:", error_subdomains)

print("\nEnumeration Completed!")
print("Results saved in results.txt")