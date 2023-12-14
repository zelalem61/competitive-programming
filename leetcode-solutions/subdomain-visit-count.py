class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dict_ = {}
        ans = []
        
        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            subdomains = domain.split(".")
            if (len(subdomains) == 3):
                subdomains = [domain, subdomains[1] + "." + subdomains[2], subdomains[2]]
            else:
                subdomains = [domain, subdomains[1]]
            
            for subdomain in subdomains:
                prevValue = dict_.get(subdomain, 0)
                dict_[subdomain] = prevValue + int(count)
        
        for key in dict_:
            ans.append(str(dict_.get(key)) + " " + key)
        return ans