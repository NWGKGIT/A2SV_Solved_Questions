from collections import Counter


def subdomainVisits(cpdomains):
    freq_domain = Counter()
    for s in cpdomains:
        n, domain = s.split(" ")
        n = int(n)
        d = domain.split(".")
        for i in range(len(d)):
            curr = ".".join(d[i:])
            freq_domain[curr] += n
    return [f"{count} {dom}" for dom, count in freq_domain.items()]
