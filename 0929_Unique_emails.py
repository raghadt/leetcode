# Unique Emails
# --- Time Complexity: O(C), where C is the total content of emails. 
# --- Space Complexity: O(C). 
email_set = set()
for email in emails:
    local, domain = email.split('@')
    
    clean_local = local.replace('.', '').split('+')[0]
    
    email_set.add(clean_local+'@'+domain)
print(email_set)