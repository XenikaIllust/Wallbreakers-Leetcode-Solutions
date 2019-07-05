"""
A counter is really important to keep track of the domain and the subdomains. Using that, I can easily append
the number of counts.
"""

from collections import Counter

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        def get_subdomains(domain):
            subdomains = []
            
            components = domain.split('.')
            count = 0
            for i in range(len(components)):
                string = ""
                for j in range(count, len(components)):
                    string += components[j]
                    string += "."
                string = string.rstrip(".")
                subdomains.append(string)
                count += 1
                
            return subdomains
        
        subdomain_count = Counter()
        for cpdomain in cpdomains:
            [count, domain] = cpdomain.split(" ")
            subdomains = get_subdomains(domain)
            
            for subdomain in subdomains:
                subdomain_count.update({subdomain: int(count)})
            
        res = []
        for key in subdomain_count.keys():
            res.append(str(subdomain_count[key]) + " " + key)
            
        return res
