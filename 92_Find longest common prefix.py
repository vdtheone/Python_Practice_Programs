# Find longest common prefix

def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]
    
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix

# Example usage
strs = ["flower", "flow", "flight"]
print("longest Common Prefix - ", longestCommonPrefix(strs))